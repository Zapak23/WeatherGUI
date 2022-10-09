from tkinter import *
import customtkinter
import requests
import json
from datetime import datetime

customtkinter.set_appearance_mode("Dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")

customroot = customtkinter.CTk()  
customroot.title("Zo's Weather App")
customroot.geometry("600x400")

city_value = StringVar() 

def show_Weather():
    api_key = "66122e988c28bbcae23baa88184cad53"
    city_name = city_value.get()
    Weather_URL = "http://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=" + api_key
    
    response = requests.get(Weather_URL)
    weather_info = response.json()

    tfield.delete("1.0", "end") #0.0 also works

    if weather_info['cod'] == 200:
        kelvin = 273 

        temp = int(weather_info['main']['temp'] - kelvin)
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        description = weather_info['weather'][0]['description']
        fahrenheit_temp = temp * 9/5 + 32
        fahrenheit_temp_feels_like = feels_like_temp * 9/5 + 32

        weather = f"\nWeather of: {city_name}\nTemperature (Fahrenheit): {fahrenheit_temp}°\nFeels like (Fahrenheit): {fahrenheit_temp_feels_like}°\nDescription: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\t Enter valid City Name !!"

    tfield.insert(INSERT, weather)

city_head = customtkinter.CTkLabel(master= customroot, text="Enter City Name", width=120, height=30,
    corner_radius=8, text_font = ("default_theme",20))
city_head.place(relx=0.5, rely=0.15, anchor=customtkinter.CENTER)
 
inp_city = customtkinter.CTkEntry(master=customroot, width=360, height=50, corner_radius=10, textvariable = city_value, 
    text_font = ("default_theme",15))
inp_city.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

 
button = customtkinter.CTkButton(master = customroot, fg_color=("black"), text="Check Weather", command= show_Weather)
button.place(relx=0.5, rely=0.45, anchor=customtkinter.CENTER)

weather_now = customtkinter.CTkLabel(master = customroot, text="The Weather is:", width=120, height=25,
    corner_radius=8, text_font = ("default_theme",20))
weather_now.place(relx=0.5, rely=0.55, anchor=customtkinter.CENTER)
 
tfield = Text(customroot, width=46, height=8, font = ("default_theme",10))
tfield.pack()
tfield.place(relx = 0.5, rely = 0.75, anchor = customtkinter.CENTER)

customroot.mainloop()