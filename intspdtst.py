from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3))+" mbps"
    up = str(round(sp.upload()/(10**6),3))+" mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)
    
sp = Tk()
sp.title(" INTERNET SPEED TEST ")
sp.geometry("500x650")
sp.config(bg="White")
lab = Label(sp,text=" INTERNET SPEED TEST ",font=("Time New Roman",25,"bold"),bg="White",fg="Black")
lab.place(x=60,y=40,height=50,width=380)

lab = Label(sp,text=" DOWNLOAD SPEED ",font=("Time New Roman",25,"bold"),bg="Black",fg="Red")
lab.place(x=60,y=130,height=50,width=380)

lab_down = Label(sp,text=" 00 ",font=("Time New Roman",25,"bold"),bg="Black",fg="Red")
lab_down.place(x=60,y=200,height=50,width=380)

lab = Label(sp,text=" UPLOAD SPEED ",font=("Time New Roman",25,"bold"),bg="Black",fg="Red")
lab.place(x=60,y=290,height=50,width=380)

lab_up = Label(sp,text=" 00 ",font=("Time New Roman",25,"bold"),bg="Black",fg="Red")
lab_up.place(x=60,y=360,height=50,width=380)

button = b=Button(sp,text=" CHECK SPEED ",font=("Time New Roman",30,"bold"),relief=RAISED,bg="Black",fg="Red",command=speedcheck)
button.place(x=75,y=480)

sp.mainloop()
