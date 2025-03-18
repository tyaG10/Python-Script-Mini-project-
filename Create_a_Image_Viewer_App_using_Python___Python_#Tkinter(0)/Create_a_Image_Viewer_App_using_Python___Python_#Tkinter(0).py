from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os


def showImage():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select image file", filetypes=(("JPG file","*.jpg"),("PNG file","*.png"),("All file","How are you .txt")))
    img = Image.open(filename)
    widthImg, heightImg= img.size
    widthImg += 20
    widthFrame = fram.winfo_width()
    heightFrame = fram.winfo_height() + 35
    widthBtn = btn.winfo_width()
    heightBtn = btn.winfo_height()
    widthBtn2 = btn2.winfo_width()
    heightBtn2 = btn2.winfo_height()
    

    print(widthFrame)
    print(heightFrame)
    print(widthImg)
    print(heightImg)
    print(widthBtn)
    print(heightBtn)
    print(widthBtn2)
    print(heightBtn2)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img
    if widthImg <= 170:
        root.geometry(f"180x{heightImg+heightFrame}")
    else:
        root.geometry(f"{widthImg}x{heightImg+heightFrame}")


root = Tk()
root.title("Image Viewer")
root.config(bg="#cbc9d0")
root.geometry("400x450")
#icon
image_icon = PhotoImage(file="icon.PNG")
root.iconphoto(False, image_icon)

fram =Frame(root,bg="#cbc9d0")
fram.pack(side=BOTTOM, padx=15, pady=15)

lbl = Label(root)
lbl.pack()

btn = Button(fram, text="Select Image", command=showImage)
btn.pack(side=tk.LEFT)

btn2 = Button(fram, text="Exit", command=lambda:exit())
btn2.pack(side=tk.LEFT, padx= 12)



root.mainloop()