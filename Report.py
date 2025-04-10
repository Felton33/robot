import os
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
from matplotlib.patches import Rectangle

# Function to generate the defect report
def generate_defect_report(image_dir, analysis_file, output_pdf):
    # Read the analysis file (assuming it's a CSV for this example)
    analysis_data = pd.read_csv(analysis_file)

    # Initialize PDF report
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Loop through the analysis data
    for _, row in analysis_data.iterrows():
        image_path = os.path.join(image_dir, row['image_name'])
        defect_coords = eval(row['defect_coords'])  # Assuming defect_coords is a stringified list of (x, y, width, height)
        defect_type = row['defect_type']
        
        # Check if image exists
        if not os.path.exists(image_path):
            print(f"Warning: Image {image_path} not found!")
            continue

        # Load and annotate image
        img = plt.imread(image_path)
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.imshow(img)
        ax.set_title(f"Defects in {row['image_name']} (Type: {defect_type})")
        ax.axis('off')
        
        # Mark defects on the image
        for x, y, w, h in defect_coords:
            rect = Rectangle((x, y), w, h, linewidth=2, edgecolor='r', facecolor='none')
            ax.add_patch(rect)
        
        # Save the annotated image temporarily
        temp_img_path = "temp_annotated.png"
        plt.savefig(temp_img_path)
        plt.close(fig)
        
        # Add the annotated image and details to the PDF
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, f"Image: {row['image_name']}", ln=True)
        pdf.cell(0, 10, f"Defect Type: {defect_type}", ln=True)
        pdf.cell(0, 10, f"Coordinates: {row['defect_coords']}", ln=True)
        pdf.image(temp_img_path, x=10, y=pdf.get_y(), w=180)

        # Remove the temporary file
        os.remove(temp_img_path)

    # Save the final report
    pdf.output(output_pdf)
    print(f"Defect report saved to {output_pdf}")

# Example usage
image_directory = "images"  # Path to the folder with images
analysis_csv = "defect_analysis.csv"  # Path to the defect analysis CSV
output_report = "defect_report.pdf"  # Output report path

# Sample CSV format:
# image_name,defect_coords,defect_type
# img1.png,"[(50, 60, 20, 30), (200, 150, 15, 15)]","Scratch"
# img2.png,"[(120, 90, 25, 25)]","Crack"

generate_defect_report(image_directory, analysis_csv, output_report)
