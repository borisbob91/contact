import sqlite3

import config

def create_user_table():

	db = sqlite3.Connection(config.db_root)

	cursor = db.cursor()

	create_user_table = '''CREATE TABLE  t_user(
			id	INTEGER PRIMARY KEY AUTOINCREMENT,
			t_user_name	TEXT NOT NULL,
			t_user_passe	TEXT NOT NULL,
			t_user_secret TEXT NOT NULL
			)'''

	db.execute(create_user_table)
	db.commit()
	db.close()

def create_repertoire_table():
	db = sqlite3.Connection(config.db_root)
	cursor = db.cursor()

	create_repertoire_table ='''CREATE TABLE t_repertoire(
		id	INTEGER PRIMARY KEY AUTOINCREMENT,
		c_name	TEXT NOT NULL,
		c_prenoms	TEXT,
		c_numero	TEXT NOT NULL,
		c_photo     TEXT,
		t_user_id	TEXT NOT NULL
	)'''
	db.execute(create_repertoire_table)
	db.commit()
	db.close()

if __name__ == '__main__':
	create_repertoire_table()
	create_repertoire_table()