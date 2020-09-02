from tkinter import *
from math import *
#-----------------------------------------------------------------------------

def EquiRectDist(lon1,lat1,lon2,lat2):
    R=6371*(10**3)
    x=(lon2-lon1)*cos((lat1+lat2)/2)
    y=lat2-lat1
    d=sqrt(pow(x,2)+pow(y,2))*R
    return d
def EquiRectDistDeg(lon1,lat1,lon2,lat2):
    return(EquiRectDist(radians(lon1),radians(lat1),radians(lon2),radians(lat2)))

def calculate():
    lon1=float(e1.get())
    lat1=float(e2.get())
    lon2=float(e3.get())
    lat2=float(e4.get())
    d=EquiRectDistDeg(lon1,lat1,lon2,lat2)
    v.set(str(d))
#-----------------------------------------------------------------------------

#MAIN PAGE

#-----------------------------------------------------------------------------


window=Tk()
window.title("Distance")
canvas = Canvas(window,width=300,height=200)
canvas.grid(row=7,column=1)
img=PhotoImage(file="1.png")
canvas.create_image(20,20,anchor=NW,image=img)
l1=Label(window,text="long1 :")
l1.grid(row=0,column=0)
l2=Label(window,text="lat1 :")
l2.grid(row=1,column=0)
l3=Label(window,text="long2 :")
l3.grid(row=2,column=0)
l4=Label(window,text="lat2 :")
l4.grid(row=3,column=0)
e1=Entry(window,bg="yellow")
e1.grid(row=0,column=1)
e2=Entry(window,bg="pink")
e2.grid(row=1,column=1)
e3=Entry(window,bg="blue")
e3.grid(row=2,column=1)
e4=Entry(window,bg="white")
e4.grid(row=3,column=1)
b1=Button(window,text="Quit",bg="orange",command=quit)
b1.grid(row=4,column=0)
b2=Button(window,text="Enter",bg="orange",command=calculate)
b2.grid(row=4,column=2)
v=StringVar()
l5=Label(window,textvariable=v)
l5.grid(row=5,column=1)



window.mainloop()

