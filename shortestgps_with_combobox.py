from tkinter import *
from tkinter import ttk
from math import *
import time
from datetime import datetime,timedelta
import os
import winsound

winsound.PlaySound("project.wav",winsound.SND_ASYNC)


time.time()
K=os.path.abspath('.')
J = os.listdir(K)
Lcsv=[]
for e in J:
    if('.csv' in e):
        Lcsv.append(e)
    

def calculate():

    F = combo.get()
    F = open(F,"r")
    d=0
    la_arr = []
    lo_arr = []
    time_arr = []
    t=0
    for l in F.readlines():
        L=l.split(";")
        la_arr.append(L[0])
        lo_arr.append(L[1])
        time_arr.append(L[4])

    #LL=[lat,lon] lat--> LL[0] AND lon --> LL[1]   
    l=len(la_arr)
    for i in range(0,l-2):
        la1=la_arr[i]
        lo1=lo_arr[i]
        la2=la_arr[i+1]
        lo2=lo_arr[i+1]
        d = d + EquiRectDistDeg(float(la1) ,float(lo1) , float(la2) , float(lo2))
        #t = t + (float(time_arr[i+1]) - float(time_arr[i]))
    #t = float(time_arr[-1])-float(time_arr[0])
    t1 = float(float(time_arr[0]) * (10**(-3)))
    t2 = float(float(time_arr[-1]) * (10**(-3)))
    #f1 = float(time.ctime(t1))
    #f2 = float(time.ctime(t2))
    t = float(t2-t1)  
    h=str(t//3600)
    v=t%3600
    m=str(v//60)
    s=str(v%60)
    sp=float(d/t)    
    D.set(str(d)+"  meters")
    #T.set(str(time.ctime(t)))
    T.set(str(h)+ "  hrs  "+str(m) + "  min  "+str(s)+"  sec  ")
    S.set(str(sp)+"  m/s ")
        

def EquiRectDistDeg(la1 , lo1 , la2 , lo2):
    return EquiRectDist(float(radians(la1)) , float(radians(lo1)) , float(radians(la2)) , float(radians(lo2)))
    




def EquiRectDist(la1 , lo1 , la2 , lo2):
    R = 6371 * (10**3)
    x = (lo2 - lo1) * cos((la1+la2)/2)
    y = la2 - la1
    d = sqrt(pow(x,2) + pow(y,2)) * R
    return (float(d))






window=Tk()
window.title("Distance")

l1=Label(window,text="File:")
l1.grid(row=0 , column = 0)

l2=Label(window,text="Distance:")
l2.grid(row=1 , column = 0)

l3=Label(window,text="Time:")
l3.grid(row=2 , column = 0)

l4=Label(window,text="Speed:")
l4.grid(row=3 , column = 0)

l5=Label(window,text=" ")
l5.grid(row=1 , column = 2)

l6=Label(window,text=" ")
l6.grid(row=2 , column = 2)

l7=Label(window,text=" ")
l7.grid(row=3 , column = 2)

b1=Button(window,text="Quit",command=quit)
b1.grid(row=4 , column = 0)

b2=Button(window,text="Calculate",command=calculate)
b2.grid(row=4 , column = 2)


#e1=Entry(window)
#e1.grid(row=0 , column = 1)


combo=ttk.Combobox(window,values=Lcsv)
combo.grid(row=0 , column = 1)
combo.current(1)


D=StringVar()
l9=Label(window , textvariable=D)
l9.grid(row=1 , column = 1)

T=StringVar()
l10=Label(window , textvariable=T)
l10.grid(row=2 , column = 1)

S=StringVar()
l11=Label(window , textvariable=S)
l11.grid(row=3 , column = 1)

photo = PhotoImage(file = r"C:\Users\KUNWARJIT SINGH\Desktop\chitkara-university-logo.png")

l8=Label(window,image = photo)
l8.grid(row=5 , column=1)



window.mainloop()
