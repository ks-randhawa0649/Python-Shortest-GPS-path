from tkinter import *
from math import *

#def calculate():
   # lt1=float(e2.get())
   # lt2=float(e4.get())
   # lo1=float(e1.get())
   # lo2=float(e3.get())
   # p = 0.017453292519943295
   # a = 0.5 - cos((lt2 - lt1) * p )/2 + cos(lt1 * p) * cos(lt2 * p) * (1-cos((lo2 - lo1) * p))/2
   # x = 12742 * asin(sqrt(a))*1000
   # V.set(str(x))

def calculate():
    la1=float(e2.get())
    la2=float(e4.get())
    lo1=float(e1.get())
    lo2=float(e3.get())
    EquiRectDistdeg(la1 , lo1 , la2 , lo2)
    
   
def EquiRectDistdeg(la1 , lo1 , la2 , lo2):
    EquiRectDist(radians(la1) , radians(lo1) , radians(la2) , radians(lo2))
    

   

def EquiRectDist(la1 , lo1 , la2 , lo2):
    R = 6371 * (10**3)
    x = (lo2 - lo1) * cos((la1+la2)/2)
    y = la2 - la1
    d = sqrt(pow(x,2) + pow(y,2)) * R
    V.set(str(d))







window=Tk()
window.title("Distance")

photo = PhotoImage(file = r"C:\Users\KUNWARJIT SINGH\Desktop\chitkara-university-logo.png")

l1=Label(window,text="Longitude 1 : ")
l1.grid(row=0 , column=1)

l2=Label(window,text="Latitude 1 : ")
l2.grid(row=1 , column=1)

l3=Label(window,text="Longitude 2 : ")
l3.grid(row=2 , column=1)

l4=Label(window,text="Latitude 2 : ")
l4.grid(row=3 , column=1)

l5=Label(window,text="     Distance in m  =  ")
l5.grid(row=4 , column=1)


e1=Entry(window)
e1.grid(row=0 , column=2)

e2=Entry(window)
e2.grid(row=1 , column=2)

e3=Entry(window)
e3.grid(row=2 , column=2)


e4=Entry(window)
e4.grid(row=3 , column=2)

b1=Button(window,text="Quit",command=quit)
b1.grid(row=5 , column=0)

b2=Button(window,text="Enter",command=calculate)
b2.grid(row=5 , column=3)

V=StringVar()
l6=Label(window,textvariable=V)
l6.grid(row=4 , column=2)

l7=Label(window,text=" ")
l7.grid(row=6 , column=0)

l8=Label(window,image = photo)
l8.grid(row=7 , column=2)

l9=Label(window,text="\t  ")
l9.grid(row=7 , column=3)
window.mainloop()

    
