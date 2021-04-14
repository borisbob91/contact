import sqlite3

db = sqlite3.Connection('models/contact.db')

cursor = db.cursor()

create_user_table = '''CREATE TABLE  t_user(
	id	INTEGER PRIMARY KEY AUTOINCREMENT,
	t_user_name	TEXT NOT NULL,
	t_user_passe	TEXT NOT NULL,
	t_user_secret TEXT NOT NULL
)'''

create_repertoire_table ='''CREATE TABLE t_repertoire (
	id	INTEGER PRIMARY KEY AUTOINCREMENT,
	c_name	TEXT NOT NULL,
	c_prenoms	TEXT,
	c_numero	TEXT NOT NULL,
	t_user_id	TEXT NOT NULL
)'''

db.execute(create_user_table)
db.execute(create_repertoire_table)
db.commit()
db.close()