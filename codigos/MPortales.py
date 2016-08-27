# -*- coding: utf-8 -*-

import sys
from PySide import QtCore, QtGui
from ui_portal_adm import Ui_portal_adm
from ui_portal_usr import Ui_mostrador

class Vtn1 (QtGui.QMainWindow):
  def iniciar(self):
    self.ui3 = Ui_portal_adm()
    self.ui3.setupUi(self)
    self.botones()
    self.show()

  def botones(self): #Se dejan activos la conexion de los botones al formulario
    #self.ui2.mstr.clicked.connect( self."metodo") agregar metodo
    #self.ui2.a_ctgr.clicked.connect( self."metodo") agregar metodo
    #self.ui2.a_ntc.clicked.connect( self."metodo")
    #self.ui2.ed_ntc.clicked.connect( self."metodo")
    #self.ui2.ed_ctgr.clicked.connect( self."metodo") agregar metodo
    #self.ui2.el_ntc.clicked.connect( self."metodo")
    #self.ui2.el_ctgr.clicked.connect( self."metodo") agregar metodo
    self.ui3.salir.clicked.connect(exit)

  #def mostrar(self):