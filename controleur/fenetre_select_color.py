import tkinter
from tkinter import Tk, Canvas, PhotoImage, mainloop
from controleur import message
from modele import m_access_to_settings

class fenSelectionColor:

    def __init__(self, fen_parent, canevas_a_colorer, lab_hexa, indice='', all_core=False, nbr_cpu=0):
        self.color = ''
        self.indice = indice
        self.all_cores = all_core
        self.nbr_cpu = nbr_cpu
        self.list_verif_hexa = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')
        self.color_perso="#010101"
        self.var_hexadecimal = tkinter.StringVar()
        self.lab_hexa_parent = lab_hexa
        self.canevas_a_colorer = canevas_a_colorer
        self.principalFrameWIDTH, self.principalFrameHEIGHT = 255, 255
        self.barreCanWIDTH = 50
        self.barreCanHEIGHT = 255
        self.barre_color_list = []
        self.window = tkinter.Toplevel(fen_parent)
        self.canvasPrincipal = Canvas(self.window, width=self.principalFrameWIDTH, height=self.principalFrameHEIGHT,
                                      bg="#000000")
        self.canvasPrincipal.bind('<Button>', self.set_color)
        self.canvasPrincipal.grid(column=1, columnspan=2, row=1)
        self.canvasSecond = Canvas(self.window, width=self.barreCanWIDTH, height=self.barreCanHEIGHT, bg="#000000")
        self.canvasSecond.bind('<Button>', self.propage_color)
        self.canvasSecond.grid(column=3, row=1)
        self.canvas_couleur_choisie = Canvas(self.window, width=self.principalFrameWIDTH, height=self.barreCanWIDTH)
        self.canvas_couleur_choisie.grid(column=1, columnspan=2, row=2)
        self.imgPrincipale = PhotoImage(width=self.principalFrameWIDTH, height=self.principalFrameHEIGHT)
        self.imgSecondaire = PhotoImage(width=self.barreCanWIDTH, height=self.barreCanHEIGHT)
        self.imamagePrincipale = self.canvasPrincipal.create_image((self.principalFrameWIDTH / 2,
                                                                    self.principalFrameHEIGHT / 2)
                                                                   , image=self.imgPrincipale, state="normal")
        self.canvasSecond.create_image((self.barreCanWIDTH / 2, self.barreCanHEIGHT / 2), image=self.imgSecondaire,
                                       state="normal")

        self.bouton_valider_couleur = tkinter.Button(self.window, text="Valider couleur",
                                                     command=self.valider_couleur)
        self.bouton_valider_couleur.grid(column=3, row=2)

        self.lab_hexa = tkinter.Label(self.window, text="Hexadecimal: ...")
        self.lab_hexa.grid(column=1, columnspan=2, row=3)

        self.label_hexa_perso = tkinter.Label(self.window, text="Entrez hexadecimal \nperso ci-contre")
        self.label_hexa_perso.grid(column=1, row=4)

        self.hexa_input = tkinter.Entry(self.window, width=10)
        self.hexa_input.grid(column=2, row=4)

        self.bouton_valider_hexa_perso = tkinter.Button(self.window, text="Appliquer valeur perso",
                                                        command=self.appliquer_hexa_perso)
        self.bouton_valider_hexa_perso.grid(column=3, row=4)

        self.listeHexa = []
        self.letter = ['a', 'b', 'c', 'd', 'e', 'f']
        self.creer_liste_hexa()
        self.list_colors_left = self.print_tableau('#ff8000')
        self.creer_barre_couleurs()

    def close_fen(self):
        self.window.destroy()

    def propage_color(self, event):
        sets = self.barre_color_list[event.y]
        self.print_tableau(sets)

    def save_and_update(self, indice, color):
        if indice[:4] == 'Netw':
            if indice[4:8] == 'Font':
                netw_font_parser = m_access_to_settings.accessToSettings('color_font.ini')
                if indice[8:] == 'Title':
                    netw_font_parser.set('Network_font', 'title', color)
                elif indice[8:] == 'Down':
                    netw_font_parser.set('Network_font', 'down', color)
                elif indice[8:] == 'Up':
                    netw_font_parser.set('Network_font', 'up', color)
            elif indice[4:6] == 'Cu':
                curve_parser = m_access_to_settings.accessToSettings('colors.ini')
                if indice[9:11] == 'Up':
                    curve_parser.set('Network', 'up_curve', color)
                elif indice[9:11] == 'Do':
                    curve_parser.set('Network', 'down_curve', color)
            elif indice[4:6] == 'Gr':
                graph_parser = m_access_to_settings.accessToSettings('colors.ini')
                if indice[6:10] == 'Cont':
                    graph_parser.set('Network', 'contour_graph', color)
                elif indice[6:10] == 'Fond':
                    graph_parser.set('Network', 'fond_graph', color)
                elif indice[6:10] == 'Axes':
                    graph_parser.set('Network', 'axes_x_et_y', color)
            elif indice[4:6] == 'Pr':
                netw_parser = m_access_to_settings.accessToSettings('colors.ini')
                netw_parser.set('Network', 'principale', color)
            elif indice[4:6] == 'Do':
                netw_parser = m_access_to_settings.accessToSettings('colors.ini')
                netw_parser.set('Network', 'coul_down', color)
            elif indice[4:6] == 'Up':
                netw_parser = m_access_to_settings.accessToSettings('colors.ini')
                netw_parser.set('Network', 'coul_up', color)
        elif indice == 'titre':
            parser_font_cpu = m_access_to_settings.accessToSettings('color_font.ini')
            parser_font_cpu.set('cpu', 'title', color)
        elif indice == 'cpu_load':
            parser_font_cpu = m_access_to_settings.accessToSettings('color_font.ini')
            parser_font_cpu.set('cpu', 'cpu_load', color)
        elif indice == 'cpu_freq':
            parser_font_cpu = m_access_to_settings.accessToSettings('color_font.ini')
            parser_font_cpu.set('cpu', 'cpu_freq', color)
        elif indice == 'font_ram':
            parser_font_cpu = m_access_to_settings.accessToSettings('color_font.ini')
            parser_font_cpu.set('cpu', 'ram', color)
        elif indice == 'font_temp':
            parser_font_cpu = m_access_to_settings.accessToSettings('color_font.ini')
            parser_font_cpu.set('cpu', 'temp', color)
        elif indice == 'font_perc_ram':
            parser_font_cpu = m_access_to_settings.accessToSettings('color_font.ini')
            parser_font_cpu.set('cpu', 'percent_ram', color)
        elif indice == 'ram':
            sette = m_access_to_settings.accessToSettings('colors.ini')
            sette.set('Cpu', 'ram', color)
        elif indice == 'fond_ram':
            see = m_access_to_settings.accessToSettings('colors.ini')
            see.set('Cpu', 'fond_ram', color)
        elif indice == '':
            setter = m_access_to_settings.accessToSettings('colors.ini')
            setter.set('Cpu', 'principale', color)
        elif indice == 'param':
            seet = m_access_to_settings.accessToSettings('colors.ini')
            seet.set('Cpu', 'bout_param', color)
        elif indice[:4] == 'fond':
            se = m_access_to_settings.accessToSettings('colors.ini')
            if self.all_cores:
                for i in range(self.nbr_cpu):
                    se.set('Cpu', 'fond_core' + str(i + 1), color)
                se.set('Cpu', 'color_all_fonds', color)
                se.set('Cpu', 'fond_all_cores', 'True')
            else:
                se.set('Cpu', 'fond_core' + str(int(indice[4:]) + 1), color)
                se.set('Cpu', 'fond_all_cores', 'False')
        elif indice[:4] == 'font':
            if indice[4:8] == 'core':
                font_core_parse = m_access_to_settings.accessToSettings('color_font.ini')
                if self.all_cores:
                    for i in range (self.nbr_cpu):
                        font_core_parse.set('cpu', 'core_' + str(i + 1), color)
                    font_core_parse.set('cpu', 'color_all', color)
                    font_core_parse.set('cpu', 'color_all_cores', 'True')
                else:
                    font_core_parse.set('cpu', 'core_' + str(int(indice[8]) + 1), color)
                    font_core_parse.set('cpu', 'color_all_cores', 'False')
            elif indice[4:8] == 'disk':
                font_core_disk_parser = m_access_to_settings.accessToSettings('color_font.ini')
                if indice[8:12] == 'titl':
                    font_core_disk_parser.set('disk', 'title', color)

        try:
            indi = int(indice)
            if 0 < int(indi) < 128:
                sett = m_access_to_settings.accessToSettings('colors.ini')
                if self.all_cores:
                    for i in range(self.nbr_cpu):
                        sett.set('Cpu', 'core' + str(i + 1), color)
                    sett.set('Cpu', 'color_all_cores', color)
                    sett.set('Cpu', 'bare_all_cores', 'True')
                else:
                    sett.set('Cpu', 'Core' + str(indice), color)
                    sett.set('Cpu', 'bare_all_cores', 'False')
        except ValueError:
            pass

        if indice[1:5] == 'disk':
            if indice[5:] == 'principal':
                disk_setter = m_access_to_settings.accessToSettings('colors.ini')
                disk_setter.set('Disks', 'principale', color)
            elif indice[5:26] == 'toutes_les_partitions':
                disk_toutes_setter = m_access_to_settings.accessToSettings('colors.ini')
                liste_colors = disk_toutes_setter.get('Disks', 'toutes').split('=>')
                liste_colors[int(indice[0])] = color
                disk_toutes_setter.set('Disks', 'toutes', "=>".join(liste_colors))
                liste_before_change_toutes = disk_toutes_setter.get('Disks', 'change_dans_applique_a_toutes').split('=>')
                if str(indice[0]) not in liste_before_change_toutes:
                    change = "=>".join(liste_before_change_toutes) + "=>" + indice[0]
                else:
                    change = "=>".join(liste_before_change_toutes)
                disk_toutes_setter.set('Disks', 'change_dans_applique_a_toutes', change)
            else:
                disk_part_setter = m_access_to_settings.accessToSettings('colors.ini')
                liste_before_change_toutes = disk_part_setter.get(
                    'Disks', 'change_dans_applique_a_toutes').split('=>')
                setter_deux = m_access_to_settings.accessToSettings('colors.ini')
                if indice[0] in liste_before_change_toutes:
                    liste_before_change_toutes.remove(str(indice[0]))
                    setter_deux.set('Disks', 'change_dans_applique_a_toutes',
                                      '=>'.join(liste_before_change_toutes))
                liste_colors = disk_part_setter.get('Disks', str(indice[5:])).split('=>')
                liste_colors[int(indice[0])] = color
                setter_deux.set('Disks', str(indice[5:]), "=>".join(liste_colors))
        elif indice[1:5] == 'font':

            if indice[9:30] == 'toutes_les_partitions':
                disk_font_setter = m_access_to_settings.accessToSettings('color_font.ini')
                liste_all_preview_colors = disk_font_setter.get('disk', 'toutes').split('=>')
                liste_all_preview_colors[int(indice[0])] = color
                disk_font_setter.set('disk', 'toutes', "=>".join(liste_all_preview_colors))
                liste_before_change_toutes = disk_font_setter.get('Disks', 'change_dans_applique_a_toutes').split('=>')
                if str(int(indice[0]) + 1) not in liste_before_change_toutes:
                    change = "=>".join(liste_before_change_toutes) + "=>" + str(int(indice[0]) + 1)
                else:
                    change = "=>".join(liste_before_change_toutes)
                disk_font_setter.set('Disks', 'change_dans_applique_a_toutes', change)
            else:
                if indice[5:] == 'title':
                    disk_font_setter_title = m_access_to_settings.accessToSettings('color_font.ini')
                    disk_font_setter_title.set('disk', 'title', color)
                else:
                    disk_font_setter_unite = m_access_to_settings.accessToSettings('color_font.ini')
                    liste_number_change_toute = disk_font_setter_unite.get('Disks', 'change_dans_applique_a_toutes').split('=>')
                    deux_set = m_access_to_settings.accessToSettings('color_font.ini')


                    if str(int(indice[0]) + 1) in liste_number_change_toute:
                        liste_number_change_toute.remove(str(int(indice[0]) + 1))
                        deux_set.set('Disks', 'change_dans_applique_a_toutes', '=>'.join(liste_number_change_toute))
                    liste_colors = disk_font_setter_unite.get('Disks', indice[9:]).split('=>')
                    liste_colors[int(indice[0])] = color
                    deux_set.set('Disks', str(indice[9:]), '=>'.join(liste_colors))

        upd_set = m_access_to_settings.accessToSettings('settings.ini')
        upd_set.set('app_settings', 'update', 'True')

    def set_color(self, event):
        self.color = self.list_colors_left[event.y][event.x]
        self.canvas_couleur_choisie.configure(background=str(self.color))
        self.lab_hexa.configure(text='Hexadecimal: ' + str(self.color))

    def valider_couleur(self, flag=""):
        if flag == "":
            self.canevas_a_colorer.configure(background=self.color)
            self.lab_hexa_parent.configure(text='Hexadecimal: ' + self.color)
            self.save_and_update(self.indice, self.color)
        else:
            self.canevas_a_colorer.configure(background=self.color_perso)
            self.lab_hexa_parent.configure(text='Hexadecimal: ' + self.color_perso)
            self.save_and_update(self.indice, self.color_perso)

    def appliquer_hexa_perso(self):
        self.color_perso = self.hexa_input.get()
        i = 0
        if len(self.color_perso) == 0:
            mess = message.AfficherMessage(self.window)
            mess.afficher_mess('Oups...', 'Il y a une erreur dans le code hexadecimal.\n'
                                          'Code inapplicable.', 'error')
            return False
        for char in self.color_perso:
            if i == 0 and char == '#' and len(self.color_perso) == 7:
                pass
                i += 1
            elif i > 0 and char in self.list_verif_hexa:
                pass
            else:
                mess = message.AfficherMessage(self.window)
                mess.afficher_mess('Oups...', 'Il y a une erreur dans le code hexadecimal.\n'
                                              'Code inapplicable.', 'error')
                return False
        self.valider_couleur(flag="hexa_perso")

    def creer_liste_hexa(self):
        i = 0
        k = 0
        while i < 16:
            if i <= 9:
                j = i
            else:
                j = self.letter[i - 10]
            while k < 16:
                if k <= 9:
                    m = k
                else:
                    m = self.letter[k - 10]

                self.listeHexa.append(str(j) + str(m))

                k += 1
            k = 0
            i += 1

    def definir_increment_y(self, color='#ff8000'):
        colorp1 = self.listeHexa.index(color[1:3])
        colorp2 = self.listeHexa.index(color[3:5])
        colorp3 = self.listeHexa.index(color[5:])
        incrementy1 = colorp1 / 255.00
        incrementy2 = colorp2 / 255.00
        incrementy3 = colorp3 / 255.00
        return incrementy1, incrementy2, incrementy3

    def get_increment_x(self, color_base, y):
        color_base1 = self.listeHexa.index(color_base[1:3])
        color_base2 = self.listeHexa.index(color_base[3:5])
        color_base3 = self.listeHexa.index(color_base[5:])
        increment_x1 = ((255 - y) - color_base1) / 256
        increment_x2 = ((255 - y) - color_base2) / 256
        increment_x3 = ((255 - y) - color_base3) / 256
        return [increment_x1, increment_x2, increment_x3]

    def print_tableau(self, color):
        self.list_colors_left = []
        incrementy = self.definir_increment_y(color)
        colort1 = self.listeHexa.index(color[1:3])
        colort2 = self.listeHexa.index(color[3:5])
        colort3 = self.listeHexa.index(color[5:])
        color_pour_inc_x = color
        for f in range(255):
            incrementx = self.get_increment_x(color_pour_inc_x, f + 1)
            colort11 = colort1 - incrementy[0] * f
            colort22 = colort2 - incrementy[1] * f
            colort33 = colort3 - incrementy[2] * f
            color_pour_inc_x = "#" + self.listeHexa[int(colort11)] + self.listeHexa[int(colort22)] +\
                               self.listeHexa[int(colort33)]
            self.list_colors_left.append([])
            for g in range(255):
                colorprincip111 = self.listeHexa[int(colort11) + int(incrementx[0] * g)]
                colorprincip222 = self.listeHexa[int(colort22) + int(incrementx[1] * g)]
                colorprincip333 = self.listeHexa[int(colort33) + int(incrementx[2] * g)]

                self.imgPrincipale.put('#' + colorprincip111 + colorprincip222 + colorprincip333, (g, f))
                self.list_colors_left[f].append('#' + colorprincip111 + colorprincip222 + colorprincip333)
        return self.list_colors_left

    def creer_barre_couleurs(self):
        global barre_color_list
        sequence = ["3", "1", "2", "3", "1", "2", "3"]
        color1 = "ff"
        color2, color3 = "0", "0"
        color2 = color2.zfill(2)
        color3 = color3.zfill(2)
        color_a_modifier = "aa"
        p = 0
        for a in sequence:
            match a:
                case "1":
                    color_a_modifier = color1
                case "2":
                    color_a_modifier = color2
                case "3":
                    color_a_modifier = color3
            if color_a_modifier == '00':
                for b in range(0, 256, 6):
                    if b >= 241:
                        b = 255
                    match a:
                        case "1":
                            color1 = self.listeHexa[b]
                        case "2":
                            color2 = self.listeHexa[b]
                        case "3":
                            color3 = self.listeHexa[b]
                    for d in range(50):
                        self.imgSecondaire.put("#" + color1 + color2 + color3, (d, p))
                    p += 1
                    self.barre_color_list.append("#" + color1 + color2 + color3)
            elif color_a_modifier == 'ff':
                for c in reversed(range(0, 256, 6)):
                    if c <= 15:
                        c = 0
                    match a:
                        case "1":
                            color1 = self.listeHexa[c]
                        case "2":
                            color2 = self.listeHexa[c]
                        case "3":
                            color3 = self.listeHexa[c]
                    for e in range(50):
                        self.imgSecondaire.put("#" + color1 + color2 + color3, (e, p))
                    p += 1
                    self.barre_color_list.append("#" + color1 + color2 + color3)
