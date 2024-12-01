import sys
from PySide6.QtWidgets import QApplication, QPushButton, QToolButton
from PySide6.QtGui import QAction, QIcon

def function():
    print("The 'function' has been called!")

app = QApplication()
button = QPushButton("Call function")
button = QToolButton()
# button.setText('Clear')
button.setIcon(QIcon('clear.png'))

button.clicked.connect(function)
button.show()


sys.exit(app.exec())