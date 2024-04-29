from tkinter import *
root=Tk()
root.title("simple interest Calculator")
root.geometry("500x300")

def Calculate():
    
    prin=int(principalentry.get())
    rat=int(rateentry.get())
    Tim=int(Timeentry.get())
    amount=(prin*rat*Tim)/100
    
    Label(text=f"{amount}",font="arial 30 bold").place(x=200,y=220)
 
        
principal=Label(root,text="Principal:",font="arial 15")
rate=Label(root,text="rate of interst:",font="arial 15")
Time=Label(root,text="Time:",font="arial 15")

principal.place(x=50,y=20)
rate.place(x=50,y=90)
Time.place(x=50,y=160)

interest=Label(root,text="Interest:",font="arial 15")
interest.place(x=50,y=230)

principalvalue=StringVar()
ratevalue=StringVar()
Timevalue=StringVar()

principalentry=Entry(root,textvariable=principalvalue,font="arial 20",width=8)
rateentry=Entry(root,textvariable=ratevalue,font="arial 20",width=8)
Timeentry=Entry(root,textvariable=Timevalue,font="arial 20",width=8)

principalentry.place(x=200,y=20)
rateentry.place(x=200,y=90)
Timeentry.place(x=200,y=160)

Button(text="Calculate",font="arial 15",command=Calculate).place(x=350,y=20)
Button(root,text="Exit",command=lambda:exit(),font="arial 15",width=8).place(x=350,y=90)


root.mainloop()
