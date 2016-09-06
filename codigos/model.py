#!/usr/bin/python
# -*- coding: utf-8 -*- 

import sqlite3

def conectar():
    con = sqlite3.connect('noticias.db')
    con.text_factory = str
    con.row_factory = sqlite3.Row
    return con


#************************obtencion de datos

#Muestra las noticias con sus etiquetas ordenadamente según lo solicitado por pauta
#select * from noticias;
def mostrar_ntcs():
  con = conectar()
  c = con.cursor()
  rsp = c.execute("select b.fecha as 'Fecha', a.nombre as 'Categoria', b.titulo as 'Titulo', b.resumen as 'Resumen',b.texto, b.publicada as 'Publicada', b.autor as 'Autor',a.nombre as 'Categoria' from categoria a left join noticias b where id_categoria = fk_id_categoria;")
  b = rsp.fetchall()
  con.close()
  return b

def refresco(texto):
  con = conectar()
  c = con.cursor()
  print [texto]
  query = "select b.fecha as 'Fecha', b.titulo as 'Titulo', b.resumen as 'Resumen',b.texto, b.publicada as 'Publicada', b.autor as 'Autor',a.nombre as 'Categoria' from categoria a left join noticias b where id_categoria = fk_id_categoria and texto like '%"+texto+"%';"
  #a = "%"+texto+"%" #esta parte del codigo debe cambiar dependiendo si la interfaz se puede acceder de manera continua o no
  #select * from noticias where texto like "%ver%";'
  respuesta = c.execute(query)
  b = respuesta.fetchall()
  con.close()
  return b

def filtro(texto):
  con = conectar()
  c = con.cursor()
  query = "select b.fecha as 'Fecha', b.titulo as 'Titulo', b.resumen as 'Resumen',b.texto, b.publicada as 'Publicada', b.autor as 'Autor',a.nombre as 'Categoria' from categoria a left join noticias b where id_categoria = fk_id_categoria and  b.publicada = '"+texto+"';"
  respuesta = c.execute(query)
  b = respuesta.fetchall()
  con.close()
  return b

#obtengo todos los datos de categorias
def obt_tb_ctgrs():
  con = conectar()
  c = con.cursor()
  rsp = c.execute("select * from categoria;")
  b = rsp.fetchall()
  con.close()
  return b




#**************************Modificación, eliminación y creación de datos

#para crear la noticia la fk_id_categoria debe ser igual que la id_categoria de la tabla categoría
def crea_ntcs(titulo,fecha,resumen,texto,publicada,autor,fk_id_categoria):
    con = conectar()
    c = con.cursor()
    query = """INSERT INTO noticias (titulo, fecha, resumen, texto, publicada, autor, fk_id_categoria) VALUES (?, ?, ?, ?, ?, ?, ?)"""
    c.execute(query, (titulo,fecha,resumen,texto,publicada,autor,fk_id_categoria))
    con.commit()


#para editar las noticas las categorías deben existir para la noticia, y validar la fk_id_categoria con id_noticia
def edita_ntcs(titulo,fecha,resumen,texto,publicada,autor,fk_id_categoria):
  con = conectar()
  c = con.cursor()
  query = "update noticias set titulo = ?, fecha= ?, resumen= ?, texto= ?, publicada= ?, autor= ?, fk_id_categoria= ?, where id_noticia = ?"
  c.execute(query, (titulo,fecha,resumen,texto,publicada,autor,fk_id_categoria))
  con.commit()


#confirma si la eliminación fue exitosa o no, dependiendo si la noticia existe o no con excepcion
def elimina_ntcs(id_ntcs):
  vdd = True
  con = conectar()
  c = con.cursor()
  query = "delete from noticias where id_noticia = ?"
  try:
    c.execute(query, (id_ntcs))
    con.commit()
  except sqlite3.Error as e:
    vdd = False
    print "Error:", e.args[0]
  con.close()
  return vdd

def crea_ctgr(texto):
  vdd = True
  con = conectar()
  c = con.cursor()
  query = "insert into categoria (nombre) values (?) ;"
  c.execute(query, texto)
  con.commit()
  

#***********************querys de prueba
#select * from categoria;
#delete from categoria where id_categoria = 11;
#insert into categoria (nombre) values ("Relogion");
#INSERT INTO noticias (titulo, fecha, resumen, texto, publicada, autor, fk_id_categoria) VALUES ("lol", 1988-05-25, "paf", "SI", "FUU", "CACA", 3); 

#update noticias set titulo= "narf", fecha='1988-05-25', resumen="cafi", texto="tula", publicada="NO", autor="PATA", fk_id_categoria="3" where id_noticia = 23;

#select * from noticias;
 
#consulta con like
#select * from noticias where texto like "%ta%";
