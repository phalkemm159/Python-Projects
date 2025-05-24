from PyPDF2 import PdfMerger

merger = PdfMerger()

pdfs = []

n = int(input("How many PDF do you wanted to merge ?\n"))

for i in range(0, n):
    name = input(f"Enter the name of PDF {i + 1} : ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)
    print("PDFs merged successfully!")

merger.write("merged-pdf.pdf")
merger.close()