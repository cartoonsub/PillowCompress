import tkinter as tk

def on_button_click():
    label.config(text="Hello, Tkinter!")

# Создаем главное окно
root = tk.Tk()
root.title("Пример Tkinter")

# Создаем метку
label = tk.Label(root, text="Нажмите кнопку")
label.pack()

# Создаем кнопку
button = tk.Button(root, text="Нажми меня", command=on_button_click)
button.pack()

# Запускаем главный цикл обработки событий
root.mainloop()