from tkinter import *

def calculate():
    #print("Aie!")
    x=float(e1.get())
    #print("The double of " , x , "is " ,2*x)
    V.set(str(2*x))





window=Tk()
window.title("Double")


l1=Label(window,text="x:")
l1.grid(row=0 , column=0)
e1=Entry(window,fg="blue",bg="white")
e1.grid(row=0 , column=1)


l2=Label(window,text="2*x:")
l2.grid(row=1 , column=0)

V=StringVar()
l3=Label(window,fg="blue",bg="white",textvariable=V)
l3.grid(row=1 , column=1)

b1=Button(window,text="Quit",command=quit)
b1.grid(row=2,column=0)

b2=Button(window,text="Calculate",command=calculate)
b2.grid(row=2,column=2)




window.mainloop()





