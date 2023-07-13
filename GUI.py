from tkinter import *
from tkinter import font
from MainModule import MainModule
from tkinter import messagebox
root=Tk()
#print(font.families())
root.title("Household PV Solar Configurator")
#root.attributes("-fullscreen",True)
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
root.geometry("%dx%d" % (width,height))
#root.geometry("700x700")
print(width,height)
root.state("zoomed")
bg=PhotoImage(file="1663640.png")
S=Label(root,image=bg)
S.place(x=0,y=0)
#S.pack()
#Photo=PhotoImage(file="Picture1.png")
#R=Label(root,image=Photo)

A=Label(root,text="Enter Average Monthly Units : ",font=("Comic Sans MS",14),bg="lightblue")
#A.pack()
A.place(x=35,y=50)
B=Entry(root,font=("Comic Sans MS",14),bg='white',highlightbackground = "skyblue",highlightthickness=4, highlightcolor= "lightblue")
B.place(x=525,y=50)
#B.pack(side=LEFT)
var=IntVar()
G=Label(root,text="Select the watt rate of Panel : ",font=("Comic Sans MS",14),bg="lightblue")
G.place(x=35,y=150)
F1=Radiobutton(root,text="60 Watts : Rs 3100",variable=var,value=(60),font=("Comic Sans MS",14),bg="lightblue")
F2=Radiobutton(root,text="165 Watts : Rs 6900",variable=var,value=(165),font=("Comic Sans MS",14),bg="lightblue")
F3=Radiobutton(root,text="350 Watts : Rs 13000",variable=var,value=(350),font=("Comic Sans MS",14),bg="lightblue")
F1.place(x=525,y=150)
F2.place(x=525,y=200)
F3.place(x=525,y=250)
H=Label(root,text="Select type of grid system : ",font=("Comic Sans MS",14),bg="lightblue")
H.place(x=35,y=325)
con=IntVar()
def a():
   global days
   global K
   global J1
   global J2
   global J3
   days=IntVar()
   K=Label(root,text="Choose number of days for battery life : ",font=("Comic Sans MS",14),bg="lightblue")
   K.place(x=35,y=450)
   J1=Radiobutton(root,text="1 day",variable=days,value=(1),font=("Comic Sans MS",14),bg="lightblue")
   J2=Radiobutton(root,text="2 days",variable=days,value=(2),font=("Comic Sans MS",14),bg="lightblue")
   J3=Radiobutton(root,text="3 days",variable=days,value=(3),font=("Comic Sans MS",14),bg="lightblue")
   J1.place(x=525,y=450)
   J2.place(x=525,y=500)
   J3.place(x=525,y=550)
def c():
   try:
      K.destroy()
      J1.destroy()
      J2.destroy()
      J3.destroy()
   except NameError:
      pass
I1=Radiobutton(root,text="On Grid(without Battery)",variable=con,value=(2),command=c,font=("Comic Sans MS",14),bg="lightblue")
I2=Radiobutton(root,text="Off Grid(with Battery)",variable=con,value=(1),command=a,font=("Comic Sans MS",14),bg="lightblue")
I1.place(x=525,y=325)
I2.place(x=525,y=375)
def b():
   Q=var.get()
   P=con.get()
   M=None
   if P==1:
      M=days.get()
      if M==0:
         messagebox.showwarning("Error","Select Number of days")
      else:
         try:
            int(B.get())
         except ValueError:
            messagebox.showerror("Error","Only Integer Entry Valid")
         if B.get()=='':
            messagebox.showwarning("Error","Type Number of Units")
         elif int(B.get())>1319:
            messagebox.showwarning("Error","Our System only supports for a maximum of 1319 units")
         elif Q==0:
            messagebox.showwarning("Error","Choose Watt Rate of Panel")
         elif P==0:
            messagebox.showwarning("Error","Choose Grid Type")
         else:MainModule(int(B.get()),Q,P,M)
   else:
      M=0
      try:
         int(B.get())
      except ValueError:
         messagebox.showerror("Error","Only Integer Entry Valid")
      if B.get()=='':
         messagebox.showwarning("Error","Type Number of Units")
      elif int(B.get())>1319:
         messagebox.showwarning("Error","Our System only supports for maximum of 1319 units")
      elif Q==0:
         messagebox.showwarning("Error","Choose Watt Rate of Panel")
      elif P==0:
         messagebox.showwarning("Error","Choose Grid Type")
      else:MainModule(int(B.get()),Q,P,M)
   print(Q)
   print(P)
Photo=PhotoImage(file="Picture1.png")
R=Label(root,image=Photo)
R.pack(side=TOP,anchor='e')
E=Button(root,text="Submit",command=b,width=40,bg='brown',fg='white',font=(14))
E.pack(side=BOTTOM)
root.mainloop()


