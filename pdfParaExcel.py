import PyPDF2
import csv

# Open the PDF file in read-binary mode
with open('razao.pdf', 'rb') as file:
    # Create a PDF file reader object
    pdf_reader = PyPDF2.PdfReader(file)
    print(len(pdf_reader.pages))
    page = pdf_reader.pages[1]
    text = page.extract_text()
    
    lines = text.strip().split('\n')
    
    valores = lines[2].split(" ")
    print(valores[1])