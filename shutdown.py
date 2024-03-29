from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
    
def restart_time():
    os.system("shutdown /r /t 20")
    
def logout():
    os.system("shutdown -1")
     
def shutdown():
    os.system("shutdown /s /t 1")
    
st = Tk()
st.title("Shutdown App")
st.geometry("500x500")
st.config(bg = "Blue")
r_button = Button(st,text="Restart",font=("Time new roman",30,"bold"),
    relief=RAISED,cursor="Plus", command=restart)
r_button.place(x=150,y=60,height=50,width=200)

rt_button = Button(st,text="Restart time",font=("Time new roman",25,"bold"),
    relief=RAISED,cursor="Plus", command=restart_time)
rt_button.place(x=150,y=170,height=50,width=200)

lg_button = Button(st,text="log_out",font=("Time new roman",30,"bold"),
    relief=RAISED,cursor="Plus", command=logout)
lg_button.place(x=150,y=270,height=50,width=200)

st_button = Button(st,text="shut-down",font=("Time new roman",30,"bold"),
    relief=RAISED,cursor="Plus", command=shutdown)
st_button.place(x=150,y=370,height=50,width=200)

st.mainloop()
