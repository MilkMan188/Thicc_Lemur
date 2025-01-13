from PySide6.QtCore import Qt, QPoint, QSize
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QWidget, QLabel


class Widget(QWidget):
    def __init__(self, gif_path):
        super().__init__()

        self.setWindowTitle("PhaesiaTwerk")

        #Remove window borders and make background transparent
        self.setWindowFlag(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        #Creat QLabel to display the GIF
        self.label = QLabel(self)
        self.label.setAttribute(Qt.WA_TranslucentBackground)

        #Load/Starts GIF
        self.movie = QMovie(gif_path)
        self.label.setMovie(self.movie)
        self.movie.start()


    def resizeEvent(self, event):

        new_size = self.size()
        self.movie.setScaledSize(new_size)
        self.label.resize(new_size)



