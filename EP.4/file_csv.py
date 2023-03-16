import csv

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #File Write
        fw.writerow(datalist) #datalist file

data = ['สินค้า','ราคา','เวลา']
writecsv(data)

def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #file read
        data = list(fr)
    return data

data = readcsv()
print(data)
