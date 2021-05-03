
contact_format = ['TEL;CELL', 'N', 'FN']
db_formats = ('name','last_name','number')

        
    
def read() -> list:
    ''' Pour lire les fichiers contact(vcard) format *.vcf ; read(file_path)->list '''
    contact =[]
    delimiter = ["BEGIN:VCARD", "END:VCARD"]
    with open(r"/home/borisbob/Documents/gui-dev/contact/00001.vcf", mode='r', encoding='utf8') as files:
        item = True
        while files and item:
            line = files.readline().replace('\n', '')
            if str(line) == delimiter[0]:
                """ debut bloc"""
                next_item= True
                bloc=[]
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
                contact.append(tuple(bloc))
    return contact

def extrate_contact(args:list) -> object():
    ''' pour extrait les données: extrate_contact([( list ou tuple),])'''
    contacts_dict = []
    contact_tuple = []
    for arg in args:
        arg = list(arg)
        bloc = []
        db_format = []
        arg = [x for x in arg if x.split(':')[0] in contact_format and len(arg)>2]
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

    return contact_tuple, contacts_dict
                              

def map_vcard(files):

    delimiter = ["BEGIN:VCARD", "END:VCARD"]
    next_item = True
    while next_item :
        next_item = False
        line = files.readline().replace('\n', '')
        if line == delimiter[0]:
            if line != delimiter[1]:
                next_item = True
                print(line)
        else:
            print('no match')

    files.close()

