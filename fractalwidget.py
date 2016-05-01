from PySide.QtOpenGL import QGLWidget
from PySide.QtGui import *
from OpenGL import GL

class FractalWidget(QGLWidget):
	def __init__(self, parent):
		QGLWidget.__init__(self, parent)
		
	def uploadShader(self, shaderText):
		self.vertexShader = GL.glCreateShader(GL.GL_VERTEX_SHADER)
		print self.vertexShader
		GL.glShaderSource(self.vertexShader, "")
		GL.glCompileShader(self.vertexShader)
		print GL.glGetShaderInfoLog(self.vertexShader)

	def initializeGL(self):
		GL.glClearColor(0, 1, 0, 1)
		self.uploadShader(True)

	def resizeGL(self, w, h):
		GL.glViewport(0, 0, w, h)
		
	def paintGL(self):
		GL.glClear(GL.GL_COLOR_BUFFER_BIT)