"""
CropGuard Computer Vision & Plant Pathology Diagnostic Engine.
Extracts leaf morphology, necrotic lesions, chlorotic halos, and rust pustules
using OpenCV and scientific computing, generating heatmaps and diagnostic predictions.
"""

import os
from typing import Dict, Any, Tuple, Optional, List
import numpy as np
import cv2
from PIL import Image

try:
    from engine.disease_db import DISEASE_DATABASE, get_disease_info
except ModuleNotFoundError:
    from disease_db import DISEASE_DATABASE, get_disease_info

class CropVisionClassifier:
    """Advanced Computer Vision & Plant Pathology Diagnostic Classifier."""

    def __init__(self):
        self.crop_keys = list(DISEASE_DATABASE.keys())

    def analyze_leaf_image(
        self,
        image_input: Any,
        crop_hint: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Processes a leaf image, segments pathology zones, generates lesion heatmap,
        calculates quantitative infection percentages, and outputs disease diagnosis.
        """
        # Convert PIL / bytes / array to standard OpenCV BGR & RGB
        if isinstance(image_input, Image.Image):
            rgb_img = np.array(image_input.convert("RGB"))
        elif isinstance(image_input, np.ndarray):
            if len(image_input.shape) == 2:
                rgb_img = cv2.cvtColor(image_input, cv2.COLOR_GRAY2RGB)
            elif image_input.shape[2] == 4:
                rgb_img = cv2.cvtColor(image_input, cv2.COLOR_RGBA2RGB)
            else:
                rgb_img = image_input.copy()
        else:
            raise ValueError("Unsupported image input format")

        h, w = rgb_img.shape[:2]
        # Standardize working resolution
        target_size = 512
        scale = target_size / max(h, w)
        new_w, new_h = int(w * scale), int(h * scale)
        img_resized = cv2.resize(rgb_img, (new_w, new_h), interpolation=cv2.INTER_AREA)

        # Color Space Transformations
        bgr = cv2.cvtColor(img_resized, cv2.COLOR_RGB2BGR)
        hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
        lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)

        # 1. Segment Leaf Foreground
        # Plant leaves occupy broad green, yellow-green, and necrotic brown hues
        # Exclude pure white/black/neutral artificial backgrounds
        lower_leaf = np.array([15, 25, 25])
        upper_leaf = np.array([100, 255, 255])
        leaf_mask_green = cv2.inRange(hsv, lower_leaf, upper_leaf)

        # Brown/dry leaf regions in HSV
        lower_brown = np.array([5, 40, 20])
        upper_brown = np.array([22, 255, 200])
        leaf_mask_brown = cv2.inRange(hsv, lower_brown, upper_brown)

        # Combine leaf masks
        leaf_mask = cv2.bitwise_or(leaf_mask_green, leaf_mask_brown)
        # Morphological clean up
        kernel_clean = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        leaf_mask = cv2.morphologyEx(leaf_mask, cv2.MORPH_CLOSE, kernel_clean)
        leaf_mask = cv2.morphologyEx(leaf_mask, cv2.MORPH_OPEN, kernel_clean)

        total_leaf_pixels = int(np.count_nonzero(leaf_mask))
        if total_leaf_pixels < 500:
            # Fallback if image has high white-balance or close-up leaf taking entire frame
            leaf_mask = np.ones((new_h, new_w), dtype=np.uint8) * 255
            total_leaf_pixels = new_h * new_w

        # 2. Extract Pathological Features
        # A) Necrosis / Dark Lesions (Dark brown, black, grey rot)
        # In LAB space: Low Lightness (L < 85) within leaf mask
        l_channel, a_channel, b_channel = cv2.split(lab)
        necrosis_mask = cv2.bitwise_and(
            leaf_mask,
            cv2.inRange(l_channel, 0, 85)
        )
        # B) Chlorosis (Yellowing halos, pale tissue)
        # In HSV: Hue between 22 and 38 with moderate-to-high saturation and value
        chlorosis_mask = cv2.bitwise_and(
            leaf_mask,
            cv2.inRange(hsv, np.array([20, 70, 80]), np.array([36, 255, 255]))
        )
        # C) Rust Pustules (Orange, cinnamon-red spots)
        rust_mask = cv2.bitwise_and(
            leaf_mask,
            cv2.inRange(hsv, np.array([5, 110, 80]), np.array([18, 255, 255]))
        )

        # Combine diseased pixels
        disease_mask = cv2.bitwise_or(necrosis_mask, chlorosis_mask)
        disease_mask = cv2.bitwise_or(disease_mask, rust_mask)

        # Count pixels and metrics
        necrosis_pixels = int(np.count_nonzero(necrosis_mask))
        chlorosis_pixels = int(np.count_nonzero(chlorosis_mask))
        rust_pixels = int(np.count_nonzero(rust_mask))
        disease_pixels = int(np.count_nonzero(disease_mask))

        infection_ratio = disease_pixels / max(total_leaf_pixels, 1)
        infected_area_pct = round(min(100.0, infection_ratio * 100), 2)
        health_index = round(max(0.0, 100.0 - infected_area_pct), 2)

        # Determine severity level
        if infected_area_pct < 3.5:
            severity = "Healthy / Minimal"
            severity_color = "#10B981"  # Emerald
        elif infected_area_pct < 15.0:
            severity = "Mild Infection"
            severity_color = "#F59E0B"  # Amber
        elif infected_area_pct < 35.0:
            severity = "Moderate Infection"
            severity_color = "#F97316"  # Orange
        else:
            severity = "Severe Infection"
            severity_color = "#EF4444"  # Red

        # 3. Lesion Morphology Analysis
        contours, _ = cv2.findContours(disease_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        significant_lesions = [c for c in contours if cv2.contourArea(c) > 35]
        spot_count = len(significant_lesions)

        aspect_ratios = []
        circularities = []
        for c in significant_lesions:
            x, y, cw, ch = cv2.boundingRect(c)
            aspect_ratios.append(max(cw, ch) / (min(cw, ch) + 1e-4))
            area = cv2.contourArea(c)
            perimeter = cv2.arcLength(c, True)
            if perimeter > 0:
                circularities.append(4 * np.pi * (area / (perimeter * perimeter)))

        mean_aspect_ratio = float(np.mean(aspect_ratios)) if aspect_ratios else 1.0
        mean_circularity = float(np.mean(circularities)) if circularities else 1.0

        # Texture gradient via Laplacian
        gray = cv2.cvtColor(img_resized, cv2.COLOR_RGB2GRAY)
        laplacian_var = float(cv2.Laplacian(gray, cv2.CV_64F).var())

        # 4. Generate Visual Saliency / Heatmap Overlay
        heatmap_overlay, contour_vis = self._generate_visualizations(
            img_resized, disease_mask, necrosis_mask, chlorosis_mask, rust_mask, significant_lesions
        )

        # 5. Probabilistic Classification & Diagnosis Matching
        predictions = self._classify_pathology(
            infected_area_pct=infected_area_pct,
            necrosis_ratio=necrosis_pixels / max(disease_pixels, 1),
            chlorosis_ratio=chlorosis_pixels / max(disease_pixels, 1),
            rust_ratio=rust_pixels / max(disease_pixels, 1),
            spot_count=spot_count,
            mean_aspect_ratio=mean_aspect_ratio,
            laplacian_var=laplacian_var,
            crop_hint=crop_hint
        )

        top_pred = predictions[0]
        disease_info = get_disease_info(top_pred["key"])

        return {
            "top_diagnosis": {
                "key": top_pred["key"],
                "disease_name": disease_info["disease_name"],
                "crop": disease_info["crop"],
                "pathogen": disease_info["pathogen"],
                "confidence": top_pred["confidence"],
                "severity": severity,
                "severity_color": severity_color
            },
            "metrics": {
                "health_index": health_index,
                "infected_area_pct": infected_area_pct,
                "total_leaf_pixels": total_leaf_pixels,
                "lesion_spot_count": spot_count,
                "necrosis_pct": round((necrosis_pixels / max(total_leaf_pixels, 1)) * 100, 2),
                "chlorosis_pct": round((chlorosis_pixels / max(total_leaf_pixels, 1)) * 100, 2),
                "rust_pct": round((rust_pixels / max(total_leaf_pixels, 1)) * 100, 2),
                "leaf_texture_score": round(laplacian_var, 1)
            },
            "visualizations": {
                "original_rgb": img_resized,
                "heatmap_overlay": heatmap_overlay,
                "contour_vis": contour_vis
            },
            "treatment_profile": disease_info,
            "all_predictions": predictions[:5]
        }

    def _generate_visualizations(
        self,
        rgb_img: np.ndarray,
        disease_mask: np.ndarray,
        necrosis_mask: np.ndarray,
        chlorosis_mask: np.ndarray,
        rust_mask: np.ndarray,
        contours: List[np.ndarray]
    ) -> Tuple[np.ndarray, np.ndarray]:
        """Creates saliency heatmap and bounding/contour inspection overlays."""
        # Multi-intensity pathology distance map for smooth heat representation
        dist_map = cv2.distanceTransform(disease_mask, cv2.DIST_L2, 5)
        if dist_map.max() > 0:
            dist_norm = (dist_map / dist_map.max() * 255).astype(np.uint8)
        else:
            dist_norm = disease_mask.copy()

        # Gaussian blur for radiant thermal glow
        heat_blur = cv2.GaussianBlur(dist_norm, (15, 15), 0)
        heatmap_colored = cv2.applyColorMap(heat_blur, cv2.COLORMAP_JET)
        heatmap_rgb = cv2.cvtColor(heatmap_colored, cv2.COLOR_BGR2RGB)

        # Blend with original image only over active zones
        alpha = 0.55
        overlay = rgb_img.copy()
        mask_3ch = cv2.cvtColor(disease_mask, cv2.COLOR_GRAY2RGB) > 0
        overlay[mask_3ch] = cv2.addWeighted(rgb_img, 1 - alpha, heatmap_rgb, alpha, 0)[mask_3ch]

        # Contour overlay with lesion markers
        contour_canvas = rgb_img.copy()
        for c in contours:
            cv2.drawContours(contour_canvas, [c], -1, (255, 60, 0), 2)
            # Add bounding box
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(contour_canvas, (x, y), (x + w, y + h), (255, 215, 0), 1)

        return overlay, contour_canvas

    def _classify_pathology(
        self,
        infected_area_pct: float,
        necrosis_ratio: float,
        chlorosis_ratio: float,
        rust_ratio: float,
        spot_count: int,
        mean_aspect_ratio: float,
        laplacian_var: float,
        crop_hint: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Calculates probabilistic match across the disease portfolio."""
        scores: Dict[str, float] = {}

        for key, info in DISEASE_DATABASE.items():
            score = 10.0
            crop_name = info["crop"].lower()

            # Prior boost if user specified crop or crop matches hint
            if crop_hint and crop_hint.lower() != "auto-detect (all crops)":
                if crop_hint.lower() in crop_name or crop_name == "all crops":
                    score += 40.0
                else:
                    score -= 50.0

            # 1. Healthy Plant Profile
            if key == "healthy_crop":
                if infected_area_pct < 4.0:
                    score += 80.0 - (infected_area_pct * 15.0)
                else:
                    score -= (infected_area_pct * 3.0)
                scores[key] = max(1.0, score)
                continue

            # 2. Diseased profiles require some infection
            if infected_area_pct < 2.0:
                scores[key] = 1.0
                continue

            score += min(35.0, infected_area_pct * 1.2)

            # Rust Diseases (Wheat Rust, Corn Common Rust)
            if "rust" in key:
                if rust_ratio > 0.25:
                    score += 45.0 * rust_ratio
                if spot_count > 15:
                    score += 15.0

            # Elongated Blights (Corn Northern Leaf Blight)
            if key == "corn_northern_leaf_blight":
                if mean_aspect_ratio > 2.2:
                    score += 35.0
                if necrosis_ratio > 0.4:
                    score += 20.0

            # Concentric / Target Spots (Early Blight)
            if "early_blight" in key:
                if chlorosis_ratio > 0.25 and necrosis_ratio > 0.35:
                    score += 30.0
                if 2 <= spot_count <= 25:
                    score += 15.0

            # Water-soaked / rapid blight (Late Blight)
            if "late_blight" in key:
                if necrosis_ratio > 0.45:
                    score += 30.0
                if infected_area_pct > 15.0:
                    score += 20.0

            # Rice Blast (diamond/spindle)
            if key == "rice_blast":
                if mean_aspect_ratio > 1.8 and spot_count > 5:
                    score += 30.0

            # Apple Scab / Grape Black Rot
            if key in ["apple_scab", "grape_black_rot"]:
                if spot_count > 8 and necrosis_ratio > 0.5:
                    score += 25.0

            # Cotton Bacterial Blight (angular leaf spot)
            if key == "cotton_bacterial_blight":
                if necrosis_ratio > 0.3 and chlorosis_ratio > 0.2:
                    score += 25.0

            scores[key] = max(1.0, score)

        # Softmax normalization
        score_keys = list(scores.keys())
        raw_vals = np.array([scores[k] for k in score_keys], dtype=np.float64)
        # Temperature scaling
        temperature = 12.0
        exp_vals = np.exp((raw_vals - np.max(raw_vals)) / (temperature / 5.0))
        probs = exp_vals / np.sum(exp_vals)

        results = []
        for i, k in enumerate(score_keys):
            conf_pct = round(float(probs[i]) * 100, 1)
            results.append({
                "key": k,
                "confidence": conf_pct,
                "raw_score": float(raw_vals[i])
            })

        results.sort(key=lambda x: x["confidence"], reverse=True)
        return results

    def query_gemini_vision(
        self,
        image_bytes: bytes,
        api_key: str,
        crop_hint: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Optional deep multimodal reasoning using Google Gemini API.
        Called if user activates Gemini Vision with their API key.
        """
        try:
            from google import genai
            from google.genai import types

            client = genai.Client(api_key=api_key)
            prompt = (
                f"You are CropGuard's Senior Agricultural Plant Pathologist. "
                f"Analyze this crop/plant leaf image carefully. "
                f"Context/Crop hint: {crop_hint or 'Auto-detect'}.\n"
                f"Provide a structured assessment covering:\n"
                f"1. Crop Identified and Disease Diagnosis (or Healthy).\n"
                f"2. Causal Pathogen (Fungus/Bacteria/Virus/Nutrient Deficiency).\n"
                f"3. Observable Visual Symptoms and Estimated Severity (Mild/Moderate/Severe).\n"
                f"4. Immediate Chemical Fungicide/Pesticide Prescriptions (dosage per liter and interval).\n"
                f"5. Organic / Biological Control Options.\n"
                f"6. Fertilizer & Nutrient Management to help the plant recover fast and maximize yield.\n"
                f"Keep it professional, highly practical for farmers, and structured."
            )

            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=[
                    types.Part.from_bytes(
                        data=image_bytes,
                        mime_type="image/jpeg",
                    ),
                    prompt,
                ],
            )
            return {
                "success": True,
                "analysis_text": response.text,
                "model_used": "gemini-2.5-flash"
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
