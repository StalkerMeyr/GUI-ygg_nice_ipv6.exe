from tkinter import *
import os
root = Tk()
root.geometry('340x230')
root.resizable(width=False, height=False)
root.title("Генератор vikulin GUI")
a=" " #Костыли наше все:)
def start():
    os.system("ygg_nice_ipv6.exe"+a+text1.get()+a+text2.get()+a+text3.get())

powtor_bite=Label(root,text="Число повторяющихся байтов")
text1=Entry(root,width=11,font='Arial 14')

gen=Label(root,text="Сколько ipv6 будет пройдено")
text2=Entry(root,width=11,font='Arial 14')

key=Label(root,text="Совпадающие части")
text3=Entry(root,width=11,font='Arial 14',)
text_pred=Label(root,text="(Можно оставить пустым)")

go=Button(text="Запуск программы",width=15,height=3,bg="#99746C",fg='#FFFFFF',font='arial 14',command=start)

text1.place(x=180,y=1)
powtor_bite.place(x=0,y=1)

gen.place(x=0,y=26)
text2.place(x=180,y=26)

key.place(x=0,y=52)
text3.place(x=180,y=52)
text_pred.place(x=0,y=70)

go.place(x=80,y=120)

root.mainloop()

