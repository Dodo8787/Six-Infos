import tkinter
from tkinter import ttk
from controleur import fenetre_select_color
from functools import partial
from psutil import cpu_count
from math import ceil
from modele import m_access_to_settings
from pathlib import Path


class fenCoulCpu:
    def __init__(self, fen_param, frame_param, indice='gen'):
        self.directory = Path(__file__).parent.parent
        self.actual_page_cpu = 1
        self.total_pages_cpu = 1
        self.cpu_tous_ou_un = 'tous'
        self.color_core = []
        self.color_fond_core = []
        self.frame_param = frame_param
        self.indice = indice
        if self.indice == 'gen':
            self.getter = m_access_to_settings.accessToSettings('colors.ini')
        else:
            self.getter = m_access_to_settings.accessToSettings('color_font.ini')
        self.nbr_cpu = cpu_count()
        if self.indice == 'gen':
            self.color_principale = ''
            self.color_bout_param = ''
            self.color_ram = ''
            self.color_fond_ram = ''
            self.liste_colors = []
            self.color_core = []
            self.color_fond_core = []
        else:
            self.color_title = ''
            self.color_cpu_load = ''
            self.color_cpu_freq = ''
            self.color_ram = ''
            self.liste_colors = []
            self.color_temp = ''
        self.obtenir_couleurs()

        if self.indice == 'gen':
            list_text = ['Fond principale:', 'Hexadecimal: ', 'Bouton parametres:', 'Barre ram:', 'Fond barre ram']
            list_commands = [self.afficher_palette_principale, self.afficher_palette_param,
                             partial(self.afficher_palette_core, 'ram', 'False'),
                             partial(self.afficher_palette_core, 'fond_ram', 'False')]
        else:
            list_text = ['Couleur titre', 'Hexadecimal: ', 'Cpu load:', 'Cpu frequence:', 'Ram "go/go":']
            list_commands = [partial(self.afficher_palette, 'titre'), partial(self.afficher_palette, 'cpu_load'),
                             partial(self.afficher_palette, 'cpu_freq'), partial(self.afficher_palette, 'ram_font')]

        self.button_color_img = tkinter.PhotoImage(file=str(self.directory) + '/Images/color_buton.png')

        self.label_principal_cpu = tkinter.Label(self.frame_param, text=list_text[0])
        self.label_principal_cpu.grid(column=1, row=2, sticky=tkinter.E)
        self.canevas_principal_cpu = tkinter.Canvas(self.frame_param, width=45, height=20, relief='groove',
                                                    borderwidth=2, background=self.liste_colors[0])
        self.canevas_principal_cpu.grid(column=2, row=2)
        self.label_hexa_principale = tkinter.Label(self.frame_param, text=list_text[1] + self.liste_colors[0])
        self.label_hexa_principale.grid(column=3, row=2)
        self.bouton_coul_principale = tkinter.Button(self.frame_param, image=self.button_color_img,
                                                     command=list_commands[0])
        self.bouton_coul_principale.grid(column=4, row=2)

        self.lab_param = tkinter.Label(self.frame_param, text=list_text[2])
        self.lab_param.grid(column=1, row=3, sticky=tkinter.E)
        self.canevas_param = tkinter.Canvas(self.frame_param, width=45, height=20, relief='groove',
                                            borderwidth=2, background=self.liste_colors[1])
        self.canevas_param.grid(column=2, row=3)
        self.lab_hexa_param = tkinter.Label(self.frame_param, text=list_text[1] + self.liste_colors[1])
        self.lab_hexa_param.grid(column=3, row=3)
        self.bouton_coul_param = tkinter.Button(self.frame_param, image=self.button_color_img,
                                                command=list_commands[1])
        self.bouton_coul_param.grid(column=4, row=3)

        self.lab_core = []
        self.can_core = []
        self.lab_hexa_core = []
        self.bouton_core = []

        self.lab_background_core = []
        self.can_background_core = []
        self.lab_back_hexa_core = []
        self.bouton_backgrount_core = []

        self.lab_ram = tkinter.Label(self.frame_param, text=list_text[3])
        self.lab_ram.grid(column=1, row=4, sticky=tkinter.E)
        self.canevas_ram = tkinter.Canvas(self.frame_param, width=45, height=20, relief='groove',
                                          borderwidth=2, background=self.liste_colors[2])
        self.canevas_ram.grid(column=2, row=4)
        self.lab_hexa_ram = tkinter.Label(self.frame_param, text=list_text[1] + self.liste_colors[2])
        self.lab_hexa_ram.grid(column=3, row=4)
        self.bouton_coul_ram = tkinter.Button(self.frame_param, image=self.button_color_img,
                                              command=list_commands[2])
        self.bouton_coul_ram.grid(column=4, row=4)

        self.lab_fond_ram = tkinter.Label(self.frame_param, text=list_text[4])
        self.lab_fond_ram.grid(column=1, row=5, sticky=tkinter.E)
        self.canevas_fond_ram = tkinter.Canvas(self.frame_param, width=45, height=20, relief='groove',
                                          borderwidth=2, background=self.liste_colors[3])
        self.canevas_fond_ram.grid(column=2, row=5)
        self.lab_hexa_fond_ram = tkinter.Label(self.frame_param, text=list_text[1] + self.liste_colors[3])
        self.lab_hexa_fond_ram.grid(column=3, row=5)
        self.bouton_coul_fond_ram = tkinter.Button(self.frame_param, image=self.button_color_img,
                                              command=list_commands[3])
        self.bouton_coul_fond_ram.grid(column=4, row=5)

        self.lab_radio = tkinter.Label(self.frame_param, text="Appliquer a:")
        self.lab_radio.grid(column=1, row=6)
        self.radio_cpu_tous = ttk.Radiobutton(self.frame_param, text="Tous les cores", value="tous",
                                              command=partial(self.afficher_pages_cpu, 1, 1))
        self.radio_cpu_tous.grid(column=2, row=6)
        self.radio_cpu_un = ttk.Radiobutton(self.frame_param, text="Un core", value="un",
                                            command=partial(self.afficher_pages_cpu, self.nbr_cpu, start=1))
        self.radio_cpu_un.grid(column=2, row=7)
        self.frame_cpu = tkinter.Frame

        if self.indice != 'gen':
            getter_font = m_access_to_settings.accessToSettings('color_font.ini')

            color_percent_ram = getter_font.get('cpu', 'percent_ram')
            self.lab_percent_ram = tkinter.Label(self.frame_param, text='Couleur % ram:')
            self.lab_percent_ram.grid(column=1, row=9, sticky=tkinter.E)
            self.canevas_font_percent_ram = tkinter.Canvas(self.frame_param, width=45, height=20, relief='groove',
                                                           borderwidth=2, background=color_percent_ram)
            self.canevas_font_percent_ram.grid(column=2, row=9)
            self.lab_hexa_font_percent_ram = tkinter.Label(self.frame_param, text='Hexadecimal: ' + color_percent_ram)
            self.lab_hexa_font_percent_ram.grid(column=3, row=9)
            self.bouton_coul_font_percent_ram = tkinter.Button(self.frame_param, image=self.button_color_img,
                                                        command=partial(self.afficher_palette, 'font_perc_ram'))
            self.bouton_coul_font_percent_ram.grid(column=4, row=9)

            color_temp = getter_font.get('cpu', 'temp')
            self.lab_font_temp = tkinter.Label(self.frame_param, text='Couleur température:')
            self.lab_font_temp.grid(column=1, row=10, sticky=tkinter.E)
            self.canevas_font_temp = tkinter.Canvas(self.frame_param, width=45, height=20, relief='groove',
                                                   borderwidth=2, background=color_temp)
            self.canevas_font_temp.grid(column=2, row=10)
            self.lab_hexa_font_temp = tkinter.Label(self.frame_param, text='Hexadecimal: ' + color_temp )
            self.lab_hexa_font_temp.grid(column=3, row=10)
            self.bouton_coul_font_temp = tkinter.Button(self.frame_param, image=self.button_color_img,
                                                       command=partial(self.afficher_palette, 'font_temp'))
            self.bouton_coul_font_temp.grid(column=4, row=10)

        self.fen_param = fen_param
        self.is_open_palette = False
        #self.fen_coul = fenetre_select_color.fenSelectionColor
        self.fen_coul = fenetre_select_color

    def obtenir_couleurs(self):
        if self.indice == 'gen':
            self.color_principale = self.getter.get('Cpu', 'principale')
            self.color_bout_param = self.getter.get('Cpu', 'bout_param')
            self.color_ram = self.getter.get('Cpu', 'ram')
            self.color_fond_ram = self.getter.get('Cpu', 'fond_ram')
            self.liste_colors = [self.color_principale, self.color_bout_param, self.color_ram, self.color_fond_ram]
            self.color_core = []
            self.color_fond_core = []
            for cpu in range(self.nbr_cpu):
                self.color_core.append(self.getter.get('Cpu', 'core' + str(cpu + 1)))
                self.color_fond_core.append(self.getter.get('Cpu', 'fond_core' + str(cpu + 1)))
        else:
            self.color_title = self.getter.get('cpu', 'title')
            self.color_cpu_load = self.getter.get('cpu', 'cpu_load')
            self.color_cpu_freq = self.getter.get('cpu', 'cpu_freq')
            self.color_ram = self.getter.get('cpu', 'ram')
            self.liste_colors = [self.color_title, self.color_cpu_load, self.color_cpu_freq, self.color_ram]
            self.color_core = []
            for cpu in range(self.nbr_cpu):
                self.color_core.append(self.getter.get('cpu', 'core_' + str(cpu + 1)))
            self.color_temp = self.getter.get('cpu', 'temp')

    def cores_suivants(self):
        if self.actual_page_cpu < self.total_pages_cpu:
            self.afficher_pages_cpu(self.nbr_cpu, start=4 * self.actual_page_cpu + 1)
        else:
            pass

    def cores_precedents(self):
        if self.actual_page_cpu > 1:
            self.afficher_pages_cpu(self.nbr_cpu, start=4 * (self.actual_page_cpu - 1) - 3)
        else:
            pass

    def afficher_pages_cpu(self, nbr_cpu, start):
        if nbr_cpu == 1:
            self.cpu_tous_ou_un = 'tous'
        else:
            self.cpu_tous_ou_un = 'un'
        self.total_pages_cpu = ceil(nbr_cpu / 4)
        self.actual_page_cpu = ceil(start / 4)
        if self.indice == 'gen':
            gtter = m_access_to_settings.accessToSettings('colors.ini')
        else:
            gtter = m_access_to_settings.accessToSettings('color_font.ini')
        for i in range(4):
            if self.indice == 'gen':
                self.color_core[i + start - 1] = gtter.get('Cpu', 'core' + str(start + i))
                self.color_fond_core[i + start - 1] = gtter.get('Cpu', 'fond_core' + str(start + i))
            else:
                self.color_core[i + start - 1] = gtter.get('cpu', 'core_' + str(start + i))
        try:
            self.frame_cpu.destroy()
        except:
            pass
        self.frame_cpu = tkinter.Frame(self.frame_param)
        self.frame_cpu.grid(column=1, row=8, columnspan=4)
        i = 0
        j = 0
        gett = m_access_to_settings.accessToSettings('colors.ini')
        gett_fon = m_access_to_settings.accessToSettings('color_font.ini')
        while (i <= 3) and (i + start <= nbr_cpu):
            if nbr_cpu == 1:
                text = " Core "
                if self.indice == 'gen':
                    is_all_fond = gett.get('Cpu', 'fond_all_cores')
                    is_all_bare = gett.get('Cpu', 'bare_all_cores')
                else:
                    is_all_fond = gett_fon.get('cpu', 'color_all_cores')
                color_bares = '#e4e8ea'
                color_fonds = '#e4e8ea'
                if self.indice == 'gen' and is_all_bare == 'True':
                    color_bares = gett.get('Cpu', 'color_all_cores')
                if is_all_fond == 'True':
                    if self.indice == 'gen':
                        color_fonds = gett.get('Cpu', 'color_all_fonds')
                    else:
                        color_bares = gett_fon.get('cpu', 'color_all')
                if len(self.can_core) < i + start:
                    if self.indice == 'gen':
                        self.color_core.append(gett.get('Cpu', 'core' + str(i + start)))
                    else:
                        self.color_core.append(gett_fon.get('cpu', 'core_' + str(i + start)))

                self.color_core[i + start - 1] = color_bares
                if self.indice == 'gen':
                    self.color_fond_core[i + start - 1] = color_fonds

            else:
                text = " Core " + str(i + start)
            if len(self.lab_core) < i + start:
                if self.indice == 'gen':
                    text2 = 'Charge' + text
                else:
                    text2 = 'Core ' + str(i + start)
                self.lab_core.append(tkinter.Label(self.frame_cpu, text=text2))
                if self.indice == 'gen':
                    self.lab_background_core.append(tkinter.Label(self.frame_cpu, text='Fond' + text))
            else:
                if self.indice == 'gen':
                    text2 = 'Charge' + text
                else:
                    text2 = 'Core ' + str(i + 1)
                self.lab_core[i + start - 1] = tkinter.Label(self.frame_cpu, text=text2)
                if self.indice == 'gen':
                    self.lab_background_core[i + start - 1] = tkinter.Label(self.frame_cpu, text='Fond' + text)
            self.lab_core[i + start - 1].grid(column=1, row=j + 1, sticky=tkinter.E)
            if self.indice == 'gen':
                self.lab_background_core[i + start - 1].grid(column=1, row=j + 2, sticky=tkinter.E)
            if len(self.can_core) < i + start:
                if self.indice == 'gen':
                    self.color_core.append(gett.get('Cpu', 'core' + str(i + start)))
                else:
                    self.color_core.append(gett_fon.get('cpu', 'Core_' + str(i + start)))
                self.can_core.append(tkinter.Canvas(self.frame_cpu, width=45, height=20, relief='groove',
                                                    borderwidth=2, background=self.color_core[i + start - 1]))
                if self.indice == 'gen':
                    self.color_fond_core.append(gett.get('Cpu', 'fond_core' + str(i + start)))
                    self.can_background_core.append(tkinter.Canvas(self.frame_cpu, width=45, height=20, relief='groove',
                                                                   borderwidth=2,
                                                                   background=self.color_fond_core[i + start - 1]))

            self.can_core[i + start - 1] = tkinter.Canvas(self.frame_cpu, width=45, height=20, relief='groove',
                                                   borderwidth=2, background=self.color_core[i + start - 1])
            self.can_core[i + start - 1].grid(column=2, row=j + 1)
            if self.indice == 'gen':
                self.can_background_core[i + start - 1] = tkinter.Canvas(self.frame_cpu, width=45, height=20, relief='groove',
                                                                         borderwidth=2,
                                                                         background=self.color_fond_core[i + start - 1])
                self.can_background_core[i + start - 1].grid(column=2, row=j + 2)
            if len(self.lab_hexa_core) < i + start:
                self.lab_hexa_core.append(tkinter.Label(self.frame_cpu, text='Hexadecimal: '
                                                                            + str(self.color_core[i + start - 1])))
                if self.indice == 'gen':
                    self.lab_back_hexa_core.append(tkinter.Label(self.frame_cpu, text='Hexadecimal: ' +
                                                                 str(self.color_fond_core[i + start - 1])))
            else:
                self.lab_hexa_core[i + start - 1] = tkinter.Label(self.frame_cpu, text='Hexadecimal: '
                                                                                  + str(self.color_core[i + start - 1]))
                if self.indice == 'gen':
                    self.lab_back_hexa_core[i + start - 1] = tkinter.Label(self.frame_cpu, text='Hexadecimal: ' +
                                                                           str(self.color_fond_core[i + start - 1]))
            self.lab_hexa_core[i + start - 1].grid(column=3, row=j + 1)
            if self.indice == 'gen':
                self.lab_back_hexa_core[i + start - 1].grid(column=3, row=j + 2)
            if nbr_cpu == 1:
                all_color = True
            else:
                all_color = False
            if i + start == 1:
                self.bouton_core = []
                self.bouton_backgrount_core = []
            if len(self.bouton_core) < i + start:
                self.bouton_core.append(
                    tkinter.Button(self.frame_cpu, image=self.button_color_img,
                                   command=partial(self.afficher_palette_core, i + start, all_color)))
            if self.indice == 'gen':
                self.bouton_backgrount_core.append(
                    tkinter.Button(self.frame_cpu, image=self.button_color_img,
                                   command=partial(self.afficher_palette_core, 'fond' + str(i + start), all_color)))
            else:
                self.bouton_core[i + start - 1] = tkinter.Button(self.frame_cpu, image=self.button_color_img,
                                                                 command=partial(self.afficher_palette_core, 'fontcore' +
                                                                                 str(i + start),
                                                                                 all_color))
            self.bouton_core[i + start - 1].grid(column=4, row=j + 1)
            if self.indice == 'gen':
                self.bouton_backgrount_core[i + start - 1] = tkinter.Button(self.frame_cpu,
                                                                            image=self.button_color_img,
                                                                            command=partial(self.afficher_palette_core,
                                                                                            'fond' + str(i + start),
                                                                                            all_color))

                self.bouton_backgrount_core[i + start - 1].grid(column=4, row=j + 2)
            i += 1
            j += 2
        if nbr_cpu > 4:
            bouton_precedent = tkinter.Button(self.frame_cpu, text="Cores précédents", command=self.cores_precedents)
            bouton_precedent.grid(column=1, columnspan=2, row=j + 3)
            bouton_suivant = tkinter.Button(self.frame_cpu, text="Cores suivants", command=self.cores_suivants)
            bouton_suivant.grid(column=3, columnspan=2, row=j + 3)

    def afficher_palette_core(self, i, all_color):
        if i == 'ram':
            canevas_a_colorer = self.canevas_ram
            label_hexa = self.lab_hexa_ram
            indice = i
        elif i == 'fond_ram':
            canevas_a_colorer = self.canevas_fond_ram
            label_hexa = self.lab_hexa_fond_ram
            indice = i
        elif str(i)[:4] == 'fond':
            i = str(i)[4:]
            canevas_a_colorer = self.can_background_core[int(i) - 1]
            label_hexa = self.lab_back_hexa_core[int(i) - 1]
            indice = str('fond' + str(int(i) - 1))
        elif str(i)[:8] == 'fontcore':
            i = str(i)[8:]
            canevas_a_colorer = self.can_core[int(i) - 1]
            label_hexa = self.lab_hexa_core[int(i) - 1]
            indice = str('fontcore' + str(int(i) - 1))
        else:
            canevas_a_colorer = self.can_core[int(i) - 1]
            label_hexa = self.lab_hexa_core[int(i) - 1]
            indice = str(i)
        try:
            self.fen_coul.close_fen()
        except AttributeError:
            pass
        if self.cpu_tous_ou_un == 'tous':
            all_cores = True
        else:
            all_cores = False
        self.fen_coul = fenetre_select_color.fenSelectionColor(self.fen_param, canevas_a_colorer, label_hexa, indice,
                                                               all_cores, nbr_cpu=self.nbr_cpu)
        self.is_open_palette = True

    def afficher_palette(self, indice):
        if indice == 'titre':
            can_a_colorer = self.canevas_principal_cpu
            hexa_a_definir = self.label_hexa_principale
            i = 'titre'
        if indice[4:9] == '_perc':
            can_a_colorer = self.canevas_font_percent_ram
            hexa_a_definir = self.lab_hexa_font_percent_ram
            i = indice
        elif indice == 'cpu_load':
            can_a_colorer = self.canevas_param
            hexa_a_definir = self.lab_hexa_param
            i = 'cpu_load'
        elif indice == 'cpu_freq':
            can_a_colorer = self.canevas_ram
            hexa_a_definir = self.lab_hexa_ram
            i = 'cpu_freq'
        elif indice == 'ram_font':
            can_a_colorer = self.canevas_fond_ram
            hexa_a_definir = self.lab_hexa_fond_ram
            i = 'font_ram'
        elif indice == 'font_temp':
            can_a_colorer = self.canevas_font_temp
            hexa_a_definir = self.lab_hexa_font_temp
            i = 'font_temp'
        try:
            self.fen_coul.close_fen()
        except AttributeError:
            pass
        self.fen_coul = fenetre_select_color.fenSelectionColor(self.fen_param, can_a_colorer, hexa_a_definir, indice=i)
        self.is_open_palette = True

    def afficher_palette_principale(self):
        try:
            self.fen_coul.close_fen()
        except:
            pass
        self.fen_coul = fenetre_select_color.fenSelectionColor(self.fen_param, self.canevas_principal_cpu,
                                                               self.label_hexa_principale)
        self.is_open_palette = True

    def afficher_palette_param(self):
        try:
            self.fen_coul.close_fen()
        except:
            pass
        self.fen_coul = fenetre_select_color.fenSelectionColor(self.fen_param, self.canevas_param,
                                                               self.lab_hexa_param, indice='param')
        self.is_open_palette = True
