import sys
from PySide import QtGui

import window

app = QtGui.QApplication(sys.argv)

win = window.Window()

win.show()

sys.exit(app.exec_())