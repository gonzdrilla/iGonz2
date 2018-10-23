from configuraciones import *
import psycopg2
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s port=%s"%(host,database,user,passwd,port))


cur = conn.cursor()
sql ="""DROP SCHEMA public CASCADE;
CREATE SCHEMA public;"""

cur.execute(sql)

sql ="""
CREATE TABLE Cancion
           (id serial PRIMARY KEY, nombre varchar(80), duracion integer);
"""

cur.execute(sql)


sql ="""
CREATE TABLE Autor
           (id integer PRIMARY KEY, nombre varchar(40));
"""

cur.execute(sql)

sql ="""
CREATE TABLE Cancion_Autor
           (Cancion_id integer, Autor_id integer);
"""

cur.execute(sql)

sql ="""
CREATE TABLE  Generos
           (id serial PRIMARY KEY, nombre varchar(140));
"""

cur.execute(sql)

sql ="""
CREATE TABLE Cancion_Genero
           (Cancion_id integer, Genero_id integer);
"""

cur.execute(sql)

sql = """
CREATE TABLE Album
           (id serial PRIMARY KEY, nombre varchar(140), ano integer);
"""

cur.execute(sql)

sql = """
CREATE TABLE Cancion_Album
           (Cancion_id integer, Album_id integer);
"""

cur.execute(sql)

sql ="""
CREATE TABLE Usuarios
	(id serial PRIMARY KEY, name varchar(40), pass varchar(100));
"""

cur.execute(sql)


conn.commit()
cur.close()
conn.close()
