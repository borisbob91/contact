# coding:utf-8
from interface.pop.progress_gui import progress_launcher, PopProgressGui, progress_destroy, set_size

from typing import NoReturn
from models import ImportModels
from interface.tkinker_import import *
from interface.message_box import show_info
import os
from models import ImportModels
from session_data import read_token
from time import time, sleep
from config import DATA_ROOT
from typing import Union
from copy import deepcopy

taille = ''
class ImportContact(ImportModels):
	contact_format = ['TEL;CELL', 'N', 'FN']
	VERSION = 2.1
	delimiter = ['BEGIN:VCARD', 'END:VCARD']

	def __init__(self, name=None, l_name=None, num=None, u_id=None, path=None):
		super().__init__(name, l_name, num, u_id)
		self.name = name
		self.l_name = l_name
		self.number = num
		self.user_id = u_id
		self.file_path = path
		self.conctact = []

	@staticmethod
	def __get_file() -> str:
		""" Get Contact file from dialogue window """

		file_path = filedialog.askopenfilename(initialdir=os.path.expanduser('~') + '/Documents', title='fichier contact', \
		filetypes=(("vcard file", "*.vcf"), ("csv file", '*.csv'), ('text file', '*.txt')))
		return file_path
	
	def _select_file(self) -> str:
		file_path = self.__get_file()
		if file_path:
			self.file_path = file_path
			_file = file_path.split('/')
			_file = f'{_file[1]}/../{_file[-2]}/{_file[-1]}'
			# from gui
			self.path_var.set(_file)

		return file_path

	@staticmethod
	def read_cvf(contact_path: str) -> list:
		''' Pour lire les fichiers contact(vcard) format *.vcf ; read(file_path)->list '''
		contact = []
		delimiter = ["BEGIN:VCARD", "END:VCARD"]
		with open(f'{contact_path}', mode='r', encoding='utf8') as files:
			item = True
			while files and item:
				line = files.readline().replace('\n', '')
				if str(line) == delimiter[0]:
					""" debut bloc"""
					next_item = True
					bloc = []
					while next_item:
						next_item = False
						if str(line) != delimiter[1]:
							bloc.append(line)
							line = files.readline().replace('\n', '')
							next_item = True
						else:
							""" fin bloc"""
							bloc.append(line)
							# print(bloc)
				if str(line) != delimiter[1]:
					item = False
				else:
					contact.append(tuple(bloc))
		return contact
	
	@staticmethod
	def read_txt(file_path):
		lists = []
		with open(file_path) as files:
			files.readline()
			for line in files:
				if ',' in line:
					line = line.strip().split(',')
				elif ';' in line:
					line = line.split(';')
				lists.append(tuple(line))
		return lists

	
	def read_csv(self, file_path):
		return self.read_txt(file_path)

	@staticmethod
	def extrate_contact_cvf(args: Union[list or tuple ]) -> list:
		''' pour extrait les données: extrate_contact([( list ou tuple),])'''
		contacts_dict = []
		contact_tuple = []
		for arg in args:
			row = list(arg)
			bloc = []
			db_format = []
			row = [x for x in row if x.split(':')[0] in ImportContact.contact_format and len(arg)>2]
			for key_value in row:
				if len(arg) > 2:
					key , value = key_value.split(':')
					value, key = value.replace(';', ''), key.split(';')[0]
					item = (key, value)
					db_format.append(value)
					bloc.append(item)
			bloc = dict(bloc)
			if len(bloc) > 0 : contacts_dict.append(bloc)
			if len(db_format)> 0: contact_tuple.append(tuple(db_format))

		return contact_tuple
	
	
	def extrate_contact(self, args: Union[list or tuple]) -> list:
		contact_list = []
		if len(args) > 0:
			for arg in args:
				if len(arg) == 3:
					contact_list.append(arg)
				elif len(arg) > 3:
					contact_list.append(arg[:3])
				else:
					pass
			return contact_list

	def clean_contact(self, contact_list: Union[list or tuple]) -> tuple:
		contact = deepcopy(list(contact_list))
		name, l_name, num = None, None, None
		if len(contact) >=2:
			if len(contact) > 3:
				contact = contact[:3]
			elif len(contact) ==2 :
				contact.insert(1, contact[0])
			else:
				pass
			
			name, l_name, num = contact

			if name == l_name:
				l_name = ''
			else:
				l_name = deepcopy(l_name.lower())	
			if name: name = deepcopy(name.lower())

			return name, l_name, num
		return False			

	def __read_by_format(self, filename):
		contact_list = []
		if filename.endswith('.vcf'):
			contact_list = self.extrate_contact_cvf(self.read_cvf(filename))
		elif filename.endswith('.txt'):
			contact_list = self.extrate_contact(self.read_txt(filename))
		elif filename.endswith('.csv'):
			contact_list = self.extrate_contact(self.read_csv(filename))
		else:
			raise BaseException('format non supproté')
		return contact_list

	def run(self, *args, **kwargs):
		if self.file_path:
			current_user_id = read_token().u_id
			compt_ok = 0
			compt_fail = 0
			compt_doubl = 0
			start = time()
			contact_list = self.__read_by_format(self.file_path)
			assert len(contact_list) > 0, ''' La liste de contact à traiter est vide !'''
			for contact in contact_list:
				if self.clean_contact(contact):
					name, l_name, num = self.clean_contact(contact)
					Import  = ImportModels(name, l_name, num, current_user_id )
					validate = Import.contact_validator()
					if validate.get('name') or validate.get('number'):
						compt_doubl += 1
					else:
						img_name = f'img_{Import.get_last_id + 1}'
						Import.set_photo(img_name)
						succes = Import.save()
						if succes:
							compt_ok += 1
						else:
							compt_fail += 1
				else:
					compt_fail += 1
			end = time()
			show_info('Importation terminé:', f' Operations Total: {len(contact_list)} éffectuées en {end-start}s. \n succès: {compt_ok}\
				\n echouées:{compt_fail}  \n doublons: {compt_doubl} \n ')
		else:
			show_info('info', 'selectionner un fichier contact')

	@property
	def get_path(self):
		if self.file_path:
			return self.file_path


def import_main():
	cvf = ImportContact()
	print(cvf.get_path)


if __name__ == '__main__':
	import_main()
