from tkinter import *
from PIL import ImageTk, Image
import os

icon_loc = '/Users/jackamu/PycharmProjects/Weather/Icons/'

root = Tk()
root.title('Images')
root.iconbitmap('')


my_img = ImageTk.PhotoImage(Image.open('/Users/jackamu/PycharmProjects/Weather/Icons/02n.png'))
my_label = Label(image=my_img)
my_label.grid()


icon = '10d'
icon_loc = '/Users/jackamu/PycharmProjects/Weather/Icons/'

weather_img = ImageTk.PhotoImage(Image.open(f'{icon_loc}{icon}.png'))
my_icon_label = Label(image = weather_img)
my_icon_label.grid()




button_quit = Button(root,text = 'Exit Program', command = root.quit)

button_quit.grid()

root.mainloop()