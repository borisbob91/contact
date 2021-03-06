import sqlite3

import config

def create_user_table():
	try:

		db = sqlite3.Connection(config.db_root)
		cursor = db.cursor()

		create_user_table = '''CREATE TABLE  t_user(
			id	INTEGER PRIMARY KEY AUTOINCREMENT,
			t_user_name	TEXT NOT NULL,
			t_user_passe	TEXT NOT NULL,
			t_user_secret TEXT NOT NULL
			)'''
		db.execute(create_user_table)
	except Exception as e:
		db.rollback()
		db.close()
		print('erreur db: ', e)
	else:

		db.commit()
		db.close()

		return {}

def create_repertoire_table():
	try:
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
	except Exception as e:
		db.rollback()
		db.close()
		print("erreur created table repertoire", e)
	else:
		db.commit()
		db.close()

def insert_contact():
	try:
		db = sqlite3.Connection(config.db_root)
		cursor = db.cursor()
		new_contact = ( 'Boris', 'bob', '0759188395', 'img', 1)
		req = '''INSERT INTO t_repertoire(c_name, c_prenoms, c_numero, c_photo, t_user_id) 
			VALUES (?, ?, ?, ?, ?)'''
		cursor.execute(req, new_contact)
			
	except Exception as e:
		db.rollback()
		print('erreur d\'ajouter contact:', e)
	else:
		db.commit()
		db.close()
		print('données enrégistrées et db fermé !')
	


def configure():
    try:
        db = open(f'{config.BASE_DIR}/{config.db_root}', 'r')
        db.close()
    except FileNotFoundError:
        create_repertoire_table()
        create_user_table()
        insert_contact()

        return 'new db created'
    else:
    	return {}

if __name__ == '__main__':
	configure()