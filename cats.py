import requests
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO

Allowed_tags=['sleep','jamp','fight','black','white','siamese','cute','play','small']


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


def open_new_window():
    tag = tag_combobox.get()
    url_tag = f'https://cataas.com/cat/{tag}' if tag else "https://cataas.com/cat"
    img = load_image(url_tag)
    if img:
        new_window = Toplevel()
        new_window.title('Картинка с котиком')
        new_window.geometry('600x480')
        label = Label(new_window, image=img)
        label.pack()
        label.image = img  # эта строчка не даст сборщику мусора питона удалить картинку


def exit():
    window.destroy()


window=Tk()
window.title('Котики')
window.geometry('600x480')

menu_bar=Menu(window)
window.config(menu=menu_bar)
file_menu=Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Загрузить фото', command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label='Выход',command=exit)

url="https://cataas.com/cat"

tag_label=Label(text='Выбери тег')
tag_label.pack()

tag_combobox = ttk.Combobox(values=Allowed_tags)
tag_combobox.pack()

load_button= Button(text='Загрузить по тегу', command=open_new_window)
load_button.pack()

window.mainloop()
