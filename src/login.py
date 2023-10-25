import sys

import sqlite3
import hashlib

import pwinput as pw

conn = sqlite3.connect("app.db")
cur  = conn.cursor()

def hash_it(text:str):
	return hashlib.sha256(text.encode('utf-8')).hexdigest()

def register(user=None):
	cur.execute(f"""CREATE TABLE IF NOT EXISTS user(
		user TEXT,
		password TEXT,
		id INTEGER PRIMARY KEY AUTOINCREMENT
	)""")

	user = input("Username: ") if user == None else user
	pwrd = pw.pwinput(f"Password for {user}: ",mask='*')
	cur.execute('''INSERT INTO user (user,password) VALUES (?,?)''',(user,hash_it(pwrd)))
	conn.commit()
