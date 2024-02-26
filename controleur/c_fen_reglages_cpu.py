import tkinter
from controleur.message import AfficherMessage
from tkinter import ttk
from configparser import ConfigParser
from pathlib import Path
from modele import m_access_to_settings


class FenReglCpu:
    fen_para = tkinter.Toplevel
    messa = AfficherMessage
    fram_param = ttk.Frame
    directory = ''
    var_aff_load = tkinter.StringVar
    var_aff_freq = tkinter.StringVar
    var_aff_ram_go = tkinter.StringVar
    var_bar_ram = tkinter.StringVar
    var_pourc_ram = tkinter.StringVar
    aff_bar_core = tkinter.StringVar
    parser_cpu = ConfigParser
    aff_pourc_cores = tkinter.StringVar
    unite_degres_cpu = tkinter.StringVar
    var_tj_max = tkinter.StringVar

    def __init__(self, fen_param, fram_para):
        self.fen_para = fen_param
        self.messa = AfficherMessage(self.fen_para)
        self.fram_param = fram_para
        self.parser_cpu = m_access_to_settings.accessToSettings('settings.ini')
        self.var_aff_load = tkinter.StringVar(value=self.parser_cpu.get('cpu_reglages', 'afficher_load'))
        self.var_aff_freq = tkinter.StringVar(value=self.parser_cpu.get('cpu_reglages', 'afficher_freq'))
        self.var_aff_ram_go = tkinter.StringVar(value=self.parser_cpu.get('cpu_reglages', 'afficher_ram_go'))
        self.var_bar_ram = tkinter.StringVar(value=self.parser_cpu.get('cpu_reglages', 'aff_bar_ram'))
        self.var_pourc_ram = tkinter.StringVar(value=self.parser_cpu.get('cpu_reglages', 'aff_pourc_ram'))
        self.aff_bar_core = tkinter.StringVar(value=self.parser_cpu.get('cpu_reglages', 'aff_bar_cores'))
        self.aff_pourc_cores = tkinter.StringVar(value=self.parser_cpu.get('cpu_reglages', 'aff_pourc_cores'))
        self.unite_degres_cpu = tkinter.StringVar(value=self.parser_cpu.get('cpu_reglages', 'degres_cpu'))
        self.var_tj_max = tkinter.StringVar(value=self.parser_cpu.get('cpu_reglages', 'tj_max'))

    def afficher_reg_cpu(self):
        fram_gen = ttk.Frame(self.fram_param)
        fram_gen.grid(column=1, row=1)

        aff_load_lab = ttk.Label(fram_gen, text='Afficher "load cpu"?')
        aff_load_lab.grid(column=1, columnspan=2, row=1)
        aff_load_oui = ttk.Radiobutton(fram_gen, text='Oui', variable=self.var_aff_load, value='True')
        aff_load_oui.grid(column=3, row=1)
        aff_load_non = ttk.Radiobutton(fram_gen, text='Non', variable=self.var_aff_load, value='False')
        aff_load_non.grid(column=4, row=1)

        aff_freq_cpu = ttk.Label(fram_gen, text='Afficher fréquence cpu?')
        aff_freq_cpu.grid(column=1, columnspan=2, row=2)
        aff_freq_oui = ttk.Radiobutton(fram_gen, text='Oui', variable=self.var_aff_freq, value='True')
        aff_freq_oui.grid(column=3, row=2)
        aff_freq_non = ttk.Radiobutton(fram_gen, text='Non', variable=self.var_aff_freq, value='False')
        aff_freq_non.grid(column=4, row=2)

        aff_ram_go = ttk.Label(fram_gen, text='Afficher ram ("ram go/go")?')
        aff_ram_go.grid(column=1, columnspan=2, row=3)
        aff_ram_oui = ttk.Radiobutton(fram_gen, text='Oui', variable=self.var_aff_ram_go, value='True')
        aff_ram_oui.grid(column=3, row=3)
        aff_ram_non = ttk.Radiobutton(fram_gen, text='Non', variable=self.var_aff_ram_go, value='False')
        aff_ram_non.grid(column=4, row=3)

        aff_bar_ram = ttk.Label(fram_gen, text='Afficher barre ram?')
        aff_bar_ram.grid(column=1, columnspan=2, row=4)
        aff_bar_ram_oui = ttk.Radiobutton(fram_gen, text='Oui', variable=self.var_bar_ram, value='True')
        aff_bar_ram_oui.grid(column=3, row=4)
        aff_bar_ram_non = ttk.Radiobutton(fram_gen, text='Non', variable=self.var_bar_ram, value='False')
        aff_bar_ram_non.grid(column=4, row=4)

        aff_pourc_ram = ttk.Label(fram_gen, text='Afficher % ram?')
        aff_pourc_ram.grid(column=1, columnspan=2, row=5)
        aff_pourc_ram_oui = ttk.Radiobutton(fram_gen, text='Oui', variable=self.var_pourc_ram, value='True')
        aff_pourc_ram_oui.grid(column=3, row=5)
        aff_pourc_ram_non = ttk.Radiobutton(fram_gen, text='Non', variable=self.var_pourc_ram, value='False')
        aff_pourc_ram_non.grid(column=4, row=5)

        aff_bar_cores = ttk.Label(fram_gen, text='Afficher barre Cores?')
        aff_bar_cores.grid(column=1, columnspan=2, row=6)
        aff_bar_cor_oui = ttk.Radiobutton(fram_gen, text='Oui', variable=self.aff_bar_core, value='True')
        aff_bar_cor_oui.grid(column=3, row=6)
        aff_bar_cor_non = ttk.Radiobutton(fram_gen, text='Non', variable=self.aff_bar_core, value='False')
        aff_bar_cor_non.grid(column=4, row=6)

        aff_pour_cores = ttk.Label(fram_gen, text='Afficher % cores?')
        aff_pour_cores.grid(column=1, columnspan=2, row=7)
        aff_pour_cor_oui = ttk.Radiobutton(fram_gen, text='Oui', variable=self.aff_pourc_cores, value='True')
        aff_pour_cor_oui.grid(column=3, row=7)
        aff_pour_cor_non = ttk.Radiobutton(fram_gen, text='Non', variable=self.aff_pourc_cores, value='False')
        aff_pour_cor_non.grid(column=4, row=7)

        aff_temp_cpu = ttk.Label(fram_gen, text='Afficher temperature cpu en:')
        aff_temp_cpu.grid(column=1, columnspan=2, row=8)
        temp_c = ttk.Radiobutton(fram_gen, text='°Celsius', variable=self.unite_degres_cpu, value='celsius')
        temp_c.grid(column=3, row=8)
        temp_f = ttk.Radiobutton(fram_gen, text='°Fahrenheit', variable=self.unite_degres_cpu, value='fahrenheit')
        temp_f.grid(column=4, row=8)

        label_adj_tj = ttk.Label(fram_gen, text='Choisir T°c max cpu (Tj):')
        label_adj_tj.grid(column=1, columnspan=2, row=9)
        entry_tj = ttk.Entry(fram_gen, textvariable=self.var_tj_max)
        entry_tj.grid(column=3, row=9)

        boutton_appliquer = ttk.Button(fram_gen, text='Appliquer', command=self.appliquer_reglages)
        boutton_appliquer.grid(column=1, columnspan=4, row=10, pady=15)

    def appliquer_reglages(self):
        load = self.var_aff_load.get()
        self.parser_cpu = m_access_to_settings.accessToSettings('settings.ini')
        if load == 'True':
            self.parser_cpu.set('cpu_reglages', 'afficher_load', 'True')
        else:
            self.parser_cpu.set('cpu_reglages', 'afficher_load', 'False')
        freq = self.var_aff_freq.get()
        if freq == 'True':
            self.parser_cpu.set('cpu_reglages', 'afficher_freq', 'True')
        else:
            self.parser_cpu.set('cpu_reglages', 'afficher_freq', 'False')
        ram = self.var_aff_ram_go.get()
        if ram == 'True':
            self.parser_cpu.set('cpu_reglages', 'afficher_ram_go', 'True')
        else:
            self.parser_cpu.set('cpu_reglages', 'afficher_ram_go', 'False')
        bar_ram = self.var_bar_ram.get()
        if bar_ram == 'True':
            self.parser_cpu.set('cpu_reglages', 'aff_bar_ram', 'True')
        else:
            self.parser_cpu.set('cpu_reglages', 'aff_bar_ram', 'False')
        pourc_ram = self.var_pourc_ram.get()
        if pourc_ram == 'True':
            self.parser_cpu.set('cpu_reglages', 'aff_pourc_ram', 'True')
        else:
            self.parser_cpu.set('cpu_reglages', 'aff_pourc_ram', 'False')
        aff_bar_cores = self.aff_bar_core.get()
        if aff_bar_cores == 'True':
            self.parser_cpu.set('cpu_reglages', 'aff_bar_cores', 'True')
        else:
            self.parser_cpu.set('cpu_reglages', 'aff_bar_cores', 'False')
        pourc_cores = self.aff_pourc_cores.get()
        if pourc_cores == 'True':
            self.parser_cpu.set('cpu_reglages', 'aff_pourc_cores', 'True')
        else:
            self.parser_cpu.set('cpu_reglages', 'aff_pourc_cores', 'False')
        degr_cpu = self.unite_degres_cpu.get()
        if degr_cpu == 'celsius':
            self.parser_cpu.set('cpu_reglages', 'degres_cpu', 'celsius')
        else:
            self.parser_cpu.set('cpu_reglages', 'degres_cpu', 'fahrenheit')
        tj_max = self.var_tj_max.get()
        try:
            if tj_max == 'auto':
                pass
            else:
                tj_max = int(tj_max)
                if tj_max < 0 or tj_max > 250:
                    self.messa.afficher_mess('erreur', 'La temperature doit être comprise entre 0°c et 250°c où entrez'
                                                   ' "auto" pour la laisser par défaut.', 'error')
                    return
        except ValueError:
            self.messa.afficher_mess('erreur', 'La temperature doit être comprise entre 0°c et 250°c où entrez'
                                               ' "auto" pour la laisser par défaut.', 'error')
            return
        self.parser_cpu.set('cpu_reglages', 'tj_max', str(tj_max))
        self.parser_cpu.set('app_settings', 'update', 'True')

        self.messa.afficher_mess('Tout est ok.', 'Vos choix ont bien été appliqués!', 'info')
