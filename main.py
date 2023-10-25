import sys
import argparse

import sqlite3
import pwinput as pw

from ascii.art import art
from src.login import *
from src.Table import Table
from src.Password import Password

conn   = sqlite3.connect("app.db")
cursor = conn.cursor()

red  = "\u001b[31m"
nm   = "\u001b[37m"

def main():
	print(art)

	parser = argparse.ArgumentParser()
	parser.add_argument("-u","--user", required=False, help="Usuário")
	parser.add_argument("-p","--password", required=False, help="Senha")
	parser.add_argument("--register",action='store_true', help="Register")
	parser.add_argument("--show",action='store_true',help="Show Psswords")

	parser.add_argument("--new",required=False)
	parser.add_argument("-s","--service",required=False)
	parser.add_argument("-l","--login",required=False)

	parser.add_argument("--delete",action='store_true', help="Delete")
	parser.add_argument("--pid", required=False)

	args = parser.parse_args()

	if args.register:

		register(args.user) if args.user else register()

	else: pass

	if args.new:

		cursor.execute(f"""SELECT id FROM user WHERE user = '{args.user}' AND password = '{hash_it(args.password)}'""")

		password = Password(args.new,args.service,args.login,cursor.fetchone()[0])

		print("Registered password")
		sys.exit()

	if args.user and args.password:

		cursor.execute(f"""SELECT * FROM user WHERE user='{args.user}' AND password='{hash_it(args.password)}'""")
		data = cursor.fetchone()

		if data is None:
			print(f"{red}Not found.{nm}")
			sys.exit()

		if args.show:
			print(f"Welcome {args.user}! \n")
			table = Table(data[2])
			table.show()
			sys.exit()

	if args.delete:

		uid = cursor.execute(f"""SELECT id FROM user WHERE user = '{args.user}' AND password='{hash_it(args.password)}'""").fetchone()[0]

		cursor.execute(f"""DELETE FROM password WHERE pass_id={args.pid} AND user_id={uid}""")
		conn.commit()

		print("Senha deletada!")

if __name__ == "__main__":
	main()
