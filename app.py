"""
CropGuard AI - Precision Crop Disease Detection, Fertilizer Advisory & Yield Booster Platform.
Features 3D WebGL Topography, 3D Elevation Meshes, 3D Yield Response Surfaces,
and 3D Glassmorphism Frontend.
"""

import sys
import os
from pathlib import Path

# Ensure project root & engine directories are in Python path (critical for Streamlit Cloud deployment)
ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))
ENGINE_DIR = ROOT_DIR / "engine"
if str(ENGINE_DIR) not in sys.path:
    sys.path.insert(0, str(ENGINE_DIR))

import io
import json
import cv2
import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components

try:
    from engine.vision_classifier import CropVisionClassifier
    from engine.disease_db import DISEASE_DATABASE, get_disease_info, list_supported_crops
    from engine.yield_predictor import CropYieldPredictor, CROP_YIELD_BASELINES
    from engine.growth_booster import get_growth_protocol
    from engine.pdf_report import generate_cropguard_pdf
    from engine.visualizer_3d import (
        generate_3d_leaf_surface_plot,
        generate_3d_yield_surface_plot,
        get_webgl_leaf_3d_html
    )
except ModuleNotFoundError:
    try:
        from vision_classifier import CropVisionClassifier
        from disease_db import DISEASE_DATABASE, get_disease_info, list_supported_crops
        from yield_predictor import CropYieldPredictor, CROP_YIELD_BASELINES
        from growth_booster import get_growth_protocol
        from pdf_report import generate_cropguard_pdf
        from visualizer_3d import (
            generate_3d_leaf_surface_plot,
            generate_3d_yield_surface_plot,
            get_webgl_leaf_3d_html
        )
    except Exception as inner_err:
        st.error(f"⚠️ CropGuard Engine Loading Error: {inner_err}")
        st.info("Please ensure the 'engine/' directory was uploaded to your GitHub repository alongside app.py.")
        st.stop()

# Page Configuration
st.set_page_config(
    page_title="CropGuard AI | 3D Crop Disease & Yield Optimizer",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-End 3D & Glassmorphic Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Ambient Background Gradient */
    .stApp {
        background: radial-gradient(circle at 10% 20%, #F0FDF4 0%, #F8FAFC 45%, #EFF6FF 100%);
    }

    /* 3D Floating Header */
    .cropguard-hero-3d {
        position: relative;
        background: linear-gradient(135deg, #022c22 0%, #064e3b 40%, #047857 75%, #059669 100%);
        color: white;
        padding: 32px 36px;
        border-radius: 20px;
        margin-bottom: 28px;
        box-shadow: 0 20px 35px -8px rgba(6, 78, 59, 0.3),
                    0 10px 15px -3px rgba(0, 0, 0, 0.1),
                    inset 0 1px 1px rgba(255, 255, 255, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.15);
        overflow: hidden;
    }
    .cropguard-hero-3d::after {
        content: '';
        position: absolute;
        top: -50%;
        right: -10%;
        width: 320px;
        height: 320px;
        background: radial-gradient(circle, rgba(52, 211, 153, 0.25) 0%, rgba(52, 211, 153, 0) 70%);
        border-radius: 50%;
        pointer-events: none;
    }
    .cropguard-hero-title {
        font-size: 2.3rem;
        font-weight: 800;
        letter-spacing: -0.8px;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 14px;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    .cropguard-hero-subtitle {
        font-size: 1.05rem;
        color: #A7F3D0;
        margin-top: 8px;
        margin-bottom: 0;
        max-width: 850px;
        line-height: 1.5;
        font-weight: 500;
    }

    /* 3D Glassmorphic Cards with Perspective Hover */
    .card-3d {
        perspective: 1200px;
        background: rgba(255, 255, 255, 0.88);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.85);
        padding: 22px;
        box-shadow: 0 10px 25px -5px rgba(6, 78, 59, 0.06),
                    0 8px 10px -6px rgba(0, 0, 0, 0.04),
                    inset 0 1px 1px rgba(255, 255, 255, 0.9);
        transition: transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.25s ease;
        margin-bottom: 18px;
    }
    .card-3d:hover {
        transform: translateY(-5px) scale(1.01);
        box-shadow: 0 20px 35px -8px rgba(6, 78, 59, 0.15),
                    0 12px 15px -8px rgba(0, 0, 0, 0.08),
                    inset 0 1px 2px rgba(255, 255, 255, 1);
    }

    /* 3D KPI Metric Card */
    .kpi-3d {
        position: relative;
        background: white;
        border-radius: 16px;
        padding: 20px 22px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 8px 20px -4px rgba(15, 23, 42, 0.06),
                    0 4px 6px -2px rgba(0, 0, 0, 0.03),
                    inset 0 1px 0 rgba(255, 255, 255, 0.8);
        transition: all 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
        overflow: hidden;
    }
    .kpi-3d:hover {
        transform: translateY(-4px);
        box-shadow: 0 16px 28px -6px rgba(6, 78, 59, 0.12),
                    0 6px 12px -4px rgba(0, 0, 0, 0.06);
        border-color: #CBD5E1;
    }
    .kpi-3d::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, #10B981, #059669);
    }
    .kpi-title {
        font-size: 0.82rem;
        font-weight: 700;
        color: #64748B;
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }
    .kpi-val {
        font-size: 2.1rem;
        font-weight: 800;
        color: #0F172A;
        margin-top: 6px;
        letter-spacing: -0.5px;
    }
    .kpi-tag {
        font-size: 0.85rem;
        font-weight: 600;
        margin-top: 6px;
        display: flex;
        align-items: center;
        gap: 4px;
    }

    /* 3D Laser Scanning HUD Box */
    .scan-viewfinder {
        position: relative;
        border-radius: 14px;
        overflow: hidden;
        border: 2px solid #10B981;
        box-shadow: 0 0 25px rgba(16, 185, 129, 0.25);
    }
    .scan-beam {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, transparent, #34D399, #10B981, #34D399, transparent);
        box-shadow: 0 0 15px #34D399, 0 0 25px #10B981;
        animation: scanAnim 2.8s ease-in-out infinite alternate;
        pointer-events: none;
        z-index: 10;
    }
    @keyframes scanAnim {
        0% { top: 2%; opacity: 0.85; }
        100% { top: 96%; opacity: 0.85; }
    }

    /* 3D Prescription Category Cards */
    .rx-box-3d {
        background: white;
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 16px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 6px 16px -2px rgba(0,0,0,0.04);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .rx-box-3d:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 24px -4px rgba(0,0,0,0.08);
    }
    .rx-box-title {
        font-size: 1.12rem;
        font-weight: 700;
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 12px;
        padding-bottom: 8px;
        border-bottom: 1px solid #F1F5F9;
    }

    /* 3D Floating Stage Pills */
    .stage-pill-3d {
        background: linear-gradient(135deg, #F8FAFC 0%, #FFFFFF 100%);
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.03);
    }

    /* Status Badges */
    .badge-3d-healthy {
        background: linear-gradient(135deg, #10B981 0%, #059669 100%);
        color: white;
        padding: 5px 14px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.88rem;
        box-shadow: 0 4px 10px rgba(16, 185, 129, 0.35);
    }
    .badge-3d-mild {
        background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%);
        color: white;
        padding: 5px 14px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.88rem;
        box-shadow: 0 4px 10px rgba(245, 158, 11, 0.35);
    }
    .badge-3d-moderate {
        background: linear-gradient(135deg, #F97316 0%, #EA580C 100%);
        color: white;
        padding: 5px 14px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.88rem;
        box-shadow: 0 4px 10px rgba(249, 115, 22, 0.35);
    }
    .badge-3d-severe {
        background: linear-gradient(135deg, #EF4444 0%, #DC2626 100%);
        color: white;
        padding: 5px 14px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.88rem;
        box-shadow: 0 4px 10px rgba(239, 68, 68, 0.35);
    }
</style>
""", unsafe_allow_html=True)

# Session State Initialization
if "classifier" not in st.session_state:
    st.session_state.classifier = CropVisionClassifier()
if "predictor" not in st.session_state:
    st.session_state.predictor = CropYieldPredictor()
if "last_diagnosis" not in st.session_state:
    st.session_state.last_diagnosis = None
if "last_yield" not in st.session_state:
    st.session_state.last_yield = None
if "selected_sample" not in st.session_state:
    st.session_state.selected_sample = None

# 3D Floating Header
st.markdown("""
<div class="cropguard-hero-3d">
    <div class="cropguard-hero-title">
        <span>🌿 CropGuard AI</span>
        <span style="background: rgba(255,255,255,0.2); font-size: 0.75rem; padding: 4px 10px; border-radius: 12px; font-weight: 600; text-shadow:none;">3D PRECISION PLATFORM</span>
    </div>
    <p class="cropguard-hero-subtitle">
        Interactive 3D Leaf Pathology Topography, Computer Vision Disease Diagnostics, Targeted Chemical/Organic Prescriptions & Yield Maximization.
    </p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    banner_path = os.path.join(ROOT_DIR, "assets", "cropguard_banner.png")
    if os.path.exists(banner_path):
        st.image(banner_path, use_container_width=True)
    else:
        sample_fallback = os.path.join(ROOT_DIR, "samples", "healthy_tomato.jpg")
        st.image(sample_fallback if os.path.exists(sample_fallback) else "https://images.unsplash.com/photo-1592417817098-8f3d6eb22509?auto=format&fit=crop&w=600&q=80", caption="CropGuard Precision Agro-Tech", use_container_width=True)

    # Home & Dashboard Navigation Buttons
    nav_btn_col1, nav_btn_col2 = st.columns(2)
    with nav_btn_col1:
        if st.button("🏠 Home Reset", use_container_width=True, help="Reset session and return to fresh home state"):
            st.session_state.last_diagnosis = None
            st.session_state.selected_sample = None
            st.rerun()
    with nav_btn_col2:
        st.link_button("🌐 Return Home", "http://localhost:5000", use_container_width=True, help="Go back to the Full-Stack Web Dashboard (Port 5000)")

    st.markdown("---")
    st.markdown("### 🚜 Farm & Target Crop")

    crop_options = ["Auto-Detect (All Crops)"] + list(CROP_YIELD_BASELINES.keys())
    selected_crop_filter = st.selectbox(
        "Crop Family Filter:",
        options=crop_options,
        index=0,
        help="Filter detection for a specific crop or allow CropGuard to auto-detect."
    )

    st.markdown("---")
    st.markdown("### 👨‍🌾 Grower & Field Profile")
    farmer_name = st.text_input("Grower / Farmer Name:", value="Ramesh Patel")
    farm_location = st.text_input("Block / Field Code:", value="Block 4B - River Valley")

    st.markdown("---")
    st.markdown("### 🤖 Diagnostic Engine")
    engine_mode = st.radio(
        "AI Diagnostic Mode:",
        ["Offline Computer Vision (Default)", "Gemini Multimodal Vision AI"],
        index=0
    )
    gemini_key = ""
    if engine_mode == "Gemini Multimodal Vision AI":
        gemini_key = st.text_input("Gemini API Key:", type="password", help="Enter Google Gemini API key for multimodal second-opinion.")
        if not gemini_key:
            st.info("Tip: Leave blank to run 100% offline via local computer vision engine.")

    st.markdown("---")
    st.markdown("#### 🌟 3D Features Active")
    st.markdown("""
    - 🌐 **Interactive 3D WebGL Topography**
    - 🏔️ **3D Scientific Elevation Meshes**
    - 📊 **3D Agronomic Yield Landscape**
    - 📑 **Official Prescription PDF**
    """)

# Navigation Tabs
tab_detect, tab_yield, tab_booster, tab_encyclopedia, tab_pdf = st.tabs([
    "🩺 AI Disease Diagnosis & 3D Topography",
    "📈 Yield Forecaster & 3D Landscape",
    "🚀 'Grow Fast & Large' Protocols",
    "📖 Crop Disease Encyclopedia",
    "📄 Export Agronomy Report"
])

# ==========================================
# TAB 1: AI DISEASE DIAGNOSIS & 3D TOPOGRAPHY
# ==========================================
with tab_detect:
    st.markdown("### 🍃 Upload or Capture Crop Leaf Image")
    st.write("Upload a crop leaf photograph or select an instant sample to analyze pathology, segment lesions, inspect in 3D, and receive exact treatment prescriptions.")

    # 1-Click Test Gallery
    samples_dir = os.path.join(os.path.dirname(__file__), "samples")
    sample_files = {
        "Tomato Late Blight": "tomato_late_blight.jpg",
        "Tomato Early Blight": "tomato_early_blight.jpg",
        "Potato Early Blight": "potato_early_blight.jpg",
        "Corn Common Rust": "corn_common_rust.jpg",
        "Rice Leaf Blast": "rice_leaf_blast.jpg",
        "Wheat Yellow Rust": "wheat_yellow_rust.jpg",
        "Healthy Tomato": "healthy_tomato.jpg",
        "Healthy Wheat": "healthy_wheat.jpg"
    }

    st.markdown("##### ⚡ Quick-Test Gallery (Instant 1-Click Samples):")
    sample_cols = st.columns(len(sample_files))
    for idx, (label, fname) in enumerate(sample_files.items()):
        with sample_cols[idx]:
            if st.button(label, key=f"btn_{fname}", use_container_width=True):
                st.session_state.selected_sample = os.path.join(samples_dir, fname)

    # Input Method
    input_col1, input_col2 = st.columns([1, 1])
    with input_col1:
        uploaded_file = st.file_uploader(
            "Upload leaf image (JPG, PNG, WEBP):",
            type=["jpg", "jpeg", "png", "webp"]
        )
    with input_col2:
        camera_file = st.camera_input("Or capture live leaf via camera:")

    active_image = None
    if uploaded_file is not None:
        active_image = Image.open(uploaded_file)
        st.session_state.selected_sample = None
    elif camera_file is not None:
        active_image = Image.open(camera_file)
        st.session_state.selected_sample = None
    elif st.session_state.selected_sample and os.path.exists(st.session_state.selected_sample):
        active_image = Image.open(st.session_state.selected_sample)

    if active_image is not None:
        st.markdown("---")
        with st.spinner("Executing 3D tissue segmentation and pathological analysis..."):
            diagnosis = st.session_state.classifier.analyze_leaf_image(
                active_image,
                crop_hint=selected_crop_filter
            )
            st.session_state.last_diagnosis = diagnosis

        top = diagnosis["top_diagnosis"]
        metrics = diagnosis["metrics"]
        profile = diagnosis["treatment_profile"]
        vis = diagnosis["visualizations"]

        # 3D KPI Metric Cards
        st.markdown(f"## 📋 Clinical Diagnosis: **{top['disease_name']}**")

        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        with kpi1:
            st.markdown(f"""
            <div class="kpi-3d">
                <div class="kpi-title">Health Index</div>
                <div class="kpi-val">{metrics['health_index']}%</div>
                <div class="kpi-tag" style="color: #10B981;">✓ Intact Active Lamina</div>
            </div>
            """, unsafe_allow_html=True)

        with kpi2:
            st.markdown(f"""
            <div class="kpi-3d">
                <div class="kpi-title">Infection Surface Area</div>
                <div class="kpi-val">{metrics['infected_area_pct']}%</div>
                <div class="kpi-tag" style="color: #EF4444;">⚠ Necrotic / Chlorotic Area</div>
            </div>
            """, unsafe_allow_html=True)

        with kpi3:
            badge_class = "badge-3d-healthy" if "Healthy" in top["severity"] else ("badge-3d-mild" if "Mild" in top["severity"] else ("badge-3d-moderate" if "Moderate" in top["severity"] else "badge-3d-severe"))
            st.markdown(f"""
            <div class="kpi-3d">
                <div class="kpi-title">Severity Rating</div>
                <div class="kpi-val" style="font-size: 1.5rem; padding-top: 6px;">
                    <span class="{badge_class}">{top['severity']}</span>
                </div>
                <div class="kpi-tag" style="color: #64748B;">{metrics['lesion_spot_count']} active lesion clusters</div>
            </div>
            """, unsafe_allow_html=True)

        with kpi4:
            st.markdown(f"""
            <div class="kpi-3d">
                <div class="kpi-title">Diagnostic Confidence</div>
                <div class="kpi-val">{top['confidence']}%</div>
                <div class="kpi-tag" style="color: #059669;">★ Ensemble CV Match</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br/>", unsafe_allow_html=True)

        # 3D vs 2D Visualization Switcher
        st.markdown("### 🔬 Multi-Dimensional Pathology Inspection")

        view_mode = st.radio(
            "Select Inspection Mode:",
            [
                "🌐 Interactive 3D WebGL Topography (Rotate & Zoom)",
                "📸 2D Pathology Thermal Heatmaps & Contours",
                "🏔️ 3D Scientific Elevation Mesh"
            ],
            horizontal=True
        )

        # Extract masks for 3D viewers
        rgb_arr = vis["original_rgb"]
        try:
            bgr = cv2.cvtColor(rgb_arr, cv2.COLOR_RGB2BGR)
            hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
            lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)
            l_channel = lab[:, :, 0]

            lower_leaf = np.array([15, 25, 25])
            upper_leaf = np.array([100, 255, 255])
            leaf_mask = cv2.inRange(hsv, lower_leaf, upper_leaf)
            necrosis_mask = cv2.bitwise_and(leaf_mask, cv2.inRange(l_channel, 0, 85))
            rust_mask = cv2.bitwise_and(leaf_mask, cv2.inRange(hsv, np.array([5, 110, 80]), np.array([18, 255, 255])))
            disease_mask = cv2.bitwise_or(necrosis_mask, rust_mask)
        except Exception:
            h, w = rgb_arr.shape[:2]
            disease_mask = np.zeros((h, w), dtype=np.uint8)
            necrosis_mask = np.zeros((h, w), dtype=np.uint8)
            rust_mask = np.zeros((h, w), dtype=np.uint8)

        if "Interactive 3D WebGL" in view_mode:
            st.markdown("""
            <div class="card-3d" style="padding: 10px; background: #0B1120;">
            """, unsafe_allow_html=True)
            webgl_html = get_webgl_leaf_3d_html(rgb_arr, disease_mask, necrosis_mask, rust_mask)
            components.html(webgl_html, height=450)
            st.markdown("</div>", unsafe_allow_html=True)
            st.caption("💡 Click and drag with mouse to orbit/rotate the leaf in 3D space. Scroll with mouse wheel to zoom. Watch necrotic lesions form crater depressions while rust pustules erupt upwards!")

        elif "2D Pathology Thermal" in view_mode:
            vis_col1, vis_col2, vis_col3 = st.columns(3)
            with vis_col1:
                st.markdown("""<div class="scan-viewfinder"><div class="scan-beam"></div>""", unsafe_allow_html=True)
                st.image(vis["original_rgb"], caption="Original Leaf Sample (Active Laser Scan)", use_container_width=True)
                st.markdown("</div>", unsafe_allow_html=True)
            with vis_col2:
                st.image(vis["heatmap_overlay"], caption="Pathology Thermal Saliency Heatmap", use_container_width=True)
            with vis_col3:
                st.image(vis["contour_vis"], caption="Lesion Contours & Boundary Localization", use_container_width=True)

        elif "3D Scientific Elevation" in view_mode:
            with st.spinner("Rendering 3D scientific elevation surface..."):
                fig_3d = generate_3d_leaf_surface_plot(rgb_arr, disease_mask, necrosis_mask, rust_mask)
                st.pyplot(fig_3d, use_container_width=True)
            st.caption("Scientific 3D topography profile showing morphological lesion depth craters and cellular breakdown zones.")

        # Prescriptions
        st.markdown("---")
        st.markdown("### 💊 Targeted Agronomic Prescription & Recovery Schedule")

        rx_col1, rx_col2 = st.columns(2)
        with rx_col1:
            st.markdown("""
            <div class="rx-box-3d" style="border-top: 4px solid #2563EB;">
                <div class="rx-box-title" style="color: #1E40AF;">
                    <span>🧪 Chemical Curative & Protectant Prescriptions</span>
                </div>
            """, unsafe_allow_html=True)
            for chem in profile.get("chemical_treatments", []):
                st.markdown(f"- **{chem}**")
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("""
            <div class="rx-box-3d" style="border-top: 4px solid #059669;">
                <div class="rx-box-title" style="color: #065F46;">
                    <span>🌱 Biological & Organic Alternatives</span>
                </div>
            """, unsafe_allow_html=True)
            for org in profile.get("organic_treatments", []):
                st.markdown(f"- **{org}**")
            st.markdown("</div>", unsafe_allow_html=True)

        with rx_col2:
            st.markdown("""
            <div class="rx-box-3d" style="border-top: 4px solid #D97706;">
                <div class="rx-box-title" style="color: #92400E;">
                    <span>⚡ Rapid Fertilizer Recovery & Cell Strengthening</span>
                </div>
            """, unsafe_allow_html=True)
            for fert in profile.get("growth_and_fertilizer_recovery", []):
                st.markdown(f"- **{fert}**")
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("""
            <div class="rx-box-3d" style="border-top: 4px solid #7C3AED;">
                <div class="rx-box-title" style="color: #5B21B6;">
                    <span>🛡️ Long-term Agronomic Cultural Sanitation</span>
                </div>
            """, unsafe_allow_html=True)
            for prev in profile.get("prevention_steps", []):
                st.markdown(f"- **{prev}**")
            st.markdown("</div>", unsafe_allow_html=True)

        # Gemini Multimodal AI Second Opinion
        if engine_mode == "Gemini Multimodal Vision AI" and gemini_key:
            st.markdown("---")
            st.markdown("### 🧠 Multimodal Gemini Vision AI Reasoning")
            with st.spinner("Consulting Gemini multimodal agricultural model..."):
                buf = io.BytesIO()
                active_image.save(buf, format="JPEG")
                gemini_res = st.session_state.classifier.query_gemini_vision(
                    buf.getvalue(),
                    api_key=gemini_key,
                    crop_hint=selected_crop_filter
                )
                if gemini_res.get("success"):
                    st.success(f"Verified by {gemini_res.get('model_used')}:")
                    st.markdown(gemini_res.get("analysis_text"))
                else:
                    st.error(f"Gemini API Error: {gemini_res.get('error')}")

    else:
        st.info("👆 Upload an image or click any of the 8 sample crop leaves above to run an instant diagnosis with 3D pathology modeling!")


# ==========================================
# TAB 2: YIELD FORECASTER & 3D LANDSCAPE
# ==========================================
with tab_yield:
    st.markdown("### 📈 Precision Crop Yield Forecaster & 3D Landscape")
    st.write("Model harvest yield potential based on soil chemistry, irrigation, microclimate, and explore the **3D Yield Response Landscape**.")

    default_crop_name = "Tomato"
    default_disease_pct = 0.0
    if st.session_state.last_diagnosis:
        diag_crop = st.session_state.last_diagnosis["top_diagnosis"]["crop"]
        if diag_crop in CROP_YIELD_BASELINES:
            default_crop_name = diag_crop
        default_disease_pct = float(st.session_state.last_diagnosis["metrics"]["infected_area_pct"])

    y_col1, y_col2 = st.columns([1, 1])
    with y_col1:
        st.markdown("#### 1. Field Soil Chemistry")
        pred_crop = st.selectbox(
            "Target Crop:",
            list(CROP_YIELD_BASELINES.keys()),
            index=list(CROP_YIELD_BASELINES.keys()).index(default_crop_name) if default_crop_name in CROP_YIELD_BASELINES else 0
        )
        land_area = st.slider("Total Land Area (Acres):", min_value=0.5, max_value=100.0, value=2.5, step=0.5)

        st.markdown("##### Soil Nutrient Reserves (kg/acre):")
        n_val = st.slider("Nitrogen (N):", min_value=10, max_value=200, value=int(CROP_YIELD_BASELINES[pred_crop]["ideal_n"] * 0.9))
        p_val = st.slider("Phosphorus (P):", min_value=5, max_value=120, value=int(CROP_YIELD_BASELINES[pred_crop]["ideal_p"] * 0.85))
        k_val = st.slider("Potassium (K):", min_value=10, max_value=200, value=int(CROP_YIELD_BASELINES[pred_crop]["ideal_k"] * 0.8))

        soil_ph = st.slider("Soil pH Level:", min_value=4.5, max_value=9.0, value=6.5, step=0.1)
        oc_pct = st.slider("Soil Organic Carbon (%):", min_value=0.2, max_value=2.0, value=0.75, step=0.05)

    with y_col2:
        st.markdown("#### 2. Environmental & Stress Inputs")
        irrig_choice = st.selectbox(
            "Irrigation Management System:",
            [
                "Precision Drip / Fertigation",
                "Canal / Flood Irrigation (Adequate)",
                "Rainfed (Good Rain)",
                "Rainfed / Moisture Stressed",
                "Waterlogged / Poor Drainage"
            ],
            index=0
        )
        avg_temp = st.slider("Average Daytime Temperature (°C):", min_value=10.0, max_value=45.0, value=25.0, step=0.5)

        disease_input = st.slider(
            "Current Leaf Pathology / Disease Damage (%):",
            min_value=0.0,
            max_value=100.0,
            value=default_disease_pct,
            step=1.0,
            help="Pre-populated from diagnosis if performed in Tab 1."
        )

        apply_booster = st.checkbox("🚀 Activate CropGuard Precision Growth Booster Protocol", value=True)

    # Compute Yield
    yield_results = st.session_state.predictor.predict_yield(
        crop=pred_crop,
        land_area_acres=land_area,
        nitrogen=n_val,
        phosphorus=p_val,
        potassium=k_val,
        soil_ph=soil_ph,
        organic_carbon_pct=oc_pct,
        irrigation_type=irrig_choice,
        avg_temp=avg_temp,
        disease_damage_pct=disease_input,
        apply_growth_booster=apply_booster
    )
    st.session_state.last_yield = yield_results

    st.markdown("---")
    st.markdown("### 📊 Harvest Yield & Revenue Forecast")

    yp_1, yp_2, yp_3, yp_4 = st.columns(4)
    with yp_1:
        st.markdown(f"""
        <div class="kpi-3d">
            <div class="kpi-title">Baseline Yield Rate</div>
            <div class="kpi-val">{yield_results['baseline_yield_per_acre']}</div>
            <div class="kpi-tag" style="color: #64748B;">{yield_results['unit']}</div>
        </div>
        """, unsafe_allow_html=True)

    with yp_2:
        st.markdown(f"""
        <div class="kpi-3d">
            <div class="kpi-title">Optimized Yield Rate</div>
            <div class="kpi-val" style="color: #047857;">{yield_results['boosted_yield_per_acre']}</div>
            <div class="kpi-tag" style="color: #10B981;">+{yield_results['yield_gain_pct']}% Potential Uplift</div>
        </div>
        """, unsafe_allow_html=True)

    with yp_3:
        st.markdown(f"""
        <div class="kpi-3d">
            <div class="kpi-title">Total Farm Harvest</div>
            <div class="kpi-val">{yield_results['total_boosted_yield']}</div>
            <div class="kpi-tag" style="color: #10B981;">+{yield_results['net_gain_amount']} Extra Output</div>
        </div>
        """, unsafe_allow_html=True)

    with yp_4:
        econ = yield_results['economic_projection']
        st.markdown(f"""
        <div class="kpi-3d">
            <div class="kpi-title">Net Revenue Uplift</div>
            <div class="kpi-val" style="color: #2563EB;">+${econ['additional_profit']:,}</div>
            <div class="kpi-tag" style="color: #2563EB;">Precision Agronomy ROI</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)

    # 3D Yield Response Landscape
    st.markdown("#### 🌐 3D Agronomic Yield Response Landscape")
    st.write("Visualizes how adjusting Nitrogen (N) and Potassium (K) shifts your field along the 3D yield production summit.")

    with st.spinner("Simulating 3D response topology..."):
        fig_yield_3d = generate_3d_yield_surface_plot(
            crop=pred_crop,
            base_n=float(n_val),
            base_k=float(k_val),
            predictor_fn=st.session_state.predictor.predict_yield,
            soil_ph=soil_ph,
            oc_pct=oc_pct
        )
        st.pyplot(fig_yield_3d, use_container_width=True)

    # Limiting Factors
    st.markdown("#### ⚖️ Liebig's Law of the Minimum - Limiting Factors")
    st.info(f"🚨 **Primary Yield-Limiting Factor:** **{yield_results['primary_limiting_factor']}**. Improving this variable produces the fastest marginal yield gains.")

    factors_df = pd.DataFrame(yield_results["factors_breakdown"])
    factors_df["Efficiency %"] = (factors_df["score"] * 100).round(1)
    st.bar_chart(factors_df.set_index("factor")[["Efficiency %"]])


# ==========================================
# TAB 3: GROW FAST & LARGE PROTOCOLS
# ==========================================
with tab_booster:
    st.markdown("### 🚀 Science-Backed Protocols to Make Crops Grow Fast, Large & High-Yielding")
    st.write("Agronomic protocols engineered to accelerate vegetative expansion, swell fruit/tuber/grain diameter, and maximize test weight.")

    growth_crop = st.selectbox(
        "Select Crop to View Growth Acceleration Program:",
        ["Tomato", "Potato", "Corn (Maize)", "Rice (Paddy)", "Wheat", "Cotton", "General Crop / Horticultural Plants"],
        index=0
    )
    protocol = get_growth_protocol(growth_crop)

    st.markdown(f"#### 🎯 Yield Potential for {protocol['crop']}: **{protocol['yield_potential']}** (Optimal pH: {protocol['optimal_ph']})")

    st.markdown("##### 🔑 Key Physiological Acceleration Secrets:")
    for secret in protocol["acceleration_secrets"]:
        st.markdown(f"""
        <div class="card-3d" style="padding: 14px 18px; margin-bottom: 10px; border-left: 5px solid #10B981;">
            <b>🌟 {secret}</b>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("##### 📅 Stage-by-Stage Fertigation & Spray Program:")

    for stage_info in protocol["stage_schedules"]:
        with st.expander(f"📌 {stage_info['stage']} - Target: {stage_info['target']}", expanded=True):
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown(f"**🌱 Soil / Fertigation Feeding:**\n\n`{stage_info['fertigation_soil']}`")
                st.markdown(f"**💦 Foliar Booster Spray:**\n\n`{stage_info['foliar_spray']}`")
            with col_b:
                st.markdown(f"**💡 Agronomic Secret Tip:**\n\n{stage_info['agronomic_tip']}")


# ==========================================
# TAB 4: CROP DISEASE ENCYCLOPEDIA
# ==========================================
with tab_encyclopedia:
    st.markdown("### 📖 Crop Disease & Agronomic Reference Manual")
    st.write("Browse CropGuard's complete diagnostic database, symptom markers, chemical actives, and organic remedies across all crops.")

    all_keys = list(DISEASE_DATABASE.keys())
    selected_disease_key = st.selectbox(
        "Select Disease Profile:",
        options=all_keys,
        format_func=lambda x: f"{DISEASE_DATABASE[x]['crop']} - {DISEASE_DATABASE[x]['disease_name']}"
    )

    d_info = DISEASE_DATABASE[selected_disease_key]

    st.markdown(f"## {d_info['disease_name']}")
    st.markdown(f"**Crop:** `{d_info['crop']}` | **Pathogen:** *{d_info['pathogen']}* | **Type:** `{d_info['type']}`")
    st.write(d_info['description'])

    enc_col1, enc_col2 = st.columns(2)
    with enc_col1:
        st.markdown("#### 🔍 Visual Diagnostic Symptoms:")
        for sym in d_info['symptoms']:
            st.markdown(f"- {sym}")

        st.markdown("#### ⚠️ Root Causes & Weather Vectors:")
        for cause in d_info['root_causes']:
            st.markdown(f"- {cause}")

    with enc_col2:
        st.markdown("#### 🧪 Chemical Treatment Schedule:")
        for chem in d_info['chemical_treatments']:
            st.markdown(f"- {chem}")

        st.markdown("#### 🌿 Organic & Bio-Protective Methods:")
        for org in d_info['organic_treatments']:
            st.markdown(f"- {org}")


# ==========================================
# TAB 5: EXPORT AGRONOMY REPORT
# ==========================================
with tab_pdf:
    st.markdown("### 📄 Export Official Agronomy Prescription Certificate (PDF)")
    st.write("Generate and download a high-resolution, agronomist-grade PDF report with complete diagnosis, treatment prescriptions, and yield optimization forecasts.")

    if st.session_state.last_diagnosis is None:
        st.warning("⚠️ Please perform a disease diagnosis in Tab 1 first, or select a sample leaf to generate a full report.")
    else:
        if st.session_state.last_yield is None:
            st.session_state.last_yield = st.session_state.predictor.predict_yield(
                crop=st.session_state.last_diagnosis["top_diagnosis"]["crop"],
                land_area_acres=2.5,
                nitrogen=100,
                phosphorus=50,
                potassium=100,
                soil_ph=6.5,
                organic_carbon_pct=0.75,
                irrigation_type="Precision Drip / Fertigation",
                avg_temp=25.0,
                disease_damage_pct=st.session_state.last_diagnosis["metrics"]["infected_area_pct"]
            )

        pdf_col1, pdf_col2 = st.columns([1, 1])
        with pdf_col1:
            st.markdown("#### Report Configuration:")
            rep_farmer = st.text_input("Report Issued To (Farmer Name):", value=farmer_name, key="pdf_rep_farmer")
            rep_loc = st.text_input("Farm / Field ID:", value=farm_location, key="pdf_rep_loc")

            generate_btn = st.button("📑 Compile & Generate PDF Prescription", type="primary", use_container_width=True)

        with pdf_col2:
            st.markdown("#### Preview Summary:")
            diag_top = st.session_state.last_diagnosis["top_diagnosis"]
            st.markdown(f"- **Target Crop:** {diag_top['crop']}")
            st.markdown(f"- **Diagnosis:** {diag_top['disease_name']}")
            st.markdown(f"- **Severity:** {diag_top['severity']}")
            st.markdown(f"- **Predicted Optimized Yield:** {st.session_state.last_yield['boosted_yield_per_acre']} {st.session_state.last_yield['unit']}")

        if generate_btn:
            with st.spinner("Generating official PDF prescription..."):
                pdf_data = generate_cropguard_pdf(
                    diagnosis_data=st.session_state.last_diagnosis,
                    yield_data=st.session_state.last_yield,
                    farmer_name=rep_farmer,
                    farm_location=rep_loc
                )
                filename = f"CropGuard_Prescription_{diag_top['crop']}_{rep_farmer.replace(' ', '_')}.pdf"

                st.success("✅ PDF Agronomy Prescription compiled successfully!")
                st.download_button(
                    label="⬇️ Download Official Agronomy Prescription PDF",
                    data=pdf_data,
                    file_name=filename,
                    mime="application/pdf",
                    use_container_width=True
                )
