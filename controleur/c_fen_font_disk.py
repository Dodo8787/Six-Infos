import tkinter
from controleur import fen_liste_police
from tkinter import ttk
from tkinter import font
from controleur import message as mess
from modele import m_access_to_settings as accesseur
from controleur import starting_verif
from psutil import disk_partitions


class fenFontDisk:
    def __init__(self, fen_param, frame_param):
        theme_actuel = accesseur.accessToSettings('theme.ini')
        theme_actuel = theme_actuel.get('theme', 'theme_actuel')
        starting_verif.verif_font_file_disks(disk_partitions(), theme_actuel)
        acces_ini = accesseur.accessToSettings('font.ini')
        self.list_font = list(font.families())
        self.list_font.append('Arial')
        self.list_font.sort()
        self.fen_param = fen_param
        self.frame_param = frame_param
        self.frame_gen = tkinter.Frame
        self.liste_part_a_afficher = []
        self.var_une_ou_toutes = tkinter.StringVar(value='toutes')
        self.var_disk_infos = tkinter.StringVar(value=str(acces_ini.get('disk_font', 'disk_infos')))
        self.fram_disk = []
        self.frame_part = tkinter.Frame
        self.label_disk = []
        self.device = []
        self.combobox_device = []
        self.var_device = []
        self.mountp_label = []
        self.combo_mp = []
        self.var_mp = []
        self.used_et_total_label = []
        self.combo_used_et_total = []
        self.var_used_et_total = []
        self.free_label = []
        self.combo_free = []
        self.var_free = []
        self.read_lab = []
        self.combo_read = []
        self.var_read = []
        self.write_lab = []
        self.combo_write = []
        self.var_write = []
        self.page_actuel = 1
        self.pages_total = 0
        self.list_disk_a_appliquer = []

    def afficher_liste_police(self):
        fen_liste_polices = fen_liste_police.fenListePolice()
        fen_liste_polices.afficher_fen()

    def disk_prec(self):
        if self.page_actuel == 1:
            pass
        else:
            self.page_actuel -= 1
            self.afficher_toutes_part((self.page_actuel - 1) * 3, (self.page_actuel - 1) * 3 + 2)

    def disk_suiv(self):
        if self.page_actuel == self.pages_total:
            return
        else:
            self.page_actuel += 1
            self.afficher_toutes_part((self.page_actuel - 1) * 3, (self.page_actuel - 1) * 3 + 2)

    def afficher_une_part(self):
        try:
            self.frame_part.destroy()
        except TypeError:
            pass
        i = 0
        self.frame_part = tkinter.Frame(self.frame_gen, relief="groove", borderwidth=1)
        self.frame_part.grid(column=1, columnspan=2, row=4, padx=2)
        lab = 'Toutes les partitions:'
        self.fram_disk[i] = tkinter.Frame(self.frame_part, relief='groove', borderwidth=1)
        self.fram_disk[i].grid(column=1, row=i + 1, pady=2, padx=2)
        self.label_disk[i] = tkinter.Label(self.fram_disk[i], text=lab)
        self.label_disk[i].grid(column=1, columnspan=2, row=1)
        self.device[i] = tkinter.Label(self.fram_disk[i], text="Nom du disque")
        self.device[i].grid(column=1, row=2)
        self.combobox_device[i] = ttk.Combobox(self.fram_disk[i], values=self.list_font,
                                               textvariable=self.var_device[i])
        self.combobox_device[i].grid(column=2, row=2, sticky=tkinter.W)

        self.mountp_label[i] = tkinter.Label(self.fram_disk[i], text='Point de montage')
        self.mountp_label[i].grid(column=3, row=2)
        self.combo_mp[i] = ttk.Combobox(self.fram_disk[i], values=self.list_font,
                                        textvariable=self.var_mp[i])
        self.combo_mp[i].grid(column=4, row=2, sticky=tkinter.W)

        self.used_et_total_label[i] = tkinter.Label(self.fram_disk[i], text='Disk % used / total')
        self.used_et_total_label[i].grid(column=1, row=3)
        self.combo_used_et_total[i] = ttk.Combobox(self.fram_disk[i], values=self.list_font,
                                                   textvariable=self.var_used_et_total[i])
        self.combo_used_et_total[i].grid(column=2, row=3, sticky=tkinter.W)

        self.free_label[i] = tkinter.Label(self.fram_disk[i], text='Free')
        self.free_label[i].grid(column=3, row=3)
        self.combo_free[i] = ttk.Combobox(self.fram_disk[i], values=self.list_font,
                                          textvariable=self.var_free[i])
        self.combo_free[i].grid(column=4, row=3, sticky=tkinter.W)

        self.read_lab[i] = tkinter.Label(self.fram_disk[i], text='Read label')
        self.read_lab[i].grid(column=1, row=4)
        self.combo_read[i] = ttk.Combobox(self.fram_disk[i], values=self.list_font,
                                          textvariable=self.var_read[i])
        self.combo_read[i].grid(column=2, row=4, sticky=tkinter.W)

        self.write_lab[i] = tkinter.Label(self.fram_disk[i], text='Write label')
        self.write_lab[i].grid(column=3, row=4)
        self.combo_write[i] = ttk.Combobox(self.fram_disk[i], values=self.list_font,
                                           textvariable=self.var_write[i])
        self.combo_write[i].grid(column=4, row=4, sticky=tkinter.W)

    def afficher_toutes_part(self, disk_prem=0, disk_last=2):
        try:
            self.frame_part.destroy()
        except TypeError:
            pass
        gaiteur = accesseur.accessToSettings('font.ini')
        self.frame_part = tkinter.Frame(self.frame_gen, relief="groove", borderwidth=1)
        self.frame_part.grid(column=1, columnspan=2, row=4, padx=2)
        i = 0
        self.list_disk_a_appliquer = []
        for disk in self.liste_part_a_afficher:
            if disk_prem <= i <= disk_last:
                lab = 'Partition ' + str(i + 1) + ': ' + disk.mountpoint
                self.fram_disk[i] = tkinter.Frame(self.frame_part, relief='groove', borderwidth=1)
                self.fram_disk[i].grid(column=1, columnspan=2, row=i + 1, pady=2, padx=2)
                self.label_disk[i] = tkinter.Label(self.fram_disk[i], text=lab)
                self.label_disk[i].grid(column=1, columnspan=4, row=1)
                self.device[i] = tkinter.Label(self.fram_disk[i], text="Nom du disque")
                self.device[i].grid(column=1, row=2)
                self.var_device[i] = tkinter.StringVar(value=str(gaiteur.get(disk.mountpoint, 'nom_device')))
                self.combobox_device[i] = ttk.Combobox(self.fram_disk[i], values=self.list_font,
                                                       textvariable=self.var_device[i])

                self.combobox_device[i].grid(column=2, row=2, sticky=tkinter.W)

                self.mountp_label[i] = tkinter.Label(self.fram_disk[i], text='Point de montage')
                self.mountp_label[i].grid(column=3, row=2)
                self.var_mp[i] = tkinter.StringVar(value=str(gaiteur.get(disk.mountpoint, 'mount_point')))
                self.combo_mp[i] = ttk.Combobox(self.fram_disk[i], values=self.list_font,
                                                textvariable=self.var_mp[i])

                self.combo_mp[i].grid(column=4, row=2, sticky=tkinter.W)

                self.used_et_total_label[i] = tkinter.Label(self.fram_disk[i], text='Disk % used / total')
                self.used_et_total_label[i].grid(column=1, row=3)
                self.var_used_et_total[i] = tkinter.StringVar(value=str(gaiteur.get(disk.mountpoint, 'used_et_total')))
                self.combo_used_et_total[i] = ttk.Combobox(self.fram_disk[i], values=self.list_font,
                                                           textvariable=self.var_used_et_total[i])

                self.combo_used_et_total[i].grid(column=2, row=3, sticky=tkinter.W)

                self.free_label[i] = tkinter.Label(self.fram_disk[i], text='Free')
                self.free_label[i].grid(column=3, row=3)
                self.var_free[i] = tkinter.StringVar(value=str(gaiteur.get(disk.mountpoint, 'free')))
                self.combo_free[i] = ttk.Combobox(self.fram_disk[i], values=self.list_font,
                                                  textvariable=self.var_free[i])

                self.combo_free[i].grid(column=4, row=3, sticky=tkinter.W)

                self.read_lab[i] = tkinter.Label(self.fram_disk[i], text='Read label')
                self.read_lab[i].grid(column=1, row=4)
                self.var_read[i] = tkinter.StringVar(value=str(gaiteur.get(disk.mountpoint, 'font_read')))
                self.combo_read[i] = ttk.Combobox(self.fram_disk[i], values=self.list_font,
                                                  textvariable=self.var_read[i])

                self.combo_read[i].grid(column=2, row=4, sticky=tkinter.W)

                self.write_lab[i] = tkinter.Label(self.fram_disk[i], text='Write label')
                self.write_lab[i].grid(column=3, row=4)
                self.var_write[i] = tkinter.StringVar(value=str(gaiteur.get(disk.mountpoint, 'font_write')))
                self.combo_write[i] = ttk.Combobox(self.fram_disk[i], values=self.list_font,
                                                   textvariable=self.var_write[i])

                self.combo_write[i].grid(column=4, row=4, sticky=tkinter.W)
                self.list_disk_a_appliquer.append(disk)
            i += 1
        self.page_preced = tkinter.Button(self.frame_part, text='Disques précédents', command=self.disk_prec)
        self.page_preced.grid(column=1, row=i + 3)
        self.pages_total = len(self.liste_part_a_afficher) // 3
        if len(self.liste_part_a_afficher) % 3 != 0:
            self.pages_total += 1
        self.label_pages = tkinter.Label(self.frame_part, text='Page ' + str(self.page_actuel) + '/'
                                                               + str(self.pages_total))
        self.label_pages.grid(column=1, columnspan=2, row=i + 2)
        self.page_suiv = tkinter.Button(self.frame_part, text='Disques Suivants', command=self.disk_suiv)
        self.page_suiv.grid(column=2, row=i + 3)

    def appliquer_reglages_suite(self, une_ou_toutes, list_a_appliquer=['void']):
        setor_font_disk = accesseur.accessToSettings('font.ini')
        setor_updt_disk = accesseur.accessToSettings('settings.ini')
        messa = mess.AfficherMessage(self.frame_gen)
        i = 0
        j = 0
        nbr_errors = 0
        font_disk_inf = str(self.var_disk_infos.get())
        if font_disk_inf in self.list_font:
            setor_font_disk.set('disk_font', 'disk_infos', font_disk_inf)
        else:
            nbr_errors += 1
        if list_a_appliquer != ['void']:
            temp_list_a_afficher = self.liste_part_a_afficher
            self.liste_part_a_afficher = list_a_appliquer
        while i < len(self.liste_part_a_afficher):

            dev = self.var_device[j].get()
            if dev not in self.list_font:
                nbr_errors += 1
            else:
                setor_font_disk.set(str(self.liste_part_a_afficher[i].mountpoint), 'nom_device', str(dev))
            mp = self.var_mp[j].get()
            if mp not in self.list_font:
                nbr_errors += 1
            else:
                setor_font_disk.set(str(self.liste_part_a_afficher[i].mountpoint), 'mount_point', str(mp))
            used_et_total = self.var_used_et_total[j].get()
            if used_et_total not in self.list_font:
                nbr_errors += 1
            else:
                setor_font_disk.set(str(self.liste_part_a_afficher[i].mountpoint), 'used_et_total', str(used_et_total))
            free = self.var_free[j].get()
            if free not in self.list_font:
                nbr_errors += 1
            else:
                setor_font_disk.set(str(self.liste_part_a_afficher[i].mountpoint), 'free', str(free))
            font_read = self.var_read[j].get()
            if font_read not in self.list_font:
                nbr_errors += 1
            else:
                setor_font_disk.set(str(self.liste_part_a_afficher[i].mountpoint), 'font_read', str(font_read))
            font_write = self.var_write[j].get()
            if font_write not in self.list_font:
                nbr_errors += 1
            else:
                setor_font_disk.set(str(self.liste_part_a_afficher[i].mountpoint), 'font_write', str(font_write))
            if une_ou_toutes == 'une':
                j += 1
            i += 1
            if une_ou_toutes == 'toutes' and i == len(self.liste_part_a_afficher):
                setter_toutes_font = accesseur.accessToSettings('font.ini')
                chaine_font_toutes = [str(dev), str(mp), str(used_et_total), str(free), str(font_read), str(font_write)]
                chaine_finale = ('=>').join(chaine_font_toutes)
                setter_toutes_font.set('disk_font', 'toutes', chaine_finale)

        if list_a_appliquer != ['void']:
            self.liste_part_a_afficher = temp_list_a_afficher
        setor_updt_disk.set('app_settings', 'update', 'True')
        if nbr_errors > 0:
            messa.afficher_mess('Info', 'Certains paramètres n\'ont pas pu être sauvegarder. '
                                        'Les autres le sont.', 'info')
        else:
            messa.afficher_mess('Tout est ok', 'Tous les paramètres sont bien enregistrés!', 'info')

    def appliquer_reglages(self):
        acces1 = accesseur.accessToSettings('font.ini')
        message = mess.AfficherMessage(self.frame_gen)
        nbr = self.var_une_ou_toutes.get()
        if nbr == 'une':
            acces1.set('disk_font', 'dernier_choix', nbr)
            self.appliquer_reglages_suite('une', self.list_disk_a_appliquer)
        elif nbr == 'toutes':
            acces1.set('disk_font', 'dernier_choix', nbr)
            self.appliquer_reglages_suite('toutes')
        else:
            message.afficher_mess('Erreur', 'Oups il y a eut une erreur...', 'error')
            return

    def afficher_frame_font_disk(self, liste_part_a_afficher):
        self.liste_part_a_afficher = liste_part_a_afficher
        get_aff_font_cpu = accesseur.accessToSettings('font.ini')
        for item in self.liste_part_a_afficher:
            self.fram_disk.append(tkinter.Frame)
            self.label_disk.append(tkinter.Label)
            self.device.append(tkinter.Label)
            self.combobox_device.append(ttk.Combobox)
            self.var_device.append(tkinter.StringVar(value=get_aff_font_cpu.get(str(item.mountpoint), 'nom_device')))
            self.mountp_label.append(tkinter.Label)
            self.combo_mp.append(ttk.Combobox)
            self.var_mp.append(tkinter.StringVar(value=get_aff_font_cpu.get(str(item.mountpoint), 'mount_point')))
            self.used_et_total_label.append(tkinter.Label)
            self.combo_used_et_total.append(ttk.Combobox)
            self.var_used_et_total.append(tkinter.StringVar(value=get_aff_font_cpu.get(str(item.mountpoint), 'used_et_total')))
            self.free_label.append(tkinter.Label)
            self.combo_free.append(ttk.Combobox)
            self.var_free.append(tkinter.StringVar(value=get_aff_font_cpu.get(str(item.mountpoint), 'free')))
            self.read_lab.append(tkinter.Label)
            self.combo_read.append(ttk.Combobox)
            self.var_read.append(tkinter.StringVar(value=get_aff_font_cpu.get(str(item.mountpoint), 'font_read')))
            self.write_lab.append(tkinter.Label)
            self.combo_write.append(ttk.Combobox)
            self.var_write.append(tkinter.StringVar(value=get_aff_font_cpu.get(str(item.mountpoint), 'font_write')))
        self.frame_gen = tkinter.Frame(self.frame_param)
        self.frame_gen.grid(column=1, row=1)
        self.bouton_liste_pol = tkinter.Button(self.frame_gen, text='Cliquez ici pour afficher la liste des polices',
                                               command=self.afficher_liste_police)
        self.bouton_liste_pol.grid(column=1, row=1, columnspan=2, pady=4, padx=4)

        self.frame_une_ou_toutes_part = tkinter.Frame(self.frame_gen, relief='groove', borderwidth=2)
        self.frame_une_ou_toutes_part.grid(column=1, columnspan=2, row=2)
        self.lab_une_ou_toutes = tkinter.Label(self.frame_une_ou_toutes_part, text='Appliquer a toutes les partitions?')
        self.lab_une_ou_toutes.grid(column=1, columnspan=2, row=1)
        self.coche_une = ttk.Radiobutton(self.frame_une_ou_toutes_part, text='Toutes', variable=self.var_une_ou_toutes,
                                         value='toutes', command=self.afficher_une_part)
        self.coche_toutes = ttk.Radiobutton(self.frame_une_ou_toutes_part, text='Une', variable=self.var_une_ou_toutes,
                                            value='une', command=self.afficher_toutes_part)
        self.coche_une.grid(column=3, row=1, sticky=tkinter.W)
        self.coche_toutes.grid(column=3, row=2, sticky=tkinter.W)
        self.lab_disk_infos = tkinter.Label(self.frame_gen, text='Disk Infos')
        self.lab_disk_infos.grid(column=1, row=3, sticky=tkinter.E)
        self.combo_disk_infos = ttk.Combobox(self.frame_gen, values=self.list_font, textvariable=self.var_disk_infos)
        self.combo_disk_infos.grid(column=2, row=3, sticky=tkinter.W)
        self.buton_appliquer = ttk.Button(self.frame_gen, text='Appliquer', command=self.appliquer_reglages)
        self.buton_appliquer.grid(column=1, columnspan=2, row=5, pady=2)
        self.afficher_une_part()
