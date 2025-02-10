from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from input_frame import InputFrame

import re
import os


def center_window(root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width - root.winfo_reqwidth()) // 2) - 300
    y = ((screen_height - root.winfo_reqheight()) // 2) - 200
    root.geometry(f"800x600+{x}+{y}")


def create_frame(label_text):
    frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 12])
    return frame


root = Tk()
root.title("Compressor")
center_window(root)
root.resizable(False, False)
root.iconbitmap(default="app/tkinter/favicon.ico")

input_frame = InputFrame(root, borderwidth=1, relief="solid", padding=[8, 12])

root.mainloop()
