from typing import NamedTuple
from collections import namedtuple
import pickle
from config import BASE_DIR
import time
from datetime import date

class SessionCredential(NamedTuple):
	s_username : str
	s_password : str
	s_user_id  : int
	s_active   : int

class SessionData:
	_file = f'{BASE_DIR}/session_data.pickle'
	max_day = 604800
	default_u = ('BotUser', None, 0, 0)

	def __init__(self, session_username:str =None, session_password:str=None, session_user_id:int=None, u_date:str =str(time.time()) ):
		assert isinstance(session_user_id, int) or session_user_id == None, ''' <class: int> '''
		self._session_username = session_username
		self._session_password = session_password
		self._session_user_id = session_user_id
		self._session_create_at = u_date
		global uid_tuple
		uid_tuple = namedtuple('uid_struct', 'u_name u_pdw u_id u_date')
		
	def save(self):
		obj = self.__set_value()
		try:
			session_file = open(SessionData._file, mode='wb')

		except FileNotFoundError:
			'''Fichier introuvable '''
		else:
			pickle_file = pickle.dump(obj, session_file)
		finally:
			session_file.close()

	def __set_value(self):

		if self._session_username != None:
			return (self._session_username, self._session_password, self._session_user_id, self._session_create_at)
		else:
			return SessionData.default_u

	@classmethod
	def read_data(cls):
		try:
			session_file = open(cls._file, 'rb')
		except :
			print('Oops!')

		else:
			pickle_freezed = pickle.load(session_file)
		finally:
			session_file.close()

		checked = SessionData._is_active(pickle_freezed[3])
		if checked:
			return cls(*pickle_freezed)
		else:
			return cls(*cls.default_u)
			self.save()

	@classmethod
	def _is_active(cls, t_date):
		active_time = time.time() - float(t_date)
		if active_time < cls.max_day:
			return True
		else:
			return False

	@property
	def get_name(self):
		return self._session_username

	@property
	def get_pwd(self):
		return self._session_password

	@property
	def get_id(self):
		return self._session_user_id
	@property
	def get_full(self):
		return uid_tuple(self._session_username, self._session_password, self._session_user_id, self._session_create_at)


def write_token(name, pwd, u_id):
	""" to wirte data in pickle file write_token(name, pwd, u_id) """
	user = SessionData(name, pwd, u_id)
	user.save()

def read_token():
	user = SessionData.read_data()

	return user.get_full


if __name__ == '__main__':

	session_username = 'BorisBob'
	session_password = 'mon_pass'
	session_user_id = None

	write_token(*args)
	read_token()

	




	#session_data = SessionCredential("boris","admin",3)
	#a = namedtuple()

	"""
	data_file = open('session_data.pickle', 'wb')

	data_pickle = pickle.dump(session_data,data_file)

	data_file.close()
	"""

	#data_file = open('session_data.pickle', 'rb')

	#freeze_data = pickle.load(data_file)

