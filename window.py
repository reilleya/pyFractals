import sys
from PySide import QtGui

import fractalwidget

class Window(QtGui.QWidget):
	def __init__(self):
		super(Window, self).__init__()
		self.resize(1280, 720)  
		self.setWindowTitle("pyFractals")
		
		fractWidget = fractalwidget.FractalWidget(self)
		
		button = QtGui.QPushButton("&Redraw", self)
		button2 = QtGui.QPushButton("&Test", self)

		all = QtGui.QHBoxLayout()
		all.addWidget(fractWidget)

		controls = QtGui.QGroupBox("Controls")
		controlsLayout = QtGui.QVBoxLayout()
		controlsLayout.addWidget(button)
		controlsLayout.addWidget(button2)
		controlsLayout.addStretch(1)
		controls.setLayout(controlsLayout)
		controls.setFixedWidth(150)
		all.addWidget(controls)
		
		self.setLayout(all) 