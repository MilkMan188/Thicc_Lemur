from PySide6.QtWidgets import QApplication
from gui.gui import Widget
import sys

app = QApplication(sys.argv)

gif_path = "img/phaesia_twerk2.gif"

window = Widget(gif_path)
window.show()

app.exec()