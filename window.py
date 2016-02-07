import sys
from PySide import QtGui

import fractalwidget

class Window(QtGui.QWidget):
	def __init__(self):
		super(Window, self).__init__()
		self.resize(320, 240)  
		self.setWindowTitle("pyFractals")
		
		#fractWidget = fractalwidget.FractalWidget(self)
		
		button = QtGui.QPushButton("&Redraw", self)
		button2 = QtGui.QPushButton("&Test", self)

		toprow = QtGui.QHBoxLayout()
		toprow.addStretch(1)
		toprow.addWidget(button)
		#hbox.addWidget(fractWidget)
		secrow = QtGui.QHBoxLayout()
		secrow.addStretch(1)
		secrow.addWidget(button2)

		vbox = QtGui.QVBoxLayout()
		vbox.addLayout(toprow)
		vbox.addStretch(1)
		vbox.addLayout(secrow)
		
		self.setLayout(vbox) 