import os
from typing import Union, NoReturn
from interface.tkinker_import import *
from models import ExportModels
from session_data import read_token
from config import  VCARD_FORMAT, DATA_ROOT, DELIMITER, vcard_VERSION
from interface.message_box import show_info

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

    def patch_contact(self, lists:list ):

        for row in lists:
            name, l_name, num = row
            if not l_name:
                l_name = name
            
    
    def make_vcf(self, extension, contact_list: Union[list or tuple], delimiter = DELIMITER, mode='a'):
        """ pour ecrit dans le fichier vcard
            recoit une list de données d'un contact
            return 1 si ok sinon 0
        """
        my_file = ExportContact._my_contact_file + extension
        files = open(my_file, mode= 'a', encoding='utf-8')
        contact_dict = self.make_dict(contact_list)
        for contact in contact_dict:
            files.write(delimiter[0] + '\n')
            files.write(f'VERSION:{vcard_VERSION}\n')
            i = len(VCARD_FORMAT) - 1 
            for key in contact.keys():
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

    def action_callback(self):
        ''' make a callback of function for action choosed '''

        return {'vcf': self.make_vcf, 'csv': self.make_csv, 'txt': self.make_txt}
    
        



