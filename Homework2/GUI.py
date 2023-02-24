from tkinter import *
from tkinter import ttk     #Theme tk
from tkinter import messagebox
from datetime import datetime
import random

GUI = Tk()                  #หน้า Home
GUI.title('My Program')           #ชื่อ Program
GUI.geometry('500x200')     #ขนาดหน้าต่าง

L1=Label(GUI,text='Date&Time',font=('TH SarabunPSK',),fg='blue')
L1.place(x=20,y=20)

######################
def Button1():
    text = datetime.now().strftime('%H:%M')
    messagebox.showinfo('Time',text)
FB1 = Frame(GUI)
FB1.place(x=40,y=50)
B1 = ttk.Button(FB1,text='Time',command=Button1)
B1.pack(ipadx=20,ipady=20)                   #ปุ่มที่ 1
######################
def Button2():
    text = datetime.now().strftime('%d-%m-%Y')
    messagebox.showinfo('Date',text)
FB2 = Frame(GUI)
FB2.place(x=160,y=50)
B2 = ttk.Button(FB2,text='Date',command=Button2)
B2.pack(ipadx=20,ipady=20)                   #ปุ่มที่ 2
######################
def Button3():
    food = ['ไอศกรีม','น้ำปั่น','ก๋วยเตี๋ยว','ข้าว','ยำ','โตเกียว','ลูกชิ้น','ไก่ทอด','ซูชิ']
    text = random.choice(food)
    messagebox.showinfo('หิว!',text)
FB3 = Frame(GUI)
FB3.place(x=280,y=50)
B3 = ttk.Button(FB3,text='กินไรดี',command=Button3)
B3.pack(ipadx=20,ipady=20)                   #ปุ่มที่ 3

GUI.mainloop()
