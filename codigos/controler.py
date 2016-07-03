#!/usr/bin/python
# -*- coding: utf-8 -*- 

import sqlite3

def conectar():
    con = sqlite3.connect('noticias.db')
    con.text_factory = str
    con.row_factory = sqlite3.Row
    return con

def agregar_noticia(titulo,fecha,resumen,texto,publicada,autor,fk_id_categoria):
    con = conectar()
    c = con.cursor()
    query = """INSERT INTO noticias (titulo, fecha, resumen, texto, publicada, autor, fk_id_categoria) VALUES (?, ?, ?, ?, ?, ?, ?)"""
    c.execute(query, (titulo,fecha,resumen,texto,publicada,autor,fk_id_categoria))
    con.commit()


