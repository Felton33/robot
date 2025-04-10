from fpdf import FPDF

def generate_pdf_report(part, images, defect_results, video_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Add report content
    pdf.cell(200, 10, txt=f"Defect Report for {part}", ln=True)
    pdf.cell(200, 10, txt=f"Defect Results: {defect_results}", ln=True)
    
    # Save the PDF
    report_path = "defect_report.pdf"
    pdf.output(report_path)
    return report_path
