from tabulate import tabulate

import sqlite3

conn   = sqlite3.connect("app.db")
cursor = conn.cursor()

#to do...
class Table:
	def __init__(self,user_id):

		self.user_id = user_id

	def show(self):

		cursor.execute(f"""SELECT passw, service, username, pass_id FROM password WHERE user_id={self.user_id}""")

		data    = [list(item) for item in cursor.fetchall()]
		headers = ['Password','Service','User','Pass_id']

		print(tabulate(data, headers, tablefmt="grid"))
