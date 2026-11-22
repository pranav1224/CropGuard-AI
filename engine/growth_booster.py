"""
CropGuard Growth Accelerator & Yield Optimization Engine.
Provides precision fertilizer recommendations, biostimulant schedules,
and actionable protocols to make crops grow fast, large, and achieve maximum yield.
"""

from typing import Dict, Any, List

GROWTH_BOOSTER_PROTOCOLS: Dict[str, Dict[str, Any]] = {
    "Tomato": {
        "crop": "Tomato",
        "yield_potential": "35 - 55 Metric Tons / Acre (High Vigor Hybrid)",
        "optimal_ph": "6.0 - 6.8",
        "acceleration_secrets": [
            "Root Expansion: Drench with Humic Acid 98% (3g/L) + Mycorrhiza within 5 days of transplanting to triple root volume.",
            "Rapid Stem & Foliage Growth: Foliar spray of Seaweed Extract (2 ml/L) + Chelated Micronutrients (1.5 g/L) at 20 days.",
            "Fruit Sizing Surge: Spray Monopotassium Phosphate (0-52-34) @ 5 g/L + Potassium Nitrate (13-0-45) @ 5 g/L during fruit set.",
            "Prevent Blossom End Rot & Cracking: Foliar Calcium Nitrate (15.5-0-0 + 18.8% Ca) @ 3 g/L + Boron (20%) @ 1 g/L."
        ],
        "stage_schedules": [
            {
                "stage": "1. Seedling & Transplanting (Days 1 - 15)",
                "target": "Fast Root Establishment & Shock Prevention",
                "fertigation_soil": "DAP (18-46-0) @ 25 kg/acre + Humic Acid @ 1 kg/acre",
                "foliar_spray": "19-19-19 @ 3 g/L + Seaweed extract @ 2 ml/L",
                "agronomic_tip": "Keep soil moist but not waterlogged. Pinch off earliest flower buds to force vegetative mass first."
            },
            {
                "stage": "2. Active Vegetative Surge (Days 16 - 35)",
                "target": "Rapid Branching & Dense Chlorophyll Canopy",
                "fertigation_soil": "Urea @ 20 kg/acre + Magnesium Sulphate @ 10 kg/acre",
                "foliar_spray": "Chelated Micronutrient Combo (Zn, Fe, Mn, Cu) @ 1.5 g/L + Amino Acids @ 2 ml/L",
                "agronomic_tip": "Trellis and prune lateral bottom suckers up to 20 cm from ground for upward energy channeling."
            },
            {
                "stage": "3. Flowering & Fruit Set (Days 36 - 60)",
                "target": "Zero Flower Drop & Maximum Cluster Setting",
                "fertigation_soil": "12-61-0 (Monoammonium Phosphate) @ 15 kg/acre",
                "foliar_spray": "0-52-34 (MKP) @ 5 g/L + Boron 20% @ 1 g/L + NAA (Planofix) @ 0.25 ml/L",
                "agronomic_tip": "Boron ensures healthy pollen germination. Avoid high nitrogen here to prevent vegetative flower abortion."
            },
            {
                "stage": "4. Fruit Bulking & Sizing (Days 61 - 90)",
                "target": "Grow Large, Heavy, Uniform Red Fruits",
                "fertigation_soil": "Potassium Nitrate (13-0-45) @ 20 kg/acre + Calcium Nitrate @ 10 kg/acre",
                "foliar_spray": "SOP (0-0-50 Potassium Sulphate) @ 5 g/L + Gibberellic Acid (GA3) @ 10 ppm",
                "agronomic_tip": "Potassium pumps sugars and water into fruits, swelling fruit diameter and increasing shelf-life."
            }
        ]
    },
    "Potato": {
        "crop": "Potato",
        "yield_potential": "18 - 28 Metric Tons / Acre",
        "optimal_ph": "5.5 - 6.5",
        "acceleration_secrets": [
            "Tuber Stolon Initiation: Apply Monopotassium Phosphate (0-52-34) at stolon hook stage (30-35 days) to double tuber count.",
            "Tuber Bulking Power: Fertigate with Potassium Sulphate (0-0-50) @ 25 kg/acre during days 45-75 to expand tuber diameter.",
            "Skin Finish & Internal Strength: Calcium Boron spray @ 2 ml/L prevents hollow heart and skin scuffing.",
            "Starch Accumulation: Zinc Sulphate (21%) @ 2 g/L foliar spray accelerates starch conversion."
        ],
        "stage_schedules": [
            {
                "stage": "1. Emergence & Vegetative (Days 1 - 30)",
                "target": "Robust Haulm Canopy & Thick Stems",
                "fertigation_soil": "10-26-26 @ 50 kg/acre + Zinc Sulphate @ 10 kg/acre at planting",
                "foliar_spray": "19-19-19 @ 4 g/L + Humic Acid @ 2 g/L",
                "agronomic_tip": "Perform high earthing-up (hilling) at 25 days to provide ample loose soil for stolon expansion."
            },
            {
                "stage": "2. Tuber Initiation (Days 31 - 50)",
                "target": "Maximum Number of Tuber Sets",
                "fertigation_soil": "12-61-0 @ 15 kg/acre through drip or band placement",
                "foliar_spray": "0-52-34 (MKP) @ 5 g/L + Boron 20% @ 1 g/L",
                "agronomic_tip": "Maintain consistent soil moisture (65-75% field capacity); dry spells cause knobby, deformed potatoes."
            },
            {
                "stage": "3. Tuber Bulking Phase (Days 51 - 80)",
                "target": "Grow Large, Heavy, Grade-A Tubers",
                "fertigation_soil": "0-0-50 (SOP) @ 25 kg/acre + Magnesium Sulphate @ 10 kg/acre",
                "foliar_spray": "13-0-45 @ 5 g/L + Seaweed extract @ 2 ml/L",
                "agronomic_tip": "Potassium is the chief driver of tuber weight. Ensure no water stress occurs during this 30-day window."
            }
        ]
    },
    "Corn (Maize)": {
        "crop": "Corn (Maize)",
        "yield_potential": "40 - 55 Quintals / Acre (Hybrid Grain Corn)",
        "optimal_ph": "6.0 - 7.5",
        "acceleration_secrets": [
            "Early Knee-High Boost: Top-dress Urea + Zinc Sulphate at V6 stage (knee-high); this determines cob length and kernel row count.",
            "Silk & Tassel Synchronization: Spray Boron (20%) @ 1 g/L + 0-52-34 @ 5 g/L 10 days before tasseling to ensure complete tip fill.",
            "Heavy Kernel Test Weight: Foliar spray of Potassium Nitrate (13-0-45) @ 5 g/L at early milk stage (R3).",
            "Deep Root Anchorage: Apply Mycorrhizal biofertilizer to withstand lodging and drought stress."
        ],
        "stage_schedules": [
            {
                "stage": "1. Seedling to Knee-High (V1 - V6)",
                "target": "Fast Vegetative Surge & Ear Row Determination",
                "fertigation_soil": "DAP @ 50 kg/acre + MOP (Potash) @ 20 kg/acre basal + Zinc Sulphate @ 10 kg/acre",
                "foliar_spray": "19-19-19 @ 4 g/L + Humic acid @ 2 g/L",
                "agronomic_tip": "Keep field strictly weed-free during the first 30 days to avoid competition."
            },
            {
                "stage": "2. Pre-Tasseling to Silking (V8 - R1)",
                "target": "Massive Stalk Girth & Complete Pollination",
                "fertigation_soil": "Urea @ 35 kg/acre split application",
                "foliar_spray": "0-52-34 @ 5 g/L + Boron 20% @ 1 g/L",
                "agronomic_tip": "Ensure adequate soil moisture during pollination; heat/drought stress during silking causes barren ear tips."
            },
            {
                "stage": "3. Grain Filling & Dent (R2 - R5)",
                "target": "Dense, Plump Kernels with High Test Weight",
                "fertigation_soil": "Potassium Sulphate (0-0-50) @ 15 kg/acre",
                "foliar_spray": "13-0-45 @ 5 g/L foliar spray",
                "agronomic_tip": "Maintain green canopy (stay-green trait) to synthesize starch right up to black layer physiological maturity."
            }
        ]
    },
    "Rice (Paddy)": {
        "crop": "Rice (Paddy)",
        "yield_potential": "30 - 45 Quintals / Acre",
        "optimal_ph": "5.5 - 7.0",
        "acceleration_secrets": [
            "Maximum Tillering: Apply Zinc Sulphate (25 kg/ha) + Urea at active tillering (15-20 DAT) to achieve 25+ productive tillers per hill.",
            "Long Panicle Exertion: Spray Gibberellic Acid (GA3) @ 15-20 ppm at 5% heading stage to push out panicle neck completely.",
            "No Chaffy / Hollow Grains: Spray 0-52-34 @ 5 g/L + Boron @ 1 g/L at boot leaf stage to ensure 95%+ grain fertility.",
            "Silicon Fortification: Apply Calcium Silicate slag @ 200 kg/acre to create erect leaves and prevent lodging."
        ],
        "stage_schedules": [
            {
                "stage": "1. Active Tillering (15 - 30 DAT)",
                "target": "Dense Tillering & High Leaf Area Index",
                "fertigation_soil": "Urea @ 25 kg/acre + Zinc Sulphate @ 10 kg/acre",
                "foliar_spray": "19-19-19 @ 4 g/L + Chelated Iron @ 1 g/L",
                "agronomic_tip": "Maintain shallow water depth (2-3 cm) to warm root zone and encourage rapid tiller emergence."
            },
            {
                "stage": "2. Panicle Initiation & Booting (45 - 60 DAT)",
                "target": "Large Panicle Branching & High Spikelet Count",
                "fertigation_soil": "Muriate of Potash (MOP) @ 20 kg/acre + Urea @ 15 kg/acre",
                "foliar_spray": "0-52-34 (MKP) @ 5 g/L + Boron 20% @ 1 g/L",
                "agronomic_tip": "Critical water stage: never let paddy field run dry during panicle initiation and flowering."
            },
            {
                "stage": "3. Grain Filling & Milking (65 - 85 DAT)",
                "target": "Heavy, Golden Grains with Zero Breakage",
                "fertigation_soil": "Potassium Sulphate (0-0-50) @ 10 kg/acre",
                "foliar_spray": "Potassium Nitrate (13-0-45) @ 5 g/L foliar spray",
                "agronomic_tip": "Drain field water completely 10-12 days before harvest to ensure uniform ripening and high milling quality."
            }
        ]
    },
    "Wheat": {
        "crop": "Wheat",
        "yield_potential": "25 - 35 Quintals / Acre",
        "optimal_ph": "6.0 - 7.5",
        "acceleration_secrets": [
            "Crown Root Initiation (CRI) Milestone: Irrigate and apply Urea @ 21 days; this controls final spike count per square meter.",
            "Spikelet Lengthening: Foliar spray of Chlormequat Chloride (Lihocin) @ 2 ml/L at jointing to thicken stem and shorten internodes, preventing lodging.",
            "Plump Grain Filling: Spray 13-0-45 @ 10 g/L at flowering and milk stage to overcome terminal heat stress.",
            "High Protein & Grain Shine: Spray Chelated Zinc (12%) @ 1 g/L + Urea @ 5 g/L at flag leaf stage."
        ],
        "stage_schedules": [
            {
                "stage": "1. Crown Root & Tillering (Days 20 - 40)",
                "target": "Deep Crown Anchorage & Multiple Tillers",
                "fertigation_soil": "Urea @ 45 kg/acre + DAP @ 50 kg/acre basal + Zinc Sulphate @ 10 kg/acre",
                "foliar_spray": "19-19-19 @ 4 g/L + Humic Acid @ 2 g/L",
                "agronomic_tip": "The first irrigation at CRI stage (21 days) is non-negotiable for wheat yields."
            },
            {
                "stage": "2. Jointing & Booting (Days 45 - 70)",
                "target": "Long Earheads & Lodging Resistance",
                "fertigation_soil": "Urea @ 25 kg/acre final top-dressing",
                "foliar_spray": "0-52-34 @ 5 g/L + Boron 20% @ 1 g/L",
                "agronomic_tip": "If high winds and heavy vegetative growth occur, use growth retardant (CCC) to prevent lodging."
            },
            {
                "stage": "3. Heading & Grain Filling (Days 75 - 105)",
                "target": "Bold, Heavy Kernels & High Test Weight",
                "fertigation_soil": "Potassium Sulphate (0-0-50) @ 15 kg/acre",
                "foliar_spray": "13-0-45 @ 10 g/L foliar spray (combats terminal heat)",
                "agronomic_tip": "Maintain light, frequent irrigations during grain filling to cool the micro-canopy."
            }
        ]
    },
    "Cotton": {
        "crop": "Cotton",
        "yield_potential": "15 - 25 Quintals / Acre (Seed Cotton)",
        "optimal_ph": "6.0 - 8.0",
        "acceleration_secrets": [
            "Boll Retention Mastery: Spray NAA (Planofix) @ 4 ml per 15L water at square and boll formation to reduce boll drop by 60%.",
            "Fast Square Formation: Foliar spray of Magnesium Sulphate (10 g/L) + Urea (10 g/L) to prevent leaf reddening.",
            "Big Heavy Bolls: Foliar spray of 0-52-34 (MKP) @ 5 g/L + Boron @ 1 g/L at peak flowering.",
            "Mepiquat Chloride (Chamatkar) @ 1.5 ml/L at 65-75 days to regulate excessive vegetative growth and direct nutrients to bolls."
        ],
        "stage_schedules": [
            {
                "stage": "1. Squaring Stage (Days 35 - 55)",
                "target": "Maximum Square Initiation & Branch Development",
                "fertigation_soil": "Urea @ 30 kg/acre + Magnesium Sulphate @ 10 kg/acre",
                "foliar_spray": "19-19-19 @ 4 g/L + Chelated Micronutrients @ 1.5 g/L",
                "agronomic_tip": "Monitor closely for sucking pests (thrips, aphids, whiteflies) which distort early square formation."
            },
            {
                "stage": "2. Peak Flowering & Boll Setting (Days 60 - 90)",
                "target": "Zero Square/Boll Dropping & Maximum Boll Size",
                "fertigation_soil": "13-0-45 @ 15 kg/acre through drip or broadcast",
                "foliar_spray": "0-52-34 @ 5 g/L + Planofix @ 0.25 ml/L + Boron 20% @ 1 g/L",
                "agronomic_tip": "Avoid severe water stress or over-flooding; sudden soil moisture fluctuations trigger ethylene surge and boll drop."
            },
            {
                "stage": "3. Boll Maturation & Bursting (Days 95 - 135)",
                "target": "Clean, Fluffy, Heavy White Bolls",
                "fertigation_soil": "Potassium Sulphate (0-0-50) @ 15 kg/acre",
                "foliar_spray": "Potassium Nitrate (13-0-45) @ 5 g/L + Zinc EDTA @ 1 g/L",
                "agronomic_tip": "Stop all chemical sprays once 15% of bolls burst open to prevent lint staining and fiber degradation."
            }
        ]
    }
}

# General Fallback for all other crops
GENERAL_GROWTH_PROTOCOL = {
    "crop": "General Crop / Horticultural Plants",
    "yield_potential": "+30% to +50% Above Baseline",
    "optimal_ph": "6.0 - 7.2",
    "acceleration_secrets": [
        "Root Explosion: Humic Acid 98% (3 g/L) + Seaweed extract (2 ml/L) stimulates massive lateral roots.",
        "Vegetative Surge: Foliar spray of balanced N-P-K 19-19-19 @ 4 g/L with chelated micronutrients (Zn, Fe, Mn).",
        "Fruit & Grain Enlargement: Spray 0-52-34 (MKP) @ 5 g/L + Boron (20%) @ 1 g/L during bloom, followed by Potassium Sulphate 0-0-50 @ 5 g/L during sizing.",
        "Stress Armor: Potassium Silicate @ 2 ml/L thickens leaf cuticle, deterring pests and fungal spores."
    ],
    "stage_schedules": [
        {
            "stage": "1. Establishment & Early Growth",
            "target": "Rapid Rooting & Strong Photosynthetic Engine",
            "fertigation_soil": "DAP or balanced NPK + Organic Compost",
            "foliar_spray": "19-19-19 @ 3 g/L + Humic Acid @ 2 g/L",
            "agronomic_tip": "Ensure good drainage and aeration around root crowns."
        },
        {
            "stage": "2. Reproductive & Flower/Fruit Set",
            "target": "Maximum Setting & Retention",
            "fertigation_soil": "High Phosphorus & Moderate Potassium fertilizer",
            "foliar_spray": "0-52-34 (MKP) @ 5 g/L + Boron 20% @ 1 g/L",
            "agronomic_tip": "Maintain uniform soil moisture; avoid drought stress during flowering."
        },
        {
            "stage": "3. Sizing & Maturity",
            "target": "Heavy Sizing, Superior Quality, High Brix",
            "fertigation_soil": "Sulphate of Potash (0-0-50) @ 15-20 kg/acre",
            "foliar_spray": "Potassium Nitrate (13-0-45) @ 5 g/L",
            "agronomic_tip": "Potassium is the universal sizing element; ensures dense filling and premium produce."
        }
    ]
}

def get_growth_protocol(crop_name: str) -> Dict[str, Any]:
    """Retrieves growth booster protocol for a specified crop."""
    for key, data in GROWTH_BOOSTER_PROTOCOLS.items():
        if key.lower() in crop_name.lower() or crop_name.lower() in key.lower():
            return data
    return GENERAL_GROWTH_PROTOCOL
