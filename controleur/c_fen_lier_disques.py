import tkinter
from tkinter import ttk
from psutil import disk_partitions
from modele import m_access_to_settings
import psutil

class fenLierDisques():
    def __init__(self, fen_root):
        self.fen_root = fen_root
        self.frame_deja_liers = tkinter.Frame
        self.list_part = []
        self.liste_disks = []
        for part in psutil.disk_io_counters(perdisk=True):
            self.list_part.append(part)
        for disks in disk_partitions(all=False):
            self.liste_disks.append(disks.device)

        self.var_part = tkinter.StringVar()
        self.var_disk = tkinter.StringVar()
        self.fen_lier = tkinter.Toplevel()
        self.creer_liste_part()
        self.creer_liste_disks()
        self.creer_bouton_appliquer()
        self.creer_liste_deja_liers()

    def creer_liste_part(self):
        frame_part = tkinter.Frame(self.fen_lier)
        frame_part.grid(column=1, row=1, pady=20)
        lab = tkinter.Label(frame_part, text='Choisissez ci-dessous une partition: ')
        lab.grid(column=1, row=1)
        combo = ttk.Combobox(frame_part, values=self.list_part, textvariable=self.var_part, width=40)
        combo.grid(column=1, row=2)


    def creer_liste_disks(self):
        frame_disk = tkinter.Frame(self.fen_lier)
        frame_disk.grid(column=1, row=2, pady=20)
        lab_disk = tkinter.Label(frame_disk, text='Choisissez ci_dessous un point de montage: ')
        lab_disk.grid(column=1, row=1)
        combo_disk = ttk.Combobox(frame_disk, values=self.liste_disks, textvariable=self.var_disk, width=40)
        combo_disk.grid(column=1, row=2)

    def creer_bouton_appliquer(self):
        buton_appliquer = tkinter.Button(self.fen_lier, text='Appliquer', command=self.appliquer)
        buton_appliquer.grid(column=1, row=3)

    def creer_liste_deja_liers(self):
        try:
            self.frame_deja_liers.destroy()
        except TypeError:
            pass
        self.frame_deja_liers = tkinter.Frame(self.fen_lier, relief='raised', borderwidth=2)
        self.frame_deja_liers.grid(column=2, row=1)
        lab_deja_liers = tkinter.Label(self.frame_deja_liers, text='Liste des partitons/point de montage déja liés:')
        lab_deja_liers.grid(column=1, row=1, pady=15, padx=15)
        getter_liaisons = m_access_to_settings.accessToSettings('liaisons.ini')
        liste_couples = getter_liaisons.get('liaisons', 'liste').split("==>")
        i = 2
        if len(liste_couples) > 0 and liste_couples != ['']:
            for elements in liste_couples:
                if elements != '':
                    elem = elements.split('=>')
                    lab_element1 = tkinter.Label(self.frame_deja_liers, text=elem[0] + ' <==> ' + elem[1])
                    lab_element1.grid(column=1, row=i)
                    i += 1
        else:
            lab_aucune_liaison = tkinter.Label(self.frame_deja_liers, text='Aucun disque de lié.')
            lab_aucune_liaison.grid(column=1, row=2)
        buton_effacer_derniere = tkinter.Button(self.fen_lier, text='Effacer dernière liaison',
                                                command=self.effacer_derniere_liaison)
        buton_effacer_derniere.grid(column=2, row=2)

    def appliquer(self):
        part = str(self.var_part.get())
        disk = str(self.var_disk.get())
        if part in self.list_part and disk in self.liste_disks:
            geter_appliquer = m_access_to_settings.accessToSettings('liaisons.ini')
            chaine_anciennes = geter_appliquer.get('liaisons', 'liste')
            chaine_nouvelle = chaine_anciennes + '==>' + part + '=>' + disk
            geter_appliquer.set('liaisons', 'liste', chaine_nouvelle)
            self.creer_liste_deja_liers()

    def effacer_derniere_liaison(self):
        getter_eff_liaisons = m_access_to_settings.accessToSettings('liaisons.ini')
        liste_couples = getter_eff_liaisons.get('liaisons', 'liste').split("==>")
        liste_couples.pop(len(liste_couples) - 1)
        getter_eff_liaisons.set('liaisons', 'liste', '==>'.join(liste_couples))
        self.creer_liste_deja_liers()
