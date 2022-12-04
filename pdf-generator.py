from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import landscape
from reportlab.pdfgen import canvas
from reportlab.platypus import Image
from datetime import datetime
import pandas as pd

def make_certificate(id, name, school):
    file_name = 'E-certificates//' + name + '_' + str(id) + '.pdf'
    img = 'participation_template.jpeg'    # add template here - It shoud be a png/jpg file
    c = canvas.Canvas(file_name, pagesize=landscape(A4))
    c.drawImage(img, 0, 0,  width=842, height=595)  #add dx, dy to give borders if needed which are 0 here
    c.setFont('Helvetica', 30, leading=None)
    c.drawCentredString(415, 305, name) #change y to move up/down the string
    c.setFont('Helvetica', 20, leading=None)
    c.drawCentredString(410, 230, school)   # school name for participation

    # ----------for winners--------------
    # c.drawCentredString(410, 245, school)
    # c.setFont('Helvetica', 18, leading=None)
    # c.drawCentredString(260, 224, pos)
    # if event == "DECODE WITH MATH":
    #     c.setFont('Helvetica', 17, leading=None)
    #     c.drawCentredString(432, 224, event)
    # elif event == "REVERSE CODING":
    #     c.setFont('Helvetica', 18, leading=None)
    #     c.drawCentredString(435, 224, event)
    # else:
    #     c.setFont('Helvetica', 19, leading=None)
    #     c.drawCentredString(435, 224, event)
    #---------------------------

    c.save()
    print('\n[#] PDF Generated : '+name)


users = pd.read_excel("./registry/Students_Certificate_List-Winners.xlsx")
name = users['NAME']
id = users['ID']
scl = users['SCHOOL']
pos = users['PRIZE']
event = users['EVENT']
for i in range(0,len(users)):
    make_certificate(id[i], name[i], scl[i], pos[i], event[i])
# make_certificate(600, "ADITHYA U", "THE TVS SCHOOL")
print("\nPDF Generation successful\n")