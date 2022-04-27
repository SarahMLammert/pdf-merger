import sys
import PyPDF2

pdfs = sys.argv[1:]

def pdf_combiner(pdfs):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdfs:
		print(pdf)
		merger.append(pdf)
	merger.write('super.pdf')

pdf_combiner(pdfs)