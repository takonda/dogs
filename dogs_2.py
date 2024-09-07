import requests
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO

from pygame.display import update


def load_image(url):
    try:
        response = requests.get(url)# запрошенное отправить в response
        response.raise_for_status() # для обработки исключений
        image_data = BytesIO(response.content)
        img=Image.open(image_data)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Произошла ошибка:{e}')
        return None


def set_image():
    img = load_image(url)
    if img:
        label.config(image=img)  # установим картинку на метку
        label.image = img  # эта строчка не даст сборщику мусора питона удалить картинку


window=Tk()
window.title('Собачки')
window.geometry('600x480')

label=Label()
label.pack()

update_button=Button(text='Обновить', command=set_image)
update_button.pack()

url="https://dog.ceo/api/breeds/image/random"
set_image()

window.mainloop()
