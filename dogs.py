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
            img.thumbnail((300,300)) # подогнали размер картинки
            img=ImageTk.PhotoImage(img)
            label.config(image=img) # загрузили картинку в метку
            label.img=img # защитили картинку от мусорщика питона
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

progress = ttk.Progressbar(mode="determinate", length=300)
progress.pack(pady=10)

window.mainloop()
