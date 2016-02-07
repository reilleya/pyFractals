import sys
from PySide import QtGui

import fractalwidget

class Window(QtGui.QWidget):
	def __init__(self):
		super(Window, self).__init__()
		self.resize(320, 240)  
		self.setWindowTitle("pyFractals")
		
		fractWidget = fractalwidget.FractalWidget(self)
		
		button = QtGui.QPushButton("&Redraw", self)

		
		hbox = QtGui.QHBoxLayout()
		hbox.addStretch(1)
		hbox.addWidget(button)

		vbox = QtGui.QVBoxLayout()
		vbox.addStretch(1)
		vbox.addLayout(hbox)
		
		self.setLayout(vbox) 