import configparser
import tkinter
from tkinter import ttk

import psutil

from controleur.c_fen_reglages_disk import FenetreReglagesDisk
from controleur.c_fen_reglages_network import FenetreReglagesNetwork
from controleur.c_fen_reglages_themes import ReglagesThemes
from controleur.c_fen_reglages_cpu import FenReglCpu
from controleur.c_fen_reglages_application import FenReglageAppli
from controleur.c_fen_font_app import fenFontApp
from controleur.c_fen_font_cpu import fenFontCpu
from controleur.c_fen_font_disk import fenFontDisk
from controleur.c_fen_font_netw import fenFontNetw
from controleur.c_fen_coul_cpu import fenCoulCpu
from controleur.c_fen_coul_disk import FenCoulDisk
from controleur.c_fen_coul_netw import FenCoulNetw
from controleur.c_fen_coul_app import fenCoulApp
from controleur.c_fen_reliefs_app import fenReliefsApp
from controleur.c_fen_reliefs_cpu import fenReliefsCpu
from controleur.c_fen_reliefs_disks import fenReliefsDisks
from controleur.c_fen_reliefs_netw import fenReliefsNetw
from modele import m_access_to_settings
from configparser import ConfigParser
from pathlib import Path
from ttkthemes import ThemedTk
from functools import partial


class FenParam:
    directoryError = Path(__file__).parent.parent
    isopen = bool
    fen_param = tkinter.Toplevel
    bouton_reglages = ttk.Button
    bouton_style = ttk.Button
    bouton_font = ttk.Button
    bouton_couleurs = ttk.Button
    bouton_application = ttk.Button
    bouton_cpu = ttk.Button
    bouton_disk = ttk.Button
    bouton_network = ttk.Button
    bouton_themes = ttk.Button
    liste_keywords = ['', '']
    liste_disk = []
    bool_actualiser_part = bool
    frame_disk = ttk.Frame
    part_a_afficher = []
    preview_choix_un = ''
    preview_choix_deux = ''
    destroy_frame = bool
    posx = 0
    posy = 0
    previewposx = 0
    previewposy = 0
    directory = ''
    label_infos1 = ttk.Label
    label_infos2 = ttk.Label
    frame_parametres = ttk.Frame

    def __init__(self, part_aa_afficher, roottk, possibles_part):
        self.bool_actualiser_part = False
        self.part_a_afficher = part_aa_afficher
        self.destroy_frame = False
        self.directory = Path(__file__).parent.parent
        self.liste_keywords = ["", ""]
        self.liste_possibles_part_afficher = possibles_part
        self.root_win = roottk
        self.posx = 0
        self.posy = 0
        self.previewposx = 1
        self.previewposy = 1
        self.is_open_palette = False
        self.fen_coul_cpu = fenCoulCpu
        self.fen_coul_disk = FenCoulDisk
        self.fen_coul_netw = FenCoulNetw
        self.buton_color_font = tkinter.Button
        self.buton_color_gen = tkinter.Button
        self.fen_lier_disks = tkinter.Toplevel
        self.fenetr_reg_dis = FenetreReglagesDisk
        self.fen_param = tkinter.Toplevel

    def on_closing_fen_param(self):
        try:
            self.fenetr_reg_dis.fen_lier_diskk.destroy()
        except TypeError:
            pass
        except AttributeError:
            pass
        try:
            self.fenetr_reg_dis.fen_black.destroy()
        except TypeError:
            pass
        except AttributeError:
            pass
        self.fen_param.destroy()


    def open_window(self):
        self.fen_param = tkinter.Toplevel()
        parser_fen_param = m_access_to_settings.accessToSettings('settings.ini')
        pos = [200, 200]
        try:
            pos[0], pos[1] = parser_fen_param.get('start', 'param_pos').split('+')[1:]
        except configparser.NoOptionError:
            parser_fen_param.set('start', 'param_pos', '+200+200')
            self.fen_param.geometry('+200+200')
        self.fen_param.geometry('+' + str(pos[0]) + '+' + str(pos[1]))
        self.fen_param.title('Parametres')
        self.fen_param.protocol("WM_DELETE_WINDOW", self.on_closing_fen_param)
        self.frame_gen = tkinter.Frame(self.fen_param, width='400p')
        self.frame_gen.grid()
        self.bouton_Reglages = tkinter.Button(self.frame_gen, text="Reglages", command=self.bout_reglages, bg='#18b499',
                                              width=18)
        self.bouton_Reglages.grid(column=1, row=1, sticky=tkinter.EW)
        self.bouton_Style = tkinter.Button(self.frame_gen, text="Style", command=self.bout_style, bg='#18b499',
                                           width=18)
        self.bouton_Style.grid(column=2, row=1, sticky=tkinter.EW)
        self.bouton_Font = tkinter.Button(self.frame_gen, text="Font", command=self.bout_font, bg='#18b499',
                                          width=18)
        self.bouton_Font.grid(column=3, row=1, sticky=tkinter.EW)
        self.bouton_Couleurs = tkinter.Button(self.frame_gen, text="Couleurs", command=self.bout_couleurs, bg='#18b499',
                                              width=18)
        self.bouton_Couleurs.grid(column=4, row=1, sticky=tkinter.EW)
        self.bouton_Application = tkinter.Button(self.frame_gen, text="Application", command=self.bout_application,
                                                 bg='#18b499', width=18)
        self.bouton_Application.grid(column=1, row=2, sticky=tkinter.EW)
        self.bouton_Cpu = tkinter.Button(self.frame_gen, text="CPU", command=self.bout_cpu, bg='#18b499',
                                         width=18)
        self.bouton_Cpu.grid(column=2, row=2, sticky=tkinter.EW)
        self.bouton_Disk = tkinter.Button(self.frame_gen, text="Disque", command=self.bout_disk, bg='#18b499',
                                          width=18)
        self.bouton_Disk.grid(column=3, row=2, sticky=tkinter.EW)
        self.bouton_Network = tkinter.Button(self.frame_gen, text="Network", command=self.bout_network, bg='#18b499',
                                             width=18)
        self.bouton_Network.grid(column=4, row=2, sticky=tkinter.EW)
        self.bouton_themes = tkinter.Button(self.frame_gen, text='Choix\nthemes', command=self.bout_themes,
                                            bg='#18b499', width=9)
        self.bouton_themes.grid(column=5, rowspan=2, row=1)
        self.label_choix = ttk.Label(self.frame_gen, text="Votre choix: ...",
                                     width=72)
        self.label_choix.grid(column=1, columnspan=4, row=3, sticky=tkinter.W)
        self.frame_parametres = tkinter.Frame(self.frame_gen, relief='groove', borderwidth=3)
        self.frame_parametres.grid(column=1, columnspan=4, row=4, pady=25)
        if self.liste_keywords[0] == '':
            self.label_infos1 = ttk.Label(self.frame_parametres,
                                          text='Veuillez choisir pour le "choix principale" entre:\n'
                                               '   "Reglages", "Style", "Font" ou "Couleurs"\n')
            self.label_infos1.grid(column=1, columnspan=4, row=1)
        if self.liste_keywords[1] == '':
            self.label_infos2 = ttk.Label(self.frame_parametres,
                                          text='Veuillez choisir pour le "choix secondaire" entre: \n '
                                          '   "Application", "Cpu", "Disque" ou "Network"')
            self.label_infos2.grid(column=1, columnspan=4, row=2)

    def store_position_fen_param(self, x, y):
        parser_fen2 = m_access_to_settings.accessToSettings('settings.ini')
        parser_fen2.set('start', 'param_pos', '+' + str(x) + '+' + str(y))
        self.previewposx = x
        self.previewposy = y

    def destroy_and_create_frame(self):
        self.frame_parametres.destroy()
        self.frame_parametres = tkinter.Frame(self.frame_gen, relief='groove', borderwidth=3)
        self.frame_parametres.grid(column=1, columnspan=4, row=4, pady=25)

    def get_list_part_a_afficher(self):
        part = psutil.disk_partitions()
        getter = m_access_to_settings.accessToSettings('settings.ini')
        part_to_forget = getter.get('disk', 'to_forget').split('=>')
        final_list = []
        for par in part:
            i = 0
            while i <= len(part_to_forget):
                if i == len(part_to_forget):
                    final_list.append(par.mountpoint)
                    break
                if par.mountpoint == part_to_forget[i]:
                    break
                i += 1
        return final_list

    def add_liste(self, word, place):
        if self.is_open_palette:
            try:
                self.fen_coul_cpu.fen_coul.close_fen()
            except AttributeError:
                pass
            try:
                self.fen_coul_disk.fen_coul.close_fen()
            except AttributeError:
                pass
            try:
                self.fen_coul_netw.fen_coul.close_fen()
            except AttributeError:
                pass
        try:
            self.fenetr_reg_dis.fen_lier_diskk.destroy()
        except TypeError:
            pass
        except AttributeError:
            pass
        try:
            self.fenetr_reg_dis.fen_black.destroy()
        except TypeError:
            pass
        except AttributeError:
            pass
            self.is_open_palette = False
        self.posx, self.posy = (int(s) for s in self.fen_param.geometry().split("+")[1:])
        if self.posx != self.previewposx or self.posy != self.previewposy:
            self.store_position_fen_param(self.posx, self.posy)
            self.previewposx = self.posx
            self.previewposy = self.posy
        if self.preview_choix_deux == 'Themes' and place == 0:
            self.liste_keywords[1] = ''
        if self.preview_choix_un == 'Themes' and place == 1:
            self.liste_keywords[0] = ''
        self.liste_keywords[place] = word

        if self.preview_choix_un == 'Reglages' and place == 0:
            self.bouton_Reglages.configure(bg='#18b499')
        elif self.preview_choix_un == 'Style' and place == 0:
            self.bouton_Style.configure(bg='#18b499')
        elif self.preview_choix_un == 'Font' and place == 0:
            self.bouton_Font.configure(bg='#18b499')
        elif self.preview_choix_un == 'Couleurs' and place == 0:
            self.bouton_Couleurs.configure(bg='#18b499')
        elif self.preview_choix_un == 'Themes' and place == 0:
            self.bouton_themes.configure(bg='#18b499')

        if self.preview_choix_deux == 'Application' and place == 1:
            self.bouton_Application.configure(bg='#18b499')
        elif self.preview_choix_deux == 'Cpu' and place == 1:
            self.bouton_Cpu.configure(bg='#18b499')
        elif self.preview_choix_deux == 'Disque' and place == 1:
            self.bouton_Disk.configure(bg='#18b499')
        elif self.preview_choix_deux == 'Network' and place == 1:
            self.bouton_Network.configure(bg='#18b499')
        elif self.preview_choix_deux == 'Themes' and place == 1:
            self.bouton_themes.configure(bg='#18b499')

        if self.liste_keywords[0] == 'Themes' or self.liste_keywords[1] == 'Themes':
            self.label_choix.configure(text='Votre choix: "Themes"')
        else:
            self.label_choix.configure(text='Votre choix: "{}" => "{}"'.
                                       format(self.liste_keywords[0], self.liste_keywords[1]))

        if word == 'Reglages':
            self.bouton_Reglages.configure(bg='#ffa500')
        elif word == 'Style':
            self.bouton_Style.configure(bg='#ffa500')
        elif word == 'Font':
            self.bouton_Font.configure(bg='#ffa500')
        elif word == 'Couleurs':
            self.bouton_Couleurs.configure(bg='#ffa500')
        elif word == 'Application':
            self.bouton_Application.configure(bg='#ffa500')
        elif word == 'Cpu':
            self.bouton_Cpu.configure(bg='#ffa500')
        elif word == 'Disque':
            self.bouton_Disk.configure(bg='#ffa500')
        elif word == 'Network':
            self.bouton_Network.configure(bg='#ffa500')
        elif word == 'Themes':
            self.bouton_themes.configure(bg='#ffa500')
        if place == 0:
            self.preview_choix_un = word
        elif place == 1:
            self.preview_choix_deux = word

        if self.liste_keywords[0] != '':
            self.label_infos1.destroy()
        if self.liste_keywords[1] != '':
            self.label_infos2.destroy()
        if self.liste_keywords[0] == 'Reglages':
            if self.liste_keywords[1] == 'Disque':
                if self.destroy_frame:
                    self.destroy_and_create_frame()
                self.destroy_frame = True
                self.fenetr_reg_dis = FenetreReglagesDisk(self.fen_param, self.root_win,
                                                          list_part_a_afficher=self.get_list_part_a_afficher())
                self.fenetr_reg_dis.afficher_liste_part(self.frame_parametres)
                self.fenetr_reg_dis.afficher_right_side_options(self.frame_parametres)


            elif self.liste_keywords[1] == 'Network':
                if self.destroy_frame:
                    self.destroy_and_create_frame()
                self.destroy_frame = True
                self.fenetr_reg_net = FenetreReglagesNetwork(self.fen_param, self.frame_parametres)
                self.fenetr_reg_net.afficher_reglages_net()
            elif self.liste_keywords[1] == 'Cpu':
                if self.destroy_frame:
                    self.destroy_and_create_frame()
                self.destroy_frame = True
                self.fenRegCpu = FenReglCpu(self.fen_param, self.frame_parametres)
                self.fenRegCpu.afficher_reg_cpu()
            elif self.liste_keywords[1] == 'Application':
                if self.destroy_frame:
                    self.destroy_and_create_frame()
                self.destroy_frame = True
                self.fenRegApp = FenReglageAppli(self.fen_param, self.frame_parametres)
                self.fenRegApp.afficher_fen_reg_app()

        elif self.liste_keywords[0] == 'Themes':
            if self.destroy_frame:
                self.frame_parametres.destroy()
                self.frame_parametres = tkinter.Frame(self.frame_gen, relief='groove', borderwidth=3)
                self.frame_parametres.grid(column=1, columnspan=4, row=4, pady=25)
            self.destroy_frame = True
            fen_reg_themes = ReglagesThemes(self.frame_parametres, self.fen_param)
            fen_reg_themes.afficher_fen()

        elif self.liste_keywords[0] == 'Font':
            if self.liste_keywords[1] == 'Application':
                if self.destroy_frame:
                    self.destroy_and_create_frame()
                self.destroy_frame = True
                self.fen_font_app = fenFontApp(self.fen_param, self.frame_parametres)
            elif self.liste_keywords[1] == 'Cpu':
                if self.destroy_frame:
                    self.destroy_and_create_frame()
                self.destroy_frame = True
                self.fen_font_cpu = fenFontCpu(self.fen_param, self.frame_parametres)
                self.fen_font_cpu.afficher_frame_font_cpu()
            elif self.liste_keywords[1] == 'Disque':
                if self.destroy_frame:
                    self.destroy_and_create_frame()
                self.destroy_frame = True
                self.fen_font_disk = fenFontDisk(self.fen_param, self.frame_parametres)
                self.fen_font_disk.afficher_frame_font_disk(liste_part_a_afficher=self.part_a_afficher)
            elif self.liste_keywords[1] == 'Network':
                if self.destroy_frame:
                    self.destroy_and_create_frame()
                self.destroy_frame = True
                self.fen_font_network = fenFontNetw(self.fen_param, self.frame_parametres)
                self.fen_font_network.afficher_frame_font_netw()

        elif self.liste_keywords[0] == 'Couleurs':
            if self.liste_keywords[1] == 'Application':
                if self.destroy_frame:
                    self.destroy_and_create_frame()
                self.destroy_frame = True
                self.fen_coul_app = fenCoulApp(self.fen_param, self.frame_parametres)
            elif self.liste_keywords[1] == 'Cpu':
                if self.destroy_frame:
                    self.destroy_and_create_frame()
                self.destroy_frame = True
                self.creer_deux_butons_coul('cpu')
                self.fen_coul_cpu = fenCoulCpu(self.fen_param, self.frame_parametres)
                self.is_open_palette = True
            if self.liste_keywords[1] == 'Disque':
                if self.destroy_frame == True:
                    self.destroy_and_create_frame()
                self.destroy_frame = True
                self.creer_deux_butons_coul('Disque')
                self.fen_coul_disk = FenCoulDisk(self.fen_param, self.frame_parametres)
                self.is_open_palette = True
            if self.liste_keywords[1] == 'Network':
                if self.destroy_frame == True:
                    self.destroy_and_create_frame()
                self.destroy_frame = True
                self.creer_deux_butons_coul('Network')
                self.fen_coul_netw = FenCoulNetw(self.fen_param, self.frame_parametres)
                self.is_open_palette = True
        elif self.liste_keywords[0] == 'Style':
            if self.liste_keywords[1] == 'Application':
                if self.destroy_frame:
                    self.destroy_and_create_frame()
                self.destroy_frame = True
                self.fen_reliefs_app = fenReliefsApp(self.fen_param, self.frame_parametres)
            elif self.liste_keywords[1] == 'Cpu':
                if self.destroy_frame:
                    self.destroy_and_create_frame()
                self.destroy_frame = True
                self.fen_reliefs_cpu = fenReliefsCpu(self.fen_param, self.frame_parametres)
            elif self.liste_keywords[1] == 'Disque':
                if self.destroy_frame:
                    self.destroy_and_create_frame()
                self.destroy_frame = True
                self.fen_reliefs_disks = fenReliefsDisks(self.fen_param, self.frame_parametres)
            elif self.liste_keywords[1] == 'Network':
                if self.destroy_frame:
                    self.destroy_and_create_frame()
                self.destroy_frame = True
                self.fen_reliefs_netw = fenReliefsNetw(self.fen_param, self.frame_parametres)

    def creer_deux_butons_coul(self, indice, colored='none', uncolored='none'):
        self.buton_color_gen = tkinter.Button(self.frame_parametres, text='Couleurs générales', bg='#18b499',
                                         command=partial(self.afficher_color, 'gen', indice))
        self.buton_color_gen.grid(column=1, columnspan=2, row=1)
        self.buton_color_font = tkinter.Button(self.frame_parametres, text='Couleurs font', bg='#18b499',
                                          command=partial(self.afficher_color, 'fon', indice))
        self.buton_color_font.grid(column=3, columnspan=2, row=1)
        if colored == 'none':
            self.buton_color_gen.configure(bg='#ffa500')
        elif colored == 'buton_gen':
            self.buton_color_gen.configure(bg="#ffa500")
            self.buton_color_font.configure(bg='#18b499')
        else:
            self.buton_color_font.configure(bg="#ffa500")
            self.buton_color_gen.configure(bg='#18b499')

    def afficher_color(self, indice1, indice2):
        if indice2 == 'cpu':
            if indice1 == 'fon':
                self.destroy_and_create_frame()
                self.creer_deux_butons_coul('cpu', colored='buton_font', uncolored='buton_gen')
                self.fen_coul_cpu = fenCoulCpu(self.fen_param, self.frame_parametres, indice='fon')
                self.is_open_palette = True
            elif indice1 == 'gen':
                self.destroy_and_create_frame()
                self.creer_deux_butons_coul('cpu', colored='buton_gen', uncolored='buton_font')
                self.fen_coul_cpu = fenCoulCpu(self.fen_param, self.frame_parametres, indice='gen')
                self.is_open_palette = True
        elif indice2 == 'Disque':
            if indice1 == 'fon':
                self.destroy_and_create_frame()
                self.creer_deux_butons_coul('Disque', colored='buton_font', uncolored='buton_gen')
                self.fen_coul_disk = FenCoulDisk(self.fen_param, self.frame_parametres, indice='fon')
                self.is_open_palette = True
            elif indice1 == 'gen':
                self.destroy_and_create_frame()
                self.creer_deux_butons_coul('Disque', colored='buton_gen', uncolored='buton_font')
                self.fen_coul_cpu = FenCoulDisk(self.fen_param, self.frame_parametres, indice='gen')
                self.is_open_palette = True
        elif indice2 == 'Network':
            if indice1 == 'fon':
                self.destroy_and_create_frame()
                self.creer_deux_butons_coul('Network', colored='buton_font', uncolored='buton_gen')
                self.fen_coul_netw = FenCoulNetw(self.fen_param, self.frame_parametres, indice='fon')
                self.is_open_palette = True
            elif indice1 == 'gen':
                self.destroy_and_create_frame()
                self.creer_deux_butons_coul('Network', colored='buton_gen', uncolored='buton_font')
                self.fen_coul_netw = FenCoulNetw(self.fen_param, self.frame_parametres, indice='gen')
                self.is_open_palette = True

    def bout_reglages(self):
        self.add_liste('Reglages', 0)

    def bout_style(self):
        self.add_liste('Style', 0)

    def bout_font(self):
        self.add_liste('Font', 0)

    def bout_couleurs(self):
        self.add_liste('Couleurs', 0)

    def bout_application(self):
        self.add_liste('Application', 1)

    def bout_cpu(self):
        self.add_liste('Cpu', 1)

    def bout_disk(self):
        self.add_liste('Disque', 1)

    def bout_network(self):
        self.add_liste('Network', 1)

    def bout_themes(self):
        self.add_liste('Themes', 0)
        self.add_liste('Themes', 1)
