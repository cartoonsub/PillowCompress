from tkinter import *
from tkinter import ttk

from logsBridge import get_logs
from globals import is_compressing

class Logs(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs, borderwidth=1, relief="solid", padding=[8, 12])
        self.grid(row=3, column=0, columnspan=6, rowspan=1,
                  sticky="nsew", padx=10, pady=10)

        for c in range(3): self.columnconfigure(index=c, weight=1)
        for r in range(2): self.rowconfigure(index=r, weight=1)

        self.create_logs_buttons()
        self.create_listbox_processings()
        self.create_listbox_errors()
        self.create_listbox_success()

        self.Errors.grid_remove()
        self.Success.grid_remove()
        self.scrollbar_errors.grid_remove()
        self.scrollbar_success.grid_remove()

        self.start_listening()

    def create_logs_buttons(self):
        process_button = ttk.Button(self, text='Processing', padding=[8, 2], command=lambda: self.show_widget(self.Processing, self.scrollbar_processing))
        process_button.grid(row=0, column=0, sticky="nsew")

        errors_button = ttk.Button(self, text='Errors', padding=[8, 2], command=lambda: self.show_widget(self.Errors, self.scrollbar_errors))
        errors_button.grid(row=0, column=1, sticky="nsew")

        success_button = ttk.Button(self, text='success', padding=[8, 2], command=lambda: self.show_widget(self.Success, self.scrollbar_success))
        success_button.grid(row=0, column=2, sticky="nsew")

        clear_button = ttk.Button(self, text='Clear', padding=[8, 2], command=self.clear_logs)
        clear_button.grid(row=2, column=0, columnspan=1, sticky="nsew")

    def create_listbox_processings(self):
        self.Processing = Listbox(self, selectmode=MULTIPLE, height=6)
        self.Processing.grid(row=1, column=0, columnspan=3, sticky="nsew")

        self.scrollbar_processing = ttk.Scrollbar(self, orient=VERTICAL, command=self.Processing.yview)
        self.scrollbar_processing.grid(row=1, column=3, sticky="ns")
        self.Processing.config(yscrollcommand=self.scrollbar_processing.set)

    def create_listbox_errors(self):
        self.Errors = Listbox(self, selectmode=MULTIPLE, height=6)
        self.Errors.grid(row=1, column=0, columnspan=3, sticky="nsew")

        self.scrollbar_errors = ttk.Scrollbar(self, orient=VERTICAL, command=self.Errors.yview)
        self.scrollbar_errors.grid(row=1, column=3, sticky="ns")
        self.Errors.config(yscrollcommand=self.scrollbar_errors.set)

    def create_listbox_success(self):
        self.Success = Listbox(self, selectmode=MULTIPLE, height=6)
        self.Success.grid(row=1, column=0, columnspan=3, sticky="nsew")

        self.scrollbar_success = ttk.Scrollbar(self, orient=VERTICAL, command=self.Success.yview)
        self.scrollbar_success.grid(row=1, column=3, sticky="ns")
        self.Success.config(yscrollcommand=self.scrollbar_success.set)

    def show_widget(self, widget, scrollbar):
        self.Processing.grid_remove()
        self.Errors.grid_remove()
        self.Success.grid_remove()

        self.scrollbar_errors.grid_remove()
        self.scrollbar_processing.grid_remove()
        self.scrollbar_success.grid_remove()

        widget.grid()
        scrollbar.grid()

    def clear_logs(self):
        self.Processing.delete(0, END)
        self.Errors.delete(0, END)
        self.Success.delete(0, END)

    def set_logs(self, logs):
        for type, log in logs.items():
            if type == 'processing':
                class_ = self.Processing
            elif type == 'error':
                class_ = self.Errors
            elif type == 'done':
                class_ = self.Success
            else: 
                print('Error: unknown log type')
                continue

            for text in log:
                class_.insert(END, text)

    def add_test_data(self):
        logs = {
            'processing': [],
            'error': [],
            'done': []
        }
        for i in range(100):
            logs['processing'].append(f"Processing {i}")
            logs['error'].append(f"Error {i}")
            logs['done'].append(f"Success {i}")

        self.set_logs(logs)

    def start_listening(self):
        current_logs = get_logs()
        if current_logs:
            self.set_logs(current_logs)
        self.after(1000, self.start_listening)

if __name__ == '__main__':
    pass
