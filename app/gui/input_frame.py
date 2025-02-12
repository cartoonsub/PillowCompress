from tkinter import *
from tkinter import ttk
from tkinter import filedialog

import os

class InputFrame(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.grid(row=0, column=0, columnspan=6, rowspan=1, sticky="nsew", padx=10, pady=10)

        for c in range(6): self.columnconfigure(index=c, weight=1)
        for r in range(6): self.rowconfigure(index=r, weight=1)

        self.create_folder_input()
        self.create_listbox()

    def choose_folder(self):
        folder_path = filedialog.askdirectory()
        if not folder_path:
            self.errmsg.set("Please enter a folder path")

        if not os.path.exists(folder_path):
            self.errmsg.set("Folder does not exist: " + folder_path)

        self.folder_entry.delete(0, END)
        self.folder_entry.insert(0, folder_path)

    def is_valid_folder(self, folder_path):
        if not folder_path:
            self.errmsg.set("Please enter a folder path")
            self.error_label.config(foreground="red")

        if os.path.exists(folder_path):
            self.errmsg.set("Correct folder path")
            self.error_label.config(foreground="green")
        else:
            self.errmsg.set("Folder does not exist: " + folder_path)
            self.error_label.config(foreground="red")

        return True

    def create_folder_input(self):
        self.errmsg = StringVar()
        self.folder_entry_var = StringVar()

        self.name_label = ttk.Label(self, text="Folder:")
        self.name_label.grid(row=0, column=0, sticky="nw", pady=0)

        self.error_label = ttk.Label(self, foreground="red", textvariable=self.errmsg)
        self.error_label.grid(row=0, column=2, sticky='nw', pady=0)

        self.check = (self.register(self.is_valid_folder), "%P")

        self.folder_entry = ttk.Entry(self, validate="all", validatecommand=self.check, textvariable=self.folder_entry_var)
        self.folder_entry.grid(row=1, column=0, columnspan=4, sticky="ew")
       
        self.folder_entry_var.trace_add("write", lambda name, index, mode: self.is_valid_folder(self.folder_entry_var.get()))

        self.folder_button = ttk.Button(self, text="Choose folder", padding=[8, 2], command=self.choose_folder)
        self.folder_button.grid(row=1, column=4, sticky="ew")

    def create_listbox(self):
        skip_folders_default = ["Done"] # брать потом из конфига
        self.skip_folders = StringVar(value=skip_folders_default)

        self.skip_label = ttk.Label(self, text="Skip folders:")
        self.skip_label.grid(row=2, column=0, sticky="nw", pady=0)

        self.grid_rowconfigure(3, weight=0)
        self.grid_columnconfigure(3, weight=0)
        self.grid_columnconfigure(4, weight=0)

        self.skip_folders_listbox = Listbox(self, listvariable=self.skip_folders, height=5, yscrollcommand=True)
        self.skip_folders_listbox.grid(row=3, column=0, sticky="nwes", columnspan=4, rowspan=2)

        self.skip_folders_entry = ttk.Entry(self)
        self.skip_folders_entry.bind("<Return>", lambda e: self.add_skip_folder())
        self.skip_folders_entry.grid(row=3, column=4, sticky="nwes", rowspan=1, columnspan=2)

        skip_add_button = ttk.Button(self, text="Add folder", padding=[8, 2], command=self.add_skip_folder)
        skip_add_button.grid(row=4, column=4, sticky="nw", columnspan=1)

        skip_delete_button = ttk.Button(self, text="Delete folder", padding=[8, 2], command=self.delete_skip_folder)
        skip_delete_button.grid(row=4, column=5, sticky="ne", columnspan=1)

    def delete_skip_folder(self):
        selection = self.skip_folders_listbox.curselection()
        if not selection:
            return

        self.skip_folders_listbox.delete(selection[0])

    def add_skip_folder(self):
        new_skip_folder = self.skip_folders_entry.get()
        if not new_skip_folder:
            return
        self.skip_folders_listbox.insert(0, new_skip_folder)
        self.skip_folders_entry.delete(0, END)