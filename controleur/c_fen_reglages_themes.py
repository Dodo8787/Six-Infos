import tkinter
from tkinter import ttk
from tkinter import *
from pathlib import Path
from ttkthemes import ThemedTk
import os
from controleur import message
import shutil
from controleur import starting_verif
from modele import m_access_to_settings
from psutil import cpu_count, disk_partitions


class ReglagesThemes:

    frame_gene = ttk.Frame
    var_theme = tkinter.StringVar
    directory = Path
    ro = ThemedTk

    def __init__(self, frame_gen, ro2t):
        self.frame_gene = frame_gen
        self.var_theme = tkinter.StringVar()
        self.directory = Path(__file__).parent.parent
        self.directory_themes = str(self.directory) + '/Themes/'
        self.ro = ro2t
        self.frame_theme = tkinter.Frame

        parser_theme = m_access_to_settings.accessToSettings('theme.ini')
        self.theme_actuel = parser_theme.get('theme', 'theme_actuel')
        self.name_new_theme = tkinter.StringVar()
        self.liste_caracteres_interdits = ['/', '*', '$']

    def appliquer_theme(self):
        parser_theme = m_access_to_settings.accessToSettings('theme.ini')
        theme = self.var_theme.get()
        self.theme_actuel = theme
        parser_theme.set('theme', 'theme_actuel', theme)
        parser_settings = m_access_to_settings.accessToSettings('settings.ini')
        parser_settings.set('app_settings', 'update', 'True')

    def afficher_fen(self):
        try:
            self.frame_theme.destroy()
        except TypeError:
            pass
        self.frame_theme = tkinter.Frame(self.frame_gene)
        self.frame_theme.grid(column=1, row=1)
        theme_label = ttk.Label(self.frame_theme, text='Choisissez le thème a appliquer:')
        theme_label.grid(column=1, columnspan=3, sticky=W, row=1, padx=5, pady=25)
        col = 1
        row = 2
        list_dir = os.listdir(self.directory_themes)
        list_dir.sort()
        for dire in list_dir:
            combo_theme = ttk.Radiobutton(self.frame_theme, text=dire, variable=self.var_theme,
                                          value=dire, command=self.appliquer_theme)
            combo_theme.grid(column=col, row=row)
            if col == 6:
                row += 1
                col = 0
            col += 1
        self.var_theme.set(self.theme_actuel)

        bouton_appliquer = ttk.Button(self.frame_theme, text='Appliquer', command=self.appliquer_theme)
        bouton_appliquer.grid(columnspan=3, column=1, row=5, pady=25)
        bouton_suprimer = ttk.Button(self.frame_theme, text='Supprimer theme sélectionné',
                                     command=self.supprimer_theme)
        bouton_suprimer.grid(columnspan=3, column=4, row=5, pady=25)
        entry = ttk.Entry(self.frame_theme, textvariable=self.name_new_theme, width=50)
        entry.grid(columnspan=6, column=1, row=6)
        bouton_ajouter_theme = tkinter.Button(self.frame_theme, text='Créer theme',
                                              command=self.creer_theme)
        bouton_ajouter_theme.grid(column=1, row=7, columnspan=6)

    def creer_theme(self):
        name_theme = self.name_new_theme.get()
        carac_interdit = False
        for carac in self.liste_caracteres_interdits:
            if carac in name_theme:
                carac_interdit = True
        if name_theme == '' or len(name_theme) > 13 or carac_interdit:
            mess = message.AfficherMessage(self.ro)
            mess.afficher_mess('Erreur', 'Veuillez entrer un nom de theme dont la longueur est'
                                         ' inférieur a 13 caractères et qui ne contient pas '
                                         'les caractéres /, *, ou $.', 'error')
            return

        carac_interdit = False
        try:
            os.makedirs(self.directory_themes + name_theme + '/')
        except FileExistsError:
            mess = message.AfficherMessage(self.ro)
            mess.afficher_mess('Erreur', 'Un theme nommé {} existe déja.'.format(name_theme), 'error')
            return

        self.var_theme.set(name_theme)
        self.appliquer_theme()
        nbr_core = cpu_count()
        list_disk = disk_partitions()
        starting_verif.Verif_file_ini_to_start(nbr_core, list_disk)
        self.afficher_fen()

    def supprimer_theme(self):
        theme = self.var_theme.get()
        if theme == '':
            mess = message.AfficherMessage(self.ro)
            mess.afficher_mess('Erreur', 'Aucun theme sélectionné.', 'error')
            return
        elif theme == 'Defaut':
            mess = message.AfficherMessage(self.ro)
            mess.afficher_mess('Erreur', 'Le theme "Defaut" ne peut pas etre supprimé.', 'error')
            return
        else:
            mess = message.AfficherMessage(self.ro)
            rep = mess.afficher_mess('Confirmation', 'Voullez vous vraime supprimer le theme nommé "{}" ?'
                                     .format(theme), 'yesno')
            if rep == False:
                return
            else:
                shutil.rmtree(self.directory_themes + self.var_theme.get())
                self.theme_actuel = 'Defaut'
                parser_theme = m_access_to_settings.accessToSettings('theme.ini')
                parser_theme.set('theme', 'theme_actuel', 'Defaut')
                self.var_theme.set('Defaut')
                self.appliquer_theme()
                self.afficher_fen()
