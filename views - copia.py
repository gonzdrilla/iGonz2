from flask import render_template, request, session, redirect, url_for
from configuraciones import *
from werkzeug.security import generate_password_hash, check_password_hash

import psycopg2
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s port=%s"%(host,database,user,passwd,port))
cur = conn.cursor()

app.secret_key = b'_p#lou8#veta.betdhzhj.flok\n\xec]/'

@app.route('/', methods=["POST", "GET"])
@app.route('/index', methods=["POST","GET"])
def index():
	sql = "select row_number() over (order by tipo), tipo from Animes group by tipo order by tipo"
	cur.execute(sql)
	tipos = cur.fetchall()
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	errorname = None
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["pass"]
		sql = "select pass from Usuarios where name like '%s'" %(username)
		cur.execute(sql)
		users = cur.fetchall()
		if users and check_password_hash(users[0][0], password):
			session['username'] = username
		else:
			errorname = "Error, su clave de acceso o usuario no son validos."
	return render_template('index.html',generos=generos,tipos=tipos,errorname=errorname)

@app.route('/animes')
def animes():
	sql = "select row_number() over (order by tipo), tipo from Animes group by tipo order by tipo"
	cur.execute(sql)
	tipos = cur.fetchall()
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	sql = "select * from Animes"
	cur.execute(sql)
	animes = cur.fetchall()
	return render_template('index.html',animes=animes,generos=generos,tipos=tipos)

@app.route('/categorias')
def categorias():
	sql = "select row_number() over (order by tipo), tipo from Animes group by tipo order by tipo"
	cur.execute(sql)
	tipos = cur.fetchall()
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	return render_template('categorias.html',generos=generos,tipos=tipos)

@app.route('/personajes')
def personajes():
	sql = "select row_number() over (order by tipo), tipo from Animes group by tipo order by tipo"
	cur.execute(sql)
	tipos = cur.fetchall()
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	sql = "select * from Personajes"
	cur.execute(sql)
	personajes = cur.fetchall()
	return render_template('personajes.html',generos=generos,personajes=personajes,tipos=tipos)

@app.route('/autores')
def autores():
	sql = "select row_number() over (order by tipo), tipo from Animes group by tipo order by tipo"
	cur.execute(sql)
	tipos = cur.fetchall()
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	sql = "select * from Autores"
	cur.execute(sql)
	autores = cur.fetchall()
	return render_template('autores.html',generos=generos,autores=autores,tipos=tipos)

@app.route('/estudios')
def estudios():
	sql = "select row_number() over (order by tipo), tipo from Animes group by tipo order by tipo"
	cur.execute(sql)
	tipos = cur.fetchall()
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	sql = "select * from Estudios"
	cur.execute(sql)
	estudios = cur.fetchall()
	return render_template('estudios.html',generos=generos,estudios=estudios,tipos=tipos)

@app.route('/categorias/<int:id>')
def categorias_id(id):
	sql = "select row_number() over (order by tipo), tipo from Animes group by tipo order by tipo"
	cur.execute(sql)
	tipos = cur.fetchall()
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	sql = "select nombre from Generos where id = " + str(id)
	cur.execute(sql)
	resultado = cur.fetchall()
	sql = "select * from Animes, Generos, Animes_Generos where anime_id = Animes.id and genero_id = Generos.id and Generos.id = " + str(id)
	cur.execute(sql)
	animes = cur.fetchall()
	return render_template('categorias_id.html',animes=animes,generos=generos,resultado=resultado,tipos=tipos)

@app.route('/animes/<int:id>')
def animes_id(id):
	sql = "select row_number() over (order by tipo), tipo from Animes group by tipo order by tipo"
	cur.execute(sql)
	tipos = cur.fetchall()
	sql = "select * from Animes where id = " + str(id)
	cur.execute(sql)
	anime = cur.fetchall()
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	sql = "select * from Personajes, Animes_Personajes where anime_id = " + str(id) + " and Personajes.id = personaje_id"
	cur.execute(sql)
	personajes = cur.fetchall()
	sql = "select * from Generos, Animes_Generos where anime_id = " + str(id) + " and Generos.id = genero_id"
	cur.execute(sql)
	categorias = cur.fetchall()
	sql = "select * from Estudios, Animes where Estudios.id = estudio_id and Animes.id = " + str(id) 
	cur.execute(sql)
	estudio = cur.fetchall()
	sql = "select * from Autores, Animes where Autores.id = autor_id and Animes.id = " + str(id)
	cur.execute(sql)
	autor = cur.fetchall()
	sql = "select * from Estados where anime_id = " + str(id)
	cur.execute(sql)
	estado = cur.fetchall()
	return render_template('animes_id.html',generos=generos,tipos=tipos,anime=anime,personajes=personajes,categorias=categorias,estudio=estudio,autor=autor,estado=estado)

@app.route('/buscar/results',methods=["GET"])
def buscar():
	sql = "select row_number() over (order by tipo), tipo from Animes group by tipo order by tipo"
	cur.execute(sql)
	tipos = cur.fetchall()
	keyword = request.args.get('search')
	keyword = str(keyword)
	sql = "select id, nombre from Animes where lower(nombre) like lower('%%%s%%')" %(keyword)
	cur.execute(sql)
	resultados = cur.fetchall()
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	return render_template('buscar.html',generos=generos,resultados=resultados,tipos=tipos)

@app.route('/estudios/<int:id>')
def estudios_id(id):
	sql = "select row_number() over (order by tipo), tipo from Animes group by tipo order by tipo"
	cur.execute(sql)
	tipos = cur.fetchall()
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	sql = "select nombre from Estudios where id = " + str(id)
	cur.execute(sql)
	resultado = cur.fetchall()
	sql = "select * from Animes, Estudios where Animes.estudio_id = Estudios.id and Estudios.id = " + str(id)
	cur.execute(sql)
	animes = cur.fetchall()
	return render_template('estudios_id.html',animes=animes,generos=generos,resultado=resultado,tipos=tipos)

@app.route('/personajes/<int:id>')
def personajes_id(id):
	sql = "select row_number() over (order by tipo), tipo from Animes group by tipo order by tipo"
	cur.execute(sql)
	tipos = cur.fetchall()
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	sql = "select nombre from Personajes where id = " + str(id)
	cur.execute(sql)
	resultado = cur.fetchall()
	sql = "select * from Animes, Personajes, Animes_Personajes where Animes.id = anime_id and Personajes.id = personaje_id and Personajes.id = " + str(id)
	cur.execute(sql)
	animes = cur.fetchall()
	return render_template('personajes_id.html',animes=animes,generos=generos,resultado=resultado,tipos=tipos)

@app.route('/autores/<int:id>')
def autores_id(id):
	sql = "select row_number() over (order by tipo), tipo from Animes group by tipo order by tipo"
	cur.execute(sql)
	tipos = cur.fetchall()
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	sql = "select nombre from Autores where id = " + str(id)
	cur.execute(sql)
	resultado = cur.fetchall()
	sql = "select * from Animes, Autores where Animes.autor_id = Autores.id and Autores.id = " + str(id)
	cur.execute(sql)
	animes = cur.fetchall()
	return render_template('autores_id.html',animes=animes,generos=generos,resultado=resultado,tipos=tipos)

@app.route('/tipos/<int:id>')
def tipos_id(id):
	sql = "select row_number() over (order by tipo), tipo from Animes group by tipo order by tipo"
	cur.execute(sql)
	tipos = cur.fetchall()
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	resultado = [tipos[0][0],tipos[0][1]]
	sql = "select * from Animes where tipo = '%s'" %(str(tipos[id-1][1]))
	cur.execute(sql)
	animes = cur.fetchall()
	return render_template('tipos.html',animes=animes,generos=generos,resultado=resultado,tipos=tipos)

@app.route('/registro', methods=["POST","GET"])
def registro():
	sql = "select row_number() over (order by tipo), tipo from Animes group by tipo order by tipo"
	cur.execute(sql)
	tipos = cur.fetchall()
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	errorname = None
	errorpass = None
	if request.method == "POST":
		username = request.form["username"]
		password = generate_password_hash(request.form["pass"])
		confirmpass = request.form["confirmpass"]
		sql = "select name from Usuarios where name like '%s'" %(username)
		cur.execute(sql)
		users = cur.fetchall()
		if users:
			errorname = "Ese usuario ya existe."
		if confirmpass != request.form["pass"]:
			errorpass = "Las claves no coinciden."
		if not errorpass and not errorname:
			sql = "insert into Usuarios (name,pass) values ('%s','%s')" %(username,password)
			cur.execute(sql)
			conn.commit()
			return redirect(url_for('index'))
	return render_template('registro.html',generos=generos,tipos=tipos,errorname=errorname,errorpass=errorpass)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))