import pytest
from myutils import clean_string
import pytest
from csv import Dialect
import sqlite3
contact_format = ['TEL;CELL', 'N', 'FN']
db_formats = ('name','last_name','number')
from copy import deepcopy
import os
import sys
from views.import_contact import ImportContact
FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(FILE_PATH)
IMAGES_DIR = os.path.join(BASE_DIR, 'images')
DB_ROOT = os.path.join(BASE_DIR, 'models')
UID_ROOT = os.path.join(BASE_DIR, 'uid')
db_root = 'models/contact.db'


@pytest.fixture
def file_vcard():
    return r"/home/borisbob/Documents/gui-dev/contact/test/vcard_test.cvf"

def read(path = None) -> list:
    ''' Pour lire les fichiers contact(vcard) format *.vcf ; read(file_path)->list '''
    contact = list()
    bloc= list()
    delimiter = ["BEGIN:VCARD", "END:VCARD"]
    with open(path, mode='r', encoding='utf8') as files:
        item = True
        while files and item:
            line = files.readline().replace('\n', '')
            if str(line) == delimiter[0]:
                """ debut bloc"""
                next_item= True
                bloc = []
                while next_item:
                    next_item=False
                    if str(line) != delimiter[1]:
                        bloc.append(line)
                        line = files.readline().replace('\n', '')
                        next_item=True
                    else:
                        """ fin bloc"""
                        bloc.append(line)
                        #rint(bloc)
            if str(line) != delimiter[1]:
                item = False
            else:
                contact.insert(len(contact)+1, tuple(bloc))
                #contact.append(tuple(bloc))
    return contact

def extrate_contact(args:list) -> object():
    ''' pour extrait les données: extrate_contact([( list ou tuple),])'''
    contacts_dict = []
    contact_tuple = []
    if args:
        for arg in args:
            arg = list(arg)
            bloc = []
            db_format = []
            arg = [x for x in arg if x.split(':')[0] in contact_format and len(arg)>2 if arg]
            for key_value in arg:
                if len(arg)> 2:
                    key , value = key_value.split(':')
                    value = value.replace(';', '')
                    key = key.split(';')[0]
                    item = (key, value)
                    db_format.append(value)
                    bloc.append(item)
            bloc = dict(bloc)
            db_format
            if len(bloc) > 0 : contacts_dict.append(bloc)
            if len(db_format)> 0: contact_tuple.append(tuple(db_format))

    return contact_tuple


def test_vcard_fonct(file_vcard):
    obtenu = read(file_vcard)
    attenu = [(), ('BEGIN:VCARD', 'VERSION:2.1', 'N:;Eddy EpA;;;', 'FN:Eddy EpA', 'TEL;CELL:52981817', 'END:VCARD'), 
        ('BEGIN:VCARD', 'VERSION:2.1', 'N:;Parrain Mohamed 7-89;;;', 'FN:Parrain Mohamed 7-89', 'TEL;CELL:65 85 63 33', 'TEL;CELL:65856333', 'END:VCARD'), 
        ('BEGIN:VCARD', 'VERSION:2.1' ,'N:;Prof Informatic;;;', 'FN:Prof Informatic', 'TEL;CELL:49 35 22 91', 'TEL;CELL:49352291', 'END:VCARD')]
    assert obtenu == attenu

def test_extrator(file_vcard):

    obtenu = extrate_contact(test_vcard_fonct(file_vcard))
    attenu = [('Eddy EpA', 'Eddy EpA', '52981817'),('Parrain Mohamed 7-89', 'Parrain Mohamed 7-89', '65 85 63 33', '65856333'), ('Prof Informatic', 'Prof Informatics', '49 35 22 91', '49352291')]
    assert obtenu == attenu


import csv

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

    


lists =[(367, "DE N'guoran David", '', '+225 0839)3(363', 'img_366', '1', 1, 'admin', 'root', 'master'), (203, 'marie claire', '', '+22549479557', 'img_202', '1', 1, 'admin', 'root', 'master')]

resul = (506, 'achyseka', 'seka achy', '79813397', None, '2')


@pytest.fixture
def data():
    return (506, 'achyseka', 'seka achy', '79813397', None, '2')

def img_id_resolver(resul):
    """try:
        db = sqlite3.Connection(db_root)
        cursor = db.cursor()
        statement = ''' SELECT * FROM t_repertoire WHERE t_user_id = ? ORDER by id DESC '''
        query = (1,)
        cursor.execute(statement, query)
    except Exception as e :
        return None
        print(e)
    else:
        resul = cursor.fetchone()
        
        return resul
    finally:
        db.close()"""
    
    def auto_update(rows = resul):
        if resul:
            rows = deepcopy(list(rows))
            rows[4] = f'img_{rows[0]}'
            return tuple(rows)
    return auto_update()

 
def test_id_resolve(data):
    obtenu = img_id_resolver(data)
    attendu = (506, 'achyseka', 'seka achy', '79813397', 'img_506', '2')

    assert obtenu == attendu

@pytest.fixture
def list_data():
    return r"/home/borisbob/Documents/gui-dev/contact/test/contact.txt"
    
def test_reader(list_data):
    Object = ImportContact()
    obtenu  = Object.read_txt(list_data)

    attendu = [('marusi','Beans','+676282673398'),
                ('Beans','marusi','+676282673398')
                ('damso', 'mausi','+676282678998'),
                ('damso','nept','+676282678998')
    ]

    assert obtenu == attendu
