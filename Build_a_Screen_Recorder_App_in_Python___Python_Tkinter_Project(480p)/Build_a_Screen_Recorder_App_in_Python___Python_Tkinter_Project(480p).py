from tkinter import *
import pyscreenrec 
from PIL import Image, ImageTk


root = Tk()
root.geometry("400x600")
root.title("Screen recorder")
root.config(bg="#fff")
root.resizable(False, False)

def start_rec():
    file = filename.get()
    rec.start_recording(str(file+".mp4"), 5)

def pause_rec():
    rec.pause_recording()

def resume_rec():
    rec.resume_recording()

def stop_rec():
    rec.stop_recording()

rec = pyscreenrec.ScreenRecorder()
    

#icon
image_icon = PhotoImage(file="icon.PNG")
root.iconphoto(False, image_icon)

#background images
image1 = Image.open("yelloww.png")
resized_image1 = image1.resize((400,400))
image1_label = ImageTk.PhotoImage(resized_image1)
Label(root, image=image1_label, bg="#fff").place(x=-100, y=-80)

image2 = Image.open("bluee.png")
resized_image2 = image2.resize((400,400))
image2_label = ImageTk.PhotoImage(resized_image2)
Label(root, image=image2_label, bg="#fff").place(x=105, y=150)



#heading
lbl = Label(root, text="Screen Recorder", bg="#fff",font="arial 15 bold")
lbl.pack(pady=20)

image3 = Image.open("recording.PNG")
resized_image3 = image3.resize((250,250))
image3_label = ImageTk.PhotoImage(resized_image3)
Label(root, image=image3_label, bd=0, bg="#f00").pack(pady=30)

#entry
filename =StringVar()
entry = Entry(root, textvariable=filename, width=18, font="arial 15").place(x=100, y=300)
filename.set("recording25")


#buttons
start = Button(root,text="Start", font="arial 20 bold", bd=2, bg="#f00", fg="#fff", command=start_rec)
start.place(x=145, y=205)

image4 = Image.open("pause.png")
resized_image4 = image4.resize((80,80))
image4_label = ImageTk.PhotoImage(resized_image4)
pause= Button(root, image=image4_label, bg="#fff",bd=0,command=pause_rec).place(x=50, y=450)

image5 = Image.open("play.png")
resized_image5 = image5.resize((80,80))
image5_label = ImageTk.PhotoImage(resized_image5)
resume = Button(root, image=image5_label, bg="#fff",bd=0, command=resume_rec).place(x=150, y=450)

image6 = Image.open("stop.png")
resized_image6 = image6.resize((80,80))
image6_label = ImageTk.PhotoImage(resized_image6)
stop = Button(root, image=image6_label, bg="#fff",bd=0,command=stop_rec).place(x=250, y=450)








root.mainloop()