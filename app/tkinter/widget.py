from tkinter import *
from tkinter import ttk


root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
root.attributes("-topmost", True)  # устанавливаем окно поверх других окон

btn4 = Button(text="TOP")
btn4.pack(side=TOP, fill=BOTH)

btn = Button(text="Hello")
# btn.pack()
# btn.pack(expand=True)
# btn.pack(anchor=SE, expand=True) # чтобы разместить кнопку внизу нужно использовать expand=True 

# заполнение по сторонам
# btn.pack(fill=X)
# btn.pack(fill=Y)
# btn.pack(fill=BOTH)

# btn.pack(anchor="nw", padx=20, pady=30) # отступы от краев окна
btn.pack(fill=X, padx=[20, 100], pady=30,) # отступы от краев окна


btnWithPosition = ttk.Button(text="Position")
btnWithPosition.place(x=20, y=40) # абсолютное позиционирование

btnWithPositionFloat = ttk.Button(text="Position @")
btnWithPositionFloat.place(relx=0.5, rely=0.5, width=80, height=40) # относительное позиционирование
btnWithPositionFloat.place(anchor=NW) # относительное позиционирование

btnRel = ttk.Button(text="Relief")
btnRel.place(relx=0.5, rely=1, anchor=S, relwidth=0.33, relheight=0.25) # относительное позиционирование

def print_info(widget, depth=0):
    widget_class=widget.winfo_class()
    widget_width = widget.winfo_width()
    widget_height = widget.winfo_height()
    widget_x = widget.winfo_x()
    widget_y = widget.winfo_y()
    print("   "*depth + f"{widget_class} width={widget_width} height={widget_height}  x={widget_x} y={widget_y}")
    for child in widget.winfo_children():
        print_info(child, depth+1)
 
root.update()     # обновляем информацию о виджетах
 
print_info(root)
 
root.mainloop()