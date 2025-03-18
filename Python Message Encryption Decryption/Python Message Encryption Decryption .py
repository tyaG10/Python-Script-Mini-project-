from genericpath import exists
from tkinter import *
import base64
from tkinter import messagebox
import tkinter.font as font

def encode(key, msg):
    enc = []
    for i in range(len(msg)):
        list_key = key[i % len(key)]
        list_enc = chr((ord(msg[i]) + ord(list_key)) % 256)
        enc.append(list_enc)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()
    
def decode(key, code):
    dec = []
    enc = base64.urlsafe_b64decode(code).decode()
    for i in range(len(enc)):
        list_key = key[i % len(key)]
        list_dec = chr((256 + ord(enc[i]) - ord(list_key)) % 256)
        
        dec.append(list_dec)
        
    return "".join(dec)

def Result():
    msg = message.get()
    k = key.get()
    i=mode.get()
    
    if(i==1):
        output.set(encode(k,msg))
    elif(i==2):
        output.set(decode(k,msg))
    else:
        messagebox.showinfo('Encrypt or decrypt', 'Please choose one of Encryption or Decryption. Try again.')

def Reset():
    message.set("")
    key.set("")
    mode.set(0)
    output.set("")
    
    
    

root =Tk()
root.geometry("500x500")
root.configure(bg = 'azure2')
root.title("Crypter/Descrypter")

message = StringVar()
key = StringVar()
mode = IntVar()
output = StringVar()

headingFrame1 = Frame(root, bg="gray91", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.7, relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to Encryption and \nDecryption project", fg='grey19', font= ('Courier', 15,'bold'))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

label1 = Label(root, text="Enter the message", font=('Courier',10))
label1.place(x=10, y=150)

msg = Entry(root, textvariable=message, width=35, font=('calibre',10,'normal'))
msg.place(x=200, y=150)

label2 = Label(root, text='Enter the key', font=('Courier',10))
label2.place(x=10, y=200)

inkey = Entry(root, textvariable=key, width=35, font=('Calibre', 10,'normal'))
inkey.place(x=200, y=200)

label3 = Label(root, text='Check one of encrypt or decrypt', font=('Courier',10,'normal'))
label3.place(x=10, y=250)

Radiobutton(root,text='Encrypt', variable=mode, value=1).place(x=100, y=300)
Radiobutton(root,text='Decrypt', variable=mode, value=2).place(x=200, y=300)

label4= Label(root, text='Result', font=('Courier',10))
label4.place(x=10,y=350)

res = Entry(root, textvariable=output, width=35, font=('calibre',10,'normal'))
res.place(x=200, y=350)

ResetBtn = Button(root, text='Reset', bg='honeydew2', fg='black', width=15,height=1,command=Reset)
ResetBtn['font'] = font.Font(size=12)
ResetBtn.place(x=15, y=400)

ShowBtn = Button(root, text='Show Message', bg='lavender blush2', fg="black", width=15, height=1,command=Result)
ShowBtn['font'] = font.Font(size=12)
ShowBtn.place(x=180, y=400)

exitBtn = Button(root, text='Exit', bg='#ebe4f9', fg='black', width=10,height=1,command=exit)
exitBtn['font'] = font.Font(size=12)
exitBtn.place(x=345, y=400)









root.mainloop()