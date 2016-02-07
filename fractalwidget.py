from PySide.QtOpenGL import QGLWidget
from PySide.QtGui import *

class FractalWidget(QGLWidget):
	def __init__(self, parent):
		QGLWidget.__init__(self, parent)
		self.setSizePolicy(QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum))

	def initializeGL(self):
		pass

	def resizeGL(self, w, h):
		pass
		
	def paintGL(self):
		pass