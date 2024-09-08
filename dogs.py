import requests # чтобы загружать изображения из интернета
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from PIL import Image, ImageTk # чтобы обрабатывать изображения
from io import BytesIO # чтобы обрабатывать картинку

from bottle import response


def get_random_dog_image():
    try:
        response=requests.get("https://dog.ceo/api/breeds/image/random") #
        response.raise_for_status() # из jason придет изображение
        data=response.json()
        return data['message'] # отправит уже картинку присланую по запросу в image_url
    except Exception as e:
        mb.showerror('Ошибка',f'Ошибка при запросе к API:{e}')
        return None


def show_image():
    image_url=get_random_dog_image()
    if image_url:
        try:
            response=requests.get(image_url, stream=True) # получаем ответ на запрос по ссылке
            response.raise_for_status() # получаем статус ответа, пригодится для обработки искл.
            img_data=BytesIO(response.content) # загрузили ответ в двоичном коде
            img=Image.open(img_data) # обработали картинку
            img_size=(int(width_spinbox.get()),int(height_spinbox.get())) # получаем значения ширины и высоты картинки
            img. thumbnail(img_size)
            img=ImageTk.PhotoImage(img)
            # new_window= Toplevel(window)
            # new_window.title('Случайное изображение')
            tab = ttk.Frame(notebook) # закладки
            notebook.add(tab, text=f'Картинка № {notebook.index("end") +1}') # добавить закладку с надписью Картинка
            lb = ttk.Label(tab, image=img) # загрузили картинку в метку в новом окне
            lb.pack(padx=10, pady=10)
            lb.image=img # защитили картинку от мусорщика питона
        except requests.RequestException as e:
            mb.showerror('Ошибка',f'Не удалось загрузить изображение:{e}')
    progress.stop()



def exit():
    window.destroy()


def prog():
    progress['value'] = 0 # начинает с нуля
    progress.start(30) # шаг увеличения в 30 миллисекунд
    window.after(3000, show_image) # через 3000 миллисекунд включается функция загрузки изображения show_image


window = Tk()
window.title('Собачки')
window.geometry('360x420')

label=ttk.Label()
label.pack(padx=10, pady=10)


button=ttk.Button(text='Загрузить изображение',command=prog)
button.pack(padx=10,pady=10)

progress = ttk.Progressbar(mode="determinate", length=300) # полоса загрузки
progress.pack(pady=10)

width_label = ttk.Label(text='Ширина:') # метка под спинбокс ширина
width_label.pack(side='left', padx=(10, 0))
width_spinbox = ttk.Spinbox(from_=200, to=500, increment=50, width=5) # изменение от 200 до 500 с шагом 50, ширина 5
width_spinbox.pack(side='left', padx=(0, 10))

height_label = ttk.Label(text='Высота:') # метка под спинбокс высота
height_label.pack(side='left', padx=(10, 0))
height_spinbox = ttk.Spinbox(from_=200, to=500, increment=50, width=5)
height_spinbox.pack(side='left', padx=(0, 10))

top_level_window=Toplevel(window)
top_level_window.title('Изображения собачек')

notebook=ttk.Notebook(top_level_window)
notebook.pack(expand=True, fill='both', padx=10, pady=10) #для полного заполнения окна и соблюдения отступов

window.mainloop()
