#!/usr/bin/python
# -*- coding: utf-8 -*- 

import sqlite3

def conectar():
    con = sqlite3.connect('noticias.db')
    con.text_factory = str
    con.row_factory = sqlite3.Row
    return con


#************************obtencion de datos

#obtengo todos los datos de noticias
def obt_tb_ntcs():
  con = conectar()
  c = con.cursor()
  rsp = c.execute("select * from noticias;")
  con.close()
  return rsp.fetchall()

#obtengo todos los datos de categorias
def obt_tb_ctgrs():
  def obt_tb_noticias():
  con = conectar()
  c = con.cursor()
  rsp = c.execute("select * from categoria;")
  con.close()
  return rsp.fetchall()

def filtro(texto):
  con = conectar()
  c = concursor()
  a = "%"+texto+"%" #esta parte del codigo debe cambiar dependiendo si la interfaz se puede acceder de manera continua o no
  query = "select id_noticia, fecha, autor, resumen from noticias where texto like '?'"
  respuesta = c.execute(query, (a))
  con.close()
  return respuesta.fetchall()




#**************************Modificación y creación de datos

#para crear la noticia la fk_id_categoria debe ser igual que la id_categoria de la tabla categoría
def crea_ntcs(titulo,fecha,resumen,texto,publicada,autor,fk_id_categoria):
    con = conectar()
    c = con.cursor()
    query = """INSERT INTO noticias (titulo, fecha, resumen, texto, publicada, autor, fk_id_categoria) VALUES (?, ?, ?, ?, ?, ?, ?)"""
    c.execute(query, (titulo,fecha,resumen,texto,publicada,autor,fk_id_categoria))
    con.commit()


def mostrar_ntcs():
  con = conectar()
  c = con.cursor()
  rsp = c.execute("select b.fecha as 'Fecha', a.nombre as 'Categoria', b.titulo as 'Titulo', b.resumen as 'Resumen', b.publicada as 'Publicada', b.autor as 'Autor' from categoria a left join noticias b where id_categoria = fk_id_categoria;")
  con.close()
  return rsp.fetchall()

def edita_ntcs( id_mdf ):
  vdd = True
  con = conectar()
  c = con.cursor()
  query = "update"
  try 

INSERT INTO noticias (titulo, fecha, resumen, texto, publicada, autor, fk_id_categoria) VALUES ("lol", 1988-05-25, "paf", "SI", "FUU", "CACA", 3); 

select * from noticias;

select * from categoria;


  
    
