import tkinter as t
def bmi():
    lblR['text']=we1.get()*2.54

w=t.Tk()
w.title('inch->cm')
w.geometry('400x320')
we1=t.DoubleVar()
wh1=t.DoubleVar()

lbW=t.Label(w,text='體重',font=('Arial',16))
lbW.grid(row=0,column=0)
lbW=t.Label(w,text='身高',font=('Arial',16))
lbW.grid(row=1,column=0)

txtw=t.Entry(w,textvariable=we1,font=('Arial',16))
we1.get()
txtw.grid(row=0,column=1)
txtw=t.Entry(w,textvariable=wh
              1,font=('Arial',16))
we1.get()
txtw.grid(row=1,column=1)

w.mainloop()
