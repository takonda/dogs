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
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)#размер картинки в окне и чтобы качество не пострадало

        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Произошла ошибка:{e}')
        return None


def set_image():
    img = load_image(url)
    if img:
        label.config(image=img)  # установим картинку на метку
        label.image = img  # эта строчка не даст сборщику мусора питона удалить картинку


def exit():
    window.destroy()


window=Tk()
window.title('Собачки')
window.geometry('600x480')

label=Label()
label.pack()

# update_button=Button(text='Обновить', command=set_image)
# update_button.pack()

menu_bar=Menu(window)
window.config(menu=menu_bar)
file_menu=Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Загрузить фото', command=set_image)
file_menu.add_separator()
file_menu.add_command(label='Выход',command=exit)

url="https://dog.ceo/api/breeds/image/random"
set_image()

window.mainloop()
