from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from gui.input_frame import InputFrame
from gui.SettingsFrame import SettingsFrame
from gui.Controls import Controls
from gui.Logs import Logs
from globals import set_stop_compressing

import os
import sys

class CompressorGui:
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
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        if hasattr(sys, '_MEIPASS'):
            icon_path = os.path.join(sys._MEIPASS, 'assets/favicon.ico')
        else:
            icon_path = os.path.join(os.path.dirname(__file__), 'assets/favicon.ico')
        self.root.iconbitmap(default=icon_path)

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = ((screen_width - self.root.winfo_reqwidth()) // 2) - 300
        y = ((screen_height - self.root.winfo_reqheight()) // 2) - 300
        self.root.geometry(f"800x700+{x}+{y}")

    def set_frames(self):
        for c in range(6):
            self.root.columnconfigure(index=c, weight=1)
        for r in range(6):
            self.root.rowconfigure(index=r, weight=1)

        input_frame = InputFrame(self.root)
        settings_frame = SettingsFrame(self.root)
        logs = Logs(self.root)

        Controls(self.root, input_frame=input_frame, settings_frame=settings_frame, logs=logs)

    def on_closing(self):
        set_stop_compressing(True)
        sys.exit()

if __name__ == '__main__':
    try:
        CompressorGui()
    except Exception as e:
        print(f"An error occurred: {e}")
        input("Press Enter to exit...")

    # pyinstaller --onefile --noconsole --add-data "assets/favicon.ico;assets" app.py
    # pyinstaller --onefile --console --add-data "assets/favicon.ico;assets" app.py
