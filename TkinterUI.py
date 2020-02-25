from tkinter import *
from PIL import ImageTk, Image
import os, requests
import main as m
import datetime

icon_loc = '/Users/jackamu/PycharmProjects/Weather/Icons/'

root = Tk()
root.title('Flying Weather App')
root.geometry('1000x800')

frame = Frame(root,bg='#e0fffc')
frame.place(width=1000,height = 700,relheight=.5)

r = 2

loc_label = Label(frame, text = f'{m.example.weather_data_list[0].city}\n{m.example.weather_data_list[0].country}', font='Helvetica 18', bg='#e0fffc')
loc_label.grid(row =0, column = 4)

sun_label = Label(frame, text = f'Sunrise: {m.example.weather_data_list[0].sunrise}\nSunset: {m.example.weather_data_list[0].sunset}', bg='#e0fffc', font='Helvetica 16')
sun_label.grid(row= 0,column = 6)

for date in m.example.dates:
    date_label = Label(frame,text = date,bg='#e0fffc',font='Helvetica 14 bold')
    date_label.grid(row=r,column =0)
    r += 1
    for j , i in enumerate(m.example.weather_data_list):
        if i.date == date and i.dark == False: # Only showing data for daylight hours
            time_label = Label(frame,text = i.tf_time,bg='#e0fffc')
            time_label.grid(row = r, column =0)

            temp_label = Label(frame,text = f'{i.temp}.C',bg='#e0fffc')
            temp_label.grid(row=r,column=3,padx = 20)

            wind_label = Label(frame,text = f'{i.wind_speed}mph  {i.cardinal}',bg='#e0fffc')
            wind_label.grid(row = r, column = 4)

            main_label = Label(frame,text = f'{i.descrpition}',bg='#e0fffc')
            main_label.grid(row=r,column=2)

            img = Image.open(icon_loc + i.iconname + '.png')
            img = img.resize((30, 30), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            icon_label = Label(frame,image=img,bg='#e0fffc')
            icon_label.image = img
            icon_label.grid(row=r,column=1)

            if i.good_to_fly() == False:
                fly_label = Label(frame,text = f'{i.why}',bg='#e0fffc')
                fly_label.grid(row=r, column=5)
            else:
                fly_label = Label(frame,bg='#e0fffc')
                fly_label.grid(row=r, column=5,padx = 100)


            if i.good_to_fly() == True:

                smile = Image.open(icon_loc + 'happy.png')
                smile = smile.resize((30, 30), Image.ANTIALIAS)
                smile = ImageTk.PhotoImage(smile)
                smile_label = Label(frame,image=smile,bg='#e0fffc')
                smile_label.image = smile

            else:
                smile = Image.open(icon_loc + 'unhappy.png')
                smile = smile.resize((30, 30), Image.ANTIALIAS)
                smile = ImageTk.PhotoImage(smile)
                smile_label = Label(frame, image=smile, bg='#e0fffc')
                smile_label.image = smile


            smile_label.grid(row=r,column=6)


        r+=1



root.mainloop()