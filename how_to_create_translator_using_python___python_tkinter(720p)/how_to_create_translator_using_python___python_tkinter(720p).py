from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import textblob
from PIL import ImageTk, Image


root = Tk()
root.title("Google translator")
root.geometry("1080x400")
root.config(bg="white")


def label_change():
    c1 = combo1.get()
    c2 = combo2.get()
    label1.configure(text=c1)
    label2.configure(text=c2)
    root.after(1000, label_change)
    
   
def translate_now():
    global language

    text_ = text1.get(1.0,END)
    c1 = combo1.get()
    c2 = combo2.get()
    if(text_):
        words = textblob.TextBlob(text_)
        lan = words.detect_language()
        for i,j in language.items():
            if(j==c2):
                lan_=i
        words = words.translate(from_lang=lan, to=str(lan_))
        text2.delete(1.0, END)
        text2.insert(END,words)
            



#icon
image_icon = PhotoImage(file="icon.PNG")
root.iconphoto(False, image_icon)

#Arrow
image = Image.open("icon_fleche.png")
resized_image = image.resize((120,120))
image1_label = ImageTk.PhotoImage(resized_image)
image_label = Label(root, image=image1_label,width=150,  bg="white").place(x=460, y=50)


language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()


combo1 = ttk.Combobox(root,values=languageV, font="Roboto 14", state="r")
combo1.place(x=110,y=20)
combo1.set("ENGLISH")

label1 = Label(root, text = "ENGLISH", font="segoe 30 bold", bg="white",width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

f =Frame(root,bg="#8fded6",bd=5)
f.place(x=10, y=118, width=440,height=210)

text1 = Text(f,font="Robote 20", bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right",fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)






combo2 = ttk.Combobox(root,values=languageV, font="RobotV 14", state="r")
combo2.place(x=730,y=20)
combo2.set("SELECT LANGUAGE")

label2 = Label(root, text = "ENGLISH", font="segoe 30 bold", bg="white",width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

f1 =Frame(root,bg="#ffbe00",bd=5)
f1.place(x=620, y=118, width=440,height=210)

text2 = Text(f1,font="Robote 20", bg="white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right",fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

#Button 
translate = Button(root, text="Translate", font="Roboto 15 bold italic",activebackground="#ffbe00",cursor="hand2",bd=1,bg="#8fded6", fg="white", command=translate_now)
translate.place(x=480,y=250)




label_change()


root.mainloop()