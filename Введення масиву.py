import tkinter
window = tkinter.Tk()
#  створення  об’єкта  для  отримання  значення  кількості 
#  елементів з текстового поля
s = tkinter.StringVar()
# створення порожнього списку
x = []
# опрацювання події натиснення кнопки
def button_click():
    n=int(s.get())
    i=0
    for i in range(n):
        # додавання до списку чергового елемента
        x.append(int(input()))

# створення текстового напису та його розміщення на головній формі
label=tkinter.Label(text='Введіть кількість елементів:')
label.pack()
# створення текстового поля та його розміщення на головній формі
edit=tkinter.Entry(window, textvariable=s)
edit.pack()
# створення кнопки та розміщення об’єкта на головній формі
button=tkinter.Button(window, text='Розпочати введення',
                      command=button_click)
button.pack()
# запуск опрацювання подій програми
window.mainloop()
