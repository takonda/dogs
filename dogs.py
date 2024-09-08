import requests # чтобы загружать изображения из интернета
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from PIL import Image, ImageTk # чтобы обрабатывать изображения
from io import BytesIO # чтобы обрабатывать картинку

from bottle import response


def get_random_dog_image():
    try:
        response=requests.get("https://dog.ceo/api/breeds/image/random")
        response.raise_for_status()
        data=response.json()
        return data['message']
    except Exception as e:
        mb.showerror('Ошибка',f'Ошибка при запросе к API:{e}')


def show_image():
    image_url=get_random_dog_image()
    if image_url:
        try:
            response=requests.get(image_url, stream=True)
            response.raise_for_status()
            img_data=BytesIO(response.content)
            img=Image.open(img_data)
            img.thumbnail((300,300))
            img=ImageTk.PhotoImage(img)
            label.config(image=img)
            label.img=img
        except requests.RequestException as e:
            mb.showerror('Ошибка',f'Не удалось загрузить изображение:{e}')



def exit():
    window.destroy()


window = Tk()
window.title('Собачки')
window.geometry('360x420')

label=Label()
label.pack(padx=10, pady=10)


button=Button(text='Загрузить изображение',command=show_image)
button.pack(padx=10,pady=10)

window.mainloop()
