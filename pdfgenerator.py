from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from io import BytesIO
import pandas as pd

def generate_scorecard(player1_name, player2_name, scores, duration, statistics):
    """Generate a PDF scorecard for the match."""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Title
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30
    )
    elements.append(Paragraph("Squash Match Scorecard", title_style))
    elements.append(Spacer(1, 12))

    # Match Information
    match_info = [
        ["Date:", pd.Timestamp.now().strftime("%Y-%m-%d")],
        ["Duration:", duration],
        ["Player 1:", player1_name],
        ["Player 2:", player2_name]
    ]
    
    t = Table(match_info, colWidths=[2*inch, 4*inch])
    t.setStyle(TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 20))

    # Score History
    elements.append(Paragraph("Score History", styles['Heading2']))
    elements.append(Spacer(1, 12))
    
    if scores:
        score_data = [[
            "Game",
            f"{player1_name} Score",
            f"{player2_name} Score"
        ]]
        for score in scores:
            score_data.append([
                str(score['game']),
                str(score['player1']),
                str(score['player2'])
            ])
        
        t = Table(score_data, colWidths=[2*inch, 2*inch, 2*inch])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        elements.append(t)
    
    # Statistics
    elements.append(Spacer(1, 20))
    elements.append(Paragraph("Match Statistics", styles['Heading2']))
    elements.append(Spacer(1, 12))
    
    stats_data = [
        ["Total Points:", str(statistics['total_points'])],
        ["Games Played:", str(statistics['games_played'])],
        ["Longest Rally:", str(statistics['longest_rally'])]
    ]
    
    t = Table(stats_data, colWidths=[2*inch, 4*inch])
    t.setStyle(TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ]))
    elements.append(t)

    # Generate PDF
    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    return pdf
