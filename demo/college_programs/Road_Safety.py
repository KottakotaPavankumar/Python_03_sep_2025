from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch


def generate_dsms_pdf():
    file_name = "Driver_Safety_Monitoring_System_Flow.pdf"
    doc = SimpleDocTemplate(file_name, pagesize=letter)
    styles = getSampleStyleSheet()

    # Custom Styles
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        spaceAfter=20,
        alignment=1  # Center
    )

    heading_style = ParagraphStyle(
        'HeadingStyle',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        spaceBefore=12,
        spaceAfter=10,
        textColor=colors.hexColor("#2E5077")
    )

    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=11,
        leading=14,
        spaceAfter=10
    )

    elements = []

    # Title
    elements.append(Paragraph("Driver Safety Monitoring System - Operational Documentation", title_style))
    elements.append(Spacer(1, 12))

    # Actors Section
    elements.append(Paragraph("System Actors", heading_style))
    actor_data = [
        ["Actor", "Description"],
        [Paragraph("Driver", body_style), Paragraph("The primary user monitored for safety and behavior.", body_style)],
        [Paragraph("Admin", body_style),
         Paragraph("Responsible for user authentication and report review.", body_style)],
        [Paragraph("Emergency Contact", body_style),
         Paragraph("Recipient of automated alerts during critical incidents.", body_style)],
        [Paragraph("Embedded System", body_style),
         Paragraph("The vehicle's hardware/software unit for sensor data processing.", body_style)]
    ]

    actor_table = Table(actor_data, colWidths=[1.5 * inch, 4.5 * inch])
    actor_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.hexColor("#F2F2F2")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ]))
    elements.append(actor_table)
    elements.append(Spacer(1, 18))

    # Use Cases Section
    elements.append(Paragraph("Functional Use Cases", heading_style))
    use_cases = [
        "Login/Authenticate Driver", "Start Vehicle (After Safety Check)",
        "Monitor Driver Behavior", "Detect Drowsiness", "Detect Mobile Usage",
        "Detect Over-speeding", "Detect Alcohol Level", "Generate Alerts",
        "Send Emergency Notification", "View Driving Report", "Maintain Safety Score"
    ]

    for uc in use_cases:
        elements.append(Paragraph(f"• {uc}", body_style))

    elements.append(Spacer(1, 18))

    # Flow Breakdown
    elements.append(Paragraph("Detailed Operational Flow", heading_style))

    elements.append(Paragraph(
        "<b>1. Pre-Drive Phase:</b> The system initializes with driver authentication. A mandatory safety check (Alcohol Level Detection) is performed. If parameters are met, the ignition is enabled.",
        body_style))

    elements.append(Paragraph(
        "<b>2. Continuous Monitoring:</b> While driving, the embedded system runs a concurrent loop to detect drowsiness, phone usage, and speeding. This data updates the 'Safety Score' in real-time.",
        body_style))

    elements.append(Paragraph(
        "<b>3. Escalation:</b> If unsafe behavior is detected, local alerts (Audio/Haptic) are triggered. If the driver remains unresponsive, the system automatically transmits GPS coordinates to the designated Emergency Contact.",
        body_style))

    # Build PDF
    doc.build(elements)
    return file_name


generate_dsms_pdf()