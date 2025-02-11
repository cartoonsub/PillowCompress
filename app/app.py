from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from gui.input_frame import InputFrame
from gui.SettingsFrame import SettingsFrame
from gui.Controls import Controls
from gui.Logs import Logs

import re
import os


def center_window(root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width - root.winfo_reqwidth()) // 2) - 300
    y = ((screen_height - root.winfo_reqheight()) // 2) - 200
    root.geometry(f"800x700+{x}+{y}")


root = Tk()
root.title("Compressor")
center_window(root)
root.resizable(False, False)
root.attributes('-topmost', True)
root.iconbitmap(default="app/tkinter/favicon.ico")

for c in range(6): root.columnconfigure(index=c, weight=1)
for r in range(6): root.rowconfigure(index=r, weight=1)

input_frame = InputFrame(root, borderwidth=1, relief="solid", padding=[8, 12])
settings_frame = SettingsFrame(root, borderwidth=1, relief="solid", padding=[8, 12])
controls = Controls(root, borderwidth=1, relief="solid", padding=[8, 12])
logs = Logs(root, borderwidth=1, relief="solid", padding=[8, 12])

root.mainloop()
