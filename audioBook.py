import pyttsx3
import PyPDF2


book = open('search-engine-optimization-starter-guide.pdf','rb') #1st one is book name
pdf = PyPDF2.PdfFileReader(book) #this is my book
pages = pdf.numPages
print(pages) #number of pages
speaker = pyttsx3.init()
first = int(input("Enter the Starting Page Number"))
for num in range(first,pages):
    page = pdf.getPage(num)
    text = page.extractText()
    print(text) #print all the Text
    speaker.say(text)
    speaker.runAndWait()
