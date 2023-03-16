from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
from datetime import datetime
import csv

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist)
def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #fr = file reader
        data = list(fr)
    return data
#############################
GUI = Tk()                      #หน้า Home
GUI.title('โปรแกรมเช็คชื่อ')        #ชื่อ Program
GUI.geometry('250x200')        #ขนาดหน้าต่าง
L1=Label(GUI,text='โปรแกรมเช็คชื่อ',font=('TH SarabunPSK',18),fg='blue')
L1.place(x=20,y=20)

LF1 = ttk.LabelFrame(GUI,text='กรอก ID Number')
LF1.place(x=20,y=20)

ID_Num = StringVar()
E1 = ttk.Entry(LF1,textvariable=ID_Num,font=('TH SarabunPSK',16))
E1.pack(pady=10,padx=10)

def SaveData():
    
    t = datetime.now().strftime('%d/%m/%Y %H:%M:%S\n')
    data = ID_Num.get() #ดึงข้อมูล ID_Num
    text = [t,data] # [เวลา,ข้อมูลที่ได้จากการกรอก]
    writecsv(text) #บันทึกลง csv
    ID_Num.set('') #ล้างข้อมูลในช่องกรอก
    messagebox.showinfo('\n',text)

B4 = ttk.Button(LF1,text='บันทึก',command=SaveData)
B4.pack(ipadx=20,ipady=20)

GUI.mainloop()
