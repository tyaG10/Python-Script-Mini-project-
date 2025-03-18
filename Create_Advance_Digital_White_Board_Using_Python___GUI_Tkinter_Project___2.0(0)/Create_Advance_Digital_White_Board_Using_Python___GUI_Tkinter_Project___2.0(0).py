from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import os

root = Tk()
root.title("WHITE BOARD")
root.geometry("1050x570+150+50")
root.config(bg="#dadadd")
root.resizable(False,False)

current_x = 0
current_y = 0
color = "black"

def locate_xy(work):
    global current_x, current_y
    
    current_x = work.x
    current_y = work.y
    

def addline(work):
    global current_x, current_y
    
    canvas.create_line((current_x,current_y,work.x, work.y), width=get_current_value(),
                       fill=color, capstyle=ROUND, smooth=True)
    current_x,current_y = work.x,work.y
    

def show_color(new_color):
    global color
    
    color = new_color

def new_canvas():
    canvas.delete('all')
    display_palette()

def insereImage():
    global filename
    global f_img
    
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file",
                                          filetypes=(("PNG file","*.png"),("All file","new.txt")))
    f_img = tk.PhotoImage(file=filename)
    my_img = canvas.create_image(180,50,image=f_img)
    root.bind("<B3-Motion>", my_callback)
    

def my_callback(event):
    global f_img
    
    f_img = tk.PhotoImage(file=filename)
    my_img = canvas.create_image(event.x, event.y, image=f_img)



#icon
image_icon = PhotoImage(file="icon.PNG")
root.iconphoto(False, image_icon)

#Sidebar
color_box = PhotoImage(file="sidebar.PNG")
Label(root, image=color_box, bg="#dadadd").place(x=10, y=20)

imageEraser = Image.open("eraser.png")
resized_imageEraser = imageEraser.resize((30,30))
eraser = ImageTk.PhotoImage(resized_imageEraser) 
Button(root, image=eraser, bg="#dadadd", command=new_canvas).place(x=30, y=390)

addImage = Image.open("addImage.png")
resized_addImage = addImage.resize((30,30))
addImage1 = ImageTk.PhotoImage(resized_addImage)
Button(root, image=addImage1, bg="#dadadd", command=insereImage).place(x=30, y=440)

#Color
colors = Canvas(root, bg="#fff", width=37, height=300, bd=0)
colors.place(x=30, y=60)

def display_palette():
    id = colors.create_rectangle((10,10,30,30), fill = "black")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('black'))

    id = colors.create_rectangle((10,40,30,60), fill = "gray")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('gray'))
    
    id = colors.create_rectangle((10,70,30,90), fill = "brown4")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('brown4'))
    
    id = colors.create_rectangle((10,100,30,120), fill = "red")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('red'))
    
    id = colors.create_rectangle((10,130,30,150), fill = "orange")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('orange'))
    
    id = colors.create_rectangle((10,160,30,180), fill = "yellow")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('yellow'))
    
    id = colors.create_rectangle((10,190,30,210), fill = "green")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('green'))

    id = colors.create_rectangle((10,220,30,240), fill = "blue")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('blue'))
    
    id = colors.create_rectangle((10,250,30,270), fill = "purple")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('purple'))


display_palette()

#main Screen
canvas = Canvas(root, width=930, height=500, background="white", cursor="hand2")
canvas.place(x=100, y=10)

canvas.bind('<Button-1>',locate_xy)
canvas.bind('<B1-Motion>', addline)


#Slider
current_value = tk.DoubleVar()
def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_change(event):
    value_label.configure(text= get_current_value())

slider = ttk.Scale(root, from_=0,to=100, orient="horizontal", command=slider_change, variable=current_value)
slider.place(x=30, y=520)

value_label=ttk.Label(root,text=get_current_value(),background="#dadadd")
value_label.place(x=26, y=552)

text_label = ttk.Label(root,text="Line size", font=("Arial",9,"bold"),background="#dadadd")
text_label.place(x=65,y=552)








root.mainloop()