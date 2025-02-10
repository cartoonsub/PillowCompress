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
        
        self.label_quality = ttk.Label(self, text="Quality:", borderwidth=2, relief="ridge", anchor="w", justify="left")
        self.label_quality.grid(row=1, column=0, columnspan=2, sticky="nsew")

        self.label_maxwidth = ttk.Label(self, text="Max width:", borderwidth=2, relief="ridge", anchor="w", justify="left")
        self.label_maxwidth.grid(row=2, column=0, columnspan=2, sticky="nsew")

        self.label_maxheight = ttk.Label(self, text="Max height:", borderwidth=2, relief="ridge", anchor="w", justify="left")
        self.label_maxheight.grid(row=3, column=0, columnspan=2, sticky="nsew")
        
        self.quality = StringVar(value=90) # брать потом из конфига
        self.check_quality = (self.register(self.change_quality), "%P")
        self.quality.trace_add("write", lambda name, index, mode: self.change_quality())
        
        self.quality_spinbox = ttk.Spinbox(self, from_=1, to=100, textvariable=self.quality, command=self.change_quality, validatecommand=self.check_quality)
        self.quality_spinbox.grid(row=1, column=2, columnspan=1, sticky="nw")
        self.quality_spinbox.set(90)

        self.maxwidth = StringVar(value=1920) # брать потом из конфига
        self.check_maxwidth = (self.register(self.change_maxwidth), "%P")
        self.maxwidth.trace_add("write", lambda name, index, mode: self.change_maxwidth())
        
        self.maxwidth_spinbox = ttk.Spinbox(self, from_=1, to=10000, textvariable=self.maxwidth, command=self.change_maxwidth, validatecommand=self.check_maxwidth)
        self.maxwidth_spinbox.grid(row=2, column=2, columnspan=1, sticky="nw")
        self.maxwidth_spinbox.set(1920)

        self.maxheight = StringVar(value=1080) # брать потом из конфига
        self.check_maxheight = (self.register(self.change_maxheight), "%P")
        self.maxheight.trace_add("write", lambda name, index, mode: self.change_maxheight())

        self.maxheight_spinbox = ttk.Spinbox(self, from_=1, to=10000, textvariable=self.maxheight, command=self.change_maxheight, validatecommand=self.check_maxheight)
        self.maxheight_spinbox.grid(row=3, column=2, columnspan=1, sticky="nw")
        self.maxheight_spinbox.set(1080)
    
    def change_quality(self):
        try:
            value = int(self.quality_spinbox.get())
        except ValueError:
            self.quality_spinbox.delete(0, END)
            self.quality_spinbox.insert(0, 90)
            return

        if value > 100 or value < 1:
            self.quality_spinbox.delete(0, END)
            self.quality_spinbox.insert(0, 90)
            return

        self.quality.set(value)
        self.label_quality["text"] = f"Quality: {value}"

    def change_maxwidth(self):
        try:
            value = int(self.maxwidth_spinbox.get())
        except ValueError:
            self.maxwidth_spinbox.delete(0, END)
            self.maxwidth_spinbox.insert(0, 1920)
            return

        if value > 10000 or value < 1:
            self.maxwidth_spinbox.delete(0, END)
            self.maxwidth_spinbox.insert(0, 1920)
            return

        self.maxwidth.set(value)
        self.label_maxwidth["text"] = f"Max width: {value}"

    def change_maxheight(self):
        try:
            value = int(self.maxheight_spinbox.get())
        except ValueError:
            self.maxheight_spinbox.delete(0, END)
            self.maxheight_spinbox.insert(0, 1080)
            return

        if value > 10000 or value < 1:
            self.maxheight_spinbox.delete(0, END)
            self.maxheight_spinbox.insert(0, 1080)
            return

        self.maxheight.set(value)
        self.label_maxheight["text"] = f"Max height: {value}"

