# pip install pdf2docx

from pdf2docx import Converter
pdf_file = 'Curriculum Vitae.pdf'
docx_file = 'CV.docx'

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()