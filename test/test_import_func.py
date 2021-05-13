import pytest

@pytest.fixture
def data():
    return '/home/borisbob/Documents/gui-dev/contact/contact.txt'

@pytest.fixture
def data2():
    return '/home/borisbob/Documents/gui-dev/contact/contact.csv'

@pytest.fixture
def data3():
    return '/home/borisbob/Documents/gui-dev/contact/test/00001.csv'

def read_txt(file_path):
    lists = []
    with open(file_path) as files:
        
        for line in files:
            if ',' in line:
                line = line.strip().split(',')
                lists.append(tuple(line))
            elif ';' in line:
                line = line.split(';')
                lists.append(tuple(line))
        return lists


def read_cvs(file_path):
    with open(file_path) as files:
        lists = []
        files.readline()
        for line in files:
            if ',' in line:
                line = line.strip().split(',')
                lists.append(tuple(line))
            elif ';' in line:
                line = line.strip().split(';')
                lists.append(tuple(line))
            else:
                raise BaseException("delimiteur supporté : ',' | ';' ")
        return lists


def test_read_txt(data):
    obtenu = read_txt(data)

    attendu = [("'Ali Elise'", " ''", " '+2250789864411'"),
                ("'Amira'", " ''", " '+2250749878726'"),
                ("'Binate'", " ''", " '+22558903779'"),
                ("'Bintou'", " ''", " '+2250748643225'"),
                ("'Bitty '", " 'Bitty'", " '53095702'"),
                ("'Bledja Ode'", " ''", " '+22502474057'"),
                ("'Carmen'", " ''", " '+22567672911'"),
                ("'DE Diallo'", " ''", " '07944987'")
    ]

    assert  obtenu == attendu

def test_read_cvs(data2):
    obtenu = read_cvs(data2)

    attendu = [('Baked', 'Beans', '981772625'),
                ('Lovely', 'Spam', '8797656545'),
                ('Wonderful', 'Spam', '09867143533')
    ]

    assert obtenu == attendu


class Export:
    def __init__(self, *args):
        self.args = args
        
    def extrate_contact_cvf(func):
        
        @staticmethod
        def wrapper(para, *args):

            ''' pour extrait les données: extrate_contact([( list ou tuple),])'''
            args = func(para)
            contact_format = ['TEL;CELL', 'N', 'FN']
            contacts_dict = []
            contact_tuple = []
            for arg in args:
                row = list(arg)
                bloc = []
                db_format = []
                row = [x for x in row if x.split(':')[0] in contact_format and len(arg)>2]
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
        return wrapper

    @extrate_contact_cvf
    def read(path = None, *args):
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
                    next_item = True
                    bloc = []
                    while next_item:
                        next_item = False
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
    
    def run(self, path):
        return self.read(path)


def test_decorateur(data3):

    bob = Export()
    obtenu = bob.run(data3)

    with open(r'./test_contact.txt') as files:
        obtenu = files.read()

    attendu = list(obtenu)

    assert obtenu == attendu