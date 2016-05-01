from PySide.QtOpenGL import QGLWidget
from PySide.QtGui import *
from OpenGL import GL

class FractalWidget(QGLWidget):
	def __init__(self, parent):
		QGLWidget.__init__(self, parent)
		#self.setSizePolicy(QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum))

	def initializeGL(self):
		GL.glClearColor(0, 0, 0, 1)

	def resizeGL(self, w, h):
		pass
		
	def paintGL(self):
		GL.glClear(GL.GL_COLOR_BUFFER_BIT)