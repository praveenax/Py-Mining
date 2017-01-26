import PyPDF2

pdfFileObj = open('review.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print pdfReader.numPages


for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(0)
    txt = pageObj.extractText()
    
    print txt



#print txt