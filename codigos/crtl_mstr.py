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

    
  def atras(self):
    self.close()
    from MPortales import Vtn1
    self.init = Vtn1()
    self.init.iniciar()
        
  def load_data(self):
    datos = db_model.obt_tb_ntcs()
    ctg = db_model.obt_tb_ctgrs()
    self.model = QtGui.QStandardItemModel(self.msrt.tabla)
    for e in datos:
      for b in ctg:
	if b["id_categoria"] == e["fk_id_categoria"]:
	  h = b["nombre"]
	  print h
      a = (e["fecha"]) + "\n"
      a = a + (e["titulo"]) + "\n"
      a = a + (e["resumen"]) + "\n"
      a = a + (e["texto"]) + "\n"
      a = a + (e["publicada"]) + "\n"
      a = a + (e["autor"]) + "\n"
      a = a + h + "\n"
      #a = a + str(e["fk_id_categoria"])
      #self.msrt.label.setText(a)
      self.item = QtGui.QStandardItem(a)
      self.model.appendRow(self.item)
      a = ""
    self.msrt.tabla.setModel(self.model)
    

     
     
  
  

  
  
  
    
    
    
    