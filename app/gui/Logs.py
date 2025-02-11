from tkinter import *
from tkinter import ttk
from tkinter import filedialog

import os


class Logs(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.grid(row=3, column=0, columnspan=6, rowspan=1,
                  sticky="nsew", padx=10, pady=10)

        for c in range(3): self.columnconfigure(index=c, weight=1)
        for r in range(2): self.rowconfigure(index=r, weight=1)

        self.create_logs_buttons()
        self.create_logslist()

    def create_logs_buttons(self):
        self.process_button = ttk.Button(self, text='Processing', padding=[8, 2])
        self.process_button.grid(row=0, column=0, sticky="nsew")

        self.errors_button = ttk.Button(self, text='Errors', padding=[8, 2])
        self.errors_button.grid(row=0, column=1, sticky="nsew")

        self.success_button = ttk.Button(self, text='success', padding=[8, 2])
        self.success_button.grid(row=0, column=2, sticky="nsew")

    def create_logslist(self):
        self.logs_listbox = Listbox(self, selectmode=SINGLE, height=10)
        self.logs_listbox.grid(row=1, column=0, columnspan=3, sticky="nsew")

        self.scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=self.logs_listbox.yview)
        self.scrollbar.grid(row=1, column=3, sticky="ns")
        self.logs_listbox.config(yscrollcommand=self.scrollbar.set)