from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from functools import partial
import os

class InputFrame(ttk.Frame):
    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs, borderwidth=1, relief="solid", padding=[8, 12])
        self.grid(row=0, column=0, columnspan=6, rowspan=1, sticky="nsew", padx=10, pady=10)

        for c in range(6):
            self.columnconfigure(index=c, weight=1)
        for r in range(6):
            self.rowconfigure(index=r, weight=1)

        self.init_params()
        self.create_folder_input()
        self.create_new_folder_input()
        self.create_listbox()

    def init_params(self) -> None:
        self.folder = StringVar()
        self.new_folder = StringVar()
        skip_folders_default = ["Done"]  # брать потом из конфига
        self.skip_folders = StringVar(value=skip_folders_default)

    def get_params(self) -> dict:
        skip_folders_list = self.skip_folders_listbox.get(0, END)
        return {
            'folder': self.folder.get(),
            'skip_folders': [folder for folder in skip_folders_list],
            'new_folder': self.new_folder.get(),
        }

    def create_folder_input(self) -> None:
        errmsg = StringVar()

        name_label = ttk.Label(self, text="Folder:")
        name_label.grid(row=0, column=0, sticky="nw", pady=0)

        error_label = ttk.Label(self, foreground="red", textvariable=errmsg)
        error_label.grid(row=0, column=2, sticky='nw', pady=0)

        checker = self.register(partial(self.is_valid_folder, error_label=error_label, errmsg=errmsg))
        folder_entry = ttk.Entry(self, validate="all", validatecommand=(checker, "%P"), textvariable=self.folder)
        folder_entry.grid(row=1, column=0, columnspan=2, sticky="ew")

        self.folder.trace_add("write", lambda name, index, mode: self.is_valid_folder(self.folder.get(), error_label, errmsg))

        folder_button = ttk.Button(self, text="Choose folder", padding=[8, 2], command=partial(self.choose_folder, errmsg, folder_entry))
        folder_button.grid(row=1, column=2, sticky="ew")

    def create_new_folder_input(self) -> None:
        errmsg = StringVar()

        name_label = ttk.Label(self, text="New folder:")
        name_label.grid(row=0, column=3, sticky="nw", pady=0)

        error_label = ttk.Label(self, foreground="red", textvariable=errmsg)
        error_label.grid(row=0, column=5, sticky='nw', pady=0)

        checker = self.register(partial(self.is_posible_folder, errmsg=errmsg, error_label=error_label))
        folder_entry = ttk.Entry(self, validate="all", validatecommand=(checker, "%P"), textvariable=self.new_folder)
        folder_entry.grid(row=1, column=3, columnspan=2, sticky="ew")

        self.new_folder.trace_add("write", lambda name, index, mode: self.is_posible_folder(err_msg=errmsg, error_label=error_label))

        folder_button = ttk.Button(self, text="Confirm", padding=[8, 2], command=partial(self.is_posible_folder, errmsg=errmsg, error_label=error_label))
        folder_button.grid(row=1, column=5, sticky="ew")

    def is_valid_folder(self, folder_path, error_label, errmsg) -> bool:
        if not folder_path:
            errmsg.set("Please enter a folder path")
            error_label.config(foreground="red")
            return False

        if os.path.exists(folder_path):
            errmsg.set("Correct folder path")
            error_label.config(foreground="green")
        else:
            errmsg.set("Folder does not exist: " + folder_path)
            error_label.config(foreground="red")

        return True

    def is_posible_folder(self, errmsg, error_label) -> bool:
        if not self.new_folder.get():
            return False

        if os.path.exists(self.new_folder.get()):
            return True

        try:
            os.makedirs(self.new_folder.get())
            os.rmdir(self.new_folder.get())
            errmsg.set("Folder can be created")
            error_label.config(foreground="green")
            return True
        except Exception as e:
            errmsg.set(f"Cannot create folder: {e}")
            error_label.config(foreground="red")
        return False

    def choose_folder(self, errmsg, entry) -> None:
        entry.delete(0, END)
        self.folder.set("")
        folder_path = filedialog.askdirectory()
        if not folder_path:
            errmsg.set("Please enter a folder path")

        if not os.path.exists(folder_path):
            errmsg.set("Folder does not exist: " + folder_path)

        entry.delete(0, END)
        entry.insert(0, folder_path)

    def create_listbox(self) -> None:
        skip_label = ttk.Label(self, text="Skip folders:")
        skip_label.grid(row=2, column=0, sticky="nw", pady=0)

        self.skip_folders_listbox = Listbox(self, listvariable=self.skip_folders, height=5, yscrollcommand=True)
        self.skip_folders_listbox.grid(row=3, column=0, sticky="nwes", columnspan=4, rowspan=2)

        self.skip_folders_entry = ttk.Entry(self)
        self.skip_folders_entry.bind("<Return>", lambda e: self.add_skip_folder())
        self.skip_folders_entry.grid(row=3, column=4, sticky="nwe", rowspan=1, columnspan=2)
        self.grid_rowconfigure(3, weight=0)

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
