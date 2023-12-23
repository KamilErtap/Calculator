from tkinter import *

def yaz(x):
    s = len(giris.get())
    giris.insert(s,str(x))

hesap = 5
s1 = 0
s2 = 0

def islem(x):
    global hesap 
    hesap = x
    global s1
    s1 = float(giris.get())
    giris.delete(0,'end')
    
def hesapla():
    global s2
    s2 = float(giris.get())
    global hesap
    sonuc = 0
    if(hesap == 0):
        sonuc = s1 + s2
    elif(hesap == 1):
        sonuc = s1 - s2
    elif(hesap == 2):
        sonuc = s1 * s2
    elif(hesap == 3):
        sonuc = s1 / s2

    giris.delete(0,'end')
    giris.insert(0,str(sonuc))

def clear():
    giris.delete(0,'end')

window = Tk()
window.geometry("250x350")

giris = Entry(font = "Verdana 14 bold", width=15, justify=RIGHT)
giris.place(x=20, y=20)

btns = []

for i in range(1,10):
    btns.append(Button(text=str(i), font="Verdana 14 bold",width=2,command=lambda x=i:yaz(x)))

sayac = 0

for i in range(0,3):
    for j in range(0,3):
        btns[sayac].place(x=20+j*50,y=80+i*50)
        sayac +=1

btnsislem = []

for i in range(0,4):
    btnsislem.append(Button(font="Verdana 14 bold",width=2,command=lambda x=i:islem(x)))

btnsislem[0]['text'] = "+"
btnsislem[1]['text'] = "-"
btnsislem[2]['text'] = "*"
btnsislem[3]['text'] = "/"

for i in range(0,4):
    btnsislem[i].place(x=170, y=80+i*50)

btnzero = Button(text = 0,font = "Verdana 14 bold",width=2,command =lambda x=0:yaz(x))
btnzero.place(x=20,y=230)

btndot = Button(text = ".",font = "Verdana 14 bold",width=2,comman = lambda x=".":yaz(x))
btndot.place(x=70,y=230)

btneq = Button(text = "=",font="Verdana 14 bold",width=2,command = hesapla)
btneq.place(x=120,y=230)

btnclr = Button(text = "C",font = "Verdana 14 bold",width=13,fg="RED",command= clear)
btnclr.place(x=23,y=280)

window.mainloop()