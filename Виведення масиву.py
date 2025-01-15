import tkinter
from tkinter import ttk
from tkinter import messagebox
import random
window = tkinter.Tk()
#  створення  об’єкта  для  отримання  значення  кількості 
#  елементів з текстового поля
s = tkinter.StringVar()
# створення порожнього списку
x = []

# опрацювання події натиснення кнопки
def button_click():
    # отримання значення кількості елементів списку
    n=int(s.get())
    # задання початкового значення рядка результату
    sl=''
    for i in range(n):
        # додавання до списку чергового елемента
        x.append(random.randint(0,10))
        # створення списку елементів у рядку
        sl=sl+str(x[i])+' '
    # виведення вікна повідомлення із результатом
    messagebox.showwarning('Результат', sl)
    
# створення текстового напису та його розміщення
# на головній формі
label=tkinter.Label(text='Введіть  кількість  елементів:')
label.pack()
# створення текстового поля та його розміщення 
# на головній формі
edit=tkinter.Entry(window, textvariable=s)
edit.pack()
# створення кнопки та розміщення об’єкта
# на головній формі
button=tkinter.Button(window, text='Розпочати',
                      command=button_click)
button.pack()
# запуск опрацювання подій програми
window.mainloop()