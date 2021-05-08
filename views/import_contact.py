# coding:utf-8
from typing import NoReturn
from models import ImportModels
from interface.tkinker_import import *
from interface.message_box import show_info
import os
from models import ImportModels
from session_data import read_token
from time import time
from typing import Union
from copy import deepcopy

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
	def get_file() -> str:
		""" Get Contact file from dialogue window """

		file_path = filedialog.askopenfilename(initialdir=os.path.expanduser('~') + '/Documents', title='fichier contact', \
		filetypes=(("vcard", "*.vcf"), ("excel", '*.cvs'), ('text', '*.txt')))
		return file_path
	
	def _select_file(self) -> str:
		file_path = self.get_file()
		self.file_path = file_path
		_file = file_path.split('/')
		_file = f'{_file[1]}/../{_file[-2]}/{_file[-1]}'
		# from gui
		self.path_var.set(_file)

		return file_path

	@staticmethod
	def read_cvf(contact_path) -> list:
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
	def extrate_contact_cvf(args: Union[list or tuple ]) -> list:
		''' pour extrait les données: extrate_contact([( list ou tuple),])'''
		contacts_dict = []
		contact_tuple = []
		for arg in args:
			arg = list(arg)
			bloc = []
			db_format = []
			arg = [x for x in arg if x.split(':')[0] in ImportContact.contact_format and len(arg)>2]
			for key_value in arg:
				if len(arg) > 2:
					key , value = key_value.split(':')
					value, key = value.replace(';', ''), key.split(';')[0]
					item = (key, value)
					db_format.append(value)
					bloc.append(item)
			bloc = dict(bloc)
			db_format
			if len(bloc) > 0 : contacts_dict.append(bloc)
			if len(db_format)> 0: contact_tuple.append(tuple(db_format))

		return contact_tuple, contacts_dict
	
	def __get_from_format(self, filename):
		contact_list = []
		if filename.endswith('.vcf'):

			contact_list = self.extrate_contact_cvf(self.read_cvf(filename))
			
		elif filename.endswith('.txt'):
			file_extention = '.txt'

		elif filename.endswith('.csv'):

			file_extention = '.csv'
		else:
			raise BaseException('format non supproté')

		return contact_list


	def run(self):
		if self.file_path:
			start = time()
			current_user_id = read_token().u_id
			compt_ok = 0
			compt_fail = 0
			compt_doubl = 0

			contact_list = self.__get_from_format(self.file_path)
			for contact in contact_list[0]:
				contact = list(contact)
				if len(contact) == 4:
					contact.pop(2)
				elif len(contact) == 5:
					contact.pop(2)
					contact.pop(2)
				elif len(contact) > 5:
					raise BaseException('Format de donnée non supporté !: max 4 args ')

				contact = tuple(contact)
				name, l_name, num = contact
				# check new methode
				"""self.init( current_user_id)
				valide = self.contact_validator()
				if valide.get('name'):
					print('exist :', valide.get('name'))
				if valide.get('number'):
					print('exist :', valide.get('number'))"""

				if name == l_name:
					l_name = ''
				else:
					l_name = deepcopy(l_name.lower())	
				
				if name: name = deepcopy(name.lower())
			
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
			end = time()
			show_info('info',f'Impport terminé: \n operations Total: {len(contact_list[0])} en {end-start}s. \n succès: {compt_ok}\
				\n echouées:{compt_fail}  \n doublons: {compt_doubl} \n ')

		else:
			show_info('info', 'selectionner un fichier contact')

	@property
	def get_path(self):
		return self.file_path


def import_main():
	cvf = ImportContact()
	print(cvf.get_path)


if __name__ == '__main__':
	import_main()
