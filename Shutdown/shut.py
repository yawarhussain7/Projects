#import tkinter package 
import tkinter
import os

#Functions 
def restart():
	os.system("Shutdown /r /t 1")

def restart_time():
	os.system("Shutdown /r /t 20")

def Log_of():
	os.system("Shutdown -l")

def Shutdown():
	os.system("Shutdown /s /t 1")

#tkinter class object
st = tkinter.Tk()
# change title of the app
st.title("Shutdown")
#change size 
st.geometry("500x500")
#change back-ground color
st.config(bg = "blue")

restart = tkinter.Button(st,text="Restart",font=("Time New Roman",18,"bold"),
	relief= tkinter.RAISED ,cursor="plus",fg="red",command = restart)
restart.place(x = 160,y = 60,height = 40,width = 200)


restart_t = tkinter.Button(st,text="Restart Time",font=("Time New Roman",14,"bold"),
	relief= tkinter.RAISED ,cursor="plus",fg="red",command = restart_time)
restart_t.place(x = 160,y = 140,height = 40,width = 200)


Log_of = tkinter.Button(st,text="Log off",font=("Time New Roman",14,"bold"),
	relief= tkinter.RAISED ,cursor="plus",fg="red",command = Log_of)
Log_of.place(x = 160,y = 220,height = 40,width = 200)

Shutdown = tkinter.Button(st,text="Shutdown",font=("Time New Roman",14,"bold"),
	relief= tkinter.RAISED ,cursor="plus",fg="red",command = Shutdown)
Shutdown.place(x = 160,y = 300,height = 40,width = 200)

st.mainloop()
