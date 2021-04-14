
import sqlite3

from interface.message_box import  show_error, show_info

db_root = 'models/contact.db'

class UserModel:
	def __init__(self, username, password, secret= None):
		self._username = username
		self._password = password
		self._secret  = secret

	def __set_user(self):
		db = sqlite3.Connection(db_root)
		cursor = db.cursor()
		new_user = ( self._username, self._password, self._secret )
		req = '''INSERT INTO t_user(t_user_name, t_user_passe, t_user_secret) 
				VALUES (?, ?, ?)'''
		cursor.execute(req, new_user)
		db.commit()
		db.close()
		
		


	def __user_verification(self):

		db = sqlite3.Connection(db_root)
		cursor = db.cursor()
		req = '''SELECT t_user_name FROM t_user WHERE t_user_name = ? '''
		user_input_data = (self._username,)
		cursor.execute(req, user_input_data)
		resultat = cursor.fetchone()
		db.close()

		return resultat


	def add_user(self):
		resultat = self.__user_verification()
		
		if not resultat:
			req = 1
			self.__set_user()
			show_info('Info', f'Votre compte a été bien crée. merci de vous connecter.\n Rappel: \n  nom:{self._username } \n  pass: {self._password} \n  scret: {self._secret}')
		else:
			show_error("Error", f'Le Nom {resultat[0] } exite déja')
			req = 0
		return req


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

		