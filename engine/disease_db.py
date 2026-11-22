"""
CropGuard Plant Pathology & Agronomic Treatment Knowledgebase.
Covers major agricultural crops, bacterial, fungal, viral diseases, nutrient deficiencies,
organic biocontrols, chemical treatments, and preventative agronomy.
"""

from typing import Dict, Any, List

DISEASE_DATABASE: Dict[str, Dict[str, Any]] = {
    "tomato_late_blight": {
        "crop": "Tomato",
        "disease_name": "Tomato Late Blight",
        "pathogen": "Phytophthora infestans (Oomycete)",
        "type": "Fungal-like Oomycete",
        "description": "Devastating foliar disease characterized by large, irregular water-soaked pale green or dark brown lesions. Rapidly blights leaves, stems, and fruits during cool, humid conditions.",
        "symptoms": [
            "Large water-soaked dark brown to purplish lesions on leaflets",
            "White velvety fungal sporulation on the underside of leaves in humid weather",
            "Brown greasy-looking lesions on stems and petiole collapse",
            "Firm, wrinkled dark brown rot on green or ripe fruits"
        ],
        "root_causes": [
            "Persistent high relative humidity (>90%) with cool temperatures (15°C - 22°C)",
            "Extended leaf wetness (>8 hours) from overhead irrigation, dew, or rain",
            "Poor air circulation in dense canopy",
            "Over-fertilization with Nitrogen creating lush, susceptible vegetative tissue"
        ],
        "organic_treatments": [
            "Bordeaux Mixture (1% copper sulfate + hydrated lime) as preventative spray",
            "Copper Hydroxide / Copper Oxychloride (2.5 - 3.0 g/L) every 7-10 days",
            "Bio-fungicide spray: Bacillus subtilis (QST 713 strain) @ 5 ml/L",
            "Trichoderma harzianum soil drench (10 g/L) to suppress resting oospores",
            "Neem oil (cold-pressed 10,000 ppm) @ 3 ml/L with emulsifier as mild spore inhibitor"
        ],
        "chemical_treatments": [
            "Curative: Metalaxyl 8% + Mancozeb 64% WP (Ridomil Gold) @ 2.5 g/L",
            "Systemic Translaminar: Dimethomorph 50% WP @ 1.0 - 1.5 g/L",
            "Protectant: Chlorothalonil 75% WP @ 2.0 g/L (repeat every 7 days under disease pressure)",
            "Anti-sporulant: Cymoxanil 8% + Mancozeb 64% WP @ 2.0 g/L",
            "Advanced: Mandipropamid 23.4% SC @ 0.8 ml/L with organosilicone sticker"
        ],
        "growth_and_fertilizer_recovery": [
            "Temporarily halt high-Nitrogen fertilizers (e.g. Urea) to prevent soft succulent growth",
            "Apply Potassium Silicate (2 ml/L foliar) to reinforce plant cuticle and epidermal cell walls",
            "Foliar spray of Potassium Sulphate (0-0-50) @ 4 g/L to restore osmoregulation",
            "Supplement with Zinc EDTA (12%) @ 1 g/L and Boron (20%) @ 1 g/L for cellular recovery"
        ],
        "prevention_steps": [
            "Switch strictly to drip irrigation; eliminate overhead sprinkler watering",
            "Prune bottom suckers and lower foliage up to 30 cm from ground for airflow",
            "Rotate crops with non-solanaceous species (maize, pulses, beans) for at least 3 years",
            "Burn or deeply bury infected plant debris; never add to compost"
        ],
        "severity_threshold": "High - Rapidly spreads; treat within 24 hours of first symptom."
    },
    "tomato_early_blight": {
        "crop": "Tomato",
        "disease_name": "Tomato Early Blight",
        "pathogen": "Alternaria solani (Fungus)",
        "type": "Fungal",
        "description": "Common foliar blight exhibiting characteristic concentric rings ('target-board' or bullseye appearance) surrounded by a chlorotic yellow halo.",
        "symptoms": [
            "Circular brown-black lesions with distinct concentric target rings on older lower leaves",
            "Yellow halo encircling necrotic lesions",
            "Leaf yellowing, drying, and premature defoliation starting from the base upwards",
            "Dark sunken cankers on stems at ground level ('collar rot' in seedlings)"
        ],
        "root_causes": [
            "Moderate to warm temperatures (24°C - 29°C) with intermittent wet and dry cycles",
            "Soil splash during heavy rain or sprinkler irrigation transmitting overwintered spores",
            "Plant stress, senescence, or Potassium and Nitrogen deficiency"
        ],
        "organic_treatments": [
            "Copper Hydroxide 53.8% DF @ 2.0 g/L every 7-10 days",
            "Trichoderma viride foliar spray @ 5 g/L combined with organic sticker",
            "Equisetum (Horsetail) silica tea spray or Chitosan oligosaccharide (1%) foliar",
            "Pruning of lower infected leaves followed by bio-protective sulfur dust (80% WDG)"
        ],
        "chemical_treatments": [
            "Mancozeb 75% WP @ 2.5 g/L as standard protective spray",
            "Azoxystrobin 18.2% + Difenoconazole 11.4% SC (Amistar Top) @ 1.0 ml/L",
            "Tebuconazole 25.9% EC @ 1.0 ml/L or Pyraclostrobin 20% WG @ 1.0 g/L",
            "Chlorothalonil 720 SC @ 2.0 ml/L applied at early onset"
        ],
        "growth_and_fertilizer_recovery": [
            "Apply balanced 19-19-19 N-P-K foliar spray @ 4 g/L to overcome defoliation stress",
            "Soil drench with Humic Acid (98%) @ 3 g/L to stimulate rapid secondary root generation",
            "Maintain soil Potassium (K) levels via Potassium Nitrate (13-0-45) @ 5 g/L"
        ],
        "prevention_steps": [
            "Apply 3-inch straw or plastic mulch around plant bases to prevent soil splash",
            "Stake and trellis tomato plants to keep all leaves elevated off soil",
            "Practice 3-year crop rotation avoiding peppers, potatoes, and eggplants"
        ],
        "severity_threshold": "Moderate - Progressive; early leaf pruning and fungicide halts spread."
    },
    "potato_late_blight": {
        "crop": "Potato",
        "disease_name": "Potato Late Blight",
        "pathogen": "Phytophthora infestans (Oomycete)",
        "type": "Fungal-like Oomycete",
        "description": "The historical pathogen of the Irish Potato Famine. Infects both haulms (canopy) and underground tubers, causing devastating rot.",
        "symptoms": [
            "Water-soaked black-brown irregular leaf lesions with white sporulation on leaf underside",
            "Stem lesions leading to haulm collapse and pungent decaying odor",
            "Tuber dry rot with reddish-brown granular necrosis under the skin extending into flesh"
        ],
        "root_causes": [
            "Cool, damp microclimates (10°C - 20°C) with RH > 90%",
            "Infected seed tubers used at planting",
            "Unmanaged volunteer potato plants in adjacent fields"
        ],
        "organic_treatments": [
            "Bordeaux mixture (1.0%) or Copper sulfate pentahydrate preventative sprays",
            "Pseudomonas fluorescens 1% WP @ 5 g/L seed and foliar treatment",
            "Potassium phosphite (Phi) foliar applications @ 2.5 ml/L to trigger systemic acquired resistance (SAR)"
        ],
        "chemical_treatments": [
            "Curative: Cymoxanil 8% + Mancozeb 64% WP @ 2.5 g/L",
            "Translaminar: Dimethomorph 50% WP @ 1.5 g/L or Fluopicolide + Propamocarb @ 2 ml/L",
            "Protectant: Mancozeb 75% WP @ 2.5 kg/ha or Chlorothalonil @ 2.0 L/ha"
        ],
        "growth_and_fertilizer_recovery": [
            "Apply Potassium Phosphonate to induce plant phytoalexin defense",
            "Apply Calcium Nitrate (15.5-0-0 + 18.8% Ca) @ 5 kg/acre to strengthen tuber peel resistance",
            "Foliar spray of Seaweed extract (Ascophyllum nodosum) @ 2 ml/L for vigor recovery"
        ],
        "prevention_steps": [
            "Plant only certified disease-free seed tubers",
            "Ensure high hilling / earthing up (15-20 cm) of soil over tubers to stop spore wash-in",
            "Desiccate haulms 10-14 days prior to harvest to prevent tuber contamination during lifting"
        ],
        "severity_threshold": "Critical - Can destroy an entire potato crop in 7-10 days if unchecked."
    },
    "potato_early_blight": {
        "crop": "Potato",
        "disease_name": "Potato Early Blight",
        "pathogen": "Alternaria solani",
        "type": "Fungal",
        "description": "Fungal foliar disease causing brown, angular spots with concentric target-board rings on potato foliage, reducing photosynthetic area and tuber sizing.",
        "symptoms": [
            "Dark brown to black concentric target rings on older mature leaves",
            "Yellow halo around lesions followed by foliage senescence",
            "Sunken, dark circular lesions on tubers with corky textured flesh beneath"
        ],
        "root_causes": [
            "Fluctuating dry and wet weather conditions with heavy dew nights",
            "Nutrient deficiency (especially low Nitrogen or Potassium) predisposing foliage",
            "Senescing crop canopy nearing tuber bulking stage"
        ],
        "organic_treatments": [
            "Copper oxychloride 50% WP @ 3.0 g/L",
            "Bacillus amyloliquefaciens foliar spray @ 4 ml/L",
            "Neem oil cake soil application @ 150 kg/acre"
        ],
        "chemical_treatments": [
            "Difenoconazole 25% EC @ 0.8 ml/L",
            "Azoxystrobin 23% SC @ 1.0 ml/L",
            "Mancozeb 75% WP @ 2.5 g/L at 10-day intervals"
        ],
        "growth_and_fertilizer_recovery": [
            "Fertigate with 0-52-34 (Monopotassium Phosphate) @ 5 kg/acre for rapid tuber bulking",
            "Apply Boron (20%) foliar spray @ 1 g/L to stimulate starch deposition into tubers",
            "Foliar Amino Acid chelate @ 2 ml/L to reboot chlorophyll synthesis"
        ],
        "prevention_steps": [
            "Maintain optimal crop nutrition throughout the vegetative phase",
            "Avoid overhead irrigation during late afternoon or evening",
            "Harvest only after skin has matured to prevent harvest wounding"
        ],
        "severity_threshold": "Moderate - Controlled effectively with timely protectant fungicides."
    },
    "corn_common_rust": {
        "crop": "Corn (Maize)",
        "disease_name": "Corn Common Rust",
        "pathogen": "Puccinia sorghi (Basidiomycete Fungus)",
        "type": "Fungal",
        "description": "Airborne fungal disease creating cinnamon-brown to golden-orange powdery pustules scattered on both upper and lower leaf surfaces of maize.",
        "symptoms": [
            "Small, oval to elongate powdery golden-brown pustules on both upper and lower surfaces",
            "Pustules rupture epidermal tissue, releasing rust-colored fungal urediniospores",
            "In advanced stages, pustules turn blackish-brown as teliospores form",
            "Severe chlorosis, leaf scorching, and premature senescence reducing grain fill"
        ],
        "root_causes": [
            "Cool to moderate temperatures (16°C - 25°C) with high relative humidity (>95%)",
            "Long spore transport via wind currents from southern corn-growing belts",
            "Susceptible hybrid varieties planted in high plant populations"
        ],
        "organic_treatments": [
            "Wettable Sulfur 80% WDG @ 3.0 g/L (avoid when temperature exceeds 32°C)",
            "Trichoderma viride + Pseudomonas fluorescens consortium spray @ 5 g/L",
            "Liquid bio-fertilizer mycorrhizal booster applied to enhance natural immunity"
        ],
        "chemical_treatments": [
            "Azoxystrobin 18.2% + Difenoconazole 11.4% SC @ 1.0 ml/L (highly effective curative & preventative)",
            "Pyraclostrobin 20% WG @ 1.2 g/L",
            "Propiconazole 25% EC @ 1.0 ml/L applied prior to tassel/silking stage",
            "Mancozeb 75% WP @ 2.5 g/L at first appearance of pustules"
        ],
        "growth_and_fertilizer_recovery": [
            "Apply Potassium Chloride (MOP) or Potassium Sulphate @ 25 kg/acre to thicken maize stalk and leaf epidermis",
            "Foliar spray of Zinc Sulphate (heptahydrate 21%) @ 2 g/L + Urea @ 5 g/L to restore photosynthesis",
            "Apply Gibberellic Acid (GA3) @ 15 ppm during knee-high stage to boost cob elongation and grain rows"
        ],
        "prevention_steps": [
            "Select rust-resistant certified hybrid seeds (carrying Rp resistance genes)",
            "Optimize planting density to promote wind circulation and dry canopy",
            "Early planting to complete grain-fill before late-season rust spore peaks"
        ],
        "severity_threshold": "Moderate to High - If rust reaches ear leaf before silking, grain yield drops 20-40%."
    },
    "corn_northern_leaf_blight": {
        "crop": "Corn (Maize)",
        "disease_name": "Corn Northern Leaf Blight (NCLB)",
        "pathogen": "Exserohilum turcicum (Setosphaeria turcica)",
        "type": "Fungal",
        "description": "Characterized by prominent cigar-shaped, grayish-green to tan elongated necrotic lesions spanning several centimeters across maize leaves.",
        "symptoms": [
            "Long, elliptical, cigar-shaped lesions (2.5 to 15 cm long) with smooth margins",
            "Lesions turn tan to grayish with dark olive-green sporulation in humid weather",
            "Lower leaves infected first, advancing upward into the ear zone canopy",
            "Extensive leaf blighting causing entire canopy dry-down and severe kernel weight loss"
        ],
        "root_causes": [
            "Moderate temperatures (18°C - 27°C) accompanied by extended periods of dew (6-18 hours)",
            "Crop residue retention without tillage harboring overwintered fungal conidia",
            "Continuous corn-on-corn monoculture without rotation"
        ],
        "organic_treatments": [
            "Copper Oxychloride 50% WP @ 2.5 g/L",
            "Bacillus subtilis biological foliar spray @ 5 ml/L",
            "Neem extract 5% leaf drench"
        ],
        "chemical_treatments": [
            "Propiconazole 13.9% + Difenoconazole 13.9% EC @ 1.0 ml/L",
            "Tebuconazole 50% + Trifloxystrobin 25% WG (Nativo) @ 0.8 g/L",
            "Pyraclostrobin + Fluxapyroxad SC @ 0.8 ml/L"
        ],
        "growth_and_fertilizer_recovery": [
            "Foliar spray of 13-0-45 (Potassium Nitrate) @ 5 g/L + Boron (20%) @ 1 g/L to accelerate grain filling",
            "Apply Soluble Silicon / Potassium Silicate to harden cell walls against hyphal penetration",
            "Ensure adequate Nitrogen split top-dressing (Urea + Ammonium Sulfate)"
        ],
        "prevention_steps": [
            "Rotate fields with soybeans, alfalfa, or sorghum for at least 1-2 seasons",
            "Perform deep chisel plowing to bury infected corn stover",
            "Utilize hybrids with multigenic quantitative resistance"
        ],
        "severity_threshold": "High - Infections occurring 2 to 3 weeks after silking cause significant yield loss."
    },
    "rice_blast": {
        "crop": "Rice (Paddy)",
        "disease_name": "Rice Leaf Blast",
        "pathogen": "Magnaporthe oryzae (Pyricularia oryzae)",
        "type": "Fungal",
        "description": "The most catastrophic fungal disease of rice worldwide. Causes spindle-shaped or diamond-shaped lesions on leaves, as well as collar, node, and neck blast.",
        "symptoms": [
            "Spindle-shaped / diamond-shaped lesions with grayish-white centers and dark brown borders",
            "Lesions enlarge, coalesce, and cause complete burning/drying of leaf blades ('blast')",
            "Brownish rot of the flag leaf collar and rotting of the panicle neck ('neck blast')",
            "Chaffy, unfilled grains with white panicle heads ('white ears')"
        ],
        "root_causes": [
            "Excessive application of chemical Nitrogen fertilizer (especially single heavy doses of Urea)",
            "Extended leaf wetness (>10 hours) and temperatures between 20°C - 28°C",
            "Aerobic soil conditions / drought stress followed by flooding",
            "High plant density and shaded cloudy days"
        ],
        "organic_treatments": [
            "Pseudomonas fluorescens 1% WP seed treatment (10 g/kg) and foliar spray (5 g/L)",
            "Silicon fertilizer application (Calcium Silicate slag @ 500 kg/ha or liquid foliar silica @ 2 ml/L)",
            "Neem Seed Kernel Extract (NSKE 5%) foliar spray",
            "Panchagavya organic spray (3%) as foliar immunity booster"
        ],
        "chemical_treatments": [
            "Tricyclazole 75% WP @ 0.6 g/L (gold standard preventative and curative blast fungicide)",
            "Isoprothiolane 40% EC @ 1.5 ml/L",
            "Kasugamycin 3% SL @ 2.0 - 2.5 ml/L (antibiotic fungicide)",
            "Azoxystrobin 18.2% + Difenoconazole 11.4% SC @ 1.0 ml/L",
            "Carbendazim 50% WP @ 1.0 g/L (alternate to prevent resistance)"
        ],
        "growth_and_fertilizer_recovery": [
            "Immediately stop top-dressing with Urea / Nitrogen until blast lesions sporulate off",
            "Apply Muriate of Potash (MOP / 0-0-60) @ 20 kg/acre to improve silica deposition",
            "Foliar spray of Chelated Zinc (Zn-EDTA 12%) @ 1.5 g/L to stimulate tiller vigor",
            "Spray Gibberellic Acid (GA3) @ 20 ppm during panicle initiation to promote uniform exertion"
        ],
        "prevention_steps": [
            "Treat seeds with Tricyclazole or Carbendazim before sowing in nursery bed",
            "Split Nitrogen fertilizer into 3-4 split applications (Basal, Active Tillering, Panicle Initiation)",
            "Maintain continuous shallow water layer (2-3 cm) in paddy field during blast-favorable periods"
        ],
        "severity_threshold": "Critical - Neck blast can cause up to 70-100% crop loss in susceptible cultivars."
    },
    "rice_brown_spot": {
        "crop": "Rice (Paddy)",
        "disease_name": "Rice Brown Spot",
        "pathogen": "Bipolaris oryzae (Cochliobolus miyabeanus)",
        "type": "Fungal",
        "description": "Foliar fungal disease producing numerous circular to oval dark brown spots on leaves and glumes. Associated with nutrient-poor or stressed soils.",
        "symptoms": [
            "Small, circular to oval dark brown spots evenly dispersed over leaf surface",
            "Larger spots develop light brown or gray centers with bright yellow halos",
            "Infected seeds show dark brown to black discoloration and poor germination rate"
        ],
        "root_causes": [
            "Nutrient-deficient soils, particularly deficiency of Nitrogen, Potassium, Silicon, or Zinc",
            "Drought stress or sandy, leached soils with low organic matter",
            "Temperatures of 25°C - 30°C with high relative humidity"
        ],
        "organic_treatments": [
            "Apply well-rotted Farmyard Manure (FYM) or vermicompost @ 5 tons/ha",
            "Seed soaking in Trichoderma viride suspension (10 g/kg seed)",
            "Foliar spray of Cow urine extract (10%) + Neem leaf decoction"
        ],
        "chemical_treatments": [
            "Propiconazole 25% EC @ 1.0 ml/L",
            "Mancozeb 75% WP @ 2.5 g/L",
            "Hexaconazole 5% SC @ 2.0 ml/L",
            "Tebuconazole 25.9% EC @ 1.0 ml/L"
        ],
        "growth_and_fertilizer_recovery": [
            "Address fundamental soil deficiency: top-dress with balanced NPK + Zinc Sulphate (25 kg/ha)",
            "Foliar spray of 19-19-19 water soluble fertilizer @ 5 g/L with micronutrient mix",
            "Foliar spray of Humic Acid (98%) @ 2.5 g/L to reboot root nutrient uptake"
        ],
        "prevention_steps": [
            "Conduct soil test and correct nutrient depletion before next cropping cycle",
            "Use hot water seed treatment (53°C - 54°C for 10-12 minutes) to eradicate seedborne inoculum",
            "Maintain balanced water management avoiding severe drying out of paddy soil"
        ],
        "severity_threshold": "Moderate - Indicator of soil nutritional stress; manageable with soil rejuvenation."
    },
    "wheat_rust": {
        "crop": "Wheat",
        "disease_name": "Wheat Yellow / Stripe Rust",
        "pathogen": "Puccinia striiformis f. sp. tritici",
        "type": "Fungal",
        "description": "Severe foliar disease producing bright yellow-orange pustules arranged in characteristic continuous linear stripes along the leaf veins.",
        "symptoms": [
            "Linear stripes or rows of bright yellow to lemon-yellow powdery pustules along leaf veins",
            "Urediniospores rub off easily onto hands and clothes like yellow dust",
            "Chlorosis and drying of entire leaves, leading to shriveled grains with low test weight"
        ],
        "root_causes": [
            "Cool, moist weather (temperatures 10°C - 15°C with night dew)",
            "High humidity and intermittent sunlight in winter wheat zones",
            "Susceptible varieties lacking Yr resistance genes"
        ],
        "organic_treatments": [
            "Foliar spray of Wettable Sulfur 80% WDG @ 3 g/L",
            "Bio-formulation of Trichoderma harzianum @ 5 g/L",
            "Application of bio-silicon and seaweed kelp extract to strengthen leaf sheath"
        ],
        "chemical_treatments": [
            "Propiconazole 25% EC (Tilt) @ 1.0 ml/L (highly effective triazole standard)",
            "Tebuconazole 25.9% EC @ 1.0 ml/L",
            "Azoxystrobin + Tebuconazole SC @ 1.0 ml/L",
            "Triadimefon 25% WP @ 1.0 g/L"
        ],
        "growth_and_fertilizer_recovery": [
            "Foliar spray of Potassium Nitrate (13-0-45) @ 10 g/L to pump starch into developing wheat grains",
            "Spray Zinc-EDTA (12%) @ 1.0 g/L to support grain protein synthesis",
            "Apply Gibberellic Acid (GA3) @ 15 ppm at jointing stage for spikelet elongation"
        ],
        "prevention_steps": [
            "Sow certified rust-resistant wheat varieties recommended for the agro-climatic zone",
            "Timely sowing in November to escape late-season epidemic peaks",
            "Regular field scouting and immediate single-spray border treatment upon early focal spotting"
        ],
        "severity_threshold": "High - Can cause 50% to 100% crop failure if infection occurs prior to heading."
    },
    "cotton_bacterial_blight": {
        "crop": "Cotton",
        "disease_name": "Cotton Bacterial Blight / Angular Leaf Spot",
        "pathogen": "Xanthomonas citri pv. malvacearum",
        "type": "Bacterial",
        "description": "Bacterial infection causing angular water-soaked lesions bounded by leaf veinlets, black arm lesions on petioles/stems, and boll rot.",
        "symptoms": [
            "Angular, water-soaked lesions restricted by veins on the underside of cotyledons and leaves",
            "Lesions turn reddish-brown to dark brown and dry up",
            "Black elongated lesions on petioles and branches ('black arm' symptom)",
            "Round, water-soaked spots on green bolls causing premature drop or lint staining"
        ],
        "root_causes": [
            "High humidity (>85%) and warm temperatures (28°C - 35°C)",
            "Wind-driven rain, sand abrasion, and insect punctures allowing bacterial entry",
            "Infected acid-delinted or fuzzy seeds"
        ],
        "organic_treatments": [
            "Copper Hydroxide 53.8% DF @ 2.0 g/L",
            "Seed treatment with Pseudomonas fluorescens @ 10 g/kg seed",
            "Foliar spray of Streptomyces or Bacillus subtilis bio-formulations"
        ],
        "chemical_treatments": [
            "Streptocycline (Streptomycin sulphate 90% + Tetracycline hydrochloride 10%) @ 100 mg/L (1g in 10L water)",
            "Tank-mix Streptocycline with Copper Oxychloride 50% WP @ 2.5 g/L for synergistic action",
            "Bromo-nitro-propane-1,3-diol (Bronopol) @ 0.5 g/L"
        ],
        "growth_and_fertilizer_recovery": [
            "Apply Magnesium Sulphate (Epsom salt) @ 5 kg/acre + Urea @ 10 g/L to reverse chlorosis",
            "Foliar spray of 00-52-34 (MKP) @ 5 g/L to enhance boll retention and size",
            "Spray Alpha-Naphthyl Acetic Acid (NAA / Planofix) @ 4 ml per 15L water to prevent square and boll shedding"
        ],
        "prevention_steps": [
            "Use acid-delinted certified seeds treated with concentrated Sulfuric Acid (100 ml/kg seed)",
            "Avoid excessive plant densities that trap humid microclimates",
            "Destroy crop stalks and stubble after harvest by deep plowing"
        ],
        "severity_threshold": "Moderate to High - Boll rot leads to stained, poor-grade lint and harvest losses."
    },
    "apple_scab": {
        "crop": "Apple",
        "disease_name": "Apple Scab",
        "pathogen": "Venturia inaequalis",
        "type": "Fungal",
        "description": "The most significant fungal disease of apple orchards. Produces olive-green velvety spots on leaves and corky, scabby lesions on fruit.",
        "symptoms": [
            "Olive-green to velvety dull-brown circular spots on leaves",
            "Leaf distortion, curling, and early summer defoliation",
            "Fruit develops dark, olive-brown scabby lesions that become corky and crack",
            "Stunted, deformed, unmarketable apples"
        ],
        "root_causes": [
            "Cool, wet spring weather (15°C - 22°C) with persistent rain and canopy moisture",
            "Overwintered fungal pseudothecia surviving on fallen leaves on orchard floor",
            "Dense tree canopy with poor sunlight and air penetration"
        ],
        "organic_treatments": [
            "Liquid Lime Sulfur spray during green tip to pink bud stages",
            "Potassium Bicarbonate @ 3.0 g/L + horticultural summer oil (0.5%)",
            "Copper Hydroxide spray at silver tip stage prior to green cluster"
        ],
        "chemical_treatments": [
            "Difenoconazole 25% EC @ 0.5 ml/L",
            "Kresoxim-methyl 44.3% SC @ 0.5 ml/L",
            "Captan 50% WP @ 2.5 g/L or Dodine 65% WP @ 1.0 g/L",
            "Myclobutanil 10% WP @ 1.0 g/L"
        ],
        "growth_and_fertilizer_recovery": [
            "Foliar spray of Chelated Calcium (EDTA-Ca) @ 1.5 g/L to strengthen fruit cuticle against cracking",
            "Apply Boron (20%) @ 1 g/L at pink bud to improve fruit set and shape",
            "Seaweed extract spray @ 2 ml/L every 15 days to assist canopy recovery"
        ],
        "prevention_steps": [
            "Rake, chop, or spray fallen autumn leaves with 5% Urea solution to accelerate decomposition",
            "Winter pruning to open the tree center for rapid drying after rain",
            "Plant resistant apple cultivars (e.g. Enterprise, Liberty, Prima)"
        ],
        "severity_threshold": "High - Causes direct fruit devaluation and tree vigor depletion."
    },
    "grape_black_rot": {
        "crop": "Grape (Vineyard)",
        "disease_name": "Grape Black Rot",
        "pathogen": "Guignardia bidwellii (Phyllosticta ampelicida)",
        "type": "Fungal",
        "description": "Severe fungal disease causing reddish-brown circular leaf spots with black fruiting bodies (pycnidia), and shriveling berries into hard black mummies.",
        "symptoms": [
            "Small reddish-brown circular spots with dark margins and tiny black pepper-like pycnidia on leaves",
            "Infected berries turn pale, then soft and rot completely within 48 hours",
            "Berries shrivel, turn purplish-black, and form hard wrinkled 'mummies' that cling to clusters"
        ],
        "root_causes": [
            "Warm, humid conditions (21°C - 27°C) with frequent rain events",
            "Overwintered mummified berries left hanging on trellises or lying on ground",
            "Poor vine training resulting in dense, shaded foliage"
        ],
        "organic_treatments": [
            "Copper Hydroxide 77% WP @ 2.0 g/L",
            "Bordeaux mixture (1.0%) preventative sprays",
            "Bacillus subtilis bio-fungicide @ 4 ml/L"
        ],
        "chemical_treatments": [
            "Myclobutanil 10% WP @ 1.0 g/L",
            "Mancozeb 75% WP @ 2.5 g/L (apply from bud break through pre-bloom)",
            "Azoxystrobin 23% SC @ 0.8 ml/L",
            "Kresoxim-methyl 44.3% SC @ 0.7 ml/L"
        ],
        "growth_and_fertilizer_recovery": [
            "Apply Potassium Nitrate (13-0-45) @ 5 g/L to optimize berry enlargement and sugar accumulation",
            "Gibberellic Acid (GA3) cluster spray @ 10-20 ppm at 3-4 mm berry size for bunch elongation and loose clusters",
            "Zinc and Boron chelated spray @ 1 g/L each during flowering for berry set"
        ],
        "prevention_steps": [
            "Strict sanitation: remove all mummified berries from vines and disc the vineyard floor",
            "Canopy management: shoot thinning, leaf pulling around fruit zones to maximize sun exposure",
            "Follow strict preventative fungicide schedule from 3-inch shoot stage to 4 weeks post-bloom"
        ],
        "severity_threshold": "High - Can wipe out 80% to 100% of grape cluster harvest if untreated during bloom."
    },
    "healthy_crop": {
        "crop": "All Crops",
        "disease_name": "Healthy Plant (No Disease Detected)",
        "pathogen": "None - Plant Tissue is Healthy and Vigorous",
        "type": "Healthy Baseline",
        "description": "The leaf shows vigorous green chlorophyll pigmentation, intact epidermal margins, active vascular vein architecture, and zero detectable pathogen lesions.",
        "symptoms": [
            "Uniform vibrant green coloration",
            "Intact leaf lamina without chlorosis, necrosis, or fungal pustules",
            "Turgid petiole and normal leaf expansion"
        ],
        "root_causes": [
            "Optimal agronomic care, balanced nutrition, and favorable climate"
        ],
        "organic_treatments": [
            "Preventative bio-inoculation: apply Trichoderma harzianum or Bacillus subtilis monthly @ 3 g/L",
            "Foliar spray of Vermiwash or Panchagavya (3%) to sustain beneficial phyllosphere microflora",
            "Mulch soil with organic straw or shredded leaves to maintain moisture"
        ],
        "chemical_treatments": [
            "No chemical fungicides or bactericides required",
            "Maintain preventative scouting every 3-5 days during monsoon or humid periods"
        ],
        "growth_and_fertilizer_recovery": [
            "Apply CropGuard Yield Booster Protocol for rapid vegetative expansion and heavy fruiting",
            "Vegetative stage: N-P-K 19-19-19 + Micronutrients (Zn, Fe, Mn) @ 4 g/L foliar",
            "Flowering/Fruiting stage: N-P-K 0-52-34 (MKP) @ 5 g/L + Boron (20%) @ 1 g/L",
            "Final Bulking stage: Potassium Sulphate 0-0-50 @ 5 g/L for maximum fruit/grain weight and size",
            "Humic Acid (98%) soil drench @ 3 g/L every 21 days for massive root proliferation"
        ],
        "prevention_steps": [
            "Maintain soil moisture at 60-70% field capacity with drip irrigation",
            "Test soil NPK and micronutrients once per crop season",
            "Ensure companion planting and crop rotation to sustain disease immunity"
        ],
        "severity_threshold": "None - Plant is thriving! Focus on maximizing yield, speed, and fruit size."
    }
}

def get_disease_info(disease_key: str) -> Dict[str, Any]:
    """Retrieve full clinical profile and treatments for a given disease."""
    return DISEASE_DATABASE.get(disease_key, DISEASE_DATABASE["healthy_crop"])

def list_supported_crops() -> List[str]:
    """List all supported crops in the knowledgebase."""
    crops = sorted(list(set([v["crop"] for v in DISEASE_DATABASE.values()])))
    return crops

def get_diseases_by_crop(crop_name: str) -> List[Dict[str, Any]]:
    """Retrieve all diseases associated with a given crop."""
    results = []
    for k, v in DISEASE_DATABASE.items():
        if crop_name.lower() in v["crop"].lower() or v["crop"] == "All Crops":
            results.append({"key": k, **v})
    return results
