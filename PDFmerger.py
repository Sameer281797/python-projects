import PyPDF2

pdfiles = ["Sameer_resume.pdf" , "AADHAR.pdf"]
merger = PyPDF2.PdfMerger()
for filename in pdfiles:
    pdfFile = open(filename , 'rb')
    pdfReader = PyPDF2.pdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write('merged.pdf')
