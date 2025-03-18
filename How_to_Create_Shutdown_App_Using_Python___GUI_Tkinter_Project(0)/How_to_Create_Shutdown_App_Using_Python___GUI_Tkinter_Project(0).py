from tkinter import *
import os


root = Tk()
root.title("Shutdown App")
root.geometry("360x580")
root.configure(bg="#fff")



def restarttime():
    os.system("shutdown /r /t 30")
    
def restart():
    os.system("shutdown /r /t 1")
    
def shutdown():
    os.system("shutdown /s /t 1")
    
def logout():
    os.system("shutdown /l")




restart_time_button = PhotoImage(file="restarttime.PNG")
first_button = Button(root, image=restart_time_button,bd=0, cursor="hand2", command=restarttime)
first_button.place(x=10, y=10)


close_time_button = PhotoImage(file="close.PNG")
second_button = Button(root, image=close_time_button,bd=0, cursor="hand2", command=root.destroy)
second_button.place(x=200, y=10)

restart_button = PhotoImage(file="restart.PNG")
third_button = Button(root, image=restart_button,bd=0, cursor="hand2", command=restart)
third_button.place(x=10, y=200)

shutdown_time_button = PhotoImage(file="shutdown.PNG")
fouth_button = Button(root, image=shutdown_time_button,bd=0, cursor="hand2", command=shutdown)
fouth_button.place(x=200, y=200)

logout_time_button = PhotoImage(file="logout.PNG")
fifth_button = Button(root, image=logout_time_button,bd=0, cursor="hand2", command=logout)
fifth_button.place(x=100, y=400)



root.mainloop()