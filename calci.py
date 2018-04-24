from tkinter import *
root=Tk()
root.title('Calculator')
con=0
cs=0
def display():
    global cs
    s=e1.get()
    e1.delete(0,END)
    e1.insert(0,eval(s))
    cs=1

def clear():
    e1.delete(0,END)
    global con
    con=0
def insert(d):
    global cs
    if cs==1:
        cs=0
        e1.delete(0,END)
    global con
    if d=='0' and con==0:
        return
    global i
    con=1
    e1.insert(i,d)
    i+=1
def clearlast():
    global i
    e1.delete(i-1)
    i-=1

i=0

def f(sv):
    s=sv.get()
    if s=='':
        return
    if s[-1]=='=':
        e1.delete(0,END)
        e1.insert(0,eval(s[:-1]))

sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: f(sv))

e1=Entry(root,bd=4,font = "Helvetica 24 bold",justify="center",width=14,textvariable=sv)

e1.grid(row=0,columnspan=4,ipadx=5,ipady=5)

Button(root,text=1,width=8,height=3,command=lambda:insert('1')).grid(row=2,column=0)
Button(root,text=2,width=8,height=3,command=lambda:insert('2')).grid(row=2,column=1)
Button(root,text=3,width=8,height=3,command=lambda:insert('3')).grid(row=2,column=2)
Button(root,text='+',width=8,height=3,command=lambda:insert('+')).grid(row=2,column=3)

Button(root,text=4,width=8,height=3,command=lambda:insert('4')).grid(row=3,column=0)
Button(root,text=5,width=8,height=3,command=lambda:insert('5')).grid(row=3,column=1)
Button(root,text=6,width=8,height=3,command=lambda:insert('6')).grid(row=3,column=2)
Button(root,text='-',width=8,height=3,command=lambda:insert('-')).grid(row=3,column=3)

Button(root,text=7,width=8,height=3,command=lambda:insert('7')).grid(row=4,column=0)
Button(root,text=8,width=8,height=3,command=lambda:insert('8')).grid(row=4,column=1)
Button(root,text=9,width=8,height=3,command=lambda:insert('9')).grid(row=4,column=2)
Button(root,text='*',width=8,height=3,command=lambda:insert('*')).grid(row=4,column=3)

Button(root,text='.',width=8,height=3,command=lambda:insert('.')).grid(row=5,column=0)
Button(root,text=0,width=8,height=3,command=lambda:insert(0)).grid(row=5,column=1)
Button(root,text='%',width=8,height=3,command=lambda:insert('%')).grid(row=5,column=2)
Button(root,text='/',width=8,height=3,command=lambda:insert('/')).grid(row=5,column=3)

Button(root,text='.',width=8,height=3,command=lambda:insert('.')).grid(row=5,column=0)
Button(root,text=0,width=8,height=3,command=lambda:insert('0')).grid(row=5,column=1)
Button(root,text='Clr',width=8,height=3,command=lambda:clearlast()).grid(row=5,column=2)
Button(root,text='C',width=8,height=3,command=lambda:clear()).grid(row=5,column=3)

Button(root,text='=',width=18,height=3,command=lambda:insert('=')).grid(row=6,columnspan=2)
Button(root,text='Close',width=18,height=3,command=quit).grid(row=6,column=2,columnspan=2)

root.mainloop()
