import tkinter
from tkinter import font
from tkinter import ttk
from controleur import message
from modele import m_access_to_settings
from controleur import fen_liste_police


class fenFontNetw:
    def __init__(self, fen_param, frame_param):
        self.fen_param = fen_param
        self.frame_param = frame_param
        self.list_font = list(font.families())
        self.list_font.append("Arial")
        self.list_font.sort()
        self.mess = message.AfficherMessage(self.fen_param)
        self.acces = m_access_to_settings.accessToSettings('font.ini')
        self.var_netw_infos = tkinter.StringVar(value=str(self.acces.get('netw_font', 'netw_infos')))
        self.var_netw_down = tkinter.StringVar(value=str(self.acces.get('netw_font', 'netw_down')))
        self.var_netw_up = tkinter.StringVar(value=str(self.acces.get('netw_font', 'netw_up')))

    def appliquer(self):
        error = 0
        access_font_netw = m_access_to_settings.accessToSettings('font.ini')
        infos = str(self.var_netw_infos.get())
        if infos not in self.list_font:
            error += 1
        else:
            access_font_netw.set('netw_font', 'netw_infos', infos)
        down = str(self.var_netw_down.get())
        if down not in self.list_font:
            error += 1
        else:
            access_font_netw.set('netw_font', 'netw_down', down)
        up = str(self.var_netw_up.get())
        if up not in self.list_font:
            error += 1
        else:
            access_font_netw.set('netw_font', 'netw_up', up)
        access_font_netw_settings = m_access_to_settings.accessToSettings('settings.ini')
        access_font_netw_settings.set('app_settings', 'update', 'True')
        mess = message.AfficherMessage(self.fen_param)
        if error == 0:
            mess.afficher_mess('Tout est ok', 'Les paramètres sont bien appliqués!', 'info')
        else:
            mess.afficher_mess('Hummm...', 'Il y a ' + str(error) + ' paramètres incorrect(s), les autres ont été appliqués.',
                               'info')

    def afficher_liste_police(self):
        fen_liste_polices = fen_liste_police.fenListePolice()
        fen_liste_polices.afficher_fen()

    def afficher_frame_font_netw(self):
        self.bouton_liste_pol = tkinter.Button(self.frame_param, text='Cliquez ici pour afficher la liste des polices',
                                               command=self.afficher_liste_police)
        self.bouton_liste_pol.grid(column=1, row=1, columnspan=2, pady=4, padx=4)

        self.lab_font_infos = tkinter.Label(self.frame_param, text='Network Infos')
        self.lab_font_infos.grid(column=1, row=2, sticky=tkinter.E)
        self.comb_font_inf = ttk.Combobox(self.frame_param, values=self.list_font, textvariable=self.var_netw_infos)
        self.comb_font_inf.grid(column=2, row=2, sticky=tkinter.W)

        self.lab_down = tkinter.Label(self.frame_param, text='Débit Down')
        self.lab_down.grid(column=1, row=3, sticky=tkinter.E)
        self.comb_down = ttk.Combobox(self.frame_param, values=self.list_font, textvariable=self.var_netw_down)
        self.comb_down.grid(column=2, row=3, sticky=tkinter.W)

        self.lab_up = tkinter.Label(self.frame_param, text='Débit Up')
        self.lab_up.grid(column=1, row=4, sticky=tkinter.E)
        self.comb_up = ttk.Combobox(self.frame_param, values=self.list_font, textvariable=self.var_netw_up)
        self.comb_up.grid(column=2, row=4, sticky=tkinter.W)

        self.bouton_valider = ttk.Button(self.frame_param, text='Appliquer', command=self.appliquer)
        self.bouton_valider.grid(column=1, columnspan=2, row=5, pady=4)
