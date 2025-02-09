from tkinter import *
 
root = Tk()     # создаем корневой объект - окно
root.title("Приложение на Tkinter")     # устанавливаем заголовок окна
root.iconbitmap(default="app/tkinter/favicon.ico")   # устанавливаем иконку окна
# icon = PhotoImage(file = "icon2.png") // альтернативный способ
# root.iconphoto(False, icon)
root.geometry("300x250+0+0")    # устанавливаем размеры окна и его положение на экране
root.attributes("-topmost", True)  # устанавливаем окно поверх других окон

root.update_idletasks() # обновляем окно
print(root.geometry()) 

# root.attributes("-fullscreen", True) # устанавливаем полноэкранный режим
# root.attributes("-alpha", 0.5)  # устанавливаем прозрачность окна
# root.attributes("-toolwindow", True) # отключение верхней панели окна (за исключением заголовка и крестика для закрытия):

# root.resizable(False, False)    # запрещаем изменение размеров окна
# root.minsize(200,150)   # минимальные размеры: ширина - 200, высота - 150
# root.maxsize(400,300)   # максимальные размеры: ширина - 400, высота - 300

label = Label(text="Hello METANIT.COM") # создаем текстовую метку
label.pack()    # размещаем метку в окне

def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")


root.protocol("WM_DELETE_WINDOW", finish)

root.mainloop()