#!/usr/bin/python
# -*- coding: utf-8 -*- 

import sys
from PySide import QtCore, QtGui
from ui_portal_adm import Ui_portal_adm
from crtl_mstr import Vtn2
from login import Main

class Vtn1 (QtGui.QMainWindow):
  def iniciar(self):
    self.ui3 = Ui_portal_adm()
    self.ui3.setupUi(self)
    self.botones()
    self.show()

  def botones(self): #Se dejan activos la conexion de los botones al formulario
    self.ui3.mstr.clicked.connect(self.mostrar) 
    #self.ui2.a_ctgr.clicked.connect( self."metodo") agregar metodo
    #self.ui2.a_ntc.clicked.connect( self."metodo")
    #self.ui2.ed_ntc.clicked.connect( self."metodo")
    #self.ui2.ed_ctgr.clicked.connect( self."metodo") agregar metodo
    #self.ui2.el_ntc.clicked.connect( self."metodo")
    #self.ui2.el_ctgr.clicked.connect( self."metodo") agregar metodo
    self.ui3.volver.clicked.connect(self.volver)

  #def mostrar(self):
  
  def volver(self):
    self.close()
    inicio = Main()
    inicio.__init__().iniciar()
    
  def mostrar(self):
    self.close()
    grid = Vtn2()
    grid.iniciar().show()
    
    
    
