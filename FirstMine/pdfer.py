import PyPDF2

pdfFileObj = open('review.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print pdfReader.numPages


for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)
    txt = pageObj.extractText()
    
    path = 'testfile_'+str(i)+'.txt'
    print path
    file = open(path,”a") 
    
    uu = txt.decode('utf8')
    s = uu.encode('cp1250')
    
    file.write(s) 

 
    file.close() 
#    print txt



#print txt