from tkinter import *
import tkinter
from tkinter import messagebox
# ====================== setting ======================
root = Tk()
root.geometry("350x450")
root.title("calculator")
root.resizable(width=False, height=False)
root.configure(bg="white")
# ====================== variable ======================
num1=IntVar()
num2=IntVar()
result=IntVar()
# ====================== frames ======================
top_first= Frame(root,width=350,height=112.5,bg="white")
top_first.pack(side=TOP)
top_second= Frame(root,width=350,height=112.5,bg="white")
top_second.pack(side=TOP)
top_third= Frame(root,width=350,height=112.5,bg="white")
top_third.pack(side=TOP)
top_forth= Frame(root,width=350,height=112.5,bg="white")
top_forth.pack(side=TOP)
# ====================== func ======================
def error(ms):
    if ms== 'error':
        tkinter.Message(messagebox.showerror("error","somthing went wrong!"))
    elif ms=="division error":
        tkinter.Message(messagebox.showerror("division error","can not divide by zero "))
def plus():
    try:
        value= float(num1.get())+ float(num2.get())
        result.set(value)
    except:
        error("error")
def minus():
    try:
        value= float(num1.get())- float(num2.get())
        result.set(value)
    except:
        error("error")
def mult():
    try:
        value= float(num1.get())* float(num2.get())
        result.set(value)
    except:
        error("error")
def div():
    if num2.get()==0:
        error("division error")
    try:
        value= float(num1.get()) / float(num2.get())
        result.set(value)
    except:
        error("error")
# ====================== buttons ======================
btn_plus= Button(top_third,text="+",width=8,highlightbackground="white",command=lambda : plus())
btn_plus.pack(side=LEFT,padx=5)
btn_minus= Button(top_third,text="-",width=8,highlightbackground="white",command=lambda : minus())
btn_minus.pack(side=LEFT,padx=5)
btn_multiple= Button(top_third,text="*",width=8,highlightbackground="white",command=lambda : mult())
btn_multiple.pack(side=LEFT,padx=5)
btn_divide= Button(top_third,text="/",width=8,highlightbackground="white",command=lambda : div())
btn_divide.pack(side=LEFT,padx=5)
# ====================== input & lbl ======================
lbl_first=Label(top_first,text="first num : ",bg="white")
lbl_first.pack(side=LEFT,padx=5,pady=5)
first_num=Entry(top_first,highlightbackground="white",textvariable=num1)
first_num.pack(side=LEFT,)
lbl_second=Label(top_second,text="second num : ",bg="white")
lbl_second.pack(side=LEFT,padx=5,pady=5)
second_num=Entry(top_second,highlightbackground="white",textvariable=num2)
second_num.pack(side=LEFT,)
result_lbl=Label(top_forth,text="result : ",bg="white")
result_lbl.pack(side=LEFT,padx=5,pady=5)
result_num=Entry(top_forth,highlightbackground="white",textvariable=result)
result_num.pack(side=LEFT,)








root.mainloop()
