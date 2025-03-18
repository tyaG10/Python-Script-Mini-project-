from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)
root.configure(bg="#dbdfe1")

def getWeather():
    city = textfield.get()
    
    geolocator = Nominatim(user_agent="GetLoc")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    print(result)
    
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")
    
    #Weather
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=5136786266be7c57afadaabad0c95c13"
    
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    
    t.config(text=(temp, "°"))
    c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
    
    w.config(text=wind)
    w.place(x=160, y=400)
    h.config(text=humidity)
    h.place(x=320,y=430)
    d.config(text=description)
    d.place(x=440, y=400)
    p.config(text=pressure)
    p.place(x=650, y=400)
    
    

#Search box
Search_image = PhotoImage(file="search.PNG")
my_image = Label(image=Search_image, bd=0)
my_image.place(x=20,y=20)

textfield = tk.Entry(root, justify="center", width=15, font=("poppins", 25,"bold"), bg="#3b3838", bd=0, fg="white")
textfield.place(x=50, y=23)
textfield.focus()
 
image = Image.open("search_icon.png")
resized_image = image.resize((40,40))
Search_icon = ImageTk.PhotoImage(resized_image)
my_image_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2",bg="#3b3838",command=getWeather)
my_image_icon.place(x=330, y=28)


#logo
image1 = Image.open("logo.png")
resized_image1 = image1.resize((200,200))
logo_image = ImageTk.PhotoImage(resized_image1)
logo = Label(image=logo_image, bd=0,bg="#dbdfe1")
logo.place(x=150, y=100)

#Bottom
Frame_image =PhotoImage(file="box.PNG")
frame_my_image = Label(image=Frame_image, bd=0)
frame_my_image.pack(padx=5, pady=5, side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"),bg="#dbdfe1",bd=0)
name.place(x=20, y=100)
clock=Label(root, font=("Helvetica",20),bg="#dbdfe1", bd=0)
clock.place(x=30, y=130)

#Label
label1 = Label(root, text="WIND", font=("Helvetica", 15,"bold"), fg="white", bg="#38e1f8")
label1.place(x=160, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15,"bold"), fg="white", bg="#38e1f8")
label2.place(x=290, y=400)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15,"bold"), fg="white", bg="#38e1f8")
label3.place(x=440, y=400)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15,"bold"), fg="white", bg="#38e1f8")
label4.place(x=630, y=400)


t= Label(font=("arial",70,"bold"), fg="#ee666d",bg="#dbdfe1",bd=0)
t.place(x=400, y=150)
c= Label(font=("arial",15,"bold"),bg="#dbdfe1",bd=0)
c.place(x=400, y=250)


w=Label(text="...", font=("arial",20,"bold"), bg="#38e1f8")
w.place(x=180,y=430)
h=Label(text="...", font=("arial",20,"bold"), bg="#38e1f8")
h.place(x=310,y=430)
d=Label(text="...", font=("arial",20,"bold"), bg="#38e1f8")
d.place(x=470,y=430)
p=Label(text="...", font=("arial",20,"bold"), bg="#38e1f8")
p.place(x=670,y=430)






root.mainloop()