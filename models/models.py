
import sqlite3

from interface.message_box import  show_error, show_info,show_warming
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
			user_and_pass = self.__get_user()
	
		return {'user': user_and_pass}


	def __get_user(self):

		db = sqlite3.Connection(config.db_root)
		cursor = db.cursor()
		req = '''SELECT t_user_name, t_user_passe FROM t_user WHERE t_user_name = ? AND t_user_passe = ?'''
		user_input_data = (self._username, self._password )
		cursor.execute(req, user_input_data)
		resultat = cursor.fetchone()
		db.close()

		return resultat

	def __get_user_id(self):
		resultat = None
		try:
			db = sqlite3.Connection(config.db_root)
			cursor = db.cursor()
			req = '''SELECT id FROM t_user WHERE t_user_name = ?'''
			user_session = (self._username, )
			cursor.execute(req, user_session)

		except Exception as e:
			db.close()
			print('erreur db:', e)
		else:
			resultat = tuple(cursor.fetchone())
			db.close()

		return resultat

	@property
	def get_id(self):
		qs = self.__get_user_id()
		if qs != None:
			return qs
		else:
			return 0


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


	def __get_contact_query(self):
		try:

			req ='''SELECT * FROM t_repertoire
					INNER JOIN t_user	
				    ON t_repertoire.t_user_id = t_user.id AND t_user.id = ? ORDER BY c_name '''

			id_user = self.get_id

			db = sqlite3.Connection(config.db_root)
			cursor = db.cursor()
			cursor.execute(req, id_user)
		except  Exception as e:
			print('selection de donnée echoué:', e)
		else:
			resultat = cursor.fetchall()
		finally:
			db.close()

		return resultat

	def get_contact_list(self):

		return self.__get_contact_query()

	def __query_search(self, query, table_code):
		id_user = self.get_id[0] 
		if id_user > 0 :
			if table_code == 1:

				try:
					db = sqlite3.connect(config.db_root)
					cursor = db.cursor()
					req_data = (f"{query}%", id_user)
					req = """ SELECT * FROM t_repertoire  WHERE c_name like ? and t_user_id = ? GROUP BY c_name"""
					cursor.execute(req, req_data)
				except Exception as e:
					print(e)

				else:
					resultat = cursor.fetchall()
				finally:
					db.close()

			elif table_code == 0:
				try:
					db = sqlite3.connect(config.db_root)
					cursor = db.cursor()
					req_data = (f"{query}%", id_user)
					req = """ SELECT * FROM t_repertoire  WHERE c_numero like ? and t_user_id = ? GROUP BY c_numero"""
					cursor.execute(req, req_data)
				except Exception as e:
					print(e)

				else:
					resultat = cursor.fetchall()
				finally:
					db.close()
			else:
				raise AssertionError ; '''indiquer un table correct'''

		return resultat

	def search_contact_by_name(self, query, table_code):
		return self.__query_search(query, table_code)

	def checking_data(self):
		if not self._username.isalnum() or ' ' in self._username :
			title = 'Attention'
			msg = "le champ ' Nom ' ne peut contenir d'espace ni de symbole et d'espace "
			show_warming(title, msg)
			assert self._username.isalnum(), "Saisie un nom correct"
		if ' ' in self._password:
			show_warming('Attention', "le champ 'password' ne peuvent contenir d'espace")
			assert not ' ' in self._password, "pas d'espace dans le mot de passe"
		if ' ' in self._secret:
			show_warming('Attention', "le champ 'secret' ne peuvent contenir d'espace")
			assert not ' ' in self._secret, ''' pas d'espace dans le secret '''



class ContactModel:
	def __init__(self, nom: str=None, prenoms: str =None, numero:str = None, photo: str=None, user_id=None):
		assert nom.isalnum(), '''Le nom doit etre en
		 caractere'''
		assert str(user_id).isnumeric() and user_id != None , 'id: <class int> and required'

		self._contact_name = nom
		self._contact_lastname = prenoms
		self._contact_number = numero
		self._contact_photo_name = photo
		self._user_id = user_id

	def checking_data(self):
		if (self._contact_name or self._contact_number):
			pass
		else:
			assert self._contact_name != None or self._contact_number != None, 'Fournit un nom ou Numero' 

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
			print('erreur d\'ajouter contact:', e)
		else:
			db.commit()
			db.close()
			print('données enrégistrées et db fermé !')

	def save(self):
		if len(self._contact_name) > 0 and len(self._contact_number) > 0 and self._user_id > 0:
			self.__set_contact()
			return 1
		else:
			return 0

	def __name_checker(self):
		try:
			db = sqlite3.Connection(config.db_root)
			cursor = db.cursor()
			req = "SELECT c_name FROM t_repertoire WHERE c_name = ? and t_user_id = ? "
			user_to_check = (self._contact_name, self._user_id)
		except Exception as e:
			db.rollback()
			print("erreur: ",e)
		else:
			cursor.execute(req, user_to_check)
			resultat = cursor.fetchone()
		finally:
			db.close()

		return resultat

	def __number_checker(self):
		try:

			db = sqlite3.Connection(config.db_root)
			cursor = db.cursor()
			req = "SELECT c_numero FROM t_repertoire WHERE c_numero = ? and t_user_id = ?"
			to_check = (self._contact_number,self._user_id)
			cursor.execute(req, to_check)
		except Exception as e:
			db.rollback()
			print('erreur db', e)
		else:
			resultat = cursor.fetchone()
			db.close()

		return resultat

	def contact_validator(self) -> dict:
		
		check_name = self.__name_checker()
		
		check_number = self.__number_checker()

		return {'name': check_name , 'number': check_number}
	
	def set_photo(self, photo_name):
		self._contact_photo_name = photo_name
		
	
	def __get_id(self) ->tuple:
		db = sqlite3.Connection(config.db_root)
		cursor = db.cursor()
		req = '''SELECT id FROM t_repertoire ORDER By id DESC'''
		cursor.execute(req)
		resultat = tuple(cursor.fetchone())
		db.close()

		return resultat

	def set_id(self, c_id):
		self._user_id = c_id

	@property
	def get_last_id(self):
		resultat = tuple(self.__get_id())
		return resultat[0]

	@property
	def get_name(self):
		return self._contact_name

	@property
	def get_full_name(self):
		return str(self._contact_name)+' '+ str(self._contact_lastname)

	@property
	def get_number(self):
		return self._contact_number

	@property
	def get_photo(self):
		return self._contact_photo_name

	@property
	def get_user_id(self):
		return self._user_id

	def search_by_name(self):
		pass

class ContactEditModle(ContactModel):
	def __init__(self):
		super().__init__()

	def update(self, contact_id):
		pass






	