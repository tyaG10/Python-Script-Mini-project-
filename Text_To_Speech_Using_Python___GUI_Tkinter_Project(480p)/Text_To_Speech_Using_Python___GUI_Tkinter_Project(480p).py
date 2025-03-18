import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
from PIL import Image, ImageTk


root = Tk()
root.title("Text to speech")
root.geometry("900x450")
root.resizable(False, False)
root.configure(bg="#305065")

engine = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0,END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')
    
    def setvoice():
        if(gender=='Male'):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
            
        else:
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()
            
    if (text):
        if(speed == "Fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif(speed == "Normal"):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()
            

def download():
    text = text_area.get(1.0,END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')
    
    def setvoice():
        if(gender=='Male'):
            engine.setProperty('voice',voices[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
            
        else:
            engine.setProperty('voice',voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
            
    if (text):
        if(speed == "Fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif(speed == "Normal"):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()  
            
            


#icon
image_icon = PhotoImage(file="icon.PNG")
root.iconphoto(False,image_icon)

#Top Frame
top_frame = Frame(root, bg="white", width=900, height=100)
top_frame.place(x=0, y=0)

image = Image.open("audio.png")
resized_image = image.resize((80,80))
Logo = ImageTk.PhotoImage(resized_image)
Label(top_frame, image=Logo, bg="white").place(x=10, y=5)

Label(top_frame, text="TEXT TO SPEECH", font="arial 20 bold", bg="white",fg="black").place(x=100,y=30)


##########
text_area = Text(root, font="Robote 20", bg="white",relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=500, height=250)

Label(root, text="VOICE", font="arial 15 bold", bg="#305065", fg="white").place(x=580,y=160)
Label(root, text="SPEED", font="arial 15 bold", bg="#305065", fg="white").place(x=760, y=160)

gender_combobox = Combobox(root, values=['Male','Female'], font="arial 14", state='r', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Male')

speed_combobox = Combobox(root, values=['Fast','Normal','Slow'], font="arial 14", state='r', width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set('Normal')


image1 = Image.open("speak.png")
resized_image1 = image1.resize((70,70))
speak_icon = ImageTk.PhotoImage(resized_image1)
btn = Button(root, text="Speak",compound=LEFT, image=speak_icon,width=130,font="arial 14 bold", command=speaknow)
btn.place(x=550, y=280)

image2 = Image.open("save.png")
resized_image2 = image2.resize((70,70))
save_icon = ImageTk.PhotoImage(resized_image2)
save = Button(root, text="Save",compound=LEFT, image=save_icon,width=130, bg="#39c790",font="arial 14 bold", command=download)
save.place(x=730, y=280)




root.mainloop()