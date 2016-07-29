#!/usr/bin/python
# -*- coding: utf-8 -*- 

import sys
import model as db_nt


def ingresar_noticia(a,b,c,d,e,f,g):
  if (a=="" and b =="" and c=="" and d=="" and e=="" and e=="" and f=="" and g==""):
    print "No ingresado a la bbs"
  else:
    db_nt.agregar_noticia(a,b,c,d,e,f,g)
    
def actualizar_noticia(a,b,c,d,e,f,g):
  if (a=="" and b =="" and c=="" and d=="" and e=="" and e=="" and f=="" and g==""):
    print "No ingresado a la bbs"
  else:
    db_nt.agregar_noticia(a,b,c,d,e,f,g)



#titulo,fecha,resumen,texto,publicada,autor,fk_id_categoria
if __name__ == "__main__":
  fecha = raw_input("Ingrese la fecha de la noticia: ")
  fk = raw_input("1 Politica;2 Educacion;3 Cultura;4 Ciencia y Tecnologia;5 Deporte;6 Espectaculo;7 Cine;8 Internacional;9 Economia;10 Salud  :")
  titulo = raw_input("Ingrese el titulo de la noticia: ")
  resumen = raw_input("Ingrese el resumen de la noticia: ")
  texto = raw_input("Ingrese el Texto de la noticia: ")
  publicada = raw_input("La noticia esta publicada? SI o NO: ")
  autor = raw_input("INgrese el autor: ")
  ingresar_noticia(titulo,fecha,resumen,texto,publicada,autor,fk)