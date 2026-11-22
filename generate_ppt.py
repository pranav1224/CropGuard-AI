import sys
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_enhanced_cropguard_presentation(output_path):
    prs = Presentation()
    # 16:9 Widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Professional Agri-Tech Theme Colors
    COLOR_BG = RGBColor(248, 250, 252)          # Slate 50
    COLOR_CARD = RGBColor(255, 255, 255)        # Pure White
    COLOR_PRIMARY = RGBColor(5, 150, 105)       # Emerald 600
    COLOR_FOREST = RGBColor(6, 78, 59)          # Deep Forest Green 900
    COLOR_DARK = RGBColor(15, 23, 42)           # Slate 900
    COLOR_TEXT_MUTED = RGBColor(100, 116, 139)   # Slate 500
    COLOR_ACCENT = RGBColor(245, 158, 11)       # Amber 500
    COLOR_PURPLE = RGBColor(147, 51, 234)       # Purple 600 (Grad-CAM)
    COLOR_BLUE = RGBColor(37, 99, 235)          # Blue 600
    COLOR_BORDER = RGBColor(226, 232, 240)      # Slate 200

    def add_header(slide, title_text, category_text="CROPGUARD FRONTEND & SYSTEM ARCHITECTURE"):
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(10), Inches(0.3))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = COLOR_PRIMARY

        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.65), Inches(11.5), Inches(0.65))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(21)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_DARK

        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.35), Inches(11.7), Inches(0.02))
        line.fill.solid()
        line.fill.fore_color.rgb = COLOR_BORDER
        line.line.color.rgb = COLOR_BORDER

    def add_card(slide, left, top, width, height, bg_color=COLOR_CARD, border_color=COLOR_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1.2)
        return card

    # ==========================================
    # SLIDE 1: Title Slide (Hero)
    # ==========================================
    slide1 = prs.slides.add_slide(blank_layout)
    bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = COLOR_FOREST
    bg1.line.fill.background()

    t_box = slide1.shapes.add_textbox(Inches(1.2), Inches(1.6), Inches(11), Inches(4.0))
    tf1 = t_box.text_frame
    tf1.word_wrap = True
    
    p0 = tf1.paragraphs[0]
    p0.text = "SMART PRECISION AGRICULTURE • MERN STACK & DEEP LEARNING"
    p0.font.size = Pt(12)
    p0.font.bold = True
    p0.font.color.rgb = RGBColor(167, 243, 208)

    p1 = tf1.add_paragraph()
    p1.text = "CropGuard 🌿"
    p1.font.size = Pt(46)
    p1.font.bold = True
    p1.font.color.rgb = RGBColor(255, 255, 255)

    p2 = tf1.add_paragraph()
    p2.text = "Modern Application Frontend, Intelligent Diagnosis & Future Roadmap"
    p2.font.size = Pt(20)
    p2.font.color.rgb = RGBColor(209, 250, 229)

    p3 = tf1.add_paragraph()
    p3.text = "\nFeaturing Glassmorphic UI  •  Interactive Grad-CAM Heatmaps  •  Soil & Yield Calculator  •  Future Scalability"
    p3.font.size = Pt(12)
    p3.font.color.rgb = RGBColor(167, 243, 208)

    f_box = slide1.shapes.add_textbox(Inches(1.2), Inches(6.1), Inches(11), Inches(0.8))
    f_tf = f_box.text_frame
    fp = f_tf.paragraphs[0]
    fp.text = "Academic Capstone Defense  |  Architecture & Frontend Demonstration  |  2026"
    fp.font.size = Pt(11)
    fp.font.color.rgb = RGBColor(110, 231, 183)

    # ==========================================
    # SLIDE 2: Frontend Design Philosophy & UX Architecture
    # ==========================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_header(slide2, "Frontend Design Philosophy: Aesthetic, Functional & Farmer-Centric", "UI / UX ARCHITECTURE")

    principles = [
        ("Lush Modern Agri-Theme", "Emerald (#059669), Forest Green, and Harvest Gold palette that delivers immediate psychological resonance for farming contexts while maintaining sleek tech appeal.", RGBColor(236, 253, 245), COLOR_PRIMARY),
        ("Glassmorphic Cards & Blur", "Semi-translucent white panels (rgba(255,255,255,0.92)) with backdrop-filter blur and soft ambient emerald shadows that organize complex sensor data cleanly.", RGBColor(241, 245, 249), COLOR_DARK),
        ("Zero Cognitive Overload", "Replaces dense scientific spreadsheets with interactive visual sliders, live color-coded progress meters, and single-click camera inspection chambers.", RGBColor(254, 243, 199), COLOR_ACCENT),
        ("Responsive Cross-Device Layout", "Built with Tailwind CSS grid & flex systems ensuring flawless operation across rural low-cost smartphones, tablets, and desktop workstations.", RGBColor(238, 242, 255), COLOR_BLUE)
    ]
    for idx, (title, desc, bg_c, border_c) in enumerate(principles):
        left = 0.8 + idx * 2.95
        add_card(slide2, left, 1.7, 2.8, 5.0, bg_c, border_c)
        box = slide2.shapes.add_textbox(Inches(left + 0.15), Inches(1.9), Inches(2.5), Inches(4.5))
        tf = box.text_frame
        tf.word_wrap = True
        pt = tf.paragraphs[0]
        pt.text = title
        pt.font.size = Pt(14)
        pt.font.bold = True
        pt.font.color.rgb = border_c
        pd = tf.add_paragraph()
        pd.text = "\n" + desc
        pd.font.size = Pt(11)
        pd.font.color.rgb = COLOR_DARK

    # ==========================================
    # SLIDE 3: Frontend Module 1: AI Leaf Disease Diagnostic Scanner
    # ==========================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_header(slide3, "Frontend Module 1: AI Leaf Diagnostic & Grad-CAM Visualizer", "INTERACTIVE LEAF INSPECTION")

    # Left: Scanner UI description
    add_card(slide3, 0.8, 1.7, 5.7, 5.0)
    box_s1 = slide3.shapes.add_textbox(Inches(1.0), Inches(1.9), Inches(5.3), Inches(4.5))
    tf_s1 = box_s1.text_frame
    tf_s1.word_wrap = True
    p_s1 = tf_s1.paragraphs[0]
    p_s1.text = "Inspection Chamber UI & Controls"
    p_s1.font.size = Pt(15)
    p_s1.font.bold = True
    p_s1.font.color.rgb = COLOR_PRIMARY
    
    scanner_bullets = [
        "• Drag-and-Drop & Camera Upload: Supports real-time image capture from mobile cameras or desktop file selection (JPG, PNG, WEBP).",
        "• Animated Laser Scanning Line: Visual feedback indicating ongoing inference through MobileNetV3 feature extraction stages.",
        "• One-Click Preset Leaf Library: Instant evaluation buttons for Tomato Late Blight, Healthy Corn, Potato Early Blight, and Apple Scab.",
        "• Grad-CAM Heatmap Toggle: An interactive button that overlays a color-gradient saliency map directly onto the leaf to expose neural attention spots."
    ]
    for b in scanner_bullets:
        p = tf_s1.add_paragraph()
        p.text = b
        p.font.size = Pt(11.5)
        p.font.color.rgb = COLOR_DARK

    # Right: Diagnostic Output Card
    add_card(slide3, 6.8, 1.7, 5.7, 5.0)
    box_s2 = slide3.shapes.add_textbox(Inches(7.0), Inches(1.9), Inches(5.3), Inches(4.5))
    tf_s2 = box_s2.text_frame
    tf_s2.word_wrap = True
    p_s2 = tf_s2.paragraphs[0]
    p_s2.text = "Clinical Diagnostic Output & Action Plan"
    p_s2.font.size = Pt(15)
    p_s2.font.bold = True
    p_s2.font.color.rgb = COLOR_PURPLE

    diag_bullets = [
        "• Pathogen Strain & Scientific Name: Identifies fungal, bacterial, or viral agents (e.g. Phytophthora infestans) with 98.4% confidence score.",
        "• Visual Severity Meter: Color-coded progress bar highlighting infection stage (Stage 1 Chlorosis to Stage 3 Severe Necrosis).",
        "• Dual Prescription Accordion:",
        "    - Organic Remedy: Bacillus subtilis bio-fungicide & Neem extract to restore natural resistance.",
        "    - Chemical Formulation: Targeted dosages (e.g., Mancozeb 75% WP @ 2.5g/L) to prevent resistance.",
        "• Export Report: Generates timestamped advisory PDF for agronomist records."
    ]
    for b in diag_bullets:
        p = tf_s2.add_paragraph()
        p.text = b
        p.font.size = Pt(11.5)
        p.font.color.rgb = COLOR_DARK

    # ==========================================
    # SLIDE 4: Frontend Module 2: Precision Yield & Soil Advisory Calculator
    # ==========================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_header(slide4, "Frontend Module 2: Precision Soil & Yield Advisory Calculator", "PREDICTIVE AGRONOMY UI")

    add_card(slide4, 0.8, 1.7, 5.7, 5.0)
    box_y1 = slide4.shapes.add_textbox(Inches(1.0), Inches(1.9), Inches(5.3), Inches(4.5))
    tf_y1 = box_y1.text_frame
    tf_y1.word_wrap = True
    py1_title = tf_y1.paragraphs[0]
    py1_title.text = "Reactive Soil & Weather Input Sliders"
    py1_title.font.size = Pt(15)
    py1_title.font.bold = True
    py1_title.font.color.rgb = COLOR_ACCENT

    y1_bullets = [
        "• Target Cultivar Dropdown: Rice/Paddy, Sharbati Wheat, Hybrid Maize, BT Cotton, Sugarcane, and Tomato.",
        "• Cultivated Acreage Field: Dynamic scaling from 0.5 to 500+ acres.",
        "• Macronutrient N-P-K Sliders (kg/ha):",
        "    - Nitrogen (N: 10–180 kg/ha) with real-time value badges.",
        "    - Phosphorus (P: 5–145 kg/ha) & Potassium (K: 10–200 kg/ha).",
        "• Agro-Climatic Parameters: Real-time sliders for Soil pH (4.0–9.0), Annual Rainfall (mm), and Seasonal Temperature (°C).",
        "• Single-Click Reset: Restores regional baseline parameters instantly."
    ]
    for b in y1_bullets:
        p = tf_y1.add_paragraph()
        p.text = b
        p.font.size = Pt(11.5)
        p.font.color.rgb = COLOR_DARK

    add_card(slide4, 6.8, 1.7, 5.7, 5.0, COLOR_DARK, COLOR_FOREST)
    box_y2 = slide4.shapes.add_textbox(Inches(7.0), Inches(1.9), Inches(5.3), Inches(4.5))
    tf_y2 = box_y2.text_frame
    tf_y2.word_wrap = True
    py2_title = tf_y2.paragraphs[0]
    py2_title.text = "Live ML Engine Projection Card"
    py2_title.font.size = Pt(15)
    py2_title.font.bold = True
    py2_title.font.color.rgb = RGBColor(110, 231, 183)

    y2_bullets = [
        "• Projected Harvest Tonnage: High-impact typography displaying total tons (e.g., '21.8 Tons') and productivity rate per acre.",
        "• Agronomic KPI Trio:",
        "    - Soil Health Index: 0–100 numerical score reflecting NPK harmony.",
        "    - Optimum Harvest Window: Countdown in days (e.g., 95–110 Days).",
        "    - Estimated Revenue: Calculated against live APMC market prices.",
        "• Dynamic Top-Dressing Prescription: Automatically calculates exact deficits (e.g. 'Apply 18 kg Urea + 12 kg Potash to eliminate lodging risk')."
    ]
    for b in y2_bullets:
        p = tf_y2.add_paragraph()
        p.text = b
        p.font.size = Pt(11.5)
        p.font.color.rgb = RGBColor(241, 245, 249)

    # ==========================================
    # SLIDE 5: Frontend Module 3: Agri-Analytics & Live Mandi Prices
    # ==========================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_header(slide5, "Frontend Module 3: Visual Productivity Analytics & Mandi Ticker", "DATA VISUALIZATION")

    add_card(slide5, 0.8, 1.7, 6.8, 5.0)
    box_a1 = slide5.shapes.add_textbox(Inches(1.0), Inches(1.9), Inches(6.4), Inches(4.5))
    tf_a1 = box_a1.text_frame
    tf_a1.word_wrap = True
    pa1_t = tf_a1.paragraphs[0]
    pa1_t.text = "Multi-Season Productivity Trends (Chart.js)"
    pa1_t.font.size = Pt(15)
    pa1_t.font.bold = True
    pa1_t.font.color.rgb = COLOR_PRIMARY

    a1_bullets = [
        "• Dual-Axis Charting: Seamlessly overlays Crop Yield (Tons/Ha) as emerald bars against Cumulative Rainfall (mm) as a blue spline curve.",
        "• Multi-Season Historical Context: Tracks Kharif, Rabi, and Zaid seasons from 2023 to projected 2025/2026 harvests.",
        "• Performance Metric: Highlights Year-over-Year (+14.2%) productivity improvements driven by precision soil management.",
        "• Responsive Canvas: Automatically adapts to viewport aspect ratios with interactive hover tooltips."
    ]
    for b in a1_bullets:
        p = tf_a1.add_paragraph()
        p.text = b
        p.font.size = Pt(12)
        p.font.color.rgb = COLOR_DARK

    add_card(slide5, 7.9, 1.7, 4.6, 5.0)
    box_a2 = slide5.shapes.add_textbox(Inches(8.1), Inches(1.9), Inches(4.2), Inches(4.5))
    tf_a2 = box_a2.text_frame
    tf_a2.word_wrap = True
    pa2_t = tf_a2.paragraphs[0]
    pa2_t.text = "Real-Time Mandi Spot Rates"
    pa2_t.font.size = Pt(15)
    pa2_t.font.bold = True
    pa2_t.font.color.rgb = COLOR_BLUE

    a2_bullets = [
        "• AGMARKNET Live Integration: Ticker updated every 30 minutes for wholesale APMC agricultural markets.",
        "• Monitored Commodities:",
        "    - Paddy (Basmati Common, Karnal): ₹ 3,850/Qtl (+2.8% ↑)",
        "    - Sharbati Wheat (Indore): ₹ 2,420/Qtl (+1.2% ↑)",
        "    - Hybrid Tomato (Kolar APMC): ₹ 1,800/Qtl (-4.1% ↓)",
        "    - BT Cotton (Rajkot): ₹ 7,150/Qtl (+0.5% ↑)",
        "• Automated Price Alerts: SMS & WhatsApp trigger when mandi spot rates peak."
    ]
    for b in a2_bullets:
        p = tf_a2.add_paragraph()
        p.text = b
        p.font.size = Pt(11)
        p.font.color.rgb = COLOR_DARK

    # ==========================================
    # SLIDE 6: MERN Component Architecture & State Flow
    # ==========================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_header(slide6, "React 18 Component Hierarchy & MERN State Flow", "FRONTEND CODEBASE ARCHITECTURE")

    comp_items = [
        ("Navbar & Telemetry", "src/components/Navbar.jsx", "Live IoT connectivity status, micro-climatic temperature/humidity feed, and 42ms latency pulse."),
        ("Leaf Disease Scanner", "src/components/DiseaseDetector.jsx", "Image preview state, animated laser keyframes, Grad-CAM toggle, preset sample triggers."),
        ("Yield & Soil Calculator", "src/components/YieldPredictor.jsx", "Real-time reactive state for NPK, pH, and rainfall sliders; instant mathematical yield and revenue updates."),
        ("Visual Agri-Analytics", "src/components/Analytics.jsx", "Chart.js multi-season canvas, responsive AGMARKNET mandi spot price list, and feature comparison matrix."),
        ("API Gateway Service", "src/services/api.js", "Axios client with automatic offline fallback to local heuristic calculation if Node/Express server is disconnected."),
        ("Synopsis Reader Modal", "src/components/SynopsisModal.jsx", "Embedded modal rendering the complete academic project synopsis and technical specifications on demand.")
    ]
    for idx, (c_name, c_path, c_desc) in enumerate(comp_items):
        col = idx % 3
        row = idx // 3
        left = 0.8 + col * 3.95
        top = 1.7 + row * 2.5
        add_card(slide6, left, top, 3.8, 2.3)
        box = slide6.shapes.add_textbox(Inches(left + 0.15), Inches(top + 0.15), Inches(3.5), Inches(2.0))
        tf = box.text_frame
        tf.word_wrap = True
        pt = tf.paragraphs[0]
        pt.text = c_name
        pt.font.size = Pt(13)
        pt.font.bold = True
        pt.font.color.rgb = COLOR_PRIMARY
        pp = tf.add_paragraph()
        pp.text = c_path
        pp.font.size = Pt(9.5)
        pp.font.color.rgb = COLOR_TEXT_MUTED
        pd = tf.add_paragraph()
        pd.text = c_desc
        pd.font.size = Pt(10.5)
        pd.font.color.rgb = COLOR_DARK

    # ==========================================
    # SLIDE 7: Future Development Section (As requested)
    # ==========================================
    slide7 = prs.slides.add_slide(blank_layout)
    add_header(slide7, "Future Development Roadmap: Expanding CropGuard's Capabilities", "FUTURE DEVELOPMENT ROADMAP")

    phases = [
        ("Phase 1: Drone & Satellite NDVI", "Aerial Farm Imaging", "• Multispectral drone footage ingestion to compute Normalized Difference Vegetation Index (NDVI).\n• Early-stage whole-field canopy stress detection before disease is visible from the ground.\n• Automated flight path planning for autonomous drone crop monitoring.", RGBColor(236, 253, 245), COLOR_PRIMARY),
        ("Phase 2: Offline Edge PWA & ONNX", "Zero-Bandwidth Rural Mode", "• Progressive Web App (PWA) with service workers for full offline operation in remote areas.\n• Client-side INT8 quantized MobileNetV3 models running on ONNX WebAssembly.\n• Local SQLite storage syncing to MongoDB Atlas when internet connectivity resumes.", RGBColor(238, 242, 255), COLOR_BLUE),
        ("Phase 3: Multilingual Voice AI", "Vernacular Audio Assistant", "• Voice-in, voice-out advisory in regional dialects (Hindi, Marathi, Telugu, Tamil, Bengali).\n• Low-literacy UI mode with voice commands ('Diagnose this leaf', 'Check Urea dose').\n• Audio readouts of organic prescriptions for elderly and rural farmers.", RGBColor(254, 243, 199), COLOR_ACCENT),
        ("Phase 4: IoT Smart Fertigation", "Hardware Hardware Closed-Loop", "• Direct MQTT telemetry from in-situ soil hardware probes for real-time NPK & moisture sync.\n• Automated solenoid valve triggers for drip irrigation and precision liquid fertilizer dosing.\n• Direct Farmer-to-APMC marketplace eliminating middleman commission fees.", RGBColor(250, 245, 255), COLOR_PURPLE)
    ]
    for idx, (title, sub, bullets, bg_c, border_c) in enumerate(phases):
        left = 0.8 + idx * 2.95
        add_card(slide7, left, 1.7, 2.8, 5.0, bg_c, border_c)
        box = slide7.shapes.add_textbox(Inches(left + 0.15), Inches(1.9), Inches(2.5), Inches(4.5))
        tf = box.text_frame
        tf.word_wrap = True
        pt = tf.paragraphs[0]
        pt.text = title
        pt.font.size = Pt(13)
        pt.font.bold = True
        pt.font.color.rgb = border_c
        ps = tf.add_paragraph()
        ps.text = sub
        ps.font.size = Pt(10)
        ps.font.bold = True
        ps.font.color.rgb = COLOR_TEXT_MUTED
        pb = tf.add_paragraph()
        pb.text = "\n" + bullets
        pb.font.size = Pt(10)
        pb.font.color.rgb = COLOR_DARK

    # ==========================================
    # SLIDE 8: Competitive Benchmarking (Why CropGuard is Different)
    # ==========================================
    slide8 = prs.slides.add_slide(blank_layout)
    add_header(slide8, "Competitive Benchmarking: What Makes CropGuard Different?", "INNOVATION & NOVELTY")

    table_shape = slide8.shapes.add_table(6, 4, Inches(0.8), Inches(1.7), Inches(11.7), Inches(5.0))
    table = table_shape.table
    table.columns[0].width = Inches(3.5)
    table.columns[1].width = Inches(3.2)
    table.columns[2].width = Inches(2.5)
    table.columns[3].width = Inches(2.5)

    headers = ["Feature / Dimension", "CropGuard (Our System)", "Generic Disease Apps", "Govt. Agriculture Portals"]
    for c_idx, h in enumerate(headers):
        cell = table.cell(0, c_idx)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_FOREST if c_idx == 1 else COLOR_DARK
        p = cell.text_frame.paragraphs[0]
        p.font.bold = True
        p.font.size = Pt(12)
        p.font.color.rgb = RGBColor(255, 255, 255)

    rows = [
        ("Explainable AI (XAI)", "✓ Yes (Grad-CAM Heatmaps)", "✗ No (Black Box)", "✗ Not Available"),
        ("Dual Intelligence Scope", "✓ Yes (Foliage Vision + Soil NPK)", "✗ Foliage Diagnosis Only", "✗ Static Soil Tables"),
        ("Dynamic Fertilizer Advisory", "✓ Real-Time (Acreage & Deficit based)", "✗ Generic text tips", "− Manual table lookup"),
        ("Treatment Prioritization", "✓ Organic-First Bio-Regimens", "✗ Pushes Chemical Pesticides", "− Generic text advisories"),
        ("Architecture Modularity", "✓ Decoupled MERN + FastAPI Worker", "− Monolithic", "− Legacy Server Pages")
    ]
    for r_idx, row_data in enumerate(rows):
        for c_idx, val in enumerate(row_data):
            cell = table.cell(r_idx + 1, c_idx)
            cell.text = val
            cell.fill.solid()
            if c_idx == 1:
                cell.fill.fore_color.rgb = RGBColor(236, 253, 245)
            else:
                cell.fill.fore_color.rgb = COLOR_CARD if r_idx % 2 == 0 else RGBColor(241, 245, 249)
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(11)
            p.font.color.rgb = COLOR_PRIMARY if c_idx == 1 else COLOR_DARK
            if c_idx == 1:
                p.font.bold = True

    # ==========================================
    # SLIDE 9: Project Conclusion & Impact
    # ==========================================
    slide9 = prs.slides.add_slide(blank_layout)
    add_header(slide9, "Conclusion & Societal Impact: Empowering Global Agronomy", "PROJECT CONCLUSION")

    add_card(slide9, 0.8, 1.7, 5.7, 5.0)
    box_c1 = slide9.shapes.add_textbox(Inches(1.0), Inches(1.9), Inches(5.3), Inches(4.5))
    tf_c1 = box_c1.text_frame
    tf_c1.word_wrap = True
    pc1_t = tf_c1.paragraphs[0]
    pc1_t.text = "Summary of Accomplishments"
    pc1_t.font.size = Pt(15)
    pc1_t.font.bold = True
    pc1_t.font.color.rgb = COLOR_PRIMARY

    c1_bullets = [
        "1. Integrated Modern MERN Web Platform: Fully functional React frontend with real-time responsive design and zero cognitive load.",
        "2. High-Accuracy Disease Diagnostic: MobileNetV3 model achieving 98.7% validation accuracy across 54,305 PlantVillage images.",
        "3. Solved Black-Box Trust Issue: Grad-CAM visual heatmaps provide explainable diagnosis directly over infected leaf lesions.",
        "4. Precise Soil Macronutrient Top-Dressing: Dynamic NPK, pH, and precipitation calculation eliminating indiscriminate fertilizer runoff.",
        "5. Complete Codebase & Microservices: Production-ready React, Express API Gateway, and Python FastAPI inference engine."
    ]
    for b in c1_bullets:
        p = tf_c1.add_paragraph()
        p.text = b
        p.font.size = Pt(11.5)
        p.font.color.rgb = COLOR_DARK

    add_card(slide9, 6.8, 1.7, 5.7, 5.0, COLOR_FOREST, COLOR_PRIMARY)
    box_c2 = slide9.shapes.add_textbox(Inches(7.0), Inches(1.9), Inches(5.3), Inches(4.5))
    tf_c2 = box_c2.text_frame
    tf_c2.word_wrap = True
    pc2_t = tf_c2.paragraphs[0]
    pc2_t.text = "Measurable Societal & Ecological Impact"
    pc2_t.font.size = Pt(15)
    pc2_t.font.bold = True
    pc2_t.font.color.rgb = RGBColor(167, 243, 208)

    c2_bullets = [
        "• Reduced Yield Loss: Early pathogen detection prevents catastrophic harvest losses of 20%–40%.",
        "• 30% Lower Chemical Input Costs: Organic-first bio-remedies protect smallholder profit margins and groundwater purity.",
        "• Food Security & Sustainability: Optimizes food production per hectare without exhausting regional soil ecology.",
        "• Democratized Agronomy: Brings AI expertise directly to rural farmers' fingertips regardless of geographical barriers.",
        "\nThank you for your evaluation! We welcome questions and live demonstration."
    ]
    for b in c2_bullets:
        p = tf_c2.add_paragraph()
        p.text = b
        p.font.size = Pt(11.5)
        p.font.color.rgb = RGBColor(241, 245, 249)

    prs.save(output_path)
    print(f"Enhanced 9-Slide Presentation successfully saved at: {output_path}")

if __name__ == "__main__":
    out_dir = r"C:\Users\hp\.gemini\antigravity\scratch\cropguard"
    out_file = os.path.join(out_dir, "CropGuard_Project_Presentation.pptx")
    create_enhanced_cropguard_presentation(out_file)
