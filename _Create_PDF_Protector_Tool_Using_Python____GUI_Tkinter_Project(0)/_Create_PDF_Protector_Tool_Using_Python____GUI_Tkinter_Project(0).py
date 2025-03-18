import code
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PyPDF2 import PdfFileWriter, PdfFileReader
from PIL import Image, ImageTk
import os

root = Tk()
root.title("Pdf Protector")
root.geometry("550x430+300+100")
root.resizable(False, False)

def browse():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title="Select Image File",
                                          filetypes=(('PDF File','*.pdf'),('all files','*.*')))
    entry1.insert(END, filename)

def Protect():
    mainfile = source.get()
    protectfile = target.get()
    code = password.get()
    
    if mainfile=="" and protectfile=="" and password.get()=="":
        messagebox.showerror("Invalid","All entries are emtry !!")
    elif mainfile=="":
        messagebox.showerror("Invalid","Please Type Source PDF Filename")
    elif protectfile=="":
        messagebox.showerror("Invalid","Please Type Target PDF Filename")
    elif password.get()=="":
        messagebox.showerror("Invalid","Please Type Password")
    else:
        try:
            out = PdfFileWriter()
            file = PdfFileReader(filename)
            num = file.numPages
            
            for Idx in range(num):
                page = file.getPage(Idx)
                out.addPage(page)
                
            #password
            out.encrypt(code)
            
            with open(protectfile, "wb") as f:
                out.write(f)
                
            source.set("")
            target.set("")
            password.set("")
            
            messagebox.showinfo("Info","Successfully done !!!")
                
        except: 
            messagebox.showerror("Invalid","Invalid Entry !!")
            

#icon
image_icon = PhotoImage(file="images/icon.PNG")
root.iconphoto(False, image_icon)



#main
Top_image = PhotoImage(file="images/topImage.PNG")
Label(root, image=Top_image).pack()

frame = Frame(root, width=530, height=320, bd=5,relief=GROOVE)
frame.place(x=10, y=100)

##########
source = StringVar()
Label(frame, text="Source PDF File: ", font="arial 10 bold", fg="#4c4542").place(x=30, y=50)
entry1 = Entry(frame, width=30, textvariable=source, font="arial 12", bd=1)
entry1.place(x=150, y=48)

image = Image.open("images/buttonImage.png")
resized_image = image.resize((35,25))
Button_icon = ImageTk.PhotoImage(resized_image)
button = Button(frame, image=Button_icon, width=35, height=25, bg="#aabac1", command=browse).place(x=450, y=40)

##########
target = StringVar()
Label(frame, text="Target PDF File: ", font="arial 10 bold", fg="#4c4542").place(x=30, y=100)
entry2 = Entry(frame, width=30, textvariable=target, font="arial 12", bd=1)
entry2.place(x=150, y=100)

##########
password = StringVar()
Label(frame, text="Set User Password: ", font="arial 10 bold", fg="#4c4542").place(x=15, y=150)
entry3 = Entry(frame, width=30, textvariable=password, font="arial 12", bd=1)
entry3.place(x=150, y=150)


image1 = Image.open("images/button.png")
resized_image1 = image1.resize((80,50))
button_icon1 = ImageTk.PhotoImage(resized_image1)
Protect = Button(root, text="Protect PDF File", compound=LEFT, image=button_icon1, height=50,font="arial 15 bold", bg="#768f99", command=Protect)
Protect.config(padx=2,pady=2)
Protect.pack(side=BOTTOM, pady=40)


root.mainloop()

