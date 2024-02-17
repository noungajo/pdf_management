import PyPDF2
import os

def merge_pdfs(input_folder, output_pdf_path):
    pdf_writer = PyPDF2.PdfWriter()

    # Iterate through each PDF file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            input_pdf_path = os.path.join(input_folder, filename)
            with open(input_pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                # Add each page to the PDF writer
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    pdf_writer.add_page(page)

    # Write the merged PDF to a file
    with open(output_pdf_path, 'wb') as output_file:
        pdf_writer.write(output_file)

# Example usage:
input_folder = '/home/benjojo/Documents/projets/pdf_management'
output_pdf_path = 'merged_output.pdf'  # Path to the merged output PDF file

merge_pdfs(input_folder, output_pdf_path)
