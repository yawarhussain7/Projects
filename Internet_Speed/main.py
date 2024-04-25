import tkinter

sp = tkinter.Tk()

sp.title("Internet Speed")
sp.geometry("500x600")

sp.config(bg="gray")

lab = tkinter.Label(sp,text="Internet Speed Testing ",font=("Time new Roman",25,"bold"),fg="black",bg="gray")
lab.place(x=50,y=35,width=380,height=50)

# Downloading Speed

lab = tkinter.Label(sp,text="Downloading Speed",font=("Time new Roman",25,"bold"),fg="white",bg="gray")
lab.place(x=70,y=130,width=380,height=50)

lab = tkinter.Label(sp,text="00-00",font=("Time new Roman",25,"bold"),fg="red",bg="gray")
lab.place(x=50,y=200,width=380,height=50)

#Uploading Speed

lab = tkinter.Label(sp,text="Uploading Speed",font=("Time new Roman",25,"bold"),fg="white",bg="gray")
lab.place(x=70,y=270,width=380,height=50)

lab = tkinter.Label(sp,text="00-00",font=("Time new Roman",25,"bold"),fg="red",bg="gray")
lab.place(x=50,y=350,width=380,height=50)

# Button 

button = tkinter.Button(sp,text="Check Now",font=("Time new Roman",18,"bold"),fg="green")
button.place(x= 150,y= 450,height=50,width=200)


sp.mainloop()