import pdfplumber

pdf = pdfplumber.open("아뱅.pdf")
first_page = pdf.pages[0]
print(first_page.extract_text())
pdf.close()
