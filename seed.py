from configuraciones import *
import psycopg2
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s port=%s"%(host,database,user,passwd,port))
cur = conn.cursor()
sql ="""
insert into Cancion (nombre, duracion) values 
 ('The Dark Side','227'),
 ('Pressure','235'),
 ('Something Human','226'),
 ('Thought Contagion','206'),
 ('Dig Down','228'),
 ('',''),
 ('',''),
 ('',''),
 ('',''),
 ('',''),
 ('',''),
 ('',''),
 ('',''),
 ('',''),
 ('',''),
 ('',''),
 ('',''),
 ('',''),
 ('',''),
 ('',''),
 ('',''),
 ('','')

returning id;
"""
cur.execute(sql)

sql ="""
insert into Autor (nombre) values 
('MUSE'),
()

returning id;

"""
cur.execute(sql)

sql ="""
insert into Cancion_Autor (cancion_id, autor_id) values 
('1','1'),('2','1'),(3'','1'),('4','1'),('5','1'),
('',''),
('',''),
('',''),
('',''),
('',''),
('',''),

"""
cur.execute(sql)

sql ="""
insert into Generos (nombre) values 
(''), 

returning id;
"""
cur.execute(sql)

sql ="""
insert into Cancion_Genero (nombre) values 
('',''),

"""
cur.execute(sql)

sql ="""
insert into Album (nombre,ano) values 
('Simulation Theory','2018'),
('',''),
('',''),
('',''),
('',''),

returning id;
"""
cur.execute(sql)

sql ="""
insert Cancion_Album (Cancion_id, Album_id) values  
('1','1'), ('2','1'), ('3','1'),('4','1'),('5','1'),
('',''),

"""
cur.execute(sql)



conn.commit()
cur.close()
conn.close()
