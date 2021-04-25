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


def image_resize(image_path: str, img_format:tuple = (130,) ):
	''' image_resize(image_file, (width, [height]) '''

	#assert  image_path.isfile(image_path),    ''' mauvais fichier: image_resize(image_file, (width, [height]))'''
	#assert  len(img_format) == 1 or len(img_format) == 2 , ''' mauvais format: image_resize(image_file, (width, [height]))'''
	assert image_path.endswith('.png') or image_path.endswith('.jpeg') or image_path.endswith('.jpg') \
	or image_path.endswith('.gif'), ''' format non valide ! '''

	image = Image.open(image_path)
	if len(img_format) == 1:
		width = img_format[0]
		height = img_format[1]
	else:
		width = img_format[0]
		height = img_format[0]
	try:
		
		image.resize((width, height))
	except:
		print('Ooops !')

	return image


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
	c_id: int
	c_nom: str
	c_prenoms : str
	c_numero: str
	c_photo: str
	c_user_id : int

