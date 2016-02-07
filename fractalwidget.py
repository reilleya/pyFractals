from PySide.QtOpenGL import QGLWidget

class FractalWidget(QGLWidget):
	def __init__(self, parent):
		QGLWidget.__init__(self, parent)

	def initializeGL(self):
		pass

	def resizeGL(self, w, h):
		pass
		
	def paintGL(self):
		pass