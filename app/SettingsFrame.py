from tkinter import *
from tkinter import ttk
from tkinter import filedialog

import os

class SettingsFrame(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.grid(row=1, column=0, columnspan=6, rowspan=1, sticky="nsew", padx=10, pady=10)

        for c in range(6): self.columnconfigure(index=c, weight=1)
        for r in range(6): self.rowconfigure(index=r, weight=1)

        self.create_image_settings()

    def create_image_settings(self):
        label = ttk.Label(self, text="Image settings", justify="center", borderwidth=2, relief="ridge", anchor="center")
        label.grid(row=0, column=0, columnspan=3, sticky="nsew")
        
        label_quality = ttk.Label(self, text="Quality:", borderwidth=2, relief="ridge", anchor="w", justify="left")
        label_quality.grid(row=1, column=0, columnspan=2, sticky="nsew")

        label_maxwidth = ttk.Label(self, text="Max width:", borderwidth=2, relief="ridge", anchor="w", justify="left")
        label_maxwidth.grid(row=2, column=0, columnspan=2, sticky="nsew")

        label_maxheight = ttk.Label(self, text="Max height:", borderwidth=2, relief="ridge", anchor="w", justify="left")
        label_maxheight.grid(row=3, column=0, columnspan=2, sticky="nsew")
        

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
        self.skip_folders_entry.grid(row=3, column=4, sticky="nwes", rowspan=1, columnspan=2)

        skip_add_button = ttk.Button(self, text="Add folder", padding=[8, 2], command=self.add_skip_folder)
        skip_add_button.grid(row=4, column=4, sticky="we", columnspan=1)

        skip_delete_button = ttk.Button(self, text="Delete folder", padding=[8, 2], command=self.delete_skip_folder)
        skip_delete_button.grid(row=4, column=5, sticky="we", columnspan=1)
        
