import requests
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO

from pygame.examples.cursors import image
from pygame.examples.moveit import load_image
from pygame.examples.sprite_texture import load_img

window = Tk()
window.title('Собачки')
window.geometry('600x480')

label=Label()
label.pack(padx=10, pady=10)

url="https://dog.ceo/api/breeds/image/random"
img=load_image(url)
if img:
    label.config(image=img)#установим картинку на метку
    label.image=img# эта строчка не даст сборщику мусора питона удалить картинку

window.mainloop()
