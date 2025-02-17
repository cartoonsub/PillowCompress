from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from Compressor import Compressor

class Controls(ttk.Frame):
    def __init__(self, master, input_frame, settings_frame, logs, *args, **kwargs):
        super().__init__(master, borderwidth=1, relief="solid", padding=[8, 12])
        self.input_frame = input_frame
        self.settings_frame = settings_frame
        self.logs = logs

        self.init_gui()
        self.create_control_buttons()

    def init_gui(self) -> None:
        self.grid(row=2, column=0, columnspan=6, rowspan=1, sticky="nsew", padx=10, pady=10)
        for c in range(3):
            self.columnconfigure(index=c, weight=1)
        for r in range(1):
            self.rowconfigure(index=r, weight=1)
        self.style = ttk.Style()
        self.style.configure('W.TButton', font=('calibri', 10, 'bold', 'underline'), foreground='gray')
        self.style.configure('G.TButton', font=('calibri', 10, 'bold', 'underline'), foreground='red')

    def create_control_buttons(self):
        self.start_button = ttk.Button(self, text='START', padding=[8, 2], command=self.start_compress, style='W.TButton')
        self.start_button.grid(row=0, column=0, sticky="nsew")

        self.pause_button = ttk.Button(self, text='PAUSE', padding=[8, 2], style='W.TButton')
        self.pause_button.grid(row=0, column=1, sticky="nsew")

        self.stop_button = ttk.Button(self, text='STOP', padding=[8, 2], style='W.TButton', command=self.reset_button)
        self.stop_button.grid(row=0, column=2, sticky="nsew")

    def start_compress(self):
        self.start_button.config(state=DISABLED)
        self.start_button.configure(text='Preparing...', style='G.TButton')
        
        params = self.get_params()
        self.start_button.configure(text='Compressing...', style='G.TButton')

        result = Compressor(params).run()
        if result:
            self.start_button.configure(text='DONE/RESTART', style='G.TButton')
        else:
            self.start_button.configure(text='ERROR/RESTART', style='G.TButton')

    def reset_button(self):
        self.start_button.config(state=NORMAL)
        self.start_button.configure(text='START', style='W.TButton')

    def get_params(self):
        input_param = self.input_frame.get_params()
        settings_param = self.settings_frame.get_params()
        params = {
            'folder': input_param['folder'],
            'skip_folders': input_param['skip_folders'],
            'new_folder': input_param['new_folder'],
            'img_params': {
                'quality': settings_param['img_quality'],
                'maxwidth': settings_param['img_maxwidth'],
                'maxheight': settings_param['img_maxheight'],
            },
            'video_params': {
                'bitrate': settings_param['video_bitrate'],
                'audio_bitrate': settings_param['audio_bitrate'],
                'maxwidth': settings_param['video_maxwidth'],
                'maxheight': settings_param['video_maxheight'],
            }
        }

        return params

if __name__ == '__main__':
    pass
