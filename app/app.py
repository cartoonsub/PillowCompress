from tkinter import *
from tkinter import ttk
from tkinter import filedialog

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


def choose_folder():
    folder_path = filedialog.askdirectory()
    if not folder_path:
        errmsg.set("Please enter a folder path")

    if not os.path.exists(folder_path):
        errmsg.set("Folder does not exist: " + folder_path)

    folder_entry.delete(0, END)
    folder_entry.insert(0, folder_path)


def is_valid_folder(folder_path):
    if not folder_path:
        errmsg.set("Please enter a folder path")
        error_label.config(foreground="red")

    if os.path.exists(folder_path):
        errmsg.set("Сorrect folder path")
        error_label.config(foreground="green")
    else:
        errmsg.set("Folder does not exist: " + folder_path)
        error_label.config(foreground="red")

    return True


root = Tk()
root.title("Compressor")
center_window(root)
root.resizable(False, False)
root.iconbitmap(default="app/tkinter/favicon.ico")

input_frame = create_frame("Input")
input_frame.pack(anchor=NW, fill=BOTH, padx=10, pady=10, expand=True)

name_label = ttk.Label(input_frame, text="Folder:")
name_label.pack(anchor=NW)

check = (root.register(is_valid_folder), "%P")
errmsg = StringVar()
folder_entry_var = StringVar()

folder_entry = ttk.Entry(master=input_frame, validate="all",
                         validatecommand=check, textvariable=folder_entry_var)
folder_entry.place(anchor=NW, relwidth=0.75)
folder_entry_var.trace_add("write", lambda name, index,
                           mode: is_valid_folder(folder_entry_var.get()))

error_label = ttk.Label(
    foreground="red", textvariable=errmsg, master=input_frame)
error_label.pack(padx=5, pady=5, anchor=NW, fill=X)


folder_button = ttk.Button(master=input_frame, text="Choose folder", padding=[
                           8, 2], command=choose_folder)
folder_button.place(anchor=NW, relx=1-0.25)


root.mainloop()
