import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
import sys
from PySide6.QtWidgets import (
    QApplication, 
    QWidget, 
    QFileDialog, 
    QGridLayout,
    QPushButton, 
    QLabel,
    QListWidget,
    QLineEdit
)
from pathlib import Path
from PySide6.QtCore import Qt, Signal

class MyWidget(QtWidgets.QWidget):
    clicked = Signal(Qt.MouseButton)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Compressor v0.1")

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

         # file selection
        file_browse = QtWidgets.QPushButton("Select File")
        file_browse.clicked.connect(self.open_file_dialog)
        self.filename_edit = QLineEdit()

        self.layout.addWidget(QLabel('File:'))
        self.layout.addWidget(self.filename_edit)
        self.layout.addWidget(file_browse)

        clear_button = QtWidgets.QToolButton()
        # clear_button.setIcon(QtGui.QIcon('clear.png'))
        clear_button.setText('Clear')
        self.layout.addWidget(clear_button)
        clear_button.clicked.connect(self.filename_edit.clear)


        # close button
        self.close_button = QtWidgets.QPushButton("Close")
        self.layout.addWidget(self.close_button)
        self.close_button.clicked.connect(self.close_app)

        # mouse click
        self.clicked.connect(self.handle_click)

    def mousePressEvent(self, event):
        self.clicked.emit(event.button())

    def open_file_dialog(self):
        filename = QFileDialog.getExistingDirectory(
            self,
            "Select a File",
            "C:/Users/tseri/Downloads",
        )
        if filename:
            path = Path(filename)
            self.filename_edit.setText(str(path))
        print(filename)

    @QtCore.Slot(str, name='magic', result=str)
    def magic(self):
        self.text.setText(f"Number: {random.randint(1, 100)}")

    @QtCore.Slot()
    def close_app(self):
        self.close()

    @QtCore.Slot(Qt.MouseButton)
    def handle_click(self, button):
        if button == Qt.LeftButton:
            print("Left button clicked")
        elif button == Qt.RightButton:
            print("Right button clicked")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())