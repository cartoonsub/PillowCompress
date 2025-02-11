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
        self.Processing.grid_remove()
        self.create_listbox_errors()
        self.Errors.grid_remove()
        self.create_listbox_success()
        self.Success.grid_remove()

        self.add_test_data()

    def create_logs_buttons(self):
        self.process_button = ttk.Button(self, text='Processing', padding=[8, 2], command=lambda: self.show_widget(self.Processing))
        self.process_button.grid(row=0, column=0, sticky="nsew")

        self.errors_button = ttk.Button(self, text='Errors', padding=[8, 2], command=lambda: self.show_widget(self.Errors))
        self.errors_button.grid(row=0, column=1, sticky="nsew")

        self.success_button = ttk.Button(self, text='success', padding=[8, 2], command=lambda: self.show_widget(self.Success))
        self.success_button.grid(row=0, column=2, sticky="nsew")

    def create_listbox_processings(self):
        self.Processing = Listbox(self, selectmode=MULTIPLE, height=10)
        self.Processing.grid(row=1, column=0, columnspan=3, sticky="nsew")

        self.scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=self.Processing.yview)
        self.scrollbar.grid(row=1, column=3, sticky="ns")
        self.Processing.config(yscrollcommand=self.scrollbar.set)

    def create_listbox_errors(self):
        self.Errors = Listbox(self, selectmode=MULTIPLE, height=10)
        self.Errors.grid(row=1, column=0, columnspan=3, sticky="nsew")

        self.scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=self.Errors.yview)
        self.scrollbar.grid(row=1, column=3, sticky="ns")
        self.Errors.config(yscrollcommand=self.scrollbar.set)

    def create_listbox_success(self):
        self.Success = Listbox(self, selectmode=MULTIPLE, height=10)
        self.Success.grid(row=1, column=0, columnspan=3, sticky="nsew")

        self.scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=self.Success.yview)
        self.scrollbar.grid(row=1, column=3, sticky="ns")
        self.Success.config(yscrollcommand=self.scrollbar.set)

    def show_widget(self, widget):
        self.Processing.grid_remove()
        self.Errors.grid_remove()
        self.Success.grid_remove()
        widget.grid()

    def add_test_data(self):
        for i in range(100):
            self.Processing.insert(END, f"Processing {i}")
            self.Errors.insert(END, f"Error {i}")
            self.Success.insert(END, f"Success {i}")
