import tkinter
from tkinter import font
from tkinter import ttk
from modele import m_access_to_settings
from controleur import fen_liste_police
from controleur import message
from psutil import cpu_count


class fenFontCpu():

    def __init__(self, fen_paramn, frame_param):

        self.fen_param = fen_paramn
        self.frame_param = frame_param
        self.messa = message.AfficherMessage(self.fen_param)
        self.list_font = list(font.families())
        self.list_font.append("Arial")
        self.gaiteur = m_access_to_settings.accessToSettings('font.ini')
        self.var_combo_cpu_inf = tkinter.StringVar(value=str(self.gaiteur.get('Cpu', 'cpu_infos')))
        self.var_combo_cpu_load = tkinter.StringVar(value=str(self.gaiteur.get('Cpu', 'cpu_load')))
        self.var_combo_cpu_freq = tkinter.StringVar(value=str(self.gaiteur.get('Cpu', 'cpu_freq')))
        self.var_combo_ram_go = tkinter.StringVar(value=str(self.gaiteur.get('Cpu', 'ram_go')))
        self.var_combo_ram_pourc = tkinter.StringVar(value=str(self.gaiteur.get('Cpu', 'ram')))
        self.var_combo_cores_pourc = tkinter.StringVar(value=str(self.gaiteur.get('Cpu', 'core1')))
        self.var_combo_temp = tkinter.StringVar(value=str(self.gaiteur.get('Cpu', 'temp')))
        self.frame_right = tkinter.Canvas

    def afficher_liste_police(self):
        fen_exemples = fen_liste_police.fenListePolice()
        fen_exemples.afficher_fen()

    def appliquer_reglages(self):
        gait_font = m_access_to_settings.accessToSettings('font.ini')
        i = 0
        if str(self.var_combo_cpu_inf.get()) in self.list_font:
            gait_font.set('Cpu', 'cpu_infos', str(self.var_combo_cpu_inf.get()))
            i += 1
        else:
            pass
        if str(self.var_combo_cpu_load.get()) in self.list_font:
            gait_font.set('Cpu', 'cpu_load', str(self.var_combo_cpu_load.get()))
            i += 1
        else:
            pass
        if str(self.var_combo_cpu_freq.get()) in self.list_font:
            gait_font.set('Cpu', 'cpu_freq', str(self.var_combo_cpu_freq.get()))
            i += 1
        else:
            pass
        if str(self.var_combo_ram_go.get()) in self.list_font:
            gait_font.set('Cpu', 'ram_go', str(self.var_combo_ram_go.get()))
            i += 1
        else:
            pass
        if str(self.var_combo_ram_pourc.get()) in self.list_font:
            gait_font.set('Cpu', 'ram', str(self.var_combo_ram_pourc.get()))
            i += 1
        else:
            pass
        j = 0
        while j < cpu_count():
            core_name = 'core' + str(j + 1)
            if str(self.var_combo_cores_pourc.get()) in self.list_font:
                gait_font.set('Cpu', core_name, str(self.var_combo_cores_pourc.get()))
                if j == 0:
                    i += 1
            else:
                pass
            j += 1
        if str(self.var_combo_temp.get()) in self.list_font:
            gait_font.set('Cpu', 'temp', str(self.var_combo_temp.get()))
            i += 1
        else:
            pass
        if i == 7:
            self.messa.afficher_mess('Tout est ok !', 'Vos choix ont été appliqués en intégralité.', 'info')
        else:
            self.messa.afficher_mess('Erreur', 'Un ou plusieurs paramètres ne peuvent pas etre appliqués\n'
                                               'car il ne sont pas dans la liste des polices autorisées.',
                                     'error')
        if i >= 1:
            gait_font_settings = m_access_to_settings.accessToSettings('settings.ini')
            gait_font_settings.set('app_settings', 'update', 'True')

    def afficher_frame_font_cpu(self):
        self.frame_font_cpu = tkinter.Frame(self.frame_param)
        self.frame_font_cpu.grid(column=1, row=1)
        buton_aff_samples = tkinter.Button(self.frame_font_cpu,
                                           text="Cliquez ici pour afficher la liste des polices",
                                           command=self.afficher_liste_police)
        buton_aff_samples.grid(column=1, row=1, columnspan=2, padx=4, pady=4)
        self.list_font.sort()

        self.lab_cpu_infos = tkinter.Label(self.frame_font_cpu, text='Cpu Infos')
        self.lab_cpu_infos.grid(column=1, row=2, sticky=tkinter.E)
        self.combobox_cpu_inf = ttk.Combobox(self.frame_font_cpu, values=self.list_font,
                                             textvariable=self.var_combo_cpu_inf)
        self.combobox_cpu_inf.grid(column=2, row=2, sticky=tkinter.W)

        self.cpu_load = tkinter.Label(self.frame_font_cpu, text='Cpu load')
        self.cpu_load.grid(column=1, row=3, sticky=tkinter.E)
        self.combobox_cpu_load = ttk.Combobox(self.frame_font_cpu, values=self.list_font,
                                             textvariable=self.var_combo_cpu_load)
        self.combobox_cpu_load.grid(column=2, row=3, sticky=tkinter.W)

        self.cpu_freq = tkinter.Label(self.frame_font_cpu, text='Cpu freq')
        self.cpu_freq.grid(column=1, row=4, sticky=tkinter.E)
        self.combobox_cpu_freq = ttk.Combobox(self.frame_font_cpu, values=self.list_font,
                                              textvariable=self.var_combo_cpu_freq)
        self.combobox_cpu_freq.grid(column=2, row=4, sticky=tkinter.W)

        self.ram_go = tkinter.Label(self.frame_font_cpu, text='Ram')
        self.ram_go.grid(column=1, row=5, sticky=tkinter.E)
        self.combobox_ram_go = ttk.Combobox(self.frame_font_cpu, values=self.list_font,
                                            textvariable=self.var_combo_ram_go)
        self.combobox_ram_go.grid(column=2, row=5, sticky=tkinter.W)

        self.ram_pourc = tkinter.Label(self.frame_font_cpu, text='Ram % utilisé')
        self.ram_pourc.grid(column=1, row=6, sticky=tkinter.E)
        self.combobox_ram_pourc = ttk.Combobox(self.frame_font_cpu, values=self.list_font,
                                              textvariable=self.var_combo_ram_pourc)
        self.combobox_ram_pourc.grid(column=2, row=6, sticky=tkinter.W)

        self.cores_pourc = tkinter.Label(self.frame_font_cpu, text='Cores % utilisé')
        self.cores_pourc.grid(column=1, row=7, sticky=tkinter.E)
        self.combobox_cores_pourc = ttk.Combobox(self.frame_font_cpu, values=self.list_font,
                                              textvariable=self.var_combo_cores_pourc)
        self.combobox_cores_pourc.grid(column=2, row=7, sticky=tkinter.W)

        self.temp = tkinter.Label(self.frame_font_cpu, text='Temperature')
        self.temp.grid(column=1, row=8, sticky=tkinter.E)
        self.combobox_temp = ttk.Combobox(self.frame_font_cpu, values=self.list_font,
                                                 textvariable=self.var_combo_temp)
        self.combobox_temp.grid(column=2, row=8, sticky=tkinter.W)

        self.bouton_valider = tkinter.Button(self.frame_font_cpu, text='Appliquer', command=self.appliquer_reglages)
        self.bouton_valider.grid(column=1, columnspan=2, row=9)


