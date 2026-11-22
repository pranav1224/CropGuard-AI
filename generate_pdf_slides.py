import os
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def generate_pdf_slides(output_path):
    # 16:9 Widescreen slide dimensions in points (1152 x 648 pt)
    WIDTH = 16 * 72
    HEIGHT = 9 * 72
    
    # Palette
    C_FOREST = HexColor("#064e3b")
    C_EMERALD = HexColor("#059669")
    C_LIGHT_GREEN = HexColor("#ecfdf5")
    C_AMBER = HexColor("#d97706")
    C_LIGHT_AMBER = HexColor("#fef3c7")
    C_BLUE = HexColor("#2563eb")
    C_LIGHT_BLUE = HexColor("#eff6ff")
    C_PURPLE = HexColor("#7c3aed")
    C_LIGHT_PURPLE = HexColor("#f5f3ff")
    C_DARK = HexColor("#0f172a")
    C_SLATE_BG = HexColor("#f8fafc")
    C_WHITE = HexColor("#ffffff")
    C_BORDER = HexColor("#e2e8f0")
    C_MUTED = HexColor("#64748b")
    C_RED = HexColor("#dc2626")
    C_LIGHT_RED = HexColor("#fef2f2")

    c = canvas.Canvas(output_path, pagesize=(WIDTH, HEIGHT))

    def draw_slide_header(title, category="CROPGUARD PRECISION AGRICULTURE", slide_num=1):
        # Base background
        c.setFillColor(C_SLATE_BG)
        c.rect(0, 0, WIDTH, HEIGHT, fill=1, stroke=0)
        
        # Header category
        c.setFillColor(C_EMERALD)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(60, HEIGHT - 45, category.upper())
        
        # Title
        c.setFillColor(C_DARK)
        c.setFont("Helvetica-Bold", 24)
        c.drawString(60, HEIGHT - 78, title)
        
        # Header line
        c.setStrokeColor(C_BORDER)
        c.setLineWidth(1)
        c.line(60, HEIGHT - 92, WIDTH - 60, HEIGHT - 92)
        
        # Footer
        c.setStrokeColor(C_BORDER)
        c.line(60, 45, WIDTH - 60, 45)
        c.setFillColor(C_MUTED)
        c.setFont("Helvetica", 10)
        c.drawString(60, 28, "CropGuard: MERN + AI Precision Agriculture Platform • Presentation Deck")
        c.drawRightString(WIDTH - 60, 28, f"Slide {slide_num} of 9")

    def draw_card(x, y, w, h, bg_color=C_WHITE, border_color=C_BORDER):
        c.setFillColor(bg_color)
        c.setStrokeColor(border_color)
        c.setLineWidth(1.2)
        c.roundRect(x, y, w, h, 14, fill=1, stroke=1)

    # ==========================================
    # SLIDE 1: Title Slide (Hero)
    # ==========================================
    c.setFillColor(C_FOREST)
    c.rect(0, 0, WIDTH, HEIGHT, fill=1, stroke=0)
    
    # Hero Title & Subtitle
    c.setFillColor(HexColor("#a7f3d0"))
    c.setFont("Helvetica-Bold", 13)
    c.drawString(80, HEIGHT - 180, "AI-POWERED PRECISION AGRICULTURE • MERN STACK & DEEP LEARNING")
    
    c.setFillColor(C_WHITE)
    c.setFont("Helvetica-Bold", 50)
    c.drawString(80, HEIGHT - 245, "CropGuard")
    
    c.setFillColor(HexColor("#34d399"))
    c.setFont("Helvetica-Bold", 40)
    c.drawString(360, HEIGHT - 245, "🌿")

    c.setFillColor(HexColor("#d1fae5"))
    c.setFont("Helvetica", 22)
    c.drawString(80, HEIGHT - 295, "Modern Application Frontend, Intelligent Diagnosis & Future Roadmap")

    # Metadata Pills
    pill_y = HEIGHT - 370
    pills = ["MobileNetV3 Deep Vision", "Grad-CAM Explainable AI", "XGBoost Yield Engine", "Decoupled MERN Stack"]
    px = 80
    for pill in pills:
        c.setFillColor(HexColor("#065f46"))
        c.setStrokeColor(HexColor("#10b981"))
        c.setLineWidth(1)
        w_pill = len(pill) * 9 + 25
        c.roundRect(px, pill_y, w_pill, 32, 8, fill=1, stroke=1)
        c.setFillColor(HexColor("#d1fae5"))
        c.setFont("Helvetica-Bold", 11)
        c.drawString(px + 12, pill_y + 10, pill)
        px += w_pill + 16

    # Bottom Presenter
    c.setStrokeColor(HexColor("#047857"))
    c.line(80, 80, WIDTH - 80, 80)
    c.setFillColor(HexColor("#a7f3d0"))
    c.setFont("Helvetica", 12)
    c.drawString(80, 55, "Final Year Project Defense & Demonstration • Academic Year 2026")
    c.drawRightString(WIDTH - 80, 55, "Presented by CropGuard Engineering Team")
    c.showPage()

    # ==========================================
    # SLIDE 2: Frontend Design Philosophy & UX
    # ==========================================
    draw_slide_header("Frontend Design Philosophy: Aesthetic, Functional & Farmer-Centric", "UI / UX ARCHITECTURE", 2)
    
    cards_s2 = [
        ("Lush Modern Agri-Theme", "Emerald (#059669), Forest Green, and Harvest Gold palette designed for psychological resonance in farming contexts while maintaining clean tech appeal.", C_LIGHT_GREEN, C_EMERALD),
        ("Glassmorphic Cards", "Semi-translucent white cards (rgba(255,255,255,0.92)) with backdrop blur and soft ambient emerald shadows to eliminate visual clutter.", C_WHITE, C_BORDER),
        ("Zero Cognitive Overload", "Replaces dense scientific spreadsheets with reactive visual sliders, color-coded severity meters, and 1-click preset leaf buttons.", C_LIGHT_AMBER, C_AMBER),
        ("Responsive Layout", "Tailwind CSS flex and grid systems ensuring seamless usability across low-cost rural smartphones, tablets, and desktop workstations.", C_LIGHT_BLUE, C_BLUE)
    ]
    card_w = (WIDTH - 120 - 45) / 4
    for idx, (title, desc, bg_c, bord_c) in enumerate(cards_s2):
        cx = 60 + idx * (card_w + 15)
        draw_card(cx, 100, card_w, HEIGHT - 220, bg_c, bord_c)
        c.setFillColor(bord_c)
        c.setFont("Helvetica-Bold", 15)
        c.drawString(cx + 20, HEIGHT - 160, title)
        
        c.setFillColor(C_DARK)
        c.setFont("Helvetica", 11)
        # Wrap text
        words = desc.split()
        line = ""
        ly = HEIGHT - 200
        for w in words:
            if len(line + " " + w) < 26:
                line += " " + w
            else:
                c.drawString(cx + 20, ly, line.strip())
                ly -= 18
                line = w
        if line:
            c.drawString(cx + 20, ly, line.strip())
    c.showPage()

    # ==========================================
    # SLIDE 3: Frontend Module 1: AI Leaf Diagnostic & Grad-CAM Interface
    # ==========================================
    draw_slide_header("Frontend Module 1: AI Leaf Diagnostic & Grad-CAM Heatmap Interface", "INTERACTIVE LEAF INSPECTION", 3)
    half_w = (WIDTH - 120 - 25) / 2
    
    # Left Card
    draw_card(60, 100, half_w, HEIGHT - 220)
    c.setFillColor(C_EMERALD)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(85, HEIGHT - 150, "Inspection Chamber UI & Controls")
    
    bullets_s3_l = [
        ("Camera API & File Dropper", "Drag-and-drop or camera snapshot support (JPG, PNG, WEBP)."),
        ("Animated Laser Scanning Line", "Visual feedback during MobileNetV3 feature extraction passes."),
        ("One-Click Preset Leaf Library", "Instant field evaluation for Tomato Late Blight, Corn, Potato, and Apple."),
        ("Interactive Grad-CAM Toggle", "Overlays color-gradient saliency maps directly onto the leaf to reveal attention.")
    ]
    by = HEIGHT - 195
    for title, desc in bullets_s3_l:
        c.setFillColor(C_DARK)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(85, by, "• " + title + ":")
        c.setFont("Helvetica", 11)
        c.setFillColor(C_MUTED)
        c.drawString(100, by - 16, desc)
        by -= 48

    # Right Card
    draw_card(60 + half_w + 25, 100, half_w, HEIGHT - 220)
    c.setFillColor(C_PURPLE)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(60 + half_w + 50, HEIGHT - 150, "Clinical Diagnostic Output & Prescription")
    
    bullets_s3_r = [
        ("Pathogen Classification", "Identifies strain & scientific name (e.g. Phytophthora infestans) with 98.4% score."),
        ("Severity Index Meter", "Color-coded progress bar highlighting stage (Stage 1 Chlorosis to Stage 3 Necrosis)."),
        ("Dual Prescription Plan", "Prioritizes organic Bacillus subtilis / neem before targeted chemical fungicides."),
        ("Advisory PDF Export", "One-click generation of timestamped agronomist consultation reports.")
    ]
    by = HEIGHT - 195
    for title, desc in bullets_s3_r:
        c.setFillColor(C_DARK)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(60 + half_w + 50, by, "• " + title + ":")
        c.setFont("Helvetica", 11)
        c.setFillColor(C_MUTED)
        c.drawString(60 + half_w + 65, by - 16, desc)
        by -= 48
    c.showPage()

    # ==========================================
    # SLIDE 4: Frontend Module 2: Precision Yield & Soil Advisory Calculator
    # ==========================================
    draw_slide_header("Frontend Module 2: Precision Soil & Yield Advisory Calculator", "PREDICTIVE AGRONOMY UI", 4)
    
    # Left Card
    draw_card(60, 100, half_w, HEIGHT - 220)
    c.setFillColor(C_AMBER)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(85, HEIGHT - 150, "Reactive Soil & Weather Input Sliders")
    
    bullets_s4_l = [
        ("Target Cultivar Selector", "Rice/Paddy, Sharbati Wheat, Maize, Cotton, Sugarcane, and Tomato."),
        ("Cultivated Acreage Field", "Dynamic inputs scaling from 0.5 to 500+ acres."),
        ("Macronutrient NPK Sliders", "Nitrogen (10–180 kg/ha), Phosphorus (5–145), and Potassium (10–200)."),
        ("Agro-Climatic Parameters", "Real-time sliders for Soil pH (4.0–9.0), Annual Rain (mm), and Temp (°C)."),
        ("1-Click Regional Reset", "Restores regional baseline parameters instantly.")
    ]
    by = HEIGHT - 195
    for title, desc in bullets_s4_l:
        c.setFillColor(C_DARK)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(85, by, "• " + title + ":")
        c.setFont("Helvetica", 11)
        c.setFillColor(C_MUTED)
        c.drawString(100, by - 16, desc)
        by -= 45

    # Right Card (Dark theme projection card)
    draw_card(60 + half_w + 25, 100, half_w, HEIGHT - 220, C_DARK, C_FOREST)
    c.setFillColor(HexColor("#34d399"))
    c.setFont("Helvetica-Bold", 18)
    c.drawString(60 + half_w + 50, HEIGHT - 150, "Live ML Projection Card (Ensemble v1.2)")
    
    c.setFillColor(HexColor("#94a3b8"))
    c.setFont("Helvetica", 11)
    c.drawString(60 + half_w + 50, HEIGHT - 185, "PROJECTED HARVEST YIELD")
    
    c.setFillColor(C_WHITE)
    c.setFont("Helvetica-Bold", 36)
    c.drawString(60 + half_w + 50, HEIGHT - 230, "21.8 Tons")
    
    c.setFillColor(HexColor("#a7f3d0"))
    c.setFont("Helvetica-Bold", 12)
    c.drawString(60 + half_w + 230, HEIGHT - 215, "(4.36 Tons per Acre • High Productivity)")
    
    # 3 mini cards
    mini_w = (half_w - 50) / 3
    my = HEIGHT - 330
    for idx, (label, val, col) in enumerate([("Soil Health", "88 / 100", HexColor("#34d399")), ("Harvest Window", "95-110 Days", HexColor("#fbbf24")), ("Est. Revenue", "₹ 4,36,000", C_WHITE)]):
        mx = 60 + half_w + 40 + idx * (mini_w + 10)
        c.setFillColor(HexColor("#1e293b"))
        c.roundRect(mx, my, mini_w, 65, 8, fill=1, stroke=0)
        c.setFillColor(HexColor("#94a3b8"))
        c.setFont("Helvetica", 9)
        c.drawString(mx + 10, my + 45, label)
        c.setFillColor(col)
        c.setFont("Helvetica-Bold", 13)
        c.drawString(mx + 10, my + 18, val)

    # Prescription
    c.setFillColor(HexColor("#1e293b"))
    c.roundRect(60 + half_w + 40, 125, half_w - 60, 75, 8, fill=1, stroke=0)
    c.setFillColor(HexColor("#34d399"))
    c.setFont("Helvetica-Bold", 11)
    c.drawString(60 + half_w + 55, 175, "Dynamic Top-Dressing Prescription:")
    c.setFillColor(HexColor("#e2e8f0"))
    c.setFont("Helvetica", 10.5)
    c.drawString(60 + half_w + 55, 155, "Top-dress 18 kg Urea at tillering + 12 kg Potash to eliminate lodging risk.")
    c.drawString(60 + half_w + 55, 138, "Soil macronutrients are in optimal ratio for Paddy.")
    c.showPage()

    # ==========================================
    # SLIDE 5: Frontend Module 3: Agri-Analytics & Live Mandi Prices
    # ==========================================
    draw_slide_header("Frontend Module 3: Visual Analytics & Live Mandi Ticker", "DATA VISUALIZATION", 5)
    w_chart = (WIDTH - 120) * 0.58
    w_mandi = (WIDTH - 120) * 0.38
    
    # Left: Analytics
    draw_card(60, 100, w_chart, HEIGHT - 220)
    c.setFillColor(C_EMERALD)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(85, HEIGHT - 150, "Multi-Season Productivity Trends (Chart.js)")
    
    bullets_s5 = [
        ("Dual-Axis Visualization", "Overlays Crop Yield (Tons/Ha) as emerald bars against Rainfall (mm) spline."),
        ("Multi-Season Scope", "Tracks Kharif, Rabi, and Zaid seasons from 2023 to projected 2025/2026 harvests."),
        ("YoY Growth Indicator", "+14.2% Year-over-Year productivity improvement under precision guidance."),
        ("Interactive Tooltips", "Real-time canvas hover tooltips providing instant data breakdown.")
    ]
    by = HEIGHT - 195
    for title, desc in bullets_s5:
        c.setFillColor(C_DARK)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(85, by, "• " + title + ":")
        c.setFont("Helvetica", 11)
        c.setFillColor(C_MUTED)
        c.drawString(100, by - 16, desc)
        by -= 48

    # Right: Mandi rates
    draw_card(60 + w_chart + 25, 100, w_mandi, HEIGHT - 220)
    c.setFillColor(C_BLUE)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(60 + w_chart + 45, HEIGHT - 150, "Live Mandi Spot Rates (AGMARKNET)")
    
    mandi_items = [
        ("Paddy (Basmati Common, Karnal)", "₹ 3,850 / Qtl", "+2.8% ↑", C_EMERALD),
        ("Sharbati Wheat (Indore Mandi)", "₹ 2,420 / Qtl", "+1.2% ↑", C_EMERALD),
        ("Hybrid Tomato (Kolar APMC)", "₹ 1,800 / Qtl", "-4.1% ↓", C_RED),
        ("BT Cotton (Rajkot Mandi)", "₹ 7,150 / Qtl", "+0.5% ↑", C_EMERALD)
    ]
    my = HEIGHT - 200
    for crop_name, price, change, col in mandi_items:
        c.setFillColor(C_SLATE_BG)
        c.setStrokeColor(C_BORDER)
        c.roundRect(60 + w_chart + 45, my, w_mandi - 40, 48, 8, fill=1, stroke=1)
        c.setFillColor(C_DARK)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(60 + w_chart + 55, my + 26, crop_name)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(60 + w_chart + 55, my + 10, price)
        c.setFillColor(col)
        c.drawRightString(60 + w_chart + w_mandi - 15, my + 18, change)
        my -= 58
    c.showPage()

    # ==========================================
    # SLIDE 6: MERN Component Architecture & State Flow
    # ==========================================
    draw_slide_header("React 18 Component Hierarchy & MERN State Flow", "FRONTEND ENGINEERING", 6)
    
    comp_items = [
        ("Navbar & Telemetry", "src/components/Navbar.jsx", "Live IoT connectivity status, micro-climatic temperature/humidity feed, and 42ms latency pulse."),
        ("Leaf Disease Scanner", "src/components/DiseaseDetector.jsx", "Image preview state, animated laser keyframes, Grad-CAM toggle, preset sample triggers."),
        ("Yield & Soil Calculator", "src/components/YieldPredictor.jsx", "Real-time reactive state for NPK, pH, and rainfall sliders; instant mathematical yield calculations."),
        ("Visual Agri-Analytics", "src/components/Analytics.jsx", "Chart.js multi-season canvas, responsive AGMARKNET mandi spot price list, and feature comparison matrix."),
        ("API Gateway Service", "src/services/api.js", "Axios client with automatic offline fallback to local heuristic calculation if Node/Express server is disconnected."),
        ("Synopsis Reader Modal", "src/components/SynopsisModal.jsx", "Embedded modal rendering the complete academic project synopsis and technical specifications on demand.")
    ]
    col_w = (WIDTH - 120 - 30) / 3
    row_h = (HEIGHT - 220 - 15) / 2
    for idx, (title, path, desc) in enumerate(comp_items):
        col = idx % 3
        row = idx // 3
        cx = 60 + col * (col_w + 15)
        cy = HEIGHT - 110 - (row + 1) * row_h - row * 15
        draw_card(cx, cy, col_w, row_h)
        c.setFillColor(C_EMERALD)
        c.setFont("Helvetica-Bold", 14)
        c.drawString(cx + 15, cy + row_h - 25, title)
        c.setFillColor(C_MUTED)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(cx + 15, cy + row_h - 40, path)
        c.setFillColor(C_DARK)
        c.setFont("Helvetica", 10.5)
        # Wrap desc
        words = desc.split()
        line = ""
        ly = cy + row_h - 60
        for w in words:
            if len(line + " " + w) < 32:
                line += " " + w
            else:
                c.drawString(cx + 15, ly, line.strip())
                ly -= 16
                line = w
        if line:
            c.drawString(cx + 15, ly, line.strip())
    c.showPage()

    # ==========================================
    # SLIDE 7: Future Development Section
    # ==========================================
    draw_slide_header("Future Development Roadmap: Expanding CropGuard Capabilities", "FUTURE DEVELOPING SECTION", 7)
    
    phases = [
        ("Phase 1: Drone & Satellite NDVI", "Aerial Farm Imaging", "Ingestion of multispectral drone footage to compute Normalized Difference Vegetation Index (NDVI) for whole-field aerial stress detection before ground symptoms emerge.", C_LIGHT_GREEN, C_EMERALD),
        ("Phase 2: Offline Edge PWA & ONNX", "Zero-Bandwidth Rural Mode", "Progressive Web App (PWA) with service workers for remote off-grid operation. Client-side INT8 quantized MobileNetV3 running on ONNX WebAssembly without internet.", C_LIGHT_BLUE, C_BLUE),
        ("Phase 3: Multilingual Voice AI", "Vernacular Audio Assistant", "Voice-in, voice-out advisory across Hindi, Marathi, Telugu, Tamil, and Bengali to empower low-literacy farmers with spoken diagnosis and treatment readouts.", C_LIGHT_AMBER, C_AMBER),
        ("Phase 4: IoT Smart Fertigation", "Hardware Closed-Loop", "Hardware integration with in-situ soil probes streaming telemetry via MQTT, automatically opening solenoid drip irrigation and liquid fertilizer valves.", C_LIGHT_PURPLE, C_PURPLE)
    ]
    card_w = (WIDTH - 120 - 45) / 4
    for idx, (title, sub, desc, bg_c, bord_c) in enumerate(phases):
        cx = 60 + idx * (card_w + 15)
        draw_card(cx, 100, card_w, HEIGHT - 220, bg_c, bord_c)
        c.setFillColor(bord_c)
        c.setFont("Helvetica-Bold", 14)
        c.drawString(cx + 15, HEIGHT - 150, title)
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(C_MUTED)
        c.drawString(cx + 15, HEIGHT - 168, sub)
        
        c.setFillColor(C_DARK)
        c.setFont("Helvetica", 11)
        words = desc.split()
        line = ""
        ly = HEIGHT - 200
        for w in words:
            if len(line + " " + w) < 25:
                line += " " + w
            else:
                c.drawString(cx + 15, ly, line.strip())
                ly -= 18
                line = w
        if line:
            c.drawString(cx + 15, ly, line.strip())
    c.showPage()

    # ==========================================
    # SLIDE 8: Competitive Benchmarking (Why CropGuard is Different)
    # ==========================================
    draw_slide_header("Competitive Benchmarking: What Makes CropGuard Different?", "INNOVATION & NOVELTY", 8)
    
    # Table Header
    tx = 60
    ty = HEIGHT - 140
    th = 40
    tw = WIDTH - 120
    col_widths = [260, 280, 240, 252]
    
    headers = ["Feature / Dimension", "CropGuard (Our System)", "Generic Disease Apps", "Govt. Agriculture Portals"]
    c.setFillColor(C_DARK)
    c.rect(tx, ty, tw, th, fill=1, stroke=0)
    c.setFillColor(C_WHITE)
    c.setFont("Helvetica-Bold", 12)
    cur_x = tx + 15
    for idx, h in enumerate(headers):
        c.drawString(cur_x, ty + 14, h)
        cur_x += col_widths[idx]
        
    rows = [
        ("Explainable AI (Grad-CAM)", "✓ Yes (Visual Heatmaps)", "✗ No (Black Box only)", "✗ Not Available"),
        ("Dual Vision + Soil Intelligence", "✓ Yes (Multi-Modal Unified)", "✗ Foliage Diagnosis Only", "✗ Static Soil Tables"),
        ("Dynamic Fertilizer Advisory", "✓ Real-Time (Acreage & Deficit based)", "✗ Generic text tips", "− Manual table lookup"),
        ("Treatment Prioritization", "✓ Organic-First Bio-Regimens", "✗ Pushes Chemical Pesticides", "− Generic text advisories"),
        ("Architecture Modularity", "✓ Decoupled MERN + FastAPI Worker", "− Monolithic", "− Legacy Server Pages")
    ]
    cur_y = ty
    for r_idx, row in enumerate(rows):
        cur_y -= 45
        c.setFillColor(HexColor("#f1f5f9") if r_idx % 2 == 0 else C_WHITE)
        c.rect(tx, cur_y, tw, 45, fill=1, stroke=0)
        c.setStrokeColor(C_BORDER)
        c.line(tx, cur_y, tx + tw, cur_y)
        
        cur_x = tx + 15
        for c_idx, val in enumerate(row):
            if c_idx == 1:
                c.setFillColor(C_EMERALD)
                c.setFont("Helvetica-Bold", 11)
            else:
                c.setFillColor(C_DARK)
                c.setFont("Helvetica", 11)
            c.drawString(cur_x, cur_y + 16, val)
            cur_x += col_widths[c_idx]
    c.showPage()

    # ==========================================
    # SLIDE 9: Conclusion & Societal Impact
    # ==========================================
    draw_slide_header("Conclusion & Measurable Societal Impact", "PROJECT CONCLUSION", 9)
    
    # Left Card
    draw_card(60, 100, half_w, HEIGHT - 220)
    c.setFillColor(C_EMERALD)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(85, HEIGHT - 150, "Summary of Accomplishments")
    
    bullets_s9_l = [
        ("Integrated MERN Platform", "Delivered a modern, responsive React frontend with glassmorphic cards and telemetry."),
        ("98.7% Diagnostic Accuracy", "Transfer-learned MobileNetV3 classifier fine-tuned on 54,305 PlantVillage leaf images."),
        ("Transparent Explainability", "Grad-CAM heatmaps highlight infected cellular lesions, building agronomist trust."),
        ("Precise Agronomy Calculations", "XGBoost ensemble estimating yield and fertilizer needs based on soil NPK.")
    ]
    by = HEIGHT - 195
    for title, desc in bullets_s9_l:
        c.setFillColor(C_DARK)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(85, by, "• " + title + ":")
        c.setFont("Helvetica", 11)
        c.setFillColor(C_MUTED)
        c.drawString(100, by - 16, desc)
        by -= 48

    # Right Card (Dark theme impact)
    draw_card(60 + half_w + 25, 100, half_w, HEIGHT - 220, C_FOREST, C_EMERALD)
    c.setFillColor(HexColor("#34d399"))
    c.setFont("Helvetica-Bold", 18)
    c.drawString(60 + half_w + 50, HEIGHT - 150, "Measurable Societal & Ecological Benefits")
    
    bullets_s9_r = [
        ("20%–40% Loss Prevention", "Timely pathogen intervention protects vulnerable harvests from devastating blights."),
        ("30% Lower Chemical Costs", "Bio-remedy prioritization cuts chemical costs and spares local groundwater."),
        ("Food Security & Sustainability", "Maximizes harvest yield per hectare without exhausting regional soil ecology."),
        ("Ready for Live Demo", "Fully operational on laptop with instant browser launch and 1-click batch scripts.")
    ]
    by = HEIGHT - 195
    for title, desc in bullets_s9_r:
        c.setFillColor(HexColor("#a7f3d0"))
        c.setFont("Helvetica-Bold", 12)
        c.drawString(60 + half_w + 50, by, "• " + title + ":")
        c.setFont("Helvetica", 11)
        c.setFillColor(HexColor("#d1fae5"))
        c.drawString(60 + half_w + 65, by - 16, desc)
        by -= 48

    c.setFillColor(C_WHITE)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(60 + half_w + 50, 130, "Thank you! We welcome questions and live demonstration.")
    c.showPage()

    c.save()
    print(f"Vector PDF Slide Deck successfully generated at: {output_path}")

if __name__ == "__main__":
    out_dir = r"C:\Users\hp\.gemini\antigravity\scratch\cropguard"
    out_file = os.path.join(out_dir, "CropGuard_Presentation_Slides.pdf")
    generate_pdf_slides(out_file)
