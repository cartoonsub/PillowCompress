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
        self.create_listbox_processings()
        self.create_listbox_errors()
        self.create_listbox_success()

    def create_logs_buttons(self):
        self.process_button = ttk.Button(self, text='Processing', padding=[8, 2], command=lambda: self.hide_widget(self.Processing))
        self.process_button.grid(row=0, column=0, sticky="nsew")

        self.errors_button = ttk.Button(self, text='Errors', padding=[8, 2])
        self.errors_button.grid(row=0, column=1, sticky="nsew")

        self.success_button = ttk.Button(self, text='success', padding=[8, 2])
        self.success_button.grid(row=0, column=2, sticky="nsew")

    def create_listbox_processings(self):
        self.Processing = Listbox(self, selectmode=MULTIPLE, height=10, bg='black', fg='gray')
        self.Processing.grid(row=1, column=0, columnspan=3, sticky="nsew")

        self.scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=self.Processing.yview)
        self.scrollbar.grid(row=1, column=3, sticky="ns")
        self.Processing.config(yscrollcommand=self.scrollbar.set)

    def create_listbox_errors(self):
        self.Errors = Listbox(self, selectmode=MULTIPLE, height=10, bg='black', fg='red')
        self.Errors.grid(row=1, column=0, columnspan=3, sticky="nsew")

        self.scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=self.Errors.yview)
        self.scrollbar.grid(row=1, column=3, sticky="ns")
        self.Errors.config(yscrollcommand=self.scrollbar.set)

    def create_listbox_success(self):
        self.Success = Listbox(self, selectmode=MULTIPLE, height=10, bg='black', fg='green')
        self.Success.grid(row=1, column=0, columnspan=3, sticky="nsew")

        self.scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=self.Success.yview)
        self.scrollbar.grid(row=1, column=3, sticky="ns")
        self.Success.config(yscrollcommand=self.scrollbar.set)

    def hide_widget(self, widget):
        widget.grid_remove()

    def show_widget(self, widget):
        widget.grid()
