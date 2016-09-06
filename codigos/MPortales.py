#!/usr/bin/python
# -*- coding: utf-8 -*- 

import sys
from PySide import QtCore, QtGui
from ui_portal_adm import Ui_portal_adm
from crtl_form import Frm
from crtl_form_ca import Frm2
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
    self.ui3.a_ntc.clicked.connect(self.ad_ntc)
    self.ui3.a_ctgr.clicked.connect(self.ad_ctgr) 
    #self.ui2.a_ntc.clicked.connect( self."metodo")
    #self.ui2.ed_ntc.clicked.connect( self."metodo")
    #self.ui2.ed_ctgr.clicked.connect( self."metodo") agregar metodo
    #self.ui2.el_ntc.clicked.connect( self."metodo")
    #self.ui2.el_ctgr.clicked.connect( self."metodo") agregar metodo
    self.ui3.volver.clicked.connect(self.volver)

  
  def ad_ctgr(self):
    self.close()
    b = Frm2()
    b.iniciar()
    b.iniciar.show()
  
  def ad_ntc(self):
    self.close()
    b = Frm()
    b.iniciar()
    b.iniciar.show()
  
  def volver(self):
    self.close()
    inicio = Main()
    inicio.__init__().iniciar()
    
  def mostrar(self):
    self.close()
    grid = Vtn2()
    grid.iniciar().show()
    
    
    
