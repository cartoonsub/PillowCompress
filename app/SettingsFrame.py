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
        self.create_video_setting()

    def create_image_settings(self):
        label = ttk.Label(self, text="Image settings", justify="center", borderwidth=2, relief="ridge", anchor="center")
        label.grid(row=0, column=0, columnspan=2, sticky="nsew")
        
        self.label_quality = ttk.Label(self, text="Quality:", borderwidth=2, relief="ridge", anchor="w", justify="left")
        self.label_quality.grid(row=1, column=0, columnspan=2, sticky="nsew")

        self.label_maxwidth_image = ttk.Label(self, text="Max width:", borderwidth=2, relief="ridge", anchor="w", justify="left")
        self.label_maxwidth_image.grid(row=2, column=0, columnspan=2, sticky="nsew")

        self.label_maxheight_image = ttk.Label(self, text="Max height:", borderwidth=2, relief="ridge", anchor="w", justify="left")
        self.label_maxheight_image.grid(row=3, column=0, columnspan=2, sticky="nsew")
        
        self.quality = StringVar(value=90) # брать потом из конфига
        self.check_quality = (self.register(self.change_value), "%P")
        self.quality.trace_add("write", lambda name, index, mode: self.change_value(self.quality_spinbox, self.label_quality, self.quality, [1, 100], "Quality"))
        
        self.quality_spinbox = ttk.Spinbox(self, from_=1, to=100, textvariable=self.quality, validatecommand=self.check_quality)
        self.quality_spinbox.grid(row=1, column=2, columnspan=1, sticky="nw")
        self.quality_spinbox.set(90)

        self.maxwidth = StringVar(value=1920) # брать потом из конфига
        self.check_maxwidth = (self.register(self.change_value), "%P")
        self.maxwidth.trace_add("write", lambda name, index, mode: self.change_value(self.maxwidth_spinbox, self.label_maxwidth_image, self.maxwidth, [1, 10000], "Max width"))
        
        self.maxwidth_spinbox = ttk.Spinbox(self, from_=1, to=10000, textvariable=self.maxwidth, validatecommand=self.check_maxwidth)
        self.maxwidth_spinbox.grid(row=2, column=2, columnspan=1, sticky="nw")
        self.maxwidth_spinbox.set(1920)

        self.maxheight = StringVar(value=1080) # брать потом из конфига
        self.check_maxheight = (self.register(self.change_value), "%P")
        self.maxheight.trace_add("write", lambda name, index, mode: self.change_value(self.maxheight_spinbox, self.label_maxheight_image, self.maxheight, [1, 10000], "Max height"))

        self.maxheight_spinbox = ttk.Spinbox(self, from_=1, to=10000, textvariable=self.maxheight, validatecommand=self.check_maxheight)
        self.maxheight_spinbox.grid(row=3, column=2, columnspan=1, sticky="nw")
        self.maxheight_spinbox.set(1080)
    
    def change_value(self, spinbox, label, var, limits, label_text):
        try:
            value = int(spinbox.get())
        except ValueError:
            spinbox.delete(0, END)
            spinbox.insert(0, spinbox.get())
            return

        if value > limits[1] or value < limits[0]:
            var.set('Exceeds limits: ' + str(limits[0]) + ' - ' + str(limits[1]))
            return

        var.set(value)
        label["text"] = f"{label_text}: {value}"

    def create_video_setting(self):
        label = ttk.Label(self, text="Video settings", justify="center", borderwidth=2, relief="ridge", anchor="center")
        label.grid(row=0, column=3, columnspan=2, sticky="nsew")

        self.label_bitrate_video = ttk.Label(self, text="Bitrate video:", borderwidth=2, relief="ridge", anchor="w", justify="left")
        self.label_bitrate_video.grid(row=1, column=3, columnspan=2, sticky="nsew")

        self.label_bitrate_audio = ttk.Label(self, text="Bitrate audio:", borderwidth=2, relief="ridge", anchor="w", justify="left")
        self.label_bitrate_audio.grid(row=2, column=3, columnspan=2, sticky="nsew")

        self.label_maxwidth_video = ttk.Label(self, text="Max width:", borderwidth=2, relief="ridge", anchor="w", justify="left")
        self.label_maxwidth_video.grid(row=3, column=3, columnspan=2, sticky="nsew")

        self.label_maxheight_video = ttk.Label(self, text="Max height:", borderwidth=2, relief="ridge", anchor="w", justify="left")
        self.label_maxheight_video.grid(row=4, column=3, columnspan=2, sticky="nsew")


        self.bitrate_video = StringVar(value=5000) # брать потом из конфига
        self.check_bitrate_video = (self.register(self.change_value), "%P")
        self.bitrate_video.trace_add("write", lambda name, index, mode: self.change_value(self.bitrate_video_spinbox, self.label_bitrate_video, self.bitrate_video, [1, 10000], "Bitrate video"))

        self.bitrate_video_spinbox = ttk.Spinbox(self, from_=1, to=10000, textvariable=self.bitrate_video, validatecommand=self.check_bitrate_video)
        self.bitrate_video_spinbox.grid(row=1, column=5, columnspan=1, sticky="nw")
        self.bitrate_video_spinbox.set(5000)

        self.bitrate_audio = StringVar(value=320) # брать потом из конфига
        self.check_bitrate_audio = (self.register(self.change_value), "%P")
        self.bitrate_audio.trace_add("write", lambda name, index, mode: self.change_value(self.bitrate_audio_spinbox, self.label_bitrate_audio, self.bitrate_audio, [1, 1000], "Bitrate audio"))

        self.bitrate_audio_spinbox = ttk.Spinbox(self, from_=1, to=1000, textvariable=self.bitrate_audio, validatecommand=self.check_bitrate_audio)
        self.bitrate_audio_spinbox.grid(row=2, column=5, columnspan=1, sticky="nw")
        self.bitrate_audio_spinbox.set(320)

        self.maxwidth_video = StringVar(value=1920) # брать потом из конфига
        self.check_maxwidth_video = (self.register(self.change_value), "%P")
        self.maxwidth_video.trace_add("write", lambda name, index, mode: self.change_value(self.maxwidth_video_spinbox, self.label_maxwidth_video, self.maxwidth_video, [1, 10000], "Max width"))

        self.maxwidth_video_spinbox = ttk.Spinbox(self, from_=1, to=10000, textvariable=self.maxwidth_video, validatecommand=self.check_maxwidth_video)
        self.maxwidth_video_spinbox.grid(row=3, column=5, columnspan=1, sticky="nw")
        self.maxwidth_video_spinbox.set(1920)

        self.maxheight_video = StringVar(value=1080) # брать потом из конфига
        self.check_maxheight_video = (self.register(self.change_value), "%P")
        self.maxheight_video.trace_add("write", lambda name, index, mode: self.change_value(self.maxheight_video_spinbox, self.label_maxheight_video, self.maxheight_video, [1, 10000], "Max height"))

        self.maxheight_video_spinbox = ttk.Spinbox(self, from_=1, to=10000, textvariable=self.maxheight_video, validatecommand=self.check_maxheight_video)
        self.maxheight_video_spinbox.grid(row=4, column=5, columnspan=1, sticky="nw")
        self.maxheight_video_spinbox.set(1080)
