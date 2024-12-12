#importing Libraries

import pyttsx3 #pip install pyttsx3
import PyPDF2 #pip install PyPDF2
import os 

#Function to increment page number
def inc_PageNo():

    #Reading the file
    with open("pageno.txt" , "r") as v:
        a = v.read()

    #Typecasting 
    a = int (a)
    a += 1
    a = str(a)

    #Writing value into file 
    with open("pageno.txt" , "w") as s:
        a = s.write(a)
        s.close()

    f = open("pageno.txt" , "r")
    pageno = f.read()
    #print("\nPage No Incremented!\n")
    return pageno

#Function to update value of page number if value of pageno is 1
def update(pg):
    pg = str (pg)
    with open("pageno.txt" , "w") as s:
        #Updating value
        pg = s.write(pg)
        s.close()

#Opening the pdf
book = open('<PDF_NAME>', 'rb')
#print("\nBook Opened!\n")

#Read the PDF using PyPDF2
pdfReader = PyPDF2.PdfFileReader(book)

#Storing total number of pages
pages = pdfReader.numPages
pages = int(pages)
#print("\nPages Extracted!\t",pages)

#Initialising pyttsx3
speaker = pyttsx3.init()

#Assigning value to RATE property 
speaker.setProperty('rate', 150)
#print("\npyttsx3 initialised\n")

#Function call
pgno = inc_PageNo()
pgno = int(pgno)

if pgno == 1:
    pgno = input("Please enter starting page from where you want to listen:  ")
    pgno = int(pgno)

    #Condition for inputed number should not be greater than total number of pages
    if pgno < pages:

        #Function call
        update(pgno)

        #Running loop from given page number to last page of PDF
        for num in range(pgno, pages):

            #Get exact page
            page = pdfReader.getPage(num)

            #Extracts the text
            text = page.extractText()

            #Just say it ;-)
            speaker.say(text)
            speaker.runAndWait()

            #Function call
            pgno = inc_PageNo()
else:
    #Condition for inputed number should not be greater than total number of pages
    if pgno < pages:

        #Running loop from given page number to last page of PDF
        for num in range(pgno, pages):

            #Get exact page
            page = pdfReader.getPage(num)

            #Extracts the text
            text = page.extractText()

            #Just say it ;-)
            speaker.say(text)
            speaker.runAndWait()
            
            #Function call
            pgno = inc_PageNo()
