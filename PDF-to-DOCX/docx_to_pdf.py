# pip install docx2pdf

from docx2pdf import convert

def convert_docx_to_pdf(docx_path, pdf_path):
    try:
        convert(docx_path, pdf_path)
        print("Conversion successful!")
    except Exception as e:
        print(f"Error during conversion: {e}")

if __name__ == "__main__":
    # Specify the paths to the input DOCX file and the output PDF file
    input_docx_path = "TrevorCV.docx"
    output_pdf_path = "CV.pdf"

    # Convert DOCX to PDF
    convert_docx_to_pdf(input_docx_path, output_pdf_path)
