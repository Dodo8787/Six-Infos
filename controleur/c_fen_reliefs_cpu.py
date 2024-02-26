import tkinter
from tkinter import ttk
from modele import m_access_to_settings
from controleur import message
from controleur import liste_reliefs
class fenReliefsCpu():

    def __init__(self, fen_param, frame_param):
        self.fen_param = fen_param
        self.frame_param = frame_param
        self.textvar = []
        self.list_actuel_relief = []
        self.list_lab_actuel_relief = []
        self.liste_reliefs = ['unchange', 'flat', 'raised', 'sunken', 'groove', 'ridge', 'solid']
        getter_reliefs_cpu = m_access_to_settings.accessToSettings('reliefs.ini')
        self.relief_widg = getter_reliefs_cpu.get('cpu', 'widg')
        self.relief_ram = getter_reliefs_cpu.get('cpu', 'ram')
        self.relief_cores = getter_reliefs_cpu.get('cpu', 'cores')
        self.liste_pour_ini = ['widg', 'ram', 'cores']
        self.creer_params_cpu()

    def creer_params_cpu(self):
        liste_reliefs.afficherListeReliefs(self.frame_param, self.liste_reliefs)
        list_labels = []

        text = ['Relief widget cpu: ', 'Relief barre ram: ', 'Relief cores: ']
        reliefs = [self.relief_widg, self.relief_ram, self.relief_cores]
        self.textvar = [tkinter.StringVar(), tkinter.StringVar(), tkinter.StringVar()]
        i = 0
        while i < 3:
            list_labels.append(tkinter.Label(self.frame_param, text=text[i]))
            list_labels[i].grid(column=1, row=i + 2)
            self.list_actuel_relief.append(tkinter.Frame(self.frame_param, relief=reliefs[i], borderwidth=3))
            self.list_actuel_relief[i].grid(column=2, row=i + 2)
            self.list_lab_actuel_relief.append(tkinter.Label(self.list_actuel_relief[i], text=reliefs[i]))
            self.list_lab_actuel_relief[i].grid(column=1, row=1)
            combo = ttk.Combobox(self.frame_param, values=self.liste_reliefs, textvariable=self.textvar[i])
            combo.grid(column=3, row=i + 2)
            self.textvar[i].set('unchange')
            i += 1
        bouton_valider = tkinter.Button(self.frame_param, text='Appliquer', command=self.appliquer)
        bouton_valider.grid(column=1, columnspan=3, row=i + 2)

    def appliquer(self):
        error = 0
        i = 0
        getter_set = m_access_to_settings.accessToSettings('reliefs.ini')
        for var in self.textvar:
            var = var.get()
            if var not in self.liste_reliefs:
                error += 1
            if var == 'unchange':
                i += 1
                continue
            else:
                self.actualiser_actuel_relief(i, var)
                getter_set.set('cpu', self.liste_pour_ini[i], var)
                getter_updt = m_access_to_settings.accessToSettings('settings.ini')
                getter_updt.set('app_settings', 'update', 'True')
            i += 1

    def actualiser_actuel_relief(self, i, var):
        self.list_actuel_relief[i].configure(relief=var)
        self.list_lab_actuel_relief[i].configure(text=var)
