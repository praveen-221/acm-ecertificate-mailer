from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import landscape
from reportlab.pdfgen import canvas
from reportlab.platypus import Image
from datetime import datetime
import pandas as pd

def make_certificate(id, name, school):
    # name = "Praveen Kumar"
    # school = "SRV Boys Higher secondary school"
    file_name = 'E-certificates//' + name + '_' + str(id) + '.pdf'
    img = 'template.jpeg'    # add template here - It shoud be a png/jpg file
    c = canvas.Canvas(file_name, pagesize=landscape(A4))
    c.drawImage(img, 0, 0,  width=842, height=595)  #add dx, dy to give borders if needed which are 0 here
    c.setFont('Helvetica', 30, leading=None)
    c.drawCentredString(415, 305, name) #change y to move up/down the string
    c.setFont('Helvetica', 20, leading=None)
    c.drawCentredString(410, 230, school)
    c.save()
    print('\n[#] PDF Generated : '+name)

# users = ["Elon", "Jeff", "Gates", "Praveen"]
# school = ["PSBB", "ST.Johns public school, chennai", "VBC", "St. Johns Public School, Chennai"]

users = pd.read_excel("./registry/AU prodigy vbc trichy.xlsx")
name = users['Name']
id = users['ID']
scl = users['School']
for i in range(0,len(users)):
    make_certificate(id[i], name[i], scl[i])
print("\nPDF Generation successful\n")