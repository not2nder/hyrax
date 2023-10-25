import sqlite3
conn   = sqlite3.connect("app.db")
cursor = conn.cursor()

class Password:
	def __init__(self,password,service,username,user_id):
		self.password = password
		self.service  = service
		self.username = username
		self.user_id  = user_id

		cursor.execute("""CREATE TABLE IF NOT EXISTS password(
		        passw TEXT,
       			service TEXT,
		        username TEXT,
        		user_id INT,
        		pass_id INTEGER PRIMARY KEY AUTOINCREMENT,
        		FOREIGN KEY (user_id) REFERENCES user(id)
		)""")
		conn.commit()


		cursor.execute(f"""INSERT INTO password (passw,service,username,user_id)
		VALUES ('{self.password}','{self.service}','{self.username}',{self.user_id})""")
		conn.commit()
