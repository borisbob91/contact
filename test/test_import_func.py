import pytest

@pytest.fixture
def data():
    return '/home/borisbob/Documents/gui-dev/contact/contact.txt'

@pytest.fixture
def data2():
    return '/home/borisbob/Documents/gui-dev/contact/contact.csv'

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