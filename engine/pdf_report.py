"""
CropGuard PDF Agronomy Prescription & Yield Report Generator.
Generates an official agronomic health certificate and prescription using ReportLab.
"""

import io
from datetime import datetime
from typing import Dict, Any

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def generate_cropguard_pdf(
    diagnosis_data: Dict[str, Any],
    yield_data: Dict[str, Any],
    farmer_name: str = "Progressive Farmer",
    farm_location: str = "Main Agronomy Block"
) -> bytes:
    """Creates a formatted PDF report bytes stream."""
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()
    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#065F46')
    )
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#4B5563')
    )
    h2_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=colors.HexColor('#047857'),
        spaceBefore=10,
        spaceAfter=4
    )
    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#1F2937')
    )
    bullet_style = ParagraphStyle(
        'BulletCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#374151'),
        leftIndent=12
    )

    story = []

    # 1. Header Banner
    story.append(Paragraph("🌿 CropGuard AI | Precision Agronomy & Crop Health Report", title_style))
    story.append(Paragraph(
        f"Generated on {datetime.now().strftime('%B %d, %Y - %H:%M')} | "
        f"Farmer: <b>{farmer_name}</b> | Location: <b>{farm_location}</b>",
        subtitle_style
    ))
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#10B981'), spaceAfter=12))

    # 2. Executive Overview Table
    diag = diagnosis_data.get("top_diagnosis", {})
    metrics = diagnosis_data.get("metrics", {})
    crop_name = diag.get("crop", yield_data.get("crop", "Target Crop"))
    disease_name = diag.get("disease_name", "N/A")
    severity = diag.get("severity", "N/A")
    health_idx = f"{metrics.get('health_index', 0)}%"
    infected_area = f"{metrics.get('infected_area_pct', 0)}%"

    overview_data = [
        [
            Paragraph("<b>Target Crop:</b>", body_style),
            Paragraph(crop_name, body_style),
            Paragraph("<b>Diagnostic Health Index:</b>", body_style),
            Paragraph(f"<b>{health_idx}</b>", body_style)
        ],
        [
            Paragraph("<b>Pathology Status:</b>", body_style),
            Paragraph(f"<b>{disease_name}</b>", body_style),
            Paragraph("<b>Infection Area:</b>", body_style),
            Paragraph(infected_area, body_style)
        ],
        [
            Paragraph("<b>Severity Assessment:</b>", body_style),
            Paragraph(severity, body_style),
            Paragraph("<b>Confidence Level:</b>", body_style),
            Paragraph(f"{diag.get('confidence', 0)}%", body_style)
        ]
    ]

    overview_table = Table(overview_data, colWidths=[110, 155, 130, 145])
    overview_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F0FDF4')),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#86EFAC')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#DCFCE7')),
        ('PADDING', (0, 0), (-1, -1), 5),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(overview_table)
    story.append(Spacer(1, 10))

    # 3. Clinical Pathology & Problem Diagnosis
    treatment = diagnosis_data.get("treatment_profile", {})
    story.append(Paragraph("1. Pathology Diagnosis & Root Causes", h2_style))
    story.append(Paragraph(f"<b>Causal Organism:</b> {treatment.get('pathogen', 'N/A')}", body_style))
    story.append(Paragraph(f"<b>Clinical Description:</b> {treatment.get('description', '')}", body_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Root Causes & Predisposing Factors:</b>", body_style))
    for cause in treatment.get("root_causes", []):
        story.append(Paragraph(f"• {cause}", bullet_style))
    story.append(Spacer(1, 8))

    # 4. Immediate Prescription: Chemical & Organic Treatment Schedule
    story.append(Paragraph("2. Targeted Treatment & Spray Prescriptions", h2_style))
    
    rx_data = [
        [
            Paragraph("<b>Treatment Stream</b>", body_style),
            Paragraph("<b>Prescribed Formulations & Dosage Protocols</b>", body_style)
        ]
    ]
    
    chem_txt = "<br/>".join([f"• {c}" for c in treatment.get("chemical_treatments", [])])
    rx_data.append([
        Paragraph("<b>Chemical Curative & Protectant</b>", body_style),
        Paragraph(chem_txt or "None required", body_style)
    ])
    
    org_txt = "<br/>".join([f"• {o}" for o in treatment.get("organic_treatments", [])])
    rx_data.append([
        Paragraph("<b>Biological / Organic Control</b>", body_style),
        Paragraph(org_txt or "Standard bio-protection", body_style)
    ])

    rx_table = Table(rx_data, colWidths=[150, 390])
    rx_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#047857')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#D1D5DB')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E5E7EB')),
        ('BACKGROUND', (0, 1), (0, -1), colors.HexColor('#F9FAFB')),
        ('PADDING', (0, 0), (-1, -1), 5),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(rx_table)
    story.append(Spacer(1, 10))

    # 5. Crop Yield Prediction & Growth Booster Plan
    story.append(Paragraph("3. Yield Forecast & Fast/Large Growth Acceleration", h2_style))
    
    unit = yield_data.get("unit", "Tons / Acre")
    base_per_acre = yield_data.get("baseline_yield_per_acre", 0)
    boost_per_acre = yield_data.get("boosted_yield_per_acre", 0)
    tot_base = yield_data.get("total_baseline_yield", 0)
    tot_boost = yield_data.get("total_boosted_yield", 0)
    gain_pct = yield_data.get("yield_gain_pct", 0)
    area = yield_data.get("land_area_acres", 1)

    yield_table_data = [
        [
            Paragraph("<b>Metric</b>", body_style),
            Paragraph("<b>Standard Practice</b>", body_style),
            Paragraph("<b>CropGuard Precision Protocol</b>", body_style),
            Paragraph("<b>Expected Net Uplift</b>", body_style)
        ],
        [
            Paragraph("Yield Rate", body_style),
            Paragraph(f"{base_per_acre} {unit}", body_style),
            Paragraph(f"<b>{boost_per_acre} {unit}</b>", body_style),
            Paragraph(f"<b>+{gain_pct}%</b>", body_style)
        ],
        [
            Paragraph(f"Total Farm Yield ({area} acres)", body_style),
            Paragraph(f"{tot_base} {unit.split('/')[0].strip()}", body_style),
            Paragraph(f"<b>{tot_boost} {unit.split('/')[0].strip()}</b>", body_style),
            Paragraph(f"<b>+{round(tot_boost - tot_base, 2)} {unit.split('/')[0].strip()}</b>", body_style)
        ]
    ]

    yield_table = Table(yield_table_data, colWidths=[140, 130, 150, 120])
    yield_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1E3A8A')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#93C5FD')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#DBEAFE')),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#EFF6FF')),
        ('PADDING', (0, 0), (-1, -1), 5),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(yield_table)
    story.append(Spacer(1, 8))

    # Growth & Fertilizer tips
    story.append(Paragraph("<b>Accelerated Growth & Sizing Fertilizer Steps:</b>", body_style))
    for step in treatment.get("growth_and_fertilizer_recovery", []):
        story.append(Paragraph(f"• {step}", bullet_style))

    story.append(Spacer(1, 14))
    # Footer disclaimer
    disclaimer = Paragraph(
        "<i>Notice: Recommendations are provided by CropGuard AI agronomic models. "
        "Always observe local safety guidelines, pesticide label instructions, and pre-harvest intervals (PHI).</i>",
        subtitle_style
    )
    story.append(disclaimer)

    doc.build(story)
    pdf_bytes = buffer.getvalue()
    buffer.close()
    return pdf_bytes
