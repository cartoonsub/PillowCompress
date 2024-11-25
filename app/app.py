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

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

         # file selection
        file_browse = QPushButton('Browse')
        file_browse.clicked.connect(self.open_file_dialog)
        self.filename_edit = QLineEdit()

        self.layout.addWidget(QLabel('File:'))
        self.layout.addWidget(self.filename_edit)
        self.layout.addWidget(file_browse)

    def open_file_dialog(self):
        filename, ok = QFileDialog.getOpenFileName(
            self,
            "Select a File", 
            "D:\\icons\\avatar\\", 
            "Images (*.png *.jpg)"
        )
        if filename:
            path = Path(filename)
            self.filename_edit.setText(str(path))

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))
        


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())