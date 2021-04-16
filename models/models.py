
import sqlite3

from interface.message_box import  show_error, show_info
import base64

import config


class UserModel:
	def __init__(self, username, password=None, secret= None):
		self._username = username
		self._password = password
		self._secret  = secret

	def __set_user(self):
		db = sqlite3.Connection(config.db_root)
		cursor = db.cursor()
		new_user = ( self._username, self._password, self._secret )
		req = '''INSERT INTO t_user(t_user_name, t_user_passe, t_user_secret) 
				VALUES (?, ?, ?)'''
		cursor.execute(req, new_user)
		db.commit()
		db.close()
		

	def __user_verification(self):

		db = sqlite3.Connection(config.db_root)
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
		user_and_pass = ''
		user = self.__user_verification()
		if not user:
			show_error("Error", f'Le Nom saisie l\'exite pas')
		else:
			user_and_pass = self._get_user()
	
		return {'user': user_and_pass}


	def _get_user(self):

		db = sqlite3.Connection(config.db_root)
		cursor = db.cursor()
		req = '''SELECT t_user_name, t_user_passe FROM t_user WHERE t_user_name = ? AND t_user_passe = ?'''
		user_input_data = (self._username, self._password )
		cursor.execute(req, user_input_data)
		resultat = cursor.fetchone()
		db.close()

		return resultat

	def user_is_valide(self):
		resultat = self.__user_verification()

		return resultat

	def __reset_pass_qeury(self, old_secret):
		db = sqlite3.Connection(config.db_root)
		cursor = db.cursor()
		req = '''SELECT * FROM t_user WHERE t_user_name = ? AND t_user_secret = ?'''
		user_input_data = (self._username, old_secret )
		cursor.execute(req, user_input_data)
		resultat = cursor.fetchone()
		db.close()

		return resultat

	def reset_password_validate(self, oldpass):
		resultat = self.__reset_pass_qeury(oldpass)
		if resultat:
			return resultat
		else:
			return None

class ContactModel:
	def __init__(self, nom: str, prenoms: str , numero:str, photo: str, user_id: int):
		assert nom.isalpha(), '''Le nom doit etre en caractere'''

		self._contact_name = nom
		self._contact_lastname = prenoms
		self._contact_number = numero
		self._contact_photo_name = photo
		self._user_id = user_id

	def __get_contact_query(self):
		
		req ='''SELECT * FROM t_repertoire
				CROSS JOIN t_user 	
				WHERE t_repertoire.t_user_id = t_user.id AND t_user.id = 1 '''
	
	def __set_contact(self):
		try:
			db = sqlite3.Connection(config.db_root)
			cursor = db.cursor()
			new_contact = ( self._contact_name, self._contact_lastname, self._contact_number, self._contact_photo_name, self._user_id )
			req = '''INSERT INTO t_repertoire(c_name, c_prenoms, c_numero, c_photo, t_user_id) 
				VALUES (?, ?, ?, ?, ?)'''
			cursor.execute(req, new_contact)
			
		except Exception as e:
			db.rollback()
			print('erreur:', e)
		else:
			db.commit()
			db.close()
			print('db closed')

	def save(self):
		if len(self._contact_name) > 0 and len(self._contact_number) > 0 and self._user_id > 0:
			self.__set_contact()
			return 1
		else:
			return 0


	def __name_checker(self) -> tuple:

		db = sqlite3.Connection(config.db_root)
		cursor = db.cursor()
		req = "SELECT c_name FROM t_repertoire WHERE c_name = ? "
		user_to_check = self._contact_name
		cursor.execute(req, (user_to_check,))
		resultat = cursor.fetchone()
		db.close()

		return resultat

	def __number_checker(self) -> tuple:

		db = sqlite3.Connection(config.db_root)
		cursor = db.cursor()
		req = "SELECT c_numero FROM t_repertoire WHERE c_numero = ? "
		to_check = self._contact_number
		cursor.execute(req, (to_check,))
		resultat = cursor.fetchone()
		db.close()

		return resultat

	def contact_validator(self) -> dict:
		
		check_name = self.__name_checker()
		
		check_number = self.__number_checker()

		return {'name': check_name , 'number': check_number}
	
	def set_photo(self, photo_name):
		self._contact_photo_name = photo_name
		
	
	def __get_id(self):
		db = sqlite3.Connection(config.db_root)
		cursor = db.cursor()
		req = '''SELECT id FROM t_repertoire ORDER By id DESC'''
		cursor.execute(req)
		resultat = list(cursor.fetchone())
		db.close()

		return resultat

	@property
	def get_last_id(self):
		resultat = list(self.__get_id())
		return resultat[0]

	@property
	def get_name(self):
		return self._contact_name

	@property
	def get_number(self):
		return self._contact_number

	@property
	def get_photo(self):
		return self._contact_photo_name





	