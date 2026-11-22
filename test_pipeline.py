"""
Unit test for CropGuard core engines.
"""

import os
from PIL import Image
from engine.vision_classifier import CropVisionClassifier
from engine.yield_predictor import CropYieldPredictor
from engine.growth_booster import get_growth_protocol
from engine.pdf_report import generate_cropguard_pdf

def test_pipeline():
    classifier = CropVisionClassifier()
    predictor = CropYieldPredictor()

    sample_path = os.path.join(os.path.dirname(__file__), "samples", "tomato_late_blight.jpg")
    img = Image.open(sample_path)

    # 1. Vision diagnosis test
    res = classifier.analyze_leaf_image(img, crop_hint="Tomato")
    diag = res["top_diagnosis"]
    metrics = res["metrics"]
    print("Diagnosis:", diag["disease_name"], "Confidence:", f"{diag['confidence']}%")
    print("Health Index:", metrics["health_index"], "Infected %:", metrics["infected_area_pct"])

    # 2. Yield prediction test
    y_res = predictor.predict_yield(
        crop="Tomato",
        land_area_acres=2.5,
        nitrogen=110,
        phosphorus=55,
        potassium=110,
        soil_ph=6.4,
        organic_carbon_pct=0.85,
        irrigation_type="Precision Drip / Fertigation",
        avg_temp=24.0,
        disease_damage_pct=metrics["infected_area_pct"],
        apply_growth_booster=True
    )
    print("Baseline Yield:", y_res["baseline_yield_per_acre"], y_res["unit"])
    print("Boosted Yield:", y_res["boosted_yield_per_acre"], y_res["unit"], f"(+{y_res['yield_gain_pct']}%)")
    print("Primary Limiting Factor:", y_res["primary_limiting_factor"])

    # 3. Growth booster test
    protocol = get_growth_protocol("Tomato")
    print("Growth Protocol Stages:", len(protocol["stage_schedules"]))

    # 4. PDF report generation test
    pdf_bytes = generate_cropguard_pdf(
        diagnosis_data=res,
        yield_data=y_res,
        farmer_name="Ramesh Patel",
        farm_location="Green Valley Block 4"
    )
    print("PDF Generated successfully! Size bytes:", len(pdf_bytes))

if __name__ == "__main__":
    test_pipeline()
