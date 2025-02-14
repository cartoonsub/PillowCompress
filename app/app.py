from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from gui.input_frame import InputFrame
from gui.SettingsFrame import SettingsFrame
from gui.Controls import Controls
from gui.Logs import Logs

class Compressor():
    def __init__(self):
        self.init_gui()
        self.set_frames()
        self.root.mainloop()

    def init_gui(self):
        self.root = Tk()
        self.root.title("Compressor")
        self.center_window()
        self.root.resizable(False, False)
        self.root.attributes('-topmost', True)
        self.root.iconbitmap(default="app/assets/favicon.ico")

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = ((screen_width - self.root.winfo_reqwidth()) // 2) - 300
        y = ((screen_height - self.root.winfo_reqheight()) // 2) - 300
        self.root.geometry(f"800x700+{x}+{y}")

    def set_frames(self):
        for c in range(6): self.root.columnconfigure(index=c, weight=1)
        for r in range(6): self.root.rowconfigure(index=r, weight=1)

        self.input_frame = InputFrame(self.root, borderwidth=1, relief="solid", padding=[8, 12])
        self.settings_frame = SettingsFrame(self.root, borderwidth=1, relief="solid", padding=[8, 12])
        self.controls = Controls(self.root, borderwidth=1, relief="solid", padding=[8, 12])
        self.logs = Logs(self.root, borderwidth=1, relief="solid", padding=[8, 12])


if __name__ == '__main__':
    Compressor()
