import sys
import os
from PIL import Image

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

	image = Image.open(image_path)
	if len(img_format) == 1:
		width  = (img_format[0] / image.size[0])
		height = (img_format[0] / image.size[1])
	else:
		width  = (img_format[0] / image.size[0])
		height = (img_format[1] / image.size[1])
		
	try:
		
		image.resize((round(image.size[0]*width), round(image.size[1]*height)))
	except:
		print('Ooops !')

	return image


class SessionData:
	def __init__(self, session_username,session_password, session_user_id):
		self.__session_username = session_username
		self.__session_password = session_password
		self.__session_user_id = session_user_id

	def get_name(self):
		pass