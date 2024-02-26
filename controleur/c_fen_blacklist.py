import tkinter
from tkinter import ttk
from modele import m_access_to_settings


class fenBlacklist():
    def __init__(self, win_root):
        self.var_entry_pm = tkinter.StringVar()
        self.fen_blac = tkinter.Toplevel()
        self.invite = tkinter.Label(self.fen_blac, text='Entrez ci-dessous le point de montage a ajouter a la blacklist'
                                                        '\n(cela peut être une portion du point de montage).')
        self.invite.grid(column=1, row=1)
        self.input = tkinter.Entry(self.fen_blac, width=40, textvariable=self.var_entry_pm)
        self.input.grid(column=1, row=2, pady=5)
        self.bouton_valider = tkinter.Button(self.fen_blac, text='Valider', command=self.valider_entry)
        self.bouton_valider.grid(column=1, row=3, pady=5)
        self.frame_liste = tkinter.Frame(self.fen_blac)
        self.frame_liste.grid(column=1, row=4, pady=10)
        self.label_liste = tkinter.Label(self.frame_liste, text='Ci-dessous les points de montage blacklistés:')
        self.label_liste.grid(column=1, row=1)
        self.frame_blacked = tkinter.Frame(self.frame_liste)
        self.frame_blacked.grid(column=1, row=2)
        self.refresh_liste_blacked()
        self.bouton_enlever = tkinter.Button(self.frame_liste, text='Supprimer dernier élément',
                                             command=self.supprimer_dernier)
        self.bouton_enlever.grid(column=1, row=3, pady=5)

    def refresh_liste_blacked(self):
        self.frame_blacked.destroy()
        self.frame_blacked = tkinter.Frame(self.frame_liste)
        self.frame_blacked.grid(column=1, row=2)
        getter_blacked = m_access_to_settings.accessToSettings('settings.ini')
        liste_blacked = getter_blacked.get('disk', 'blacklist').split('=>')
        i = 0
        for elem in liste_blacked:
            lab = tkinter.Label(self.frame_blacked, text=elem)
            lab.grid(column=1, row=i + 1)
            i += 1

    def valider_entry(self):
        getter_valider = m_access_to_settings.accessToSettings('settings.ini')
        liste_blacked = getter_valider.get('disk', 'blacklist').split('=>')
        if len(self.var_entry_pm.get()) > 0:
            if liste_blacked == ['La liste est vide']:
                liste_blacked = []
            liste_blacked.append(str(self.var_entry_pm.get()))
            getter_valider.set('disk', 'blacklist', '=>'.join(liste_blacked))
            getter_valider.set('app_settings', 'update', 'True')
            self.var_entry_pm.set('')
            self.refresh_liste_blacked()


    def supprimer_dernier(self):
        getter_supp = m_access_to_settings.accessToSettings('settings.ini')
        liste_blacked = getter_supp.get('disk', 'blacklist').split('=>')
        liste_blacked.pop(len(liste_blacked) - 1)
        if len(liste_blacked) == 0:
            liste_blacked = ['La liste est vide']
        getter_supp.set('disk', 'blacklist', '=>'.join(liste_blacked))
        getter_supp.set('disk_reglages', 'update', 'True')
        self.refresh_liste_blacked()
