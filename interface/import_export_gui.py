#! user/bin/env python3
#coding: utf-8

from views.import_contact import ImportContact, import_main

from .tkinker_import import *

class ImportExport(ImportContact):
    
    _formt_list = ['vcf','txt', 'csv']

    def __init__(self, top):
        super().__init__()
        self.import_export_frame = tk.LabelFrame(top)
        self.import_export_frame.place(relx=0.329, rely=0.597, relheight=0.219
                , relwidth=0.659)
        self.import_export_frame.configure(relief='groove')
        self.import_export_frame.configure(text='''Import / Export''')

        self.select_format_box = ttk.Combobox(self.import_export_frame)
        self.select_format_box.place(relx=0.226, rely=0.221, relheight=0.11
                , relwidth=0.261, bordermode='ignore')
        self.select_format_box.configure(font="-family {gothic} -size 11")
        self.select_format_box.configure(textvariable='')
        self.select_format_box.configure(value = ImportExport._formt_list)
        self.select_format_box.set('choisir un format')

        self.Label2 = tk.Label(self.import_export_frame)
        self.Label2.place(relx=0.017, rely=0.221, height=16, width=130
                , bordermode='ignore')
        self.Label2.configure(font="-family {gothic} -size 11")
        self.Label2.configure(text='''Choix Format :''')

        self.Label3 = tk.Label(self.import_export_frame)
        self.Label3.place(relx=0.2, rely=0.517, height=16, width=189
                , bordermode='ignore')
        self.Label3.configure(relief="sunken")
        self.Label3.configure(text='''c:/user/.../folder''')

        self.TButton3 = ttk.Button(self.import_export_frame)
        self.TButton3.place(relx=0.025, rely=0.497, height=22, width=94
                , bordermode='ignore')
        self.TButton3.configure(takefocus="")
        self.TButton3.configure(text='''Destination''')

        self.export_btn = ttk.Button(self.import_export_frame)
        self.export_btn.place(relx=0.238, rely=0.731, height=22, width=114
                , bordermode='ignore')
        self.export_btn.configure(takefocus="")
        self.export_btn.configure(text='''Exporter''')

        self.TSeparator2 = ttk.Separator(self.import_export_frame)
        self.TSeparator2.place(relx=0.539, rely=0.11, relheight=0.876
                , bordermode='ignore')
        self.TSeparator2.configure(orient="vertical")

        self.select_file_btn = ttk.Button(self.import_export_frame)
        self.select_file_btn.place(relx=0.666, rely=0.421, height=22, width=94
                , bordermode='ignore')
        self.select_file_btn.configure(takefocus="")
        self.select_file_btn.configure(text='''Fichier''')
        self.select_file_btn.configure(command=self._select_file)
        
        self.path_var = tk.StringVar()
        self.path_var.set('''c:/user/.../folder''')
        self.lable_path = tk.Label(self.import_export_frame)
        self.lable_path.place(relx=0.582, rely=0.221, height=16, width=200
                , bordermode='ignore')
        self.lable_path.configure(activebackground="#f9f9f9")
        self.lable_path.configure(relief="sunken")
        self.lable_path.configure(textvariable=self.path_var)

        self.import_btn = ttk.Button(self.import_export_frame)
        self.import_btn.place(relx=0.651, rely=0.738, height=22, width=114
                , bordermode='ignore')
        self.import_btn.configure(takefocus="")
        self.import_btn.configure(text='''Importer''')
        self.import_btn.configure(command=self.run)
        