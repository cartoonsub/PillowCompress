from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from Compressor import Compressor
import threading
from globals import set_stop_compressing, set_pause_compressing, set_is_compressing, is_compressing

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
        self.style.configure('G.TButton', font=('calibri', 10, 'bold', 'underline'), foreground='green')
        self.style.configure('R.TButton', font=('calibri', 10, 'bold', 'underline'), foreground='red')

    def create_control_buttons(self):
        self.start_button = ttk.Button(self, text='START', padding=[8, 2], command=self.start_compress, style='W.TButton')
        self.start_button.grid(row=0, column=0, sticky="nsew")

        self.pause_button = ttk.Button(self, text='PAUSE', padding=[8, 2], style='W.TButton', command=self.pause_compress)
        self.pause_button.grid(row=0, column=1, sticky="nsew")

        self.stop_button = ttk.Button(self, text='STOP', padding=[8, 2], style='W.TButton', command=self.stop_compress)
        self.stop_button.grid(row=0, column=2, sticky="nsew")

    def start_compress(self):
        set_stop_compressing(False)
        set_pause_compressing(False)
        if is_compressing:
            self.buttons_switch('start_processing')
            return

        self.buttons_switch('start')


        def compress():
            set_is_compressing(True)
            params = self.get_params()
            result = Compressor(params).run()
    
            if result:
                self.buttons_switch('finish', styleType='G.TButton')
            else:
                self.buttons_switch('error', styleType='R.TButton')
            self.start_button.config(state=NORMAL)
            set_is_compressing(False)

        self.thread = threading.Thread(target=compress)
        self.thread.start()

    def stop_compress(self):
        set_stop_compressing(True)
        self.buttons_switch('stop')
        self.check_thread_status()

    def check_thread_status(self):
        if self.thread.is_alive():
            self.buttons_switch('stop_processing')
            self.after(100, self.check_thread_status)
        else:
            self.buttons_switch('stop')

    def pause_compress(self):
        set_pause_compressing(True)
        self.buttons_switch('pause')

    def buttons_switch(self, state, styleType='W.TButton'):
        if state == 'start':
            self.start_button.config(state=DISABLED, style=styleType, text='Working...')
            self.pause_button.config(state=NORMAL, text='PAUSE', style=styleType)
            self.stop_button.config(state=NORMAL, text='STOP', style=styleType)
            return
        
        if state == 'start_processing':
            self.start_button.config(state=DISABLED, text='Working...', style=styleType)
            self.pause_button.config(state=NORMAL, text='PAUSE', style=styleType)
            self.stop_button.config(state=NORMAL, text='STOP', style=styleType)
            self.after(3000, self.buttons_switch, 'start')
            return

        if state == 'pause':
            self.start_button.config(state=NORMAL, text='RESUME', style=styleType)
            self.pause_button.config(state=DISABLED, text='PAUSED', style=styleType)
            self.stop_button.config(state=NORMAL, text='STOP', style=styleType)
            return

        if state == 'stop':
            self.start_button.config(state=NORMAL, text='RESTART', style=styleType)
            self.pause_button.config(state=DISABLED, text='PAUSE', style=styleType)
            self.stop_button.config(state=DISABLED, text='STOPPED', style=styleType)
            return

        if state == 'stop_processing':
            self.start_button.config(state=DISABLED, text='STOPPING...', style=styleType)
            self.pause_button.config(state=DISABLED, text='PAUSE', style=styleType)
            self.stop_button.config(state=DISABLED, text='STOP', style=styleType)
            return

        if state == 'finish':
            self.start_button.config(state=NORMAL, text='DONE/RESTART', style=styleType)
            self.pause_button.config(state=DISABLED, text='PAUSE', style=styleType)
            self.stop_button.config(state=DISABLED, text='STOP', style=styleType)
            return
        
        if state == 'error':
            self.start_button.config(state=NORMAL, text='ERROR/RESTART', style=styleType)
            self.pause_button.config(state=DISABLED, text='PAUSE', style=styleType)
            self.stop_button.config(state=DISABLED, text='STOP', style=styleType)
            return

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
