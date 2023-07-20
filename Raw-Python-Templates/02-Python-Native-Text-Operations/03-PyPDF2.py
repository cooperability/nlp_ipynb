# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import PyPDF2



myfile = open('US_Declaration.pdf',mode='rb')

pdf_reader=PyPDF2.PdfReader(myfile)

len(pdf_reader.pages)

page_one = pdf_reader.pages[0]

print(page_one.extract_text())

mytext = page_one.extract_text()

myfile.close()

f = open('US_Declaration.pdf', 'rb')

pdf_reader = PyPDF2.PdfReader(f)

first_page = pdf_reader.pages[0]

pdf_writer = PyPDF2.PdfWriter()

pdf_writer.add_page(first_page)

pdf_output = open('PYPDFEXPERIMENT.pdf','wb')

pdf_writer.write(pdf_output)

pdf_output.close()

f.close()



brand_new = open('PYPDFEXPERIMENT.pdf','rb')
pdf_reader = PyPDF2.PdfReader(brand_new)

len(pdf_reader.pages)

f = open('US_Declaration.pdf','rb')
pdf_text = [0]
pdf_reader = PyPDF2.PdfReader(f)
for p in range(len(pdf_reader.pages)):
    page=pdf_reader.pages[p]
    pdf_text.append(page.extract_text())
f.close()

pdf_text

len(pdf_text)

for page in pdf_text:
    print(page)
    print('\n')
    print('\n')
    print('\n')
    print('\n')


