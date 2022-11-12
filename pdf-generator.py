from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import landscape
from reportlab.pdfgen import canvas
from reportlab.platypus import Image
from datetime import datetime
import pandas as pd

def make_certificate(name, school):
    # name = "Praveen Kumar"
    # school = "SRV Boys Higher secondary school"
    file_name = name.replace(" ","_")
    file_name = 'E-certificates//'+file_name+'.pdf'
    img = 'template.png'    # add template here - It shoud be a png/jpg file
    c = canvas.Canvas(file_name, pagesize=landscape(A4))
    c.drawImage(img, 0, 0,  width=842, height=595)  #add dx, dy to give borders if needed which are 0 here
    c.setFont('Times-Italic', 30, leading=None)
    c.drawCentredString(415, 305, name) #change y to move up/down the string
    c.setFont('Times-Italic', 17, leading=None)
    c.drawCentredString(410, 230, school)
    c.save()
    print('\n[#] PDF Generated : '+name)

users = ["Elon", "Jeff", "Gates"]
school = ["PSBB", "ST.Johns public school, chennai", "VBC"]

for i in range(0,len(users)):
    make_certificate(users[i], school[i])
print("PDF Generation successful")