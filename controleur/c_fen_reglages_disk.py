import configparser
from tkinter import ttk
import tkinter
from tkinter import *
from modele import m_access_to_settings
from pathlib import Path
from controleur.message import AfficherMessage as message
from controleur.c_disk import CDisk
from psutil import disk_partitions
from Classes.disquee import UnDisque
import modele.m_access_to_settings as accesseur
from controleur import c_fen_lier_disques
from controleur import c_fen_blacklist
from time import sleep
import platform


class FenetreReglagesDisk:
    isopene = bool
    part_a_afficher = []
    disk_part = []
    dic_check_button = {}
    dic_check_button_updated = {}
    param_fen = tkinter.Toplevel
    liste_disque_to_forget = []
    actualiser_disques_afficher = bool
    list_number = []
    list_letters2 = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'i1', 'j1', 'k1', 'l1', 'm1', 'n1', 'o1', 'p1',
                     'q1', 'r1', 's1', 't1']
    liste_nbr_part_choix = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    list_intvar = []
    for pp in disk_part:
        dic_check_button[str(pp)] = 0
    directory2 = ""
    check_nom_device = IntVar
    check_mount_point = IntVar
    check_devmp_unchange = IntVar
    une_ou_deux_ligne = StringVar
    used_oui_non = StringVar
    nbr_part_a_appliquer = StringVar
    afficherLigneFree = StringVar
    nbr_part_a_afficher = StringVar
    frame_une_part = ttk.Frame
    unite_r_w = StringVar
    var_adjust_used = StringVar
    radio_conv = IntVar
    paren = tkinter.Toplevel
    liste_w_r = ['unchange', 'auto', 'o', 'ko', 'mo', 'go', 'to']
    list_adjust_used = ['-10', '-9','-8', '-7', '-6', '-5', '-4', '-3', '-2', '-1', 'unchange', '0', '+1', '+2', '+3', '+4',
                        '+5', '+6', '+7', '+8', '+9', '+10']
    messager = message
    canvas = Canvas
    pond_value = StringVar
    liste_pond_values = ('unchange', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
    var_affich_general = StringVar

    def __init__(self, parent, win_root, actualiser=False, list_part_a_afficher=[]):
        self.os_actual = platform.system()
        self.isopene = False
        self.part_a_afficher = list_part_a_afficher
        disk_partiti = disk_partitions()
        self.disk_part = disk_partiti
        self.actualiser_disques_afficher = actualiser
        self.param_fen = {}
        self.dic_check_button_updated = {}
        for mo in disk_partiti:
            self.dic_check_button[mo] = 0
        self.directory2 = Path(__file__).parent.parent
        parser2 = m_access_to_settings.accessToSettings('settings.ini')
        try:
            unite_conv = int(parser2.get('disk_reglages', 'converter'))
        except configparser.NoOptionError:
            unite_conv = 1024
        try:
            self.nbr_part_a_afficher = int(parser2.get('disk_reglages', 'nbr_disk_a_afficher'))
        except:
            self.nbr_part_a_afficher = 3
        self.aff_gen = parser2.get('disk_reglages', 'afficher_general')
        self.check_nom_device = IntVar(value=0)
        self.check_mount_point = IntVar(value=0)
        self.check_devmp_unchange = IntVar(value=1)

        self.var_adjust_used = StringVar(value='unchange')
        self.une_ou_deux_ligne = StringVar(value='unchange')
        self.used_oui_non = StringVar(value='unchange')

        self.afficherLigneFree = StringVar(value='unchange')
        self.nbr_part_a_appliquer = StringVar(value='toutes')
        self.unite_r_w = StringVar(value='unchange')

        self.variable_nbr_part_a_afficher_toute_ou_une= StringVar(value='toutes')
        self.var_adjust_used = StringVar(value='unchange')
        self.radio_conv = IntVar(value=int(unite_conv))
        self.pond_value = StringVar(value='unchange')
        self.messager = message(parent)
        self.var_affich_general = StringVar(value=parser2.get('disk_reglages', 'afficher_general'))
        self.frame_choix_une_ou_plus_part = ttk.Frame
        self.canvas_left = tkinter.Canvas
        self.canvas_right = tkinter.Canvas
        self.frame_right = ttk.Frame
        self.frame_part = tkinter.Frame
        self.win_root = win_root
        self.afficher_list_part_right_side = False
        self.var_nbr_part_a_afficher = StringVar(value=str(self.nbr_part_a_afficher))
        self.fen_lier_diskk = tkinter.Toplevel
        self.fen_black = tkinter.Toplevel

    def appliquer_reglages_left_side(self):
        j = 0
        str_forget_arranged = ''
        self.liste_disque_to_forget = []
        self.liste_mountp_to_forget = []
        self.part_a_afficher = []
        for part in self.disk_part:
            aa = self.list_number[j]
            i = aa.get()
            self.dic_check_button_updated[str(part.mountpoint)] = i
            if i == 1:      # 1=if checked
                self.part_a_afficher.append(part)
            else:
                self.liste_disque_to_forget.append(part)
                self.liste_mountp_to_forget.append(part.mountpoint)
                str_forget_arranged += str(part.mountpoint) + '=>'
            j += 1
        str_forget_final = str_forget_arranged[:-2]
        access_forg_reg = accesseur.accessToSettings('settings.ini')
        access_forg_reg.set('app_settings', 'update', 'True')
        access_forg_reg.set('disk', 'to_forget', str(str_forget_final))

        self.messager.afficher_mess('Tout est ok.', 'Vos choix ont bien été appliqués!', 'info')

    def set_param_to_unchange(self):
        self.var_affich_general.set(self.aff_gen)
        self.check_nom_device.set(0)
        self.check_mount_point.set(0)
        self.check_devmp_unchange.set(1)

        self.var_adjust_used.set('unchange')
        self.une_ou_deux_ligne.set('unchange')
        self.used_oui_non.set('unchange')

        self.afficherLigneFree.set('unchange')
        self.unite_r_w.set('unchange')
        self.pond_value.set('unchange')

        self.var_adjust_used.set('unchange')
        if self.afficher_list_part_right_side:
            self.variable_nbr_part_a_afficher_toute_ou_une.set('une')
            i = 0
            for leter in self.list_letters2:
                try:
                    leter.set(0)
                    i += 1
                except AttributeError:
                    break
        else:
            self.variable_nbr_part_a_afficher_toute_ou_une.set('toutes')

    def appliquer_reglages_right_side(self):
        self.aff_gen = self.var_affich_general.get()
        if self.pond_value.get() in self.liste_pond_values:
            pond_value = self.pond_value.get()
        else:
            self.messager.afficher_mess('erreur', 'Votre choix pour la valeur de pondération "R", "W" ne peut pas'
                                                  ' etre accepté.', 'error')
            return
        try:
            nbr_part = int(self.var_nbr_part_a_afficher.get())
        except ValueError:
            self.messager.afficher_mess('erreur', 'Il semble que la valeur pour le nombre de partions a afficher ne soit pas un'
                                            ' nombre valide', 'error')
            return
        if nbr_part < 0:
            self.messager.afficher_mess('erreur', 'Il n est pas possible d\'afficher moins de 0 partitions.', 'error')
            return
        elif nbr_part > 10:
            question_nbr_part = self.messager.afficher_mess('Info', 'Souhaitez vous afficher {} partitions ?'
                                                      .format(nbr_part), 'yesno')
            if question_nbr_part == False:
                return
        adjust_used = self.var_adjust_used.get()
        if adjust_used in self.list_adjust_used:
            pass
        else:
            self.messager.afficher_mess('erreur', 'La valeur demandée pour l\'ajustement de % used n\'est pas prise en'
                                                  ' charge, veuillez la choisir dans la liste.', 'error')
            return
        unite_rw = self.unite_r_w.get()
        if (unite_rw in self.liste_w_r):
            pass
        else:
            self.messager.afficher_mess('Erreur', '{} n\'est pas dans la liste des options "read, write"'.format(unite_rw),
                                  'error')
            return



        devicemount = ''
        if self.check_nom_device.get() == 1:
            devicemount = 'device'
        if self.check_mount_point.get() == 1:
            devicemount += 'mountp'
        if self.check_devmp_unchange.get() == 1:
            devicemount = 'unchange'
        nbrLignes = str(self.une_ou_deux_ligne.get())
        used = str(self.used_oui_non.get())
        part_a_appliquer = str(self.variable_nbr_part_a_afficher_toute_ou_une.get())
        ligneFree = str(self.afficherLigneFree.get())
        unite_read_write = str(self.unite_r_w.get())
        radio_convert = self.radio_conv.get()
        if radio_convert != 1024 and radio_convert != 1000:
            radio_convert = 1024
        parser_right_side = accesseur.accessToSettings('settings.ini')
        i = 0
        liste_moun = []
        for leter in self.list_letters2:
            try:
                if leter.get() == 1:
                    liste_moun.append(self.part_a_afficher[i])
                i += 1
            except AttributeError:
                break
        if part_a_appliquer == 'une' and len(liste_moun) == 0:
            self.messager.afficher_mess('Il manque quelque chose...', 'Vous avez séléctionner: \n'
                                                              '"appliquer a une ou plusieurs partitions", \n'
                                                              'mais vous n avez pas sélectionner la ou les partitions.',
                                  'info')
            return
        if part_a_appliquer == 'toutes':
            rep = self.messager.afficher_mess('Info', 'Etes-vous sûr de vouloir appliquer ces changements a toutes les'
                                                ' partitions?', 'yesno')
            if rep == False:
                return
            for part in self.disk_part:
                if self.os_actual == 'Windows':
                    part_moun = part.mountpoint[:1]
                else:
                    part_moun = part.mountpoint
                liste_param = parser_right_side.get('disk_reglages', part_moun).split('=>')
                if devicemount == 'unchange':
                    devicemount = liste_param[0]
                if nbrLignes == 'unchange':
                    nbrLignes = liste_param[1]
                if used == 'unchange':
                    used = liste_param[2]
                if ligneFree == 'unchange':
                    ligneFree = liste_param[3]
                if unite_read_write == 'unchange':
                    unite_read_write = liste_param[4]
                if self.var_adjust_used.get() == 'unchange':
                    adjust_used = liste_param[5]
                else:
                    adjust_used = str(self.var_adjust_used.get())
                if pond_value == 'unchange':
                    pond_value = liste_param[6]
                parser_right_side.set('disk_reglages', part_moun, devicemount + '=>' + nbrLignes + '=>' + used + '=>'
                           + ligneFree + '=>' + unite_read_write + '=>' + adjust_used + '=>' + pond_value)
                parser_right_side.set('disk_reglages', 'appliquer_all', 'True')
            parser_right_side.set('disk_reglages', 'settings_all', devicemount + '=>' + nbrLignes + '=>' + used + '=>'
                                  + ligneFree + '=>' + unite_read_write + '=>' + adjust_used + '=>' + pond_value)
        else:
            for dis in liste_moun:
                if self.os_actual == 'Windows':
                    dis = dis[:1]
                liste_param = parser_right_side.get('disk_reglages', dis).split('=>')
                if devicemount == 'unchange':
                    devicemount = liste_param[0]
                if nbrLignes == 'unchange':
                    nbrLignes = liste_param[1]
                if used == 'unchange':
                    used = liste_param[2]
                if ligneFree == 'unchange':
                    ligneFree = liste_param[3]
                if unite_read_write == 'unchange':
                    unite_read_write = liste_param[4]
                if self.var_adjust_used.get() == 'unchange':
                    adjust_used = liste_param[5]
                else:
                    adjust_used = str(self.var_adjust_used.get())
                if pond_value == 'unchange':
                    pond_value = liste_param[6]
                parser_right_side.set('disk_reglages', str(dis), devicemount + '=>' + nbrLignes + '=>' + used + '=>'
                                      + ligneFree + '=>' + unite_read_write + '=>' + str(adjust_used) + '=>' + pond_value)
                parser_right_side.set('disk_reglages', 'appliquer_all', 'False')
        nbr_part = self.var_nbr_part_a_afficher.get()
        self.nbr_part_a_afficher = nbr_part
        parser_right_side.set('disk_reglages', 'nbr_disk_a_afficher', str(nbr_part))
        parser_right_side.set('disk_reglages', 'update', 'True')
        parser_right_side.set('disk_reglages', 'converter', str(radio_convert))
        parser_right_side.set('disk_reglages', 'afficher_general', self.aff_gen)
        parser_right_side.set('disk_reglages', 'adjust_used', adjust_used)
        parser_right_side.set('app_settings', 'update', 'True')
        if part_a_appliquer == 'une':
            self.afficher_list_part_right_side = True
        elif part_a_appliquer == 'toutes':
            self.afficher_list_part_right_side = False
        self.messager.afficher_mess('Tout est ok', 'Vos choix ont bien été appliqués!', 'info')
        self.set_param_to_unchange()

    def left_scroll_event(self, event):
        self.canvas_left.configure(scrollregion=self.canvas_left.bbox("all"))

    def afficher_liste_part(self, fram):
        if self.isopene:
            pass
        else:
            parser = accesseur.accessToSettings('settings.ini')
            parsed = parser.get('disk', 'to_forget')
            if parsed != '' and parsed != 'void':
                liste_mountpoint_to_forget = parsed.split('=>')
            else:
                liste_mountpoint_to_forget = ''
            try:
                conv = int(parser.get('disk_reglages', 'converter'))
            except configparser.NoOptionError:
                conv = 1024
            self.liste_disque_to_forget = []
            for mountpoint in liste_mountpoint_to_forget:
                try:
                    splitedString = parser.get('disk_reglages', mountpoint).split('=>')
                except configparser.NoOptionError:
                    splitedString = ["devicemountp", "1ligne", "afficherused", "afficherLigneFree", "auto", "0",
                                     "1"]
                dis = UnDisque()
                dis.creer_disque(mountpoint, conv, pond=splitedString[6], lignes=splitedString[1],
                                   afficher_used=splitedString[2], ligne_free=splitedString[3])
                self.liste_disque_to_forget.append(dis)
            self.isopene = True

            left_fen_fram = ttk.Frame(fram, relief='groove', borderwidth=3)
            left_fen_fram.grid(column=1, row=1, padx=5, pady=5)
            liste_part_frame = ttk.Frame(left_fen_fram)
            liste_part_frame.grid(column=1, row=3)

            label_choisir = ttk.Label(liste_part_frame, text='Selectionez ci-dessous les partitions\n'
                                                             'a afficher:')
            label_choisir.grid(column=1, columnspan=2, row=1)

            self.canvas_left = Canvas(liste_part_frame, height=400)
            frame = Frame(self.canvas_left)
            myscrollbar = Scrollbar(liste_part_frame, orient="vertical", command=self.canvas_left.yview)
            self.canvas_left.configure(yscrollcommand=myscrollbar.set)
            myscrollbar.grid(column=4, row=2, sticky=NS)
            self.canvas_left.grid(column=1, columnspan=3, row=2)
            self.canvas_left.create_window((0, 0), window=frame, anchor='nw')
            frame.bind("<Configure>", self.left_scroll_event)

            j = 0
            kk = 0
            liste_black = parser.get('disk', 'blacklist').split('=>')
            end_loop = False
            for part in self.disk_part:
                end_loop = False
                for black in liste_black:
                    if black[:len(black)] == part.mountpoint[:len(black)]:
                        self.list_number.append(IntVar(value=0))  # set 0 for uncheck box
                        k = ttk.Checkbutton(frame, text=str(part.mountpoint),
                                            variable=self.list_number[j])
                        k.grid(column=2, columnspan=3, row=j)

                        j += 1
                        end_loop = True
                        break
                for disk_forget in self.liste_disque_to_forget:
                    if end_loop:
                        break
                    if part.mountpoint == disk_forget.mountpoint:

                        self.list_number.append(IntVar(value=0))  # set 0 for uncheck box
                        k = ttk.Checkbutton(frame, text=str(part.mountpoint),
                                            variable=self.list_number[j])
                        k.grid(column=2, columnspan=3, row=j)

                        j += 1
                        break
                    elif kk == len(self.liste_disque_to_forget) - 1:
                        self.list_number.append(IntVar(value=1))  # set 1 for check box
                        k = ttk.Checkbutton(frame, text=str(part.mountpoint),
                                            variable=self.list_number[j])
                        k.grid(column=2, columnspan=3, row=j)
                        j += 1
                    kk += 1
                if self.liste_disque_to_forget == []:
                    if end_loop:
                        continue
                    self.list_number.append(IntVar(value=1))
                    k = ttk.Checkbutton(frame, text=str(part.mountpoint),
                                        variable=self.list_number[j])
                    k.grid(column=2, columnspan=3, row=j)
                    j += 1
                kk = 0
            bouton_blacklist = tkinter.Button(liste_part_frame, text='Accéder a blacklist', command=self.acces_blacklist)
            bouton_blacklist.grid(column=1, row=4, pady=10)
            bouton_appliquer = tkinter.Button(liste_part_frame, text='Appliquer',
                                          command=self.appliquer_reglages_left_side)
            bouton_appliquer.grid(column=2, row=3)
            bouton_map = tkinter.Button(liste_part_frame, text='Lier partitions à disque',
                                          command=self.open_map_disk_window)
            bouton_map.grid(column=3, row=4, pady=10)

    def acces_blacklist(self):
        try:
            self.fen_lier_diskk.destroy()
        except TypeError:
            pass
        except AttributeError:
            pass
        fen_blacklist = c_fen_blacklist.fenBlacklist(self.win_root)
        self.fen_black = fen_blacklist.fen_blac
    def open_map_disk_window(self):
        try:
            self.fen_black.destroy()
        except TypeError:
            pass
        except AttributeError:
            pass
        fen_lier_dis = c_fen_lier_disques.fenLierDisques(self.win_root)
        self.fen_lier_diskk = fen_lier_dis.fen_lier

    def afficher_parts_a_selectionner(self):
        self.afficher_actualiser_part_a_appliquer(self.frame_choix_une_ou_plus_part)

    def cacher_parts_a_selectionner(self):
        self.afficher_actualiser_part_a_appliquer(self.frame_choix_une_ou_plus_part, True)

    def uncheck_dev_et_mp(self):
        self.check_nom_device.set(0)
        self.check_mount_point.set(0)

    def unchek_unchange_devmp(self):
        self.check_devmp_unchange.set(0)

    def make_match_right_side_with_ini(self):
        get = accesseur.accessToSettings('settings.ini')
        nbr_disk = get.get('disk_reglages', 'nbr_disk_a_afficher')
        self.var_nbr_part_a_afficher.set(nbr_disk)

    def right_scroll_event(self, event):
        self.canvas_right.configure(scrollregion=self.canvas_right.bbox("all"))

    def afficher_actualiser_part_a_appliquer(self, frame_boite, hide_part=False):
        try:
            self.frame_part.destroy()
        except NameError:
            pass
        if hide_part:
            return
        self.frame_part = tkinter.Frame(frame_boite)
        self.frame_part.grid(column=1, columnspan=3, row=4)
        self.canvas_right = Canvas(self.frame_part, height=40)
        self.frame_right = Frame(self.canvas_right, height=15)
        myscrollbar_right = Scrollbar(self.frame_part, orient="vertical", command=self.canvas_right.yview)
        self.canvas_right.configure(yscrollcommand=myscrollbar_right.set)
        myscrollbar_right.grid(column=3, row=2, sticky=NS)
        self.canvas_right.grid(column=1, columnspan=2, row=2)
        self.canvas_right.create_window((0, 0), window=self.frame_right, anchor='nw')
        self.frame_right.bind("<Configure>", self.right_scroll_event)
        i = 0
        cdisk = CDisk(None, self.win_root)
        liste_comp_mtp = cdisk.creer_list_possibles_mountpoint()

        self.nbr_part_a_afficher = int(self.var_nbr_part_a_afficher.get())
        for mp in liste_comp_mtp:
            if mp in self.liste_disque_to_forget:
                break
            self.list_letters2[i] = IntVar()
            check_part = ttk.Checkbutton(self.frame_right, text=mp, variable=self.list_letters2[i],
                                         onvalue=1)
            check_part.grid(column=1, columnspan=3, row=i + 2)
            i += 1
            if i >= 20 or i >= self.nbr_part_a_afficher:
                break

    def afficher_right_side_options(self, frame_param):
        rightFrame = ttk.Frame(frame_param, relief='groove', borderwidth=3)
        rightFrame.grid(column=2, row=1, sticky=N, padx=5, pady=5)

        affich_label = ttk.Label(rightFrame, text='Afficher infos disques?')
        affich_label.grid(column=1, columnspan=2, row=1)
        affich_radio_oui = ttk.Radiobutton(rightFrame, text='Oui', variable=self.var_affich_general, value='True')
        affich_radio_oui.grid(column=3, row=1)
        affich_radio_non = ttk.Radiobutton(rightFrame, text='Non', variable=self.var_affich_general, value='False')
        affich_radio_non.grid(column=4, row=1)

        frame_device_et_mp = ttk.Frame(rightFrame, relief='groove', borderwidth=2)
        frame_device_et_mp.grid(column=1, columnspan=3, row=2, sticky=W)
        labelNomDisque = ttk.Label(frame_device_et_mp, text='Afficher:')
        labelNomDisque.grid(column=1, row=1, sticky=W)
        chek_box_device = ttk.Checkbutton(frame_device_et_mp, text='Nom device', variable=self.check_nom_device,
                                          command=self.unchek_unchange_devmp)
        chek_box_device.grid(column=2, columnspan=2, row=1, sticky=W)
        check_box_mountpoint = ttk.Checkbutton(frame_device_et_mp, text='Point de montage',
                                               variable=self.check_mount_point, command=self.unchek_unchange_devmp)
        check_box_mountpoint.grid(column=2, columnspan=2, row=2, sticky=W)
        check_box_unchange_devmp = ttk.Checkbutton(frame_device_et_mp, text='unchange',
                                                   variable=self.check_devmp_unchange,
                                                   command=self.uncheck_dev_et_mp)
        check_box_unchange_devmp.grid(column=2, columnspan=2, row=3, sticky=W)
        frame_deux_lignes = Frame(frame_device_et_mp)
        frame_deux_lignes.grid(column=1, columnspan=3, row=4)
        label_afficher_sur = ttk.Label(frame_deux_lignes, text='Afficher sur:')
        label_afficher_sur.grid(column=1, row=1, sticky=W)
        radio_une_ligne = ttk.Radiobutton(frame_deux_lignes, text='1 ligne', variable=self.une_ou_deux_ligne,
                                          value="1ligne")
        radio_une_ligne.grid(column=2, row=1, sticky=W)
        radio_deux_lignes = ttk.Radiobutton(frame_deux_lignes, text="2 lignes", variable=self.une_ou_deux_ligne,
                                            value="2lignes")
        radio_deux_lignes.grid(column=3, row=1, sticky=W)
        radio_ligne_unchange = ttk.Radiobutton(frame_deux_lignes, text='unchange', variable=self.une_ou_deux_ligne,
                                               value='unchange')
        radio_ligne_unchange.grid(column=2, row=2, sticky=W)
        frame_used = ttk.Frame(rightFrame, relief='groove', borderwidth=2)
        frame_used.grid(column=1, columnspan=3, row=3, sticky=W, pady=5)
        label_used = ttk.Label(frame_used, text='Afficher "%used":')
        label_used.grid(column=1, row=1, sticky=W)

        radio_used_oui = ttk.Radiobutton(frame_used, text="oui", variable=self.used_oui_non,
                                         value="afficherused")
        radio_used_oui.grid(column=2, row=1, sticky=W)
        radio_used_non = ttk.Radiobutton(frame_used, text="non", variable=self.used_oui_non,
                                         value="pasafficherused")
        radio_used_non.grid(column=3, row=1, sticky=W)
        radio_used_unchange = ttk.Radiobutton(frame_used, text='unchange', variable=self.used_oui_non,
                                              value='unchange')
        radio_used_unchange.grid(column=2, row=2, sticky=W)
        label_adjust_used = ttk.Label(frame_used, text='Ajustez "%used" ici:')
        label_adjust_used.grid(column=1, row=3, sticky=W)
        adjust_entry = ttk.Combobox(frame_used, values=self.list_adjust_used, textvariable=self.var_adjust_used,
                                    width=11)
        adjust_entry.grid(column=2, row=3)
        frame_free_space = ttk.Frame(rightFrame, relief='groove', borderwidth=2)
        frame_free_space.grid(column=1, columnspan=3, row=4, sticky=W)
        free_lab = ttk.Label(frame_free_space, text='Afficher espace libre:')
        free_lab.grid(column=1, row=1)
        radio_free_oui = ttk.Radiobutton(frame_free_space, text='oui', variable=self.afficherLigneFree,
                                         value='afficherLigneFree')
        radio_free_oui.grid(column=2, row=1)
        radio_free_non = ttk.Radiobutton(frame_free_space, text='non', variable=self.afficherLigneFree,
                                         value='nepasafficherLigneFree')
        radio_free_non.grid(column=3, row=1)
        radio_free_unchange = ttk.Radiobutton(frame_free_space, text='unchange', variable=self.afficherLigneFree,
                                              value='unchange')
        radio_free_unchange.grid(column=2, row=2)
        frame_choix_R_W = ttk.Frame(rightFrame, relief='groove', borderwidth=2)
        frame_choix_R_W.grid(column=1, columnspan=3, row=5, sticky=W, pady=5)
        label_w_r = ttk.Label(frame_choix_R_W, text='Choix unité read/write:')
        label_w_r.grid(column=1, columnspan=2, row=1)
        liste_w_r = ttk.Combobox(frame_choix_R_W, values=self.liste_w_r, textvariable=self.unite_r_w, width=11)
        liste_w_r.grid(column=3, row=1)
        frame_ponderation = ttk.Frame(rightFrame, relief='groove', borderwidth=2)
        frame_ponderation.grid(column=1, columnspan=3, row=6)
        label_pond = Label(frame_ponderation, text='Pondération \'R\', \'W\' en secondes:')
        label_pond.grid(column=1, columnspan=2, row=1)
        combo_pond = ttk.Combobox(frame_ponderation, values=self.liste_pond_values, textvariable=self.pond_value,
                                  width=11)
        combo_pond.grid(column=3, row=1)
        self.frame_choix_une_ou_plus_part = ttk.Frame(rightFrame, relief='groove', borderwidth=2)
        self.frame_choix_une_ou_plus_part.grid(columnspan=3, column=1, row=7, sticky=W)
        appliquer_a = ttk.Label(self.frame_choix_une_ou_plus_part, text='Appliquer a:')
        appliquer_a.grid(column=1, row=1)
        radio_une_part = ttk.Radiobutton(self.frame_choix_une_ou_plus_part, text='Une ou plusieurs partition',
                                         variable=self.variable_nbr_part_a_afficher_toute_ou_une, value='une',
                                         command=self.afficher_parts_a_selectionner)
        radio_une_part.grid(column=2, columnspan=2, row=1, sticky=W)
        radio_toutes_part = ttk.Radiobutton(self.frame_choix_une_ou_plus_part, text='Toutes les patitions',
                                            variable=self.variable_nbr_part_a_afficher_toute_ou_une,
                                            value='toutes', command=self.cacher_parts_a_selectionner)
        radio_toutes_part.grid(column=2, columnspan=2, row=2, sticky=W)
        # self.frame_une_part = ttk.Frame(self.frame_choix_une_ou_plus_part)
        # self

        self.frame_part = Canvas(self.frame_choix_une_ou_plus_part, height=40)
        self.frame_part.grid(column=1, columnspan=3, row=4)


        frame_convertisseur = ttk.Frame(rightFrame, relief='groove', borderwidth=2)
        frame_convertisseur.grid(column=1, columnspan=3, row=8, sticky=W, pady=5)
        radio_conv_1000 = ttk.Radiobutton(frame_convertisseur, text="1Go = 1000Mo", variable=self.radio_conv,
                                          value=1000)
        radio_conv_1000.grid(column=1, row=1)
        radio_conv_1024 = ttk.Radiobutton(frame_convertisseur, text="1Go = 1024Mo", variable=self.radio_conv,
                                          value=1024)
        radio_conv_1024.grid(column=2, row=1)
        frame_nbr_part = ttk.Frame(rightFrame, relief='groove', borderwidth=2)
        frame_nbr_part.grid(column=1, columnspan=3, row=9, sticky=W, pady=5)
        lab_nbr_part_choix = ttk.Label(frame_nbr_part, text='Quantité de partitions a afficher')
        lab_nbr_part_choix.grid(column=1, columnspan=3, row=1)
        nbr_part_choix = ttk.Combobox(frame_nbr_part, values=self.liste_nbr_part_choix,
                                      textvariable=self.var_nbr_part_a_afficher, width=5)
        nbr_part_choix.grid(column=1, columnspan=3, row=2)
        buton_valider_part = ttk.Button(rightFrame, text='Appliquer',
                                        command=self.appliquer_reglages_right_side)
        buton_valider_part.grid(column=1, columnspan=3, row=10)
        self.make_match_right_side_with_ini()
        self.cacher_parts_a_selectionner()