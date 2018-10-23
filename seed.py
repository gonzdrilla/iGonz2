from configuraciones import *
import psycopg2
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s port=%s"%(host,database,user,passwd,port))
cur = conn.cursor()
sql ="""
insert into Cancion (nombre, duracion) values 
 ('Algorithm',''),
 ('The Dark Side','227'),
 ('Pressure','235'),
 ('Propaganda',''),
 ('Break it to Me',''),
 ('Something Human','226'),
 ('Thought Contagion','206'),
 ('Get UP and Fight',''),
 ('Blockades',''),
 ('Dig Down','228'),
 ('The Void',''),
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
(),()

returning id;

"""
cur.execute(sql)

sql ="""
insert into Cancion_Autor (cancion_id, autor_id) values 
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
('Simulation Theory','2018')

returning id;
"""
cur.execute(sql)

sql ="""
insert Cancion_Album (Cancion_id, Album_id) values  
('',''),

"""
cur.execute(sql)



conn.commit()
cur.close()
conn.close()
