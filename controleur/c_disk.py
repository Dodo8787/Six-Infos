import tkinter
from psutil import disk_usage, disk_partitions
from tkinter import ttk
import configparser
import modele.m_access_to_settings as getter
import vue.v_disk as v_disk
import controleur.c_convert_bit as convert_bit
import controleur.column_setter as col_setter
import controleur.generals_actions as general
import Classes.disquee as disque
import platform


class CDisk:

    def __init__(self, frame_root, win_root):
        self.os_actual = platform.system()
        self.listpathtoforget2 = []
        self.listeDiskAfficher = []
        self.diskframegeneral = tkinter.Frame
        self.diskframegeneral2 = tkinter.Frame
        self.diskframegeneral3 = tkinter.Frame
        self.diskframegeneral4 = tkinter.Frame
        self.disques_already_actualised = False
        self.colu_pour_network = 1
        gett = getter.accessToSettings('settings.ini')
        self.zone_1_max = int(gett.get('disk_reglages', 'zone_1_max'))
        self.zone_2_max = int(gett.get('disk_reglages', 'zone_2_max'))
        getter_color = getter.accessToSettings('colors.ini')
        self.color1 = getter_color.get('Disks', 'toutes').split('=>')[2]
        self.color2 = getter_color.get('Disks', 'toutes').split('=>')[3]
        self.color3 = getter_color.get('Disks', 'toutes').split('=>')[4]
        self.zoom_rat = 1
        self.v_disk = v_disk.VDisk(win_root)
        self.frame_root = frame_root
        self.col = 0
        self.row = 0
        self.liste_disk_afficher = []
        self.liste_disques = []

    def creer_list_possibles_mountpoint(self):
        geter_possi = getter.accessToSettings('settings.ini')
        disk_to_forget = geter_possi.get('disk', 'to_forget').split('=>')
        liste_disk = disk_partitions()
        liste_mtp = []
        i = 0
        for comp in liste_disk:
            if disk_to_forget == [''] or disk_to_forget == ['void']:
                liste_mtp.append(comp.mountpoint)
                continue
            for forg in disk_to_forget:
                if forg == comp.mountpoint:
                    i = 0
                    break
                elif i == len(disk_to_forget) - 1:
                    liste_mtp.append(comp.mountpoint)
                    i = 0
                i += 1

        return liste_mtp

    def afficher_disks(self, frame_root, col, row, zoom_ratio, destroy=False):
        self.col = col
        self.row = row
        self.zoom_rat = zoom_ratio
        self.liste_disk_afficher, col_network, row_network, frame_network, self.diskframegeneral, self.diskframegeneral2, \
            self.diskframegeneral3, self.diskframegeneral4, self.liste_disques = self.v_disk.v_afficher_disks(
                                                                                 frame_root
                                                                                 , col, row, zoom_ratio,
                                                                                 self.zone_1_max, self.zone_2_max,
                                                                                 self.color1, self.color2,
                                                                                 self.color3, destroy=destroy)
        return self.liste_disk_afficher, col_network, row_network, frame_network, self.diskframegeneral, self.diskframegeneral2, \
            self.diskframegeneral3, self.diskframegeneral4, self.liste_disques


    def refresh_disk(self, zoom_ratio, disque):
        gete = getter.accessToSettings('settings.ini')
        gete_color = getter.accessToSettings('colors.ini')
        color_list_change_toutes = gete_color.get('Disks', 'change_dans_applique_a_toutes').split('=>')
        color_list_toutes = gete_color.get('Disks', 'toutes').split('=>')
        try:
            color_list = gete_color.get('Disks', disque.mountpoint).split('=>')
        except configparser.NoOptionError:
            gete_color.set('Disks', disque.mountpoint, '#b4885e=>#b4885e=>#b4885e=>#b4885e=>#b4885e=>#b4885e=>#b4885e=>')
            color_list = '#b4885e=>#b4885e=>#b4885e=>#b4885e=>#b4885e=>#b4885e=>#b4885e=>'.split('=>')
        if '2' in color_list_change_toutes:
            color1 = color_list_toutes[2]
        else:
            color1 = color_list[2]
        if '3' in color_list_change_toutes:
            color2 = color_list_toutes[3]
        else:
            color2 = color_list[3]
        if '4' in color_list_change_toutes:
            color3 = color_list_toutes[4]
        else:
            color3 = color_list[4]
        unit_convert = gete.get('disk_reglages', 'converter')
        adjust = gete.get('disk_reglages', 'adjust_used')
        unite_r_w = disque.unit_w_r
        converter = convert_bit.ConvertBit()
        try:
            if self.os_actual == 'Windows':
                disque.mountpoint += ':\\'
            disku = disk_usage(disque.mountpoint)
            diskTotal = converter.convert_bit_to_go(disku.total, unit_convert)
            diskfree = converter.convert_bit_to_go(disku.free, unit_convert)
            diskpercent = disku.percent
            if adjust[0] == '+':
                diskpercent += int(adjust[1:])
            elif adjust[0] != '0':
                diskpercent -= int(adjust[1:])
            if disque.afficher_used == 'afficherused' and disque.disklabe != '':
                if disque.disklabe is not None:
                    disque.disklabe.configure(text='Disk ' + '{:.2f}'.format(diskpercent) + '% used / '
                                              + '{:.2f}'.format(diskTotal[0]) + ' ' + str(diskTotal[1] + ' total'))
            if disque.ligne_free == 'afficherLigneFree' and disque.disklabelfree != '':
                if disque.disklabelfree is not None:
                    disque.disklabelfree.configure(text='{:.2f}'.format(diskfree[0]) + ' '
                                                   + str(diskfree[1]) + ' free')
            if diskpercent <= self.zone_1_max:
                color = color1
            elif diskpercent <= self.zone_2_max:
                color = color2
            else:
                color = color3
            if disque.diskcanevas != '':
                disque.diskcanevas.delete(disque.disbar)
            disk_bar_set = diskpercent * zoom_ratio + 2
            if disque.disbar != '':
                disque.disbar = disque.diskcanevas.create_rectangle(0, 3.0, disk_bar_set, 12 * zoom_ratio, fill=color)
            if disque.disk_label_read != '' and disque.disk_label_write != '':
                try:
                    disque.read_write_disk(unite_r_w)
                except KeyError:
                    pass
        except FileNotFoundError:
            print("FileNotFoundError : " + str(disque.mountpoint) + "\nLigne 50 obsolete_Disk.py => Erreur bien gérée!"
                                                                  "(erreur peu importante)")
        except FileExistsError:
            print("FileExistError : " + str(disque.mountpoint) + "\nLigne 50 obsolete_Disk.py => Erreur bien gérée!"
                                                               "(erreur peu importante)")

    def actualiser_ini_path_to_forget(self, liste_mp_to_forget):
        preview_mp_to_forget = liste_mp_to_forget
        iii = 0
        value = ''
        if len(liste_mp_to_forget) >= 1:
            for part in liste_mp_to_forget:
                if iii < (len(liste_mp_to_forget) - 1):
                    value += part.mountpoint + '=>'
                else:
                    value += part.mountpoint
                iii += 1

            geter = getter.accessToSettings('settings.ini')
            geter.set('disk', 'to_forget', value)
            geter.set('disk_reglages', 'update', 'True')

    def verif_if_add_new_disk(self, preview_part_add_new, disk_partitions_add_new, col_net, row_net):
        if preview_part_add_new != disk_partitions_add_new:
            return True
        else:
            return False

    '''def add_new_disk(self, disk_partitions_add_new):
        gete = getter.accessToSettings('settings.ini')
        if gete.get('disk_reglages', 'afficher_general') == 'True':

            lis_dev = []
            part_to_forget = gete.get('disk', 'to_forget').split('=>')
            try:
                conv = int(gete.get('disk_reglages', 'convertion'))
            except configparser.NoOptionError:
                conv = 1024
            for dis in disk_partitions_add_new:
                try:
                    parser_splt = gete.get('disk_reglages', dis.mountpoint).split('=>')
                except configparser.NoOptionError:
                    parser_splt = [dis.mountpoint, '1lignes', 'afficherused', 'afficherLigneFree', 'auto', '0', '1']
                    gete.set('disk_reglages', dis.mountpoint,
                             'devicemountp=>2lignes=>afficherused=>afficherLigneFree=>auto=>0=>1')

                disk = disque.UnDisque()
                dev = disk.creer_disque(dis.mountpoint, conv, pond=parser_splt[6], lignes=parser_splt[1],
                                    afficher_used=parser_splt[2], ligne_free=parser_splt[3],
                                    unit_w_r=parser_splt[4], adjuste=parser_splt[5], devisse=dis.device)
                lis_dev.append(dev)
            # mp_to_forget = []
            # for dev in part_to_forget:
                # mp_to_forget.append(dev.mountpoint)
            # try:
                # nbr_part_a_afficher = int(gete.get('disk_reglages', 'part_a_afficher'))
            # except configparser.NoOptionError:
                # nbr_part_a_afficher = 3

            liste_disk_afficher, col_network, row_network, frame_network, frame_col_1, frame_col_2, \
                frame_col_3, frame_col_4, list_disks = self.v_disk.v_afficher_disks(self.frame_root, self.col,
                                                                                         self.row, self.zoom_rat,
                                                                                         self.zone_1_max, self.zone_2_max,
                                                                                         self.color1, self.color2,
                                                                                         self.color3, destroy=True)

            # diskFrameGeneral = caneva_disque.diskframegeneral
            # diskFrameGeneral2 = caneva_disque.diskframegeneral2
            # diskFrameGeneral3 = caneva_disque.diskframegeneral3
            # frame_pour_network = caneva_disque.frame_pour_network
            # row_network = caneva_disque.row_pour_network
            # column_network = caneva_disque.colu_pour_network

            for di in liste_disk_afficher:
                try:
                    unit = gete.get('disk_reglages', di.mountpoint).split('=>')
                except configparser.NoOptionError:
                    unit = ['devicemountp', '2lignes', 'afficherused', 'afficherLigneFree', 'auto', '0', '1']
                try:
                    di.unite_w_r = unit[4]
                except IndexError:
                    di.unite_w_r = 'auto'
            # disk_partitions = disk_partitions_add_new
            gete.set('disk_reglages', 'update', 'False')
        return liste_disk_afficher, col_network, row_network '''

    def delete_widget_disk(self):
        try:
            self.destroy(self.diskframegeneral)
            self.diskframegeneral2.destroy()
            self.diskframegeneral3.destroy()
            self.diskframegeneral4.destroy()
        except TypeError:
            pass

    def update_style(self):
        self.v_disk.v_update_style()