# -*- coding: utf-8 -*-

import sys
from PySide import QtCore, QtGui
#importar ventana portal para cargarla despues del login
from ui_login import Ui_Noticias


class Main(QtGui.QMainWindow):
  def __init__(self):
    super(Main, self).__init__()
    self.ui1 = Ui_Noticias()
    self.ui1.setupUi(self)
    self.show()







def run():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()