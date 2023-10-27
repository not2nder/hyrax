import sys
import argparse

import sqlite3
import pwinput as pw

from ascii.art import art
from ascii.colors import *
from src.login import *
from src.Table import Table
from src.Password import Password

conn   = sqlite3.connect("app.db")
cursor = conn.cursor()

def main():
	print(art)

	parser = argparse.ArgumentParser()
	parser.add_argument("-u","--user", required=False, help="Usuário")
	parser.add_argument("-p","--password", required=False, help="Senha")
	parser.add_argument("--register",action='store_true', help="Register")

	parser.add_argument("--show",action='store_true',help="Show Psswords")
	parser.add_argument("--color", action='store_true')
	parser.add_argument("--style", required=False)


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

		new(args.user,args.password,args.new,args.login,args.service)

	if args.user and args.password:

		if get_pass_data(args.user,args.password) is None:
			print(f"{red}Error: Not found.{nm}")
			sys.exit()

		if args.show:
			print(f"{cy if args.color else nm}	      Welcome {args.user}! {nm}\n")
			table = Table(get_pass_data(args.user,args.password))
			table.show(color=True if args.color else False,style=args.style)
			sys.exit()

	if args.delete:

		delete(args.user, args.password, args.pid)

def get_uid(user,password):
	return cursor.execute(f"""SELECT id FROM user WHERE user='{user}' AND password='{hash_it(password)}'""").fetchone()[0]

def get_pass_data(user,password):
	return cursor.execute(f"""SELECT * FROM user WHERE user='{user}' AND password='{hash_it(password)}'""").fetchone()[2]

def delete(user,password,pid):

	if pid is None:

		table = Table(get_pass_data(user,password))
		table.show()

		pid = int(input("Password Id to be deleted: "))

	else: pass

	delete = cursor.execute(f"""SELECT * FROM password WHERE pass_id={pid}""").fetchone()[0]
	confirm = input("Confirme password to be deleted: ")

	if confirm != delete:
		print(f"{red}Error: Passwords don't match. {nm}")
		sys.exit(1)

	cursor.execute(f"""DELETE FROM password WHERE pass_id='{pid}' AND user_id='{get_uid(user,password)}'""")
	conn.commit()

	print("Deleted!")

def new(user,password,n_pass,login,service):

	password = Password(n_pass,login,service,get_uid(user,password))
	print("Registered password")
	sys.exit(0)

if __name__ == '__main__':
	main()
