
import sqlite3

from interface.message_box import  show_error, show_info, show_warming
import base64
import config
from copy import deepcopy
from models import db_config

class UserModel:

	def __init__(self, username, password=None, secret=None):
		self._username = username
		self._password = password
		self._secret = secret

	@property
	def get_user_data(self):
		if self.__user_verification():
			return (self._username, self._password, self.get_id[0])

	def __set_user(self):
		db = sqlite3.Connection(config.db_root)
		cursor = db.cursor()
		new_user = (self._username, self._password, self._secret)
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
		req = '''SELECT  t_user_name, t_user_passe FROM t_user WHERE t_user_name = ? AND t_user_passe = ?'''
		user_input_data = (self._username, self._password)
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
			user_session = (self._username,)
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
		user_input_data = (self._username, old_secret)
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

			req = '''SELECT * FROM t_repertoire
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
		
		return [contact[:6] for contact in self.__get_contact_query()]

	def __query_search(self, query, table_code):
		id_user = self.get_id[0] 
		if id_user > 0 :
			if table_code == 1:
				try:
					db = sqlite3.connect(config.db_root)
					cursor = db.cursor()
					req_data = (f"{query}%", f"{query}%", id_user)
					req = """ SELECT * FROM t_repertoire  WHERE ( c_name like ? or c_prenoms like ? ) and t_user_id = ? GROUP BY c_name"""
					cursor.execute(req, req_data)
				except:
					print('erreur recherche')
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
				raise BaseException('''indiquer une table correct''')
			return resultat

	def search_contact_by_name(self, query):
		table_code = 1
		return self.__query_search(query, table_code)

	def search_contact_by_number(self, query):
		table_code = 0
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

	def __init__(self, nom: str=None, prenoms: str=None, numero: str=None, photo: str=None, \
		user_id: int=None, contact_id: int=None):
		# assert str(nom).isalnum() or nom == None, '''Le nom doit etre en caractere'''
		assert str(user_id).isnumeric() or user_id == None , 'id: <class int> and required'

		if nom : nom = deepcopy(nom.lower())
		if prenoms : prenoms = deepcopy(prenoms.lower())

		self._contact_name = nom		
		self._contact_lastname = prenoms
		self._contact_number = numero
		self._contact_photo_name = photo
		self._user_id = user_id
		self._contact_id = contact_id

	def checking_data(self):
		if (self._contact_name or self._contact_number):
			print('erreur')
		else:
			assert self._contact_name != None or self._contact_number != None, 'Fournit un nom ou Numero' 
			print('erreur')

	def __set_contact(self):
		try:
			db = sqlite3.Connection(config.db_root)
			cursor = db.cursor()
			new_contact = (self._contact_name, self._contact_lastname, self._contact_number, self._contact_photo_name, self._user_id)
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
			req = "SELECT id, c_name, c_prenoms FROM t_repertoire WHERE (c_name = ? and c_prenoms = ? ) and t_user_id = ? "
			user_to_check = (self._contact_name, self._contact_lastname, self._user_id)
		except Exception as e:
			print("erreur: ", e)
		else:
			cursor.execute(req, user_to_check)
			resultat = cursor.fetchone()
		finally:
			db.close()

		return resultat

	def __number_checker(self) -> tuple:
		try:

			db = sqlite3.Connection(config.db_root)
			cursor = db.cursor()
			req = "SELECT c_numero FROM t_repertoire WHERE c_numero = ? and t_user_id = ?"
			to_check = (self._contact_number, self._user_id)
			cursor.execute(req, to_check)
		except Exception as e:
			print('erreur db', e)
		else:
			resultat = cursor.fetchone()
			db.close()

		return resultat

	def contact_validator(self) -> dict:
		check_name = []
		check_id = []
		if self.__name_checker():

			check_name = self.__name_checker()[1:]
			check_id = self.__name_checker()[0]
		
		check_number = self.__number_checker()

		return {'id': check_id, 'name': check_name , 'number': check_number}

	def set_photo(self, photo_name):
		self._contact_photo_name = photo_name	
	
	def __get_id(self) -> tuple:
		''' return contact id '''
		db = sqlite3.Connection(config.db_root)
		cursor = db.cursor()
		req = '''SELECT id FROM t_repertoire ORDER By id DESC'''
		cursor.execute(req)
		resultat = tuple(cursor.fetchone())
		db.close()

		return resultat

	def __contact_update_query(self) -> int:
		try:
			db = sqlite3.Connection(config.db_root)		
			cursor = db.cursor()
			query = (self._contact_name, self._contact_lastname, self._contact_number, self._contact_photo_name , self._contact_id , self._user_id)
			statment = ''' UPDATE t_repertoire SET c_name = ? , c_prenoms = ?, c_numero = ?, c_photo = ? WHERE id = ? and t_user_id = ? '''
			cursor.execute(statment, query)
		except Exception as e:
			db.rollback()
			return 0
			print('update echoué !', e)
		else:
			db.commit()
			return 1
		finally:
			db.close()

	def __get_last_row_query(self, contact_id: int, photo_name, user_id: int):
		""" Obet
		
		Keyword arguments:
		contact_id : int (id contact de la base de donnée)
		photo_name : str (image à rennomer)
		user_id : int (id de l'utilisateur)
		argument -- description
		Return: un tuple avec la photo rennommer comme ce-ci: "img_contact_id"

		"""
	
		try:
			db = sqlite3.Connection(config.db_root)		
			cursor = db.cursor()
			query = (photo_name, contact_id, user_id)
			statment = ''' UPDATE t_repertoire SET  c_photo = ? WHERE id = ? and t_user_id = ? '''
			cursor.execute(statment, query)
		except Exception as e:
			db.rollback()
			return 0
			print('update echoué !', e)
		else:
			db.commit()
			return 1
		finally:
			db.close()

	def update_img(self):
		self._contact_photo_name = f'img_{self._contact_id}'

	def __update_validator_query(self) -> tuple:
		resultat = ()
		try:
			db = sqlite3.Connection(config.db_root)
			cursor = db.cursor()
			query = (self._contact_name, self._contact_lastname, self._contact_id, self._user_id)
			statement = ''' SELECT count(*) FROM t_repertoire WHERE c_name = ? and c_prenoms = ?  AND id != ? and t_user_id = ? '''
			cursor.execute(statement, query)
		except Exception as e:
			print('probleme de verification de donnée')
			print(e)
		else:
			resultat = cursor.fetchall()
			db.close()
		return resultat[0]
	
	def update_valide(self) -> bool:
		
		if self.__update_validator_query()[0] == 0:
			q = True  # on accepte la modification
		else:
			q = False
		return q

	def update(self):
		return self.__contact_update_query()

	def __contact_delete_query(self):
		"""Contact delection fonction from DB"""
		
		statement = ''' DELETE from t_repertoire WHERE id = ? and t_user_id = ? '''
		query = (self._contact_id, self._user_id)
		try:
			db = sqlite3.Connection(config.db_root)
			cursor = db.cursor()
			cursor.execute(statement, query)
		except Exception as e:
			return False
			print("suppression echoué ", e)
		else:
			db.commit()
		finally:
			db.close()
			return True


	def delete(self):
		return self.__contact_delete_query()
		
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
		return str(self._contact_name) + ' ' + str(self._contact_lastname)

	@property
	def get_number(self):
		return self._contact_number

	@property
	def get_photo(self):
		return self._contact_photo_name

	@property
	def get_user_id(self):
		return self._user_id


class ImportModels(ContactModel):

	def __init__(self, name, l_name, num, u_id):
		super().__init__(nom=name, prenoms=l_name, numero=num, user_id=u_id)

	@classmethod
	def init(cls, name, last_name, number, user_id: int):
		""" Initialize class : 
			ImportContact(name, last_name, number, [user_id]) 
		
		args:
			name: str
			last_name: str
			number: int
			user_id: int
		"""
		if name == last_name:
			last_name = ''
		else:
			last_name = deepcopy(last_name.lower())	
				
		if name: name = deepcopy(name.lower())
		
		return cls(name, last_name, number, user_id)


class ExportModels:
	def __init__(self, user_id = None):
		self._user_id = user_id
	
	@classmethod
	def init_export(cls, user_id: int):
		""" Initialize class : 
			ExportModels(user_id)
			this method must run before __retreive_contact_query() methode
		
		args:
			user_id: int
		"""
		
		return cls(int(user_id))
		
	def get_data(self):
		return self.__get_all_contact_query()

	def __get_all_contact_query(self):
		rows = []
		try:
			db = sqlite3.Connection(config.db_root)
			cursor = db.cursor()
			statement = """ SELECT c_name, c_prenoms, c_numero FROM t_repertoire WHERE t_user_id = ? ORDER by c_name """
			query = (self._user_id,)
			cursor.execute(statement, query)
		except Exception as e:
			print("export: selete db fail. ", e)
		else:
			rows = cursor.fetchall()
		finally:
			db.close()
		return rows
	
			

class CheckSuperUser:

	def __init__(self, u_id=None, username=None, pwd=None):
		self.username = username
		self.pwd = pwd
		self.u_id = u_id

	def __contains__(self, u_id, username, pwd):
		pass

	@classmethod
	def init(cls, u_id, username, pwd):
		db = sqlite3.Connection(config.db_root)
		cursor = db.cursor()
		# query = (self.u_id, self.username, self.pwd)
		query = (u_id, username, pwd)
		statment = """ SELECT t_user_name as name FROM t_user WHERE id = ? AND t_user_name = ? AND t_user_passe = ? """
		row = cursor.execute(statment, query)

		return row.fetchone()
		
