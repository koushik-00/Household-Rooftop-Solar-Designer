from tkinter import *
from MainModule import MainModule
root=Tk()
root.title("Input Tab")
root.geometry("700x500")
A=Label(root,text="Enter total units : ")
#A.pack()
A.place(x=35,y=50)
B=Entry(root,bd=5)
B.place(x=500,y=50)
#B.pack(side=LEFT)
C=Label(root,text="Enter number of months : ")
#C.pack(side=LEFT)
C.place(x=35,y=100)
D=Entry(root,bd=5)
D.place(x=500,y=100)
var=IntVar()
G=Label(root,text="Select the watt rate of Panel : ")
G.place(x=35,y=150)
F1=Radiobutton(root,text="60 Watts : Rs 3100",variable=var,value=(60))
F2=Radiobutton(root,text="165 Watts : Rs 6900",variable=var,value=(165))
F3=Radiobutton(root,text="350 Watts : Rs 13000",variable=var,value=(350))
F1.place(x=500,y=150)
F2.place(x=500,y=175)
F3.place(x=500,y=200)
H=Label(root,text="Select type of grid system : ")
H.place(x=35,y=250)
con=IntVar()
def a():
   global days
   days=IntVar()
   K=Label(root,text="Choose number of days for the battery to store power: ")
   K.place(x=35,y=325)
   J1=Radiobutton(root,text="1 day",variable=days,value=(1))
   J2=Radiobutton(root,text="2 days",variable=days,value=(2))
   J3=Radiobutton(root,text="3 days",variable=days,value=(3))
   J1.place(x=500,y=325)
   J2.place(x=500,y=350)
   J3.place(x=500,y=375)
def c():
   L=Label(root,text="                                                                                                  ")
   L1=Label(root,text="                                                       ")
   L2=Label(root,text="                                                       ")
   L3=Label(root,text="                                                       ")
   L.place(x=35,y=325)
   L1.place(x=500,y=325)
   L2.place(x=500,y=350)
   L3.place(x=500,y=375)
I1=Radiobutton(root,text="On Grid(without Battery)",variable=con,value=(2),command=c)
I2=Radiobutton(root,text="Off Grid(with Battery)",variable=con,value=(1),command=a)
I1.place(x=500,y=250)
I2.place(x=500,y=275)
def b():
   Q=var.get()
   P=con.get()
   if P==1:
      M=days.get()
   else:M=0
   MainModule(int(B.get()),int(D.get()),Q,P,M)
   print(Q)
   print(P)
E=Button(root,text="submit",command=b)
E.pack(side=BOTTOM)


