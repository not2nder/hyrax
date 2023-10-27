from tabulate import tabulate

import sqlite3

from ascii.colors import*

conn   = sqlite3.connect("app.db")
cursor = conn.cursor()

#to do...
class Table:
	def __init__(self,user_id):

		self.user_id = user_id

	def show(self,color=False,style="grid"):

		cursor.execute(f"""SELECT passw, service, username, pass_id FROM password WHERE user_id={self.user_id}""")

		data    = [list(item) for item in cursor.fetchall()]
		headers = ['Password','Service','Login','PID']

		styles = {
			'1':"grid",
			'2':"pipe",
			'3':"orgtbl",
			'4':"rst",
			'5':"simple",
			None:"grid"
		}

		print(f"{nm if not(color) else cy}{tabulate(data, headers, tablefmt=styles[style])}{nm}")
