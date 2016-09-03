#!/usr/bin/python
# -*- coding: utf-8 -*- 

import sys
from PySide import QtCore, QtGui
from MPortales import *
from ui_portal_usr import Ui_mostrador
import model as db_model

#Inicia Ventana de Mostrado de detalles de noticias

class Vtn2 (QtGui.QMainWindow):
  def iniciar(self):
    self.msrt = Ui_mostrador()
    self.msrt.setupUi(self)
    self.load_data()
    self.botones()
    self.show()
      
  def botones(self):
    self.msrt.volver.clicked.connect(self.atras)
    self.msrt.filtro.textChanged.connect(self.cambio_tbl)
    
  def atras(self):
    self.close()
    from MPortales import Vtn1
    self.init = Vtn1()
    self.init.iniciar()
  
  def load_data(self):
    datos = db_model.mostrar_ntcs()
    self.model = QtGui.QStandardItemModel(self.msrt.tabla)
    for e in datos:
      a = (e["fecha"]) + "\n"
      a = a + (e["titulo"]) + "\n"
      a = a + (e["resumen"]) + "\n"
      a = a + (e["texto"]) + "\n"
      a = a + (e["publicada"]) + "\n"
      a = a + (e["autor"]) + "\n"
      a = a + (e["Categoria"])
      self.item = QtGui.QStandardItem(a)
      self.model.appendRow(self.item)
      a = ""
    self.msrt.tabla.setModel(self.model)
    
  def cambio_tbl(self, text):
    fltr = db_model.refresco(text) #llamo tabla noticias filtrada  de la consulta a la bss y la guardo en fltr
    self.model = QtGui.QStandardItemModel(self.msrt.tabla)#creo objeto modelo de tabla
    for e in fltr:
      a = (e["fecha"]) + "\n"
      a = a + (e["titulo"]) + "\n"
      a = a + (e["resumen"]) + "\n"
      a = a + (e["texto"]) + "\n"
      a = a + (e["publicada"]) + "\n"
      a = a + (e["autor"]) + "\n"
      a = a + (e["Categoria"])
      self.item = QtGui.QStandardItem(a)
      self.model.appendRow(self.item)
      a = ""
    self.msrt.tabla.setModel(self.model)	#Reescribe la tabla con el dato que reciba
    
    