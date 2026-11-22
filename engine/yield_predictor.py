"""
CropGuard Yield Prediction & Agronomic Factor Regression Engine.
Estimates crop yield based on soil chemistry (NPK, pH, OC), climate, disease stress,
and calculates the yield booster expansion potential.
"""

from typing import Dict, Any, List
import numpy as np

CROP_YIELD_BASELINES: Dict[str, Dict[str, Any]] = {
    "Tomato": {
        "unit": "Tons / Acre",
        "min_yield": 12.0,
        "avg_yield": 24.0,
        "max_potential": 48.0,
        "ideal_n": 120,   # kg/acre
        "ideal_p": 60,
        "ideal_k": 120,
        "ideal_ph_range": (6.0, 6.8),
        "ideal_temp_range": (18.0, 28.0),
        "economic_value_per_unit": 20000, # Approx currency value
    },
    "Potato": {
        "unit": "Tons / Acre",
        "min_yield": 8.0,
        "avg_yield": 15.0,
        "max_potential": 26.0,
        "ideal_n": 100,
        "ideal_p": 50,
        "ideal_k": 100,
        "ideal_ph_range": (5.5, 6.5),
        "ideal_temp_range": (16.0, 24.0),
        "economic_value_per_unit": 18000,
    },
    "Corn (Maize)": {
        "unit": "Quintals / Acre",
        "min_yield": 18.0,
        "avg_yield": 32.0,
        "max_potential": 54.0,
        "ideal_n": 100,
        "ideal_p": 45,
        "ideal_k": 40,
        "ideal_ph_range": (6.0, 7.5),
        "ideal_temp_range": (20.0, 32.0),
        "economic_value_per_unit": 2200,
    },
    "Rice (Paddy)": {
        "unit": "Quintals / Acre",
        "min_yield": 15.0,
        "avg_yield": 26.0,
        "max_potential": 42.0,
        "ideal_n": 80,
        "ideal_p": 35,
        "ideal_k": 35,
        "ideal_ph_range": (5.5, 7.0),
        "ideal_temp_range": (22.0, 33.0),
        "economic_value_per_unit": 2300,
    },
    "Wheat": {
        "unit": "Quintals / Acre",
        "min_yield": 12.0,
        "avg_yield": 20.0,
        "max_potential": 34.0,
        "ideal_n": 75,
        "ideal_p": 35,
        "ideal_k": 30,
        "ideal_ph_range": (6.0, 7.5),
        "ideal_temp_range": (14.0, 25.0),
        "economic_value_per_unit": 2400,
    },
    "Cotton": {
        "unit": "Quintals / Acre",
        "min_yield": 7.0,
        "avg_yield": 13.0,
        "max_potential": 22.0,
        "ideal_n": 70,
        "ideal_p": 30,
        "ideal_k": 35,
        "ideal_ph_range": (6.2, 7.8),
        "ideal_temp_range": (24.0, 36.0),
        "economic_value_per_unit": 7000,
    },
    "Apple": {
        "unit": "Tons / Acre",
        "min_yield": 5.0,
        "avg_yield": 12.0,
        "max_potential": 24.0,
        "ideal_n": 80,
        "ideal_p": 40,
        "ideal_k": 90,
        "ideal_ph_range": (6.0, 6.8),
        "ideal_temp_range": (15.0, 25.0),
        "economic_value_per_unit": 60000,
    },
    "Grape": {
        "unit": "Tons / Acre",
        "min_yield": 6.0,
        "avg_yield": 14.0,
        "max_potential": 25.0,
        "ideal_n": 60,
        "ideal_p": 35,
        "ideal_k": 90,
        "ideal_ph_range": (6.0, 7.2),
        "ideal_temp_range": (18.0, 30.0),
        "economic_value_per_unit": 45000,
    }
}

class CropYieldPredictor:
    """Multi-variable agronomic regression engine for crop yield estimation."""

    def predict_yield(
        self,
        crop: str,
        land_area_acres: float,
        nitrogen: float,
        phosphorus: float,
        potassium: float,
        soil_ph: float,
        organic_carbon_pct: float,
        irrigation_type: str,
        avg_temp: float,
        disease_damage_pct: float = 0.0,
        apply_growth_booster: bool = True
    ) -> Dict[str, Any]:
        """Calculates expected baseline yield, optimized yield, and limiting factors."""
        # Find matching crop baseline
        baseline = CROP_YIELD_BASELINES.get("Tomato")
        for k in CROP_YIELD_BASELINES.keys():
            if k.lower() in crop.lower() or crop.lower() in k.lower():
                baseline = CROP_YIELD_BASELINES[k]
                break

        # 1. Nutrient Sufficiency Factors (Liebig's Law of the Minimum)
        n_ratio = min(1.3, nitrogen / max(baseline["ideal_n"], 1))
        p_ratio = min(1.3, phosphorus / max(baseline["ideal_p"], 1))
        k_ratio = min(1.3, potassium / max(baseline["ideal_k"], 1))

        # Nonlinear diminishing return curves for NPK
        n_factor = 1.0 - 0.45 * np.exp(-1.8 * n_ratio)
        p_factor = 1.0 - 0.40 * np.exp(-2.0 * p_ratio)
        k_factor = 1.0 - 0.45 * np.exp(-1.9 * k_ratio)

        # 2. Soil pH Penalty Factor
        ideal_ph_low, ideal_ph_high = baseline["ideal_ph_range"]
        if ideal_ph_low <= soil_ph <= ideal_ph_high:
            ph_factor = 1.0
        elif soil_ph < ideal_ph_low:
            ph_factor = max(0.45, 1.0 - (ideal_ph_low - soil_ph) * 0.22)
        else:
            ph_factor = max(0.50, 1.0 - (soil_ph - ideal_ph_high) * 0.18)

        # 3. Organic Carbon Factor (OC improves CEC, microbial activity, root aeration)
        # 0.75% is considered healthy benchmark
        oc_factor = min(1.15, max(0.65, 0.70 + (organic_carbon_pct / 0.75) * 0.30))

        # 4. Irrigation Factor
        irrig_map = {
            "Precision Drip / Fertigation": 1.15,
            "Canal / Flood Irrigation (Adequate)": 1.00,
            "Rainfed (Good Rain)": 0.88,
            "Rainfed / Moisture Stressed": 0.65,
            "Waterlogged / Poor Drainage": 0.55
        }
        irrig_factor = irrig_map.get(irrigation_type, 1.0)

        # 5. Temperature Stress Factor
        temp_low, temp_high = baseline["ideal_temp_range"]
        if temp_low <= avg_temp <= temp_high:
            temp_factor = 1.0
        elif avg_temp < temp_low:
            temp_factor = max(0.6, 1.0 - (temp_low - avg_temp) * 0.04)
        else:
            temp_factor = max(0.55, 1.0 - (avg_temp - temp_high) * 0.05)

        # 6. Disease Burden Penalty
        # Direct foliar loss reduces photosynthetically active radiation (PAR)
        disease_loss_factor = max(0.15, 1.0 - (disease_damage_pct / 100.0) * 0.85)

        # Baseline Agronomic Index
        agronomic_index = (
            (n_factor * 0.28 + p_factor * 0.22 + k_factor * 0.30 + oc_factor * 0.20)
            * ph_factor
            * irrig_factor
            * temp_factor
            * disease_loss_factor
        )

        base_potential = baseline["avg_yield"]
        predicted_yield_per_acre = base_potential * agronomic_index
        predicted_yield_per_acre = max(baseline["min_yield"] * 0.7, min(baseline["max_potential"], predicted_yield_per_acre))

        # Growth Booster Simulation
        # If farmer applies CropGuard Booster (Humic + MKP + Boron + SOP + Microchelate):
        # - Resolves nutrient uptake efficiency (+18%)
        # - Overcomes pH/salinity root lockup via Humic chelation (+12%)
        # - Swells fruit/grain sizing with late Potassium SOP (+10%)
        # - Mitigates 70% of disease yield drag via systemic resistance
        if apply_growth_booster:
            boosted_disease_factor = max(0.35, 1.0 - (disease_damage_pct / 100.0) * 0.30)
            boosted_index = (
                (min(1.2, n_factor * 1.15) * 0.25 +
                 min(1.2, p_factor * 1.20) * 0.25 +
                 min(1.25, k_factor * 1.25) * 0.30 +
                 min(1.2, oc_factor * 1.15) * 0.20)
                * min(1.0, ph_factor * 1.12)
                * min(1.18, irrig_factor * 1.08)
                * temp_factor
                * boosted_disease_factor
            )
            boosted_yield_per_acre = base_potential * boosted_index * 1.15
            boosted_yield_per_acre = min(baseline["max_potential"], max(predicted_yield_per_acre * 1.22, boosted_yield_per_acre))
        else:
            boosted_yield_per_acre = predicted_yield_per_acre

        total_baseline_yield = round(predicted_yield_per_acre * land_area_acres, 2)
        total_boosted_yield = round(boosted_yield_per_acre * land_area_acres, 2)
        yield_gain_pct = round(((boosted_yield_per_acre - predicted_yield_per_acre) / max(predicted_yield_per_acre, 1e-3)) * 100, 1)

        # Identify Limiting Factors
        factors = [
            {"factor": "Potassium (K) Availability", "score": k_factor, "status": "Critical Sizing Element"},
            {"factor": "Nitrogen (N) Vigour", "score": n_factor, "status": "Vegetative Growth Engine"},
            {"factor": "Phosphorus (P) Rooting", "score": p_factor, "status": "Energy & Root Cell Division"},
            {"factor": "Soil pH Acidity / Alkalinity", "score": ph_factor, "status": "Nutrient Lockup Risk"},
            {"factor": "Soil Organic Carbon", "score": oc_factor, "status": "Soil Microbe & Moisture Sponge"},
            {"factor": "Irrigation Efficiency", "score": irrig_factor, "status": "Transpiration & Sap Flow"},
            {"factor": "Disease Lesion Burden", "score": disease_loss_factor, "status": "Photosynthesis Deficit"}
        ]
        factors.sort(key=lambda x: x["score"])
        primary_limiting_factor = factors[0]["factor"]

        return {
            "crop": crop,
            "unit": baseline["unit"],
            "land_area_acres": land_area_acres,
            "baseline_yield_per_acre": round(predicted_yield_per_acre, 2),
            "total_baseline_yield": total_baseline_yield,
            "boosted_yield_per_acre": round(boosted_yield_per_acre, 2),
            "total_boosted_yield": total_boosted_yield,
            "yield_gain_pct": yield_gain_pct,
            "net_gain_amount": round(total_boosted_yield - total_baseline_yield, 2),
            "primary_limiting_factor": primary_limiting_factor,
            "factors_breakdown": factors,
            "economic_projection": {
                "unit_value": baseline["economic_value_per_unit"],
                "est_baseline_income": round(total_baseline_yield * baseline["economic_value_per_unit"]),
                "est_boosted_income": round(total_boosted_yield * baseline["economic_value_per_unit"]),
                "additional_profit": round((total_boosted_yield - total_baseline_yield) * baseline["economic_value_per_unit"])
            }
        }
