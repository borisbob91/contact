import os
from typing import Union, NoReturn
from interface.tkinker_import import *
from models import ExportModels
from session_data import read_token
from config import  VCARD_FORMAT, DATA_ROOT, DELIMITER, vcard_VERSION
from interface.message_box import show_info, show_warming

class ExportContact(ExportModels):
    my_directory = os.path.expanduser('~') + '/Documents'
    _my_contact_file = os.path.join(my_directory, "contact.")
    contact_format = None
    def __init__(self, user_id = None):
        super().__init__(user_id)

    @staticmethod
    def __get_file_directory():
        """ to get directory where to save user data from dialogue window """

        my_directory = filedialog.askdirectory(initialdir= os.path.expanduser('~') + '/Documents')
        return my_directory

    def choose_directory(self):
        ExportContact.my_directory = self.__get_file_directory()

    def run_export(self):
        Export  = ExportModels.init_export(read_token().u_id)
        contact_list = Export.get_data()
        format_choosed = self.get_format()

        if format_choosed in self.action_callback().keys():
            action = self.action_callback().get(format_choosed)
            action(format_choosed, contact_list)
        else:
            show_warming('Attention', 'Veuillez choisir le format de fichier')
   

    @staticmethod
    def make_dict(lists: list, contact_format: list= VCARD_FORMAT ) -> list:
        dico = []
        for index in range(len(lists)):
            d = list()
            for key, elem in enumerate(lists[index]):
                for i, j in zip(contact_format, lists[index]):
                    contact_dico = (str(i), str(j))
                    d.append(contact_dico)
            d = dict(d)
            dico.append(d)
        return dico

    @staticmethod
    def patch_contact(lists:list ):
        Contact_list = []
        for row in lists:
            row = row[:3]
            name, l_name, num = row
            if not l_name:
                l_name = name
            Contact_list.append((str(name), str(l_name), str(num)))        
        return Contact_list
    
    def make_vcf(self, extension, contact_list: Union[list or tuple], delimiter = DELIMITER, mode='a'):
        """ pour ecrit dans le fichier vcard
            recoit une list de données d'un contact
            return 1 si ok sinon 0
        """
        serialize_num = self.format_num
        patcher = self.patch_contact
        number_duplication = 2

        my_file = ExportContact._my_contact_file + extension
        files = open(my_file, mode= 'w', encoding='utf-8')
        
        contact_dict = self.make_dict(patcher(contact_list))
        for contact in contact_dict:
            files.write(delimiter[0] + '\n')
            files.write(f'VERSION:{vcard_VERSION}\n')
            i = len(VCARD_FORMAT) + number_duplication
            for key in contact.keys():
                if key == 'TEL;CELL':
                    files.write(f"{key}:{serialize_num(contact[key]).get('num1')}" + f'{i * ";"}' + '\n')
                    files.write(f"{key}:{serialize_num(contact[key]).get('num2')}"  + f'{i * ";"}' + '\n')
                    files.write(f"{key}:{serialize_num(contact[key]).get('num3')}" + f'{i * ";"}' + '\n')
                else:
                    files.write(f'{key}:{contact[key]}' + f'{i * ";"}' + '\n')
                i = 0
            files.write(delimiter[1] + '\n')
        files.close()
        show_info("info", f'importation terminie. \n Destination: {my_file}')
            

    def make_csv(self, extension, contact_list) -> NoReturn:
        import csv
        my_file = ExportContact._my_contact_file + extension

        with open(my_file, 'w', newline='') as csvfile:
            fieldnames = ['nom', 'prénoms', 'numero']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for contact in contact_list:
                name , l_name, num = contact
                if not l_name:
                    l_name = name
                writer.writerow({'nom': name, 'prénoms': l_name, 'numero': num})
        show_info("info", f'importation terminie. \n Destination: {my_file}')
                 
    def make_txt(self, extension, contact_list, delimiter = ','):
        my_file = ExportContact._my_contact_file + extension

        with open(my_file, 'w', newline='') as files:
            fieldnames = ['nom', 'prénoms', 'numero']
            files.write(f"{fieldnames[0]} {delimiter} {fieldnames[1]} {delimiter} {fieldnames[2]}\n")
            for contact in contact_list:
                name , l_name, num = contact
                if not l_name:
                    l_name = name
                files.write(f'{name} {delimiter} {l_name} {delimiter} {num}\n')
        show_info("info", f'importation terminie. \n Destination: {my_file}')

    def get_format(self):
        """  to retrieve the value of contact file format extension name"""
        return self.select_format_box.get()

    @staticmethod
    def format_num(num):
        if '+225' in num:
            num = num[len('+225'):]
        if " " in num:
            num = num.replace(' ','')
        if len(num) %  2 == 0:
            num = num.strip()
            y = list(num[::2])
            w = list(num[1::2])
            size = len(w)
            lists = []
            for i in range(size):
                row = str(y[i]) + str(w[i])
                lists.append(row)
            num1 = '+225 ' + ' '.join(lists)
            num2 = '+225' + ''.join(lists)
            num3 = ' '.join(lists)
            num4 = ''.join(lists)
            
        else:
            num1 = num
            num2 = num
            num3 = num
            num4 = num
        
        return {'num1':num1, 'num2':num2, 'num3':num3, 'num4':num4}

    def action_callback(self):
        ''' make a callback of function for action choosed '''

        return {'vcf': self.make_vcf, 'csv': self.make_csv, 'txt': self.make_txt}
    
        



