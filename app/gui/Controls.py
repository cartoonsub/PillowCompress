from tkinter import *
from tkinter import ttk
from tkinter import filedialog


class Controls(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, borderwidth=1, relief="solid", padding=[8, 12])
        self.grid(row=2, column=0, columnspan=6, rowspan=1, sticky="nsew", padx=10, pady=10)

        for c in range(3):
            self.columnconfigure(index=c, weight=1)
        for r in range(1):
            self.rowconfigure(index=r, weight=1)

        self.style = ttk.Style()
        self.style.configure('W.TButton', font=('calibri', 10, 'bold', 'underline'), foreground='gray')
        self.style.configure('G.TButton', font=('calibri', 10, 'bold', 'underline'), foreground='red')

        self.create_control_buttons()


    def create_control_buttons(self):
        self.start_button = ttk.Button(self, text='START', padding=[8, 2], command=self.start_compress, style='W.TButton')
        self.start_button.grid(row=0, column=0, sticky="nsew")

        self.pause_button = ttk.Button(self, text='PAUSE', padding=[8, 2], style='W.TButton')
        self.pause_button.grid(row=0, column=1, sticky="nsew")

        self.stop_button = ttk.Button(self, text='STOP', padding=[8, 2], style='W.TButton')
        self.stop_button.grid(row=0, column=2, sticky="nsew")

    def start_compress(self):
        self.start_button.config(state=DISABLED)
        self.start_button.configure(text='Compressing...', style='G.TButton')
        self.after(2000, self.reset_button)

    def reset_button(self):
        self.start_button.config(state=NORMAL)
        self.start_button.configure(text='START', style='W.TButton')
