import sys
from PySide import QtGui


class Window(QtGui.QWidget):
	def __init__(self):
		super(Window, self).__init__()
		self.resize(320, 240)  
		self.setWindowTitle("pyFractals")
		
		button = QtGui.QPushButton("&Redraw", self)