
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
from PIL import ImageTk, Image
import os


root = Tk()
root.title("Python IDLE")
root.geometry("1280x600+150+80")
root.configure(bg="#323846")
root.resizable(False,False)

file_path = ''

def set_file_path(path):
    global file_path
    file_path = path

def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        code_input.delete('1.0', END)
        code_input.insert('1.0', code)
        set_file_path(path)

def save():
    if file_path == '':
        path = askopenfilename(filetypes=[('Python','*.py')])
    else:
        path=file_path
        
    with open(path,'w') as file:
        code = code_input.get('1.0',END)
        file.write(code)
        set_file_path(path)

def run():
    if file_path == '':
        messagebox.showerror("Python IDLE, save your code ")
        return
    command = f"python(file_path)"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    
    code_output.insert('1.0',output)
    code_output.insert('1.0',error)
    









#icon
image_icon = PhotoImage(file="icon.PNG")
root.iconphoto(False,image_icon)

#code input
code_input = Text(root, font="consolas 15", bg="#323846",fg="lightgreen")
code_input.place(x=180, y=0, width=680, height=600)

#output code
code_output = Text(root, font="consolas 15", bg="#323846",fg="lightgreen")
code_output.place(x=860, y=0, width=420, height=600)


#Buttons


open =Image.open("plus.png")
resized_open = open.resize((80,80))
open_icon = ImageTk.PhotoImage(resized_open)
Button(image=open_icon, borderwidth=0, cursor="hand2", bg="#323846", command=open_file).place(x=30, y=30)

save = Image.open("save.png")
resized_save = save.resize((80,80))
save_icon = ImageTk.PhotoImage(resized_save)
Button(image=save_icon, borderwidth=0, cursor="hand2", bg="#323846", command=save).place(x=30, y=145)

run = Image.open("run.png")
resized_run = run.resize((80,80))
run_icon = ImageTk.PhotoImage(resized_run)
Button(image=run_icon, borderwidth=0, cursor="hand2", bg="#323846", command=run).place(x=30, y=260)









root.mainloop()