from flask import Flask
app = Flask(__name__)

from flask import render_template, request, redirect, url_for, Flask
from configuraciones import *

import psycopg2
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s port=%s"%(host,database,user,passwd,port))
cur = conn.cursor()

@app.route('/')
@app.route('/index')

def index():	
	sql = "select * from canciones"
	cur.execute(sql)
	canciones = cur.fetchall()

	sql = "select * from canciones"
	cur.execute(sql)
	canciones = cur.fetchall()

	sql = "select * from canciones"
	cur.execute(sql)
	canciones = cur.fetchall()

	sql = "select * from canciones"
	cur.execute(sql)
	canciones = cur.fetchall()

	return render_template("index.html",canciones = canciones)

@app.route('/cancion/<int:id>')	
def cancion(id):
	sql = "select * from Canciones where id = " + str(id)
	cur.execute(sql)
	cancion = cur.fetchall()

	sql = "select Autor_id from Canciones_Autores where Cancion_id = " + str(id)
	cur.execute(sql)
	autor_id = cur.fetchall()
	autor = []
	for i in autor_id: 
		sql = "select * from Autores where id = " + str(i[0]) 
		cur.execute(sql)
		autor.append(cur.fetchall())

	return render_template('cancion.html',autor=autor,cancion=cancion)

app.run(port=80)
