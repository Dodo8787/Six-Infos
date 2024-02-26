import configparser
import tkinter
from psutil import disk_partitions
from modele import m_access_to_settings
from controleur import fenetre_select_color
from functools import partial
from pathlib import Path
from tkinter import ttk


class FenCoulDisk:
    def __init__(self, fen_param, frame_param, indice='gen'):
        self.indice = indice
        self.directory = Path(__file__).parent.parent
        self.button_color_img = tkinter.PhotoImage(file=str(self.directory) + '/Images/color_buton.png')
        getter = m_access_to_settings.accessToSettings('colors.ini')
        self.color_principale = getter.get('Disks', 'principale')
        self.fen_param = fen_param
        self.frame_param = frame_param
        self.frame_part = tkinter.Frame
        self.var_une_toutes = tkinter.StringVar()
        if self.indice == 'fon':
            getter_font = m_access_to_settings.accessToSettings('color_font.ini')
            self.color_font_title = getter_font.get('disk', 'title')

        self.afficher_fen_coul_disk()
        self.start = 0
        self.fen_coul = fenetre_select_color.fenSelectionColor
        self.liste_colors = []
        self.liste_lab_name = []
        self.liste_can = []
        self.liste_lab_hexa = []
        self.liste_param_command = []

        self.can_fond_principal = tkinter.Canvas
        self.lab_hexa_principal = tkinter.Label
        self.can = []
        self.lab_hexa_princ = []
        self.lab_hexa_fond = []
        self.can_fond_princ = []
        self.can_color_bar_zone1 = []
        self.can_color_bar_zone2 = []
        self.can_color_bar_zone3 = []
        self.lab_hexa_color_bar_zone1 = []
        self.lab_hexa_color_bar_zone2 = []
        self.lab_hexa_color_bar_zone3 = []
        self.can_color_fond = []
        self.can_write = []
        self.lab_hexa_write = []
        self.can_color_read = []
        self.lab_hexa_read = []
        self.can_color_font_disk = []
        self.lab_hexa_color_font_disk = []
        self.can_color_font_mount = []
        self.lab_hexa_color_font_mount = []
        self.can_color_font_used_total = []
        self.lab_hexa_color_font_used_total = []
        self.can_color_font_free = []
        self.lab_hexa_color_font_free = []
        self.can_color_font_write = []
        self.lab_hexa_color_font_write = []
        self.can_color_font_read = []
        self.lab_hexa_color_font_read = []
        self.flag = ''
        self.pages_total = 0
        self.page_actuelle = 0
        self.fen_coul = fenetre_select_color

    def afficher_fen_coul_disk(self):
        if self.indice == 'gen':
            lab_color_principal = tkinter.Label(self.frame_param, text='Fond principal:')
            lab_color_principal.grid(column=1, row=2)
            self.can_fond_principal = tkinter.Canvas(self.frame_param, width=45, height=20, relief='groove',
                                                borderwidth=2, background=self.color_principale)
            self.can_fond_principal.grid(column=2, row=2)
            self.lab_hexa_principal = tkinter.Label(self.frame_param, text='Hexadecimal: ' + self.color_principale)
            self.lab_hexa_principal.grid(column=3, row=2)
            self.bouton_coul_principale = tkinter.Button(self.frame_param, image=self.button_color_img,
                                                         command=partial(self.afficher_palette, '0diskprincipal',
                                                                         self.can_fond_principal, self.lab_hexa_principal))
            self.bouton_coul_principale.grid(column=4, row=2)

            lab_une_toutes = tkinter.Label(self.frame_param, text='Appliquer a: ')
            lab_une_toutes.grid(column=1, row=3)
            radio_une = ttk.Radiobutton(self.frame_param, text='une partition', value='une',
                                        command=partial(self.afficher_part, 'une', 0))
            radio_une.grid(column=2, row=3)
            radio_toutes = ttk.Radiobutton(self.frame_param, text='toutes les partitions', value='toutes',
                                           command=partial(self.afficher_part, 'toutes', 0))
            radio_toutes.grid(column=2, row=4)
        else:
            lab_color_title = tkinter.Label(self.frame_param, text='Couleur du titre:')
            lab_color_title.grid(column=1, row=2)
            self.can_font_title = tkinter.Canvas(self.frame_param, width=45, height=20, relief='groove',
                                                     borderwidth=2, background=self.color_font_title)
            self.can_font_title.grid(column=2, row=2)
            self.lab_hexa_font_title = tkinter.Label(self.frame_param, text='Hexadecimal: ' + self.color_font_title)
            self.lab_hexa_font_title.grid(column=3, row=2)
            self.bouton_coul_font_title = tkinter.Button(self.frame_param, image=self.button_color_img,
                                                         command=partial(self.afficher_palette, '0fonttitle',
                                                                         self.can_font_title,
                                                                         self.lab_hexa_font_title))
            self.bouton_coul_font_title.grid(column=4, row=2)

            lab_une_toutes = tkinter.Label(self.frame_param, text='Appliquer a: ')
            lab_une_toutes.grid(column=1, row=3)
            radio_une = ttk.Radiobutton(self.frame_param, text='une partition', value='une',
                                        command=partial(self.afficher_part, 'une', 0))
            radio_une.grid(column=2, row=3)
            radio_toutes = ttk.Radiobutton(self.frame_param, text='toutes les partitions', value='toutes',
                                           command=partial(self.afficher_part, 'toutes', 0))
            radio_toutes.grid(column=2, row=4)

    def afficher_palette(self, flag, canevas, hexa):
        try:
            self.fen_coul.close_fen()
        except:
            pass
        self.fen_coul = fenetre_select_color.fenSelectionColor(self.fen_param, canevas, hexa, flag)

    def page_suivante(self):
        if self.page_actuelle < self.pages_total:
            self.afficher_part(self.flag, self.page_actuelle * 2)
        else:
            pass

    def page_precedente(self):
        if self.page_actuelle > 1:
            self.afficher_part(self.flag, self.page_actuelle * 2 - 4)
        else:
            pass

    def afficher_part(self, flag, start):
        try:
            self.frame_part.destroy()
        except:
            pass
        self.flag = flag
        if start == 0:
            self.page_actuelle = 1
        else:
            self.page_actuelle = start // 2 + 1

        self.frame_part = tkinter.Frame(self.frame_param)
        self.frame_part.grid(column=1, columnspan=4, row=5)
        total_part = disk_partitions()
        geter = m_access_to_settings.accessToSettings('settings.ini')
        if self.indice == 'gen':
            get = m_access_to_settings.accessToSettings('colors.ini')
        else:
            get = m_access_to_settings.accessToSettings('color_font.ini')
        list_to_forget = geter.get('disk', 'to_forget').split('=>')
        get_max_part = m_access_to_settings.accessToSettings('settings.ini')
        nbr_max_part = int(get_max_part.get('disk_reglages', 'nbr_disk_a_afficher'))
        change_dans_appliquer_a_toutes = get.get('Disks', 'change_dans_applique_a_toutes').split('=>')
        part_a_afficher = []
        for tot_part in total_part:
            if len(part_a_afficher) == nbr_max_part:
                break
            j = 0
            for j in range(len(list_to_forget) + 1):
                if j == len(list_to_forget):
                    part_a_afficher.append(tot_part.mountpoint)
                    break
                elif tot_part.mountpoint == list_to_forget[j]:
                    break
                j += 1
        i = 0
        if len(part_a_afficher) % 2 == 0:
            self.pages_total = len(part_a_afficher) // 2
        else:
            self.pages_total = len(part_a_afficher) // 2 + 1
        if flag == 'une':
            if self.indice == 'gen':
                list_color_princ = []
                liste_color_fond = []
                liste_color_bar_zone1 = []
                liste_color_bar_zone2 = []
                liste_color_bar_zone3 = []
                liste_fond_write = []
                liste_fond_read = []
                for part in part_a_afficher:
                    change_toutes_setter = m_access_to_settings.accessToSettings('colors.ini')
                    try:
                        liste_brute = get.get('Disks', part).split('=>')
                    except configparser.NoOptionError:
                        liste_brute = get.get('Disks', 'toutes').split('=>')
                    liste_toutes = get.get('Disks', 'toutes').split('=>')
                    liste_toute_change = []
                    if '0' in change_dans_appliquer_a_toutes:
                        list_color_princ.append(liste_toutes[0])
                        liste_toute_change.append(liste_toutes[0])
                    else:
                        list_color_princ.append(liste_brute[0])
                        liste_toute_change.append(liste_brute[0])
                    if '1' in change_dans_appliquer_a_toutes:
                        liste_color_fond.append(liste_toutes[1])
                        liste_toute_change.append(liste_toutes[1])
                    else:
                        liste_color_fond.append(liste_brute[1])
                        liste_toute_change.append(liste_brute[1])
                    if '2' in change_dans_appliquer_a_toutes:
                        liste_color_bar_zone1.append(liste_toutes[2])
                        liste_toute_change.append(liste_toutes[2])
                    else:
                        liste_color_bar_zone1.append(liste_brute[2])
                        liste_toute_change.append(liste_brute[2])
                    if '3' in change_dans_appliquer_a_toutes:
                        liste_color_bar_zone2.append(liste_toutes[3])
                        liste_toute_change.append(liste_toutes[3])
                    else:
                        liste_color_bar_zone2.append(liste_brute[3])
                        liste_toute_change.append(liste_brute[3])
                    if '4' in change_dans_appliquer_a_toutes:
                        liste_color_bar_zone3.append(liste_toutes[4])
                        liste_toute_change.append(liste_toutes[4])
                    else:
                        liste_color_bar_zone3.append(liste_brute[4])
                        liste_toute_change.append(liste_brute[4])
                    if '5' in change_dans_appliquer_a_toutes:
                        liste_fond_write.append(liste_toutes[5])
                        liste_toute_change.append(liste_toutes[5])
                    else:
                        liste_fond_write.append(liste_brute[5])
                        liste_toute_change.append(liste_brute[5])
                    if '6' in change_dans_appliquer_a_toutes:
                        liste_fond_read.append(liste_toutes[6])
                        liste_toute_change.append(liste_toutes[6])
                    else:
                        liste_fond_read.append(liste_brute[6])
                        liste_toute_change.append(liste_brute[6])
                    change_toutes_setter.set('Disks', part, '=>'.join(liste_toute_change) + '=>')
                self.liste_colors = [list_color_princ, liste_color_fond, liste_color_bar_zone1, liste_color_bar_zone2,
                                     liste_color_bar_zone3, liste_fond_write, liste_fond_read]
                self.liste_lab_name = ['Point de montage: ', 'Fond de la barre: ', 'Couleur barre zone 1: ',
                                       'Couleur barre zone 2: ', 'Couleur barre zone 3: ', 'Zone "write": ',
                                       'Zone "read": ']
                get = m_access_to_settings.accessToSettings('colors.ini')
                get.set('Last_choice', 'colors_disks', 'une')
            else:
                list_color_font_disk = []
                liste_color_mount_font = []
                liste_color_used_total_font = []
                liste_color_free_font = []
                liste_color_write_font = []
                liste_color_read_font = []

                for part in part_a_afficher:
                    change_toutes_setter_font = m_access_to_settings.accessToSettings('color_font.ini')
                    try:
                        liste_brute = get.get('Disks', part).split('=>')
                    except configparser.NoOptionError:
                        liste_brute = get.get('disk', 'toutes').split('=>')
                    liste_toutes = get.get('disk', 'toutes').split('=>')
                    liste_toute_font_change = []
                    if '0' in change_dans_appliquer_a_toutes:
                        list_color_font_disk.append(liste_toutes[0])
                        liste_toute_font_change.append(liste_toutes[0])
                    else:
                        list_color_font_disk.append(liste_brute[0])
                        liste_toute_font_change.append(liste_brute[0])
                    if '1' in change_dans_appliquer_a_toutes:
                        liste_color_mount_font.append(liste_toutes[1])
                        liste_toute_font_change.append(liste_toutes[1])
                    else:
                        liste_color_mount_font.append(liste_brute[1])
                        liste_toute_font_change.append(liste_brute[1])
                    if '2' in change_dans_appliquer_a_toutes:
                        liste_color_used_total_font.append(liste_toutes[2])
                        liste_toute_font_change.append(liste_toutes[2])
                    else:
                        liste_color_used_total_font.append(liste_brute[2])
                        liste_toute_font_change.append(liste_brute[2])
                    if '3' in change_dans_appliquer_a_toutes:
                        liste_color_free_font.append(liste_toutes[3])
                        liste_toute_font_change.append(liste_toutes[3])
                    else:
                        liste_color_free_font.append(liste_brute[3])
                        liste_toute_font_change.append(liste_brute[3])
                    if '4' in change_dans_appliquer_a_toutes:
                        liste_color_write_font.append(liste_toutes[4])
                        liste_toute_font_change.append(liste_toutes[4])
                    else:
                        liste_color_write_font.append(liste_brute[4])
                        liste_toute_font_change.append(liste_brute[4])
                    if '5' in change_dans_appliquer_a_toutes:
                        liste_color_read_font.append(liste_toutes[5])
                        liste_toute_font_change.append(liste_toutes[5])
                    else:
                        liste_color_read_font.append(liste_brute[5])
                        liste_toute_font_change.append(liste_brute[5])
                    change_toutes_setter_font.set('Disks', part, '=>'.join(liste_toute_font_change) + '=>')
                self.liste_colors = [list_color_font_disk, liste_color_mount_font, liste_color_used_total_font,
                                     liste_color_free_font, liste_color_write_font, liste_color_read_font]
                self.liste_lab_name = ['Nom du disque: ', 'Point de montage: ', 'Texte used/total: ',
                                       'Texte free: ', 'Texte write: ', 'Texte read: ']
                get = m_access_to_settings.accessToSettings('color_font.ini')
                get.set('Last_choice', 'colors_font_disks', 'une')
        else:
            part_a_afficher[0] = 'Toutes les partitions:'
            if self.indice == 'gen':
                liste_brute = get.get('Disks', 'toutes').split('=>')
                toutes_getter = m_access_to_settings.accessToSettings('colors.ini')
                indices_toutes = toutes_getter.get('Disks', 'change_dans_applique_a_toutes').split('=>')
            else:
                liste_brute = get.get('disk', 'toutes').split('=>')
                toutes_getter = m_access_to_settings.accessToSettings('color_font.ini')
                indices_toutes = toutes_getter.get('Disks', 'change_dans_applique_a_toutes').split('=>')
            i = 0
            while i < len(liste_brute):
                if str(i) not in indices_toutes:
                    liste_brute[i] = '#e4e8ea'
                i += 1
            i = 0
            if self.indice == 'gen':
                list_color_princ = [liste_brute[0]]
                liste_color_fond = [liste_brute[1]]
                liste_color_bar_zone1 = [liste_brute[2]]
                liste_color_bar_zone2 = [liste_brute[3]]
                liste_color_bar_zone3 = [liste_brute[4]]
                liste_fond_write = [liste_brute[5]]
                liste_fond_read = [liste_brute[6]]
                get.set('Last_choice', 'colors_disks', 'toutes')
                self.liste_colors = [list_color_princ, liste_color_fond, liste_color_bar_zone1, liste_color_bar_zone2,
                                liste_color_bar_zone3, liste_fond_write, liste_fond_read]
                self.liste_lab_name = ['Point de montage: ', 'Fond de la barre: ', 'Couleur barre zone 1: ',
                                  'Couleur barre zone 2: ', 'Couleur barre zone 3: ', 'Zone "write": ',
                                  'Zone "read": ']
            else:
                list_color_font_disk = [liste_brute[0]]
                liste_color_mount_font = [liste_brute[1]]
                liste_color_used_total_font = [liste_brute[2]]
                liste_color_free_font = [liste_brute[3]]
                liste_color_write_font = [liste_brute[4]]
                liste_color_read_font = [liste_brute[5]]
                get.set('last_choice', 'colors_font_disks', 'toutes')
                self.liste_colors = [list_color_font_disk, liste_color_mount_font, liste_color_used_total_font,
                                liste_color_free_font, liste_color_write_font, liste_color_read_font]
                self.liste_lab_name = ['Nom du disque: ', 'Point de montage: ', 'Texte used/total: ',
                                       'Texte free: ', 'Texte write: ', 'Texte read: ']
        while i < 2 and i < len(part_a_afficher) - start:
            if flag == 'une':
                part = part_a_afficher[i + start]
            else:
                part = 'toutes_les_partitions'
            if len(self.can_fond_princ) <= i + start + 1:
                if self.indice == 'gen':
                    self.can.append(tkinter.Canvas)
                    self.can_fond_princ.append(tkinter.Canvas)
                    self.lab_hexa_princ.append(tkinter.Label)
                    self.can_color_fond.append(tkinter.Canvas)
                    self.lab_hexa_fond.append(tkinter.Label)
                    self.can_color_bar_zone1.append(tkinter.Canvas)
                    self.can_color_bar_zone2.append(tkinter.Canvas)
                    self.can_color_bar_zone3.append(tkinter.Canvas)
                    self.lab_hexa_color_bar_zone1.append(tkinter.Label)
                    self.lab_hexa_color_bar_zone2.append(tkinter.Label)
                    self.lab_hexa_color_bar_zone3.append(tkinter.Label)
                    self.can_write.append(tkinter.Canvas)
                    self.lab_hexa_write.append(tkinter.Label)
                    self.can_color_read.append(tkinter.Canvas)
                    self.lab_hexa_read.append(tkinter.Label)
                    self.liste_can = [self.can_fond_princ, self.can_color_fond, self.can_color_bar_zone1,
                                 self.can_color_bar_zone2, self.can_color_bar_zone3, self.can_write,
                                 self.can_color_read]
                    self.liste_lab_hexa = [self.lab_hexa_princ, self.lab_hexa_fond, self.lab_hexa_color_bar_zone1,
                                      self.lab_hexa_color_bar_zone2, self.lab_hexa_color_bar_zone3,
                                      self.lab_hexa_write, self.lab_hexa_read]
                    self.liste_param_command = ['0disk', '1disk', '2disk', '3disk', '4disk', '5disk', '6disk']
                else:
                    self.can.append(tkinter.Canvas)
                    self.can_color_font_disk.append(tkinter.Canvas)
                    self.lab_hexa_color_font_disk.append(tkinter.Label)
                    self.can_color_font_mount.append(tkinter.Canvas)
                    self.lab_hexa_color_font_mount.append(tkinter.Label)
                    self.can_color_font_used_total.append(tkinter.Canvas)
                    self.lab_hexa_color_font_used_total.append(tkinter.Label)
                    self.can_color_font_free.append(tkinter.Canvas)
                    self.lab_hexa_color_font_free.append(tkinter.Label)
                    self.can_color_font_write.append(tkinter.Canvas)
                    self.lab_hexa_color_font_write.append(tkinter.Label)
                    self.can_color_font_read.append(tkinter.Canvas)
                    self.lab_hexa_color_font_read.append(tkinter.Label)
                    self.liste_can = [self.can_color_font_disk, self.can_color_font_mount,
                                 self.can_color_font_used_total, self.can_color_font_free, self.can_color_font_write,
                                 self.can_color_font_read]
                    self.liste_lab_hexa = [self.lab_hexa_color_font_disk, self.lab_hexa_color_font_mount,
                                      self.lab_hexa_color_font_used_total, self.lab_hexa_color_font_free,
                                      self.lab_hexa_color_font_write, self.lab_hexa_color_font_read]
                    self.liste_param_command = ['0fontdisk', '1fontdisk', '2fontdisk', '3fontdisk', '4fontdisk',
                                           '5fontdisk']
            self.can[i + start] = tkinter.Canvas(self.frame_part, relief='groove', borderwidth=2)
            self.can[i + start].grid(column=1, row=1 + i)
            lab_principal_part = tkinter.Label(self.can[i + start], text='Point de montage: ' + part_a_afficher[i + start])
            lab_principal_part.grid(column=1, columnspan=4, row=1, sticky=tkinter.W)

            lab_fond_princ = tkinter.Label(self.can[i + start], text=self.liste_lab_name[0])
            lab_fond_princ.grid(column=1, row=2)
            self.liste_can[0][i + start] = tkinter.Canvas(self.can[i + start], width=45, height=20, relief='groove',
                                                     borderwidth=2, background=self.liste_colors[0][i + start])
            self.liste_can[0][i + start].grid(column=2, row=2)
            self.liste_lab_hexa[0][i + start] = tkinter.Label(self.can[i + start],
                                                              text='Hexadecimal: ' + self.liste_colors[0][i + start])
            self.liste_lab_hexa[0][i + start].grid(column=3, row=2)
            self.bouton_coul_princ = tkinter.Button(self.can[i + start], image=self.button_color_img,
                                                    command=partial(self.afficher_palette, self.liste_param_command[0] + part,
                                                                    self.liste_can[0][i + start],
                                                                    self.liste_lab_hexa[0][i + start]))
            self.bouton_coul_princ.grid(column=4, row=2)

            lab_color_fond = tkinter.Label(self.can[i + start], text=self.liste_lab_name[1])
            lab_color_fond.grid(column=1, row=3)
            self.liste_can[1][i + start] = tkinter.Canvas(self.can[i + start], width=45, height=20, relief='groove',
                                                          borderwidth=2, background=self.liste_colors[1][i + start])
            self.liste_can[1][i + start].grid(column=2, row=3)
            self.liste_lab_hexa[1][i + start] = tkinter.Label(self.can[i + start],
                                                              text='Hexadecimal: ' + self.liste_colors[1][i + start])
            self.liste_lab_hexa[1][i + start].grid(column=3, row=3)
            self.bouton_coul_fond = tkinter.Button(self.can[i + start], image=self.button_color_img,
                                                   command=partial(self.afficher_palette, self.liste_param_command[1] + part,
                                                                   self.liste_can[1][i + start],
                                                                   self.liste_lab_hexa[1][i + start]))
            self.bouton_coul_fond.grid(column=4, row=3)

            lab_color_bar1 = tkinter.Label(self.can[i + start], text=self.liste_lab_name[2])
            lab_color_bar1.grid(column=1, row=4)
            self.liste_can[2][i + start] = tkinter.Canvas(self.can[i + start], width=45, height=20, relief='groove',
                                                          borderwidth=2,
                                                          background=self.liste_colors[2][i + start])
            self.liste_can[2][i + start].grid(column=2, row=4)
            self.liste_lab_hexa[2][i + start] = tkinter.Label(self.can[i + start],
                                                              text='Hexadecimal: ' + self.liste_colors[2][i + start])
            self.liste_lab_hexa[2][i + start].grid(column=3, row=4)
            bouton_color_bar_zone1 = tkinter.Button(self.can[i + start], image=self.button_color_img,
                                                    command=partial(self.afficher_palette, self.liste_param_command[2] + part,
                                                                    self.liste_can[2][i + start],
                                                                    self.liste_lab_hexa[2][i + start]))
            bouton_color_bar_zone1.grid(column=4, row=4)

            lab_color_bar2 = tkinter.Label(self.can[i + start], text=self.liste_lab_name[3])
            lab_color_bar2.grid(column=1, row=5)
            self.liste_can[3][i + start] = tkinter.Canvas(self.can[i + start], width=45, height=20,
                                                          relief='groove', borderwidth=2,
                                                          background=self.liste_colors[3][i + start])
            self.liste_can[3][i + start].grid(column=2, row=5)
            self.liste_lab_hexa[3][i + start] = tkinter.Label(self.can[i + start], text='Hexadecimal: ' +
                                                              self.liste_colors[3][i + start])
            self.liste_lab_hexa[3][i + start].grid(column=3, row=5)
            bouton_color_bar_zone2 = tkinter.Button(self.can[i + start], image=self.button_color_img,
                                                    command=partial(self.afficher_palette, self.liste_param_command[3] + part,
                                                                    self.liste_can[3][i + start],
                                                                    self.liste_lab_hexa[3][i + start]))
            bouton_color_bar_zone2.grid(column=4, row=5)

            lab_color_bar3 = tkinter.Label(self.can[i + start], text=self.liste_lab_name[4])
            lab_color_bar3.grid(column=1, row=6)
            self.liste_can[4][i + start] = tkinter.Canvas(self.can[i + start], width=45, height=20,
                                                          relief='groove', borderwidth=2,
                                                          background=self.liste_colors[4][i + start])
            self.liste_can[4][i + start].grid(column=2, row=6)
            self.liste_lab_hexa[4][i + start] = tkinter.Label(self.can[i + start],
                                                         text='Hexadecimal: ' + self.liste_colors[4][i + start])
            self.liste_lab_hexa[4][i + start].grid(column=3, row=6)
            bouton_color_bar_zone3 = tkinter.Button(self.can[i + start], image=self.button_color_img,
                                                    command=partial(self.afficher_palette, self.liste_param_command[4] + part,
                                                                    self.liste_can[4][i + start],
                                                                    self.liste_lab_hexa[4][i + start]))
            bouton_color_bar_zone3.grid(column=4, row=6)

            lab_fond_write = tkinter.Label(self.can[i + start], text=self.liste_lab_name[5])
            lab_fond_write.grid(column=1, row=7)
            self.liste_can[5][i + start] = tkinter.Canvas(self.can[i + start], width=45, height=20, relief='groove',
                                                     borderwidth=2, background=self.liste_colors[5][i + start])
            self.liste_can[5][i + start].grid(column=2, row=7)
            self.liste_lab_hexa[5][i + start] = tkinter.Label(self.can[i + start],
                                                         text='Hexadecimal: ' + self.liste_colors[5][i + start])
            self.liste_lab_hexa[5][i + start].grid(column=3, row=7)
            bouton_coul_write = tkinter.Button(self.can[i + start], image=self.button_color_img,
                                               command=partial(self.afficher_palette, self.liste_param_command[5] + part,
                                                               self.liste_can[5][i + start],
                                                               self.liste_lab_hexa[5][i + start]))
            bouton_coul_write.grid(column=4, row=7)

            if self.indice == 'gen':
                lab_color_read = tkinter.Label(self.can[i + start], text=self.liste_lab_name[6])
                lab_color_read.grid(column=1, row=8)
                self.liste_can[6][i + start] = tkinter.Canvas(self.can[i + start], width=45, height=20, relief='groove',
                                                borderwidth=2, background=self.liste_colors[6][i + start])
                self.liste_can[6][i + start].grid(column=2, row=8)
                self.liste_lab_hexa[6][i + start] = tkinter.Label(self.can[i + start],
                                                             text='Hexadecimal: ' + self.liste_colors[6][i + start])
                self.liste_lab_hexa[6][i + start].grid(column=3, row=8)
                bouton_coul_read = tkinter.Button(self.can[i + start], image=self.button_color_img,
                                                  command=partial(self.afficher_palette, self.liste_param_command[6] +
                                                                  part, self.liste_can[6][i + start],
                                                                  self.liste_lab_hexa[6][i + start]))
                bouton_coul_read.grid(column=4, row=8)
            if flag == 'une':
                i += 1
            else:
                i = 3
        if len(part_a_afficher) > 2 and flag == 'une':
            caneva_butons = tkinter.Canvas(self.frame_part)
            caneva_butons.grid(column=1, columnspan=4, row=1 + i, pady=5)
            bouton_prec = tkinter.Button(caneva_butons, text='Partitions précédentes', command=self.page_precedente)
            bouton_prec.grid(column=1, row=1)
            page_label = tkinter.Label(caneva_butons, text=str(self.page_actuelle) + '/' +
                                                           str(self.pages_total))
            page_label.grid(column=2, row=1)
            bouton_suiv = tkinter.Button(caneva_butons, text='partitions suivantes', command=self.page_suivante)
            bouton_suiv.grid(column=3, row=1)
