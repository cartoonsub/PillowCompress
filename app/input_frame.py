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
        # self.create_listbox()

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

        self.check = (self.register(self.is_valid_folder), "%P")

        self.folder_entry = ttk.Entry(self, validate="all", validatecommand=self.check, textvariable=self.folder_entry_var)
        self.folder_entry.grid(row=1, column=5, sticky="nw")
        # self.folder_entry_var.trace_add("write", lambda name, index,
        #                                 mode: self.is_valid_folder(self.folder_entry_var.get()))

        # self.error_label = ttk.Label(self, foreground="red", textvariable=self.errmsg)
        # self.error_label.pack(padx=5, pady=5, anchor=NW)

        # self.folder_button = ttk.Button(self, text="Choose folder", padding=[8, 2], command=self.choose_folder)
        # self.folder_button.place(anchor=NW, relx=0.25)

    def create_listbox(self):
        skip_folders_default = ["Done"]
        self.skip_folders = StringVar(value=skip_folders_default)

        self.skip_folders_entry = ttk.Entry(self)
        self.skip_folders_entry.place(anchor=NW, relwidth=0.75)

        skip_add_button = ttk.Button(self, text="Add folder", padding=[8, 2], command=self.add_skip_folder)

        self.skip_folders_listbox = Listbox(self, listvariable=self.skip_folders)
        self.skip_folders_listbox.place(anchor=NW, relwidth=0.75)

    # def delete():
    #     selection = languages_listbox.curselection()
    #     # мы можем получить удаляемый элемент по индексу
    #     # selected_language = languages_listbox.get(selection[0])
    #     languages_listbox.delete(selection[0])
 
 
    def add_skip_folder(self):
        self.new_skip_folder = self.skip_folders_entry.get()
        self.skip_folders_listbox.insert(0, self.new_skip_folder)