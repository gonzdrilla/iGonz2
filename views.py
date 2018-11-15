from flask import render_template, request, redirect, url_for, Flask
from configuraciones import *

import psycopg2
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s port=%s"%(host,database,user,passwd,port))
cur = conn.cursor()

@app.route('/')
@app.route('/index')
def index():	
	return "fuck me1"