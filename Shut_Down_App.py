from tkinter import *
import os
from tkinter import Button


def Log_out():
    os.system("shutdown -l")
def Shut_down():
    os.system("shutdown /r /t 1")
def Restart():
    os.system("shutdown /r /t 1")
def Restart_time():
    os.system("shutdown /r /t 20")

root = Tk()
root.title("ShutDown App")
root.geometry("500x500")
root.config(bg="black")

button1 = Button(text="Log-Out",font=("Time New Roman", 12, "bold"),relief=RAISED, cursor="plus",command=Log_out)
button1.place(x=130,y=250,height=50,width=200)

button2 = Button(text="ShutDown",font=("Time New Roman", 12, "bold"),relief=RAISED, cursor="plus",command=Shut_down)
button2.place(x=130,y=350,height=50,width=200)

button3 = Button(text="Restart",font=("Time New Roman", 12, "bold"),relief=RAISED, cursor="plus",command=Restart)
button3.place(x=130,y=50,height=50,width=200)

button4 = Button(text="Restart Time",font=("Time New Roman", 12, "bold"),relief=RAISED, cursor="plus",command=Restart_time)
button4.place(x=130,y=150,height=50,width=200)



root.mainloop()