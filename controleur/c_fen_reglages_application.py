import tkinter
from tkinter import ttk
from pathlib import Path
import modele.m_access_to_settings as access_app
from controleur.message import AfficherMessage


class FenReglageAppli:

    def __init__(self, fen_para, frame_para):
        self.list_zoom = ['40', '50', '60', '70', '80', '90', '100', '110', '120', '130', '140', '150',
                          '160', '170', '180', '190', '200']
        self.var_zoom = tkinter.StringVar
        self.var_start = tkinter.StringVar
        self.fen_param = fen_para
        self.frame_param = frame_para
        self.directory = Path(__file__).parent.parent
        self.message = AfficherMessage(self.fen_param)
        self.access_appli = access_app.accessToSettings('settings.ini')
        self.var_zoom = tkinter.StringVar(value=self.access_appli.get('app_settings', 'zoom'))
        star = self.access_appli.get('app_settings', 'start')
        start = ''
        if star == 'True' or star == 'False':
            start = star
        self.var_start = tkinter.StringVar(value=start)

    def afficher_fen_reg_app(self):
        label_zoom = ttk.Label(self.frame_param, text='Definissez le zoom (en %):')
        label_zoom.grid(column=1, columnspan=2, row=1)
        combo_zoom = ttk.Combobox(self.frame_param, values=self.list_zoom, textvariable=self.var_zoom)
        combo_zoom.grid(column=3, row=1)

        bouton_appliquer = ttk.Button(self.frame_param, text='Appliquer', command=self.appliquer_app_reglages)
        bouton_appliquer.grid(column=1, columnspan=3, row=2, pady=15)

    def appliquer_app_reglages(self):
        zoom = self.var_zoom.get()
        self.parser_app2 = access_app.accessToSettings('settings.ini')

        if zoom in self.list_zoom:
            self.parser_app2.set('app_settings', 'zoom', zoom)
        else:
            self.message.afficher_mess('erreur', 'La valeur de zoom choisie n\'est pas dans la liste des'
                                                 ' possibilités', 'error')
            return
        self.parser_app2.set('app_settings', 'zoom_need_update', 'True')

        self.message.afficher_mess('Tout est ok.', 'Vos choix ont bien été appliqués!', 'info')
