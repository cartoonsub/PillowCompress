from tkinter import ttk, filedialog, StringVar, END, NW, BOTH, X
import os

class InputFrame(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.pack(anchor=NW, fill=BOTH, padx=10, pady=10, expand=True)

        self.create_folder_input()

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
        self.name_label.pack(anchor=NW)

        self.check = (self.register(self.is_valid_folder), "%P")

        self.folder_entry = ttk.Entry(self, validate="all",
                                      validatecommand=self.check, textvariable=self.folder_entry_var)
        self.folder_entry.place(anchor=NW, relwidth=0.75)
        self.folder_entry_var.trace_add("write", lambda name, index,
                                        mode: self.is_valid_folder(self.folder_entry_var.get()))

        self.error_label = ttk.Label(
            self, foreground="red", textvariable=self.errmsg)
        self.error_label.pack(padx=5, pady=5, anchor=NW, fill=X)

        self.folder_button = ttk.Button(self, text="Choose folder", padding=[
                                        8, 2], command=self.choose_folder)
        self.folder_button.place(anchor=NW, relx=1-0.25)
