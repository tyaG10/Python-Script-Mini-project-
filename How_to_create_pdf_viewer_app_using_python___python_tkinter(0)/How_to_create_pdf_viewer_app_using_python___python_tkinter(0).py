from tkinter import *
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf
import os


root = Tk()
root.geometry("630x700+400+100")
root.title("PDF viewer")
root.configure(bg="white")

def browseFile():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title="Select pdf file",
                                          filetype=(("PDF File",".pdf"),
                                                    ("PDF File",".PDF"),
                                                    ("All file",".txt")))
    
    v1 = pdf.ShowPdf()
    v2 = v1.pdf_view(root,pdf_location=open(filename,"r"),width=77,height=100)
    v2.pack(pady=(0,0))
    
    

Button(root, text="open", command=browseFile, width=40, font="arial 20", bd=4).pack()



root.mainloop()