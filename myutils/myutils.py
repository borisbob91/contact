import sys
import os
from PIL import Image
#from collections import namedtuple
from typing import NamedTuple
import config 

def set_syspath(absolute_dependencies: list):

	for directory in absolute_dependencies:
		existe = os.path.exists(directory) and os.path.isdir(directory)
	if not existe:
		raise BaseException(f"[set_syspath] le dossier du Python Path [{directory}] n'existe pas")
	else:
		sys.path.insert(0, directory)


def clean_string(string_to_clean) -> tuple:
	""" this is a utility to clean contact item 
	para : tuple
	clean_string(para) -> tuple
	 """
	cleaned_list = []
	if isinstance(string_to_clean, tuple) or isinstance(string_to_clean, list) :
		for item in string_to_clean:
			item = str(item)
			item = item.replace("'", "").replace("+", "").replace("(", "").replace(")", "").replace(" ", "").replace("-", "").replace(".", "")
			cleaned_list.append(item)
		return tuple(cleaned_list)
	elif isinstance(string_to_clean, int) or isinstance(string_to_clean, str):
		item = str(string_to_clean)
		item =  item.replace("'", "").replace("+", "").replace("(", "").replace(")", "").replace(" ", "").replace("-", "").replace(".", "")
		cleaned_list.append(item)
		return tuple(cleaned_list)
	else:
		print("unbable to complete operation")


class ImageEdit:
	def __init__(self, image_path:str, image_format:tuple = (130,), dest:str=None ):
		''' ImageEdit(image_path, [(width,height)]) '''
		extention = ['.png', '.jpeg', '.jpg', '.gif']

		assert image_path.endswith('.png') or image_path.endswith('.jpeg') or image_path.endswith('.jpg') \
			or image_path.endswith('.gif'), ''' format non valide ! '''

		self.image_path = image_path
		self.image_format=  image_format
		self.image = Image.open(self.image_path)
		self.dest = dest

	def __new_size(self):

		if len(self.image_format) == 1:
			width = self.image_format[0]
			height = self.image_format[0]

		elif len(self.image_format) == 2:
			width = self.image_format[0]
			height = self.image_format[1]

		else:
			raise BaseException('impossible de traiter l image')

		return {'width':width, 'height':height}

	def __set_size(self):
		image_format = self.__new_size()
		image = self.image.convert('RGB')
		image = image.resize((image_format.get('width'),  image_format.get('height')))

		return image
	@classmethod
	def init(cls, image_path:str, image_format:tuple = (130,), dest:str=None ):
		cls(image_path, image_format, dest)
		self.save(dest)
		
	def save(self, distination:str =None):

		image = self.__set_size()
		if distination == None:
			try:

				image.save((self.dest))
				return 1
			except Exception as e:
				print('sauvegarde de photo echoué')
				return 0

		else:
			try:

				image.save((distination))
				return 1
			except Exception as e:
				print('sauvegarde de photo echoué')
				return 1


class  Contact_Struct(NamedTuple):
	"""contact structure
	argument :
				c_id: int
				c_nom: str
				c_prenoms : str
				c_numero: str
				c_photo: str
				c_user_id : int

	Return: namedtuple
	"""
	c_id: int
	c_nom: str
	c_prenoms : str
	c_numero: str
	c_photo: str
	c_user_id : int


