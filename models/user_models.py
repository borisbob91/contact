
import sqlite3

db_root = 'models/contact.db'
class UserModel:
	def __init__(self, username, password, secret= None):
		self._username = username
		self._password = password
		self._secret  = secret

	def __set_user(self):
		db = sqlite3.Connection(db_root)
		cursor = db.cursor()
		new_user = (cursor.lastrowid, self._username, self._password, self._secret )
		req = '''INSERT INTO t_user(t_user_name, t_user_passe, t_user_secret) 
				VALUES (?, ?, ?)'''
		cursor.execute(req, new_user)
		db.commit()
		db.close()
	
	def add_user(self):
		self.__set_user()

	def user_validator(self):
		self._get_user()

	def _get_user(self):
		import sqlite3
		db = sqlite3.Connection(db_root)
		cursor = db.cursor()
		req = '''SELECT t_user_name, t_user_passe FROM t_user WHERE t_user_name = ? AND t_user_passe = ?'''
		user_input_data = (self._username, self._password )
		cursor.execute(req, user_input_data)
		resultat =cursor.fetchone()
		db.close()

		if resultat != 0:
			find = 1
		else:
			find = 0
		
		return find

		