# Libraries
from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# tkinter
root = Tk()
root.geometry('1200x500')
root.config(bg = 'black')
root.title("Language Translator")
Label(root, text = "LANGUAGE TRANSLATOR", font = "georgia 20 bold", fg = 'silver', bg = 'black').pack()

# Input Text
Label(root,text ="Enter Text", font = 'georgia 18 bold',fg = 'silver', bg = 'black').place(x=200,y=80)
Input_text = Text(root,font = 'georgia 10', height = 14, wrap = WORD, padx=5, pady=5, width = 50, bg= 'white')
Input_text.place(x=40,y = 140)

# Output Text
Label(root,text ="Translated Text", font = 'georgia 18 bold',fg = 'silver', bg = 'black').place(x=830,y=80)
Output_text = Text(root,font = 'georgia 10', height = 14, wrap = WORD, padx=5, pady= 5, width =50)
Output_text.place(x = 690 , y = 140)

# Dropdown
language = list(LANGUAGES.values())
style= ttk.Style()
style.theme_use('clam')

# Input Language Dropdown
src_lang = ttk.Combobox(root, values= language, width = 10, font = 'georgia 9 bold')
src_lang.place(x=40,y=120)
src_lang.set('INPUT')

# Output Language Deopdown
dest_lang = ttk.Combobox(root, values= language, width = 10, font = 'georgia 9 bold')
dest_lang.place(x=690,y=120)
dest_lang.set('OUTPUT')

#Translate Function
def Translate():
    translator = Translator()
    global Input_text
    translated = translator.translate(text = Input_text.get(1.0, END) , src = src_lang.get(), dest = dest_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)

trans_btn = Button(root, text = 'TRANSLATE',font = 'georgia 12 bold',pady = 5,command = Translate , bg = 'white', activebackground = 'grey')
trans_btn.place(x = 535, y= 400 )

root.mainloop()
