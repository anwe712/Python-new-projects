import pyttsx3 # pip install pyttsx3(python text to speech version 3)
import PyPDF2

book = open('op.pdf', 'rb') # rb = read binary
pdfReader = PyPDF2.PdfReader(book)
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init()
page = pdfReader.getPage(7)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()



