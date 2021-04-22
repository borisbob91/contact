from typing import NamedTuple
import pickle

session_username = 'BorisBob'
session_password = 'mon_pass'
session_user_id = None

class SessionData:
	def __init__(self, session_username,session_password, session_user_id):
		self.__session_username = session_username
		self.__session_password = session_password
		self.__session_user_id = session_user_id
	@property
	def get_name(self):
		return self.__session_username

	@property
	def get_password(self):
		return self.__session_password

	@property
	def get_id(self):
		return self.__session_user_id

class SessionCredential(NamedTuple):
	s_username : str
	s_password : str
	s_user_id  : int


session_data = SessionCredential("boris","admin",3)

"""
data_file = open('session_data.pickle', 'wb')

data_pickle = pickle.dump(session_data,data_file)

data_file.close()
"""

data_file = open('session_data.pickle', 'rb')

freeze_data = pickle.load(data_file)

print(freeze_data)


