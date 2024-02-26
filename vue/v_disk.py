import modele.m_access_to_settings as getter
from psutil import disk_partitions, disk_usage, disk_io_counters
import tkinter
from tkinter import ttk
import controleur.column_setter as col_setter
import Classes.disquee as UNdisque
import configparser
import platform


class VDisk:
    def __init__(self, win_root):
        self.os_actual = platform.system()
        self.diskframegeneral = tkinter.Frame
        self.diskframegeneral2 = tkinter.Frame
        self.diskframegeneral3 = tkinter.Frame
        self.diskframegeneral4 = tkinter.Frame
        self.frame_root = tkinter.Frame
        self.win_root = win_root
        self.frame_col_1 = None
        self.frame_col_2 = None
        self.frame_col_3 = None
        self.frame_col_4 = None
        self.list_disks = []
        self.listDiskFrame = []
        self.listDiskCanevas = []
        self.listDiskFrameRead = []
        self.listDiskFrameWrite= []

    def v_afficher_disks(self, frame_root, col, row, zoom_ratio, zone_1_max, zone_2_max, color1, color2, color3,
                         destroy=False):
        self.frame_root = frame_root
        font_color_getter = getter.accessToSettings('color_font.ini')
        font_color_number_for_all = font_color_getter.get('Disks', 'change_dans_applique_a_toutes').split('=>')
        color_getter = getter.accessToSettings('colors.ini')
        color_princ = color_getter.get('Disks', 'principale')
        color_une_ou_toutes = color_getter.get('Last_choice', 'colors_disks')

        liste_disk_afficher = []
        geter_vdisk = getter.accessToSettings('settings.ini')
        conv = geter_vdisk.get('disk_reglages', 'converter')
        geter_font_disk = getter.accessToSettings('font.ini')
        disk_inf_font_toutes_ou_une = str(geter_font_disk.get('disk_font', 'dernier_choix'))
        disk_inf_font = str(geter_font_disk.get('disk_font', 'disk_infos'))
        list_font_toutes = geter_font_disk.get('disk_font', 'toutes').split('=>')
        self.list_disks = disk_partitions()
        nbr_a_afficher = geter_vdisk.get('disk_reglages', 'nbr_disk_a_afficher')
        liste_path_from_file = geter_vdisk.get('disk', 'to_forget')
        if liste_path_from_file == 'void':
            liste_path_to_forget = []
        else:
            liste_path_to_forget = liste_path_from_file.split('=>')

        geter = getter.accessToSettings('settings.ini')
        to_continue = True
        i = 0
        self.listpathtoforget2 = liste_path_to_forget
        if self.listpathtoforget2 is None or len(self.listpathtoforget2) == 0:
            self.listpathtoforget2 = [""]
        listDiskFrameGen = [self.diskframegeneral, self.diskframegeneral2, self.diskframegeneral3]
        self.listDiskFrame = []

        canevas1 = tkinter.Canvas
        canevas2 = tkinter.Canvas
        canevas3 = tkinter.Canvas
        self.disques_already_actualised = False
        aa = 0
        list_diskFrame = ['diskFrame1', 'diskFrame2', 'diskFrame3']
        iFrameGen = 0

        col_disk = 1
        if destroy:
            self.destroy_all_disk()
        self.frame_col_1 = tkinter.Frame(self.frame_root)
        self.frame_col_1.grid(column=1, row=2, sticky=tkinter.N)
        self.diskframegeneral = tkinter.Frame(self.frame_col_1, relief='raised', borderwidth=4,
                                              background=color_princ)
        self.diskframegeneral.grid(column=col, row=row, rowspan=25, sticky=tkinter.N)
        self.row_pour_network = row + 1
        color_font_title = font_color_getter.get('disk', 'title')
        diskLabelGen = ttk.Label(self.diskframegeneral, text=" Disk Infos:", width=35, font=(disk_inf_font,
                                                                                            int(10 * zoom_ratio)),
                                 background=color_princ, foreground=color_font_title)
        diskLabelGen.grid(column=1, columnspan=2, row=1)
        self.row_pour_network = 3
        self.colu_pour_network = 1
        frame_root.update()
        col_seter = col_setter.ColumnSetter(self.win_root)
        if not col_seter.valide_height(frame_root.winfo_height()):
            self.diskframegeneral.grid(column=col + 1, row=1, sticky=tkinter.N)
            frame_root.update()
            col += 2
            self.row_pour_network = 3
        canevas = tkinter.Canvas(self.diskframegeneral, height=0, width=int(10 * zoom_ratio))
        canevas.grid(column=1, row=2, sticky=tkinter.W)
        self.frame_pour_network = self.frame_root
        varcanevas = canevas
        row = 1
        count_frame_gen = 0
        diskframerow = 2
        sep = ""
        colors_list_toutes = color_getter.get('Disks', 'toutes').split('=>')
        colors_list_indices_toutes = color_getter.get('Disks', 'change_dans_applique_a_toutes').split('=>')
        can_count = 0
        getter_blacklist = getter.accessToSettings('settings.ini')
        liste_disks_blacklist = getter_blacklist.get('disk', 'blacklist').split('=>')
        list_white = []
        for disks in self.list_disks:
            i = 0
            for black in liste_disks_blacklist:
                if black[:len(black)] == disks.mountpoint[:len(black)] and black != '':
                    break
                if i == len(liste_disks_blacklist) - 1:
                    list_white.append(disks)
                i += 1
        i = 0
        for disque in list_white:
            if self.os_actual == 'Windows':
                disque_mnt = disque.mountpoint[:1]
            else:
                disque_mnt = disque.mountpoint

            breaking = False
            try:
                font_color_list = font_color_getter.get('Disks', disque_mnt).split('=>')
                font_color_toutes = font_color_getter.get('disk', 'toutes').split('=>')
                for index in font_color_number_for_all:
                    if index == '':
                        continue
                    font_color_list[int(index) - 1] = font_color_toutes[int(index) - 1]
            except configparser.NoOptionError:
                font_color_list = font_color_getter.get('disk', 'toutes').split('=>')
            try:
                colors_list = color_getter.get('Disks', disque_mnt).split('=>')
            except configparser.NoOptionError:
                colors_list = color_getter.get('Disks', 'toutes').split('=>')
            for mp in self.listpathtoforget2:
                if mp == disque_mnt:
                    breaking = True
                    break
            if breaking:
                continue
            # obtenir font
            getter_font = getter.accessToSettings('font.ini')

            if disk_inf_font_toutes_ou_une == 'toutes':
                font_nom_device = list_font_toutes[0]
                font_mount_point = list_font_toutes[1]
                font_used_et_total = list_font_toutes[2]
                font_free = list_font_toutes[3]
                font_read = list_font_toutes[4]
                font_write = list_font_toutes[5]
            else:
                try:
                    font_nom_device = str(getter_font.get(disque_mnt, 'nom_device'))
                    if font_nom_device == 'None':
                        font_nom_device = list_font_toutes[0]

                    font_mount_point = str(getter_font.get(disque_mnt, 'mount_point'))
                    if font_mount_point == 'None':
                        font_mount_point = list_font_toutes[1]

                    font_used_et_total = str(getter_font.get(disque_mnt, 'used_et_total'))
                    if font_used_et_total == 'None':
                        font_used_et_total = list_font_toutes[2]

                    font_free = str(getter_font.get(disque_mnt, 'free'))
                    if font_free == 'None':
                        font_free = list_font_toutes[3]

                    font_read = str(getter_font.get(disque_mnt, 'font_read'))
                    if font_read == 'None':
                        font_read = list_font_toutes[4]

                    font_write = str(getter_font.get(disque_mnt, 'font_write'))
                    if font_write == 'None':
                        font_write = list_font_toutes[5]

                except configparser.NoSectionError:
                    font_nom_device = str(getter_font.set(disque_mnt, 'nom_device', 'Arial'))
                    font_mount_point = str(getter_font.set(disque_mnt, 'mount_point', 'Arial'))
                    font_used_et_total = str(getter_font.set(disque_mnt, 'used_et_total', 'Arial'))
                    font_free = str(getter_font.set(disque_mnt, 'free', 'Arial'))
                    font_read = str(getter_font.set(disque_mnt, 'font_read', 'Arial'))
                    font_write = str(getter_font.set(disque_mnt, 'font_write', 'Arial'))


            try:
                reglages = geter.get('disk_reglages', disque_mnt)
                reglages_splited = reglages.split('=>')
            except configparser.NoOptionError:
                reglages_splited = geter.get('disk_reglages', 'settings_all').split('=>')
            '''if len(reglages_splited) < 5:
                reglages_splited = ['devicemountp', '1lignes', 'afficherused', 'afficherLigneFree', 'auto', '0']'''
            ii = 0
            if reglages_splited[1] == '1ligne':
                sep = " "
            else:
                sep = "\n"
            coll = 1
            for path2 in self.listpathtoforget2:
                if str(disque_mnt) == str(path2):
                    break
                elif ii >= len(self.listpathtoforget2) - 1:
                    if aa < int(nbr_a_afficher):

                        disk = disk_usage(disque.mountpoint)
                        if '0' in colors_list_indices_toutes:
                            colors_list[0] = colors_list_toutes[0]
                        self.listDiskFrame.append(tkinter.Frame(varcanevas, width=14, relief="raised", borderwidth=1,
                                                           background=colors_list[0]))
                        self.listDiskFrame[i].grid(column=1, columnspan=2, row=diskframerow, sticky=tkinter.W)
                        roww = 2
                        if reglages_splited[0] == 'devicemountp':
                            if sep == "\n":
                                colspan = 2
                                widt = 30
                            else:
                                colspan = 1
                                widt = 15
                            diskTitle = ttk.Label(self.listDiskFrame[i], width=widt, text=str(disque.device),
                                                  font=(font_nom_device, int(10 * zoom_ratio)),
                                                  background=colors_list[0], foreground=font_color_list[0])
                            diskTitle.grid(column=1, columnspan=colspan, row=roww, sticky=tkinter.W)
                            if sep == '\n':
                                roww += 1
                                coll = 1
                            else:
                                coll = 2
                            diskTitle2 = ttk.Label(self.listDiskFrame[i], width=widt, text=str(disque.mountpoint),
                                                   font=(font_mount_point, int(10 * zoom_ratio)),
                                                   background=colors_list[0], foreground=font_color_list[1])
                            diskTitle2.grid(column=coll, columnspan=colspan, row=roww, sticky=tkinter.W)
                            roww += 1
                        elif reglages_splited[0] == 'device':
                            diskTitle = ttk.Label(self.listDiskFrame[i], width=30, text=str(disque.device),
                                                  font=(font_nom_device, int(10 * zoom_ratio)),
                                                  background=colors_list[0], foreground=font_color_list[0])
                            diskTitle.grid(column=1, columnspan=2, row=roww, sticky=tkinter.W)
                            roww += 1
                        elif reglages_splited[0] == 'mountp':
                            diskTitle = ttk.Label(self.listDiskFrame[i], width=30, text=str(disque.mountpoint),
                                                  font=(font_mount_point, int(10 * zoom_ratio)),
                                                  background=colors_list[0], foreground=font_color_list[1])
                            diskTitle.grid(column=1, columnspan=2, row=2, sticky=tkinter.W)
                            roww += 1
                        if reglages_splited[2] == 'afficherused':
                            diskLabel = ttk.Label(self.listDiskFrame[i], width=32, text='Disk ...% used / ...',
                                                  font=(font_used_et_total, int(10 * zoom_ratio)),
                                                  background=colors_list[0], foreground=font_color_list[2])
                            diskLabel.grid(column=1, columnspan=2, row=roww, sticky=tkinter.W)
                            roww += 1
                        else:
                            diskLabel = None
                            self.row_pour_network -= 1
                        if '1' in colors_list_indices_toutes:
                            colors_list[1] = colors_list_toutes[1]
                        self.listDiskCanevas.append(tkinter.Canvas(self.listDiskFrame[i], height=10 * zoom_ratio,
                                                              width=int(100 * zoom_ratio), relief='raised', borderwidth=2,
                                                              background=colors_list[1], highlightthickness=0))
                        self.listDiskCanevas[can_count].grid(column=1, row=roww, sticky=tkinter.W)
                        diskx1 = disk.percent
                        if diskx1 <= zone_1_max:
                            if '2' in colors_list_indices_toutes:
                                color = colors_list_toutes[2]
                            else:
                                color = colors_list[2]
                        elif diskx1 <= zone_2_max:
                            if '3' in colors_list_indices_toutes:
                                color = colors_list_toutes[3]
                            else:
                                color = colors_list[3]
                        else:
                            if '3' in colors_list_indices_toutes:
                                color = colors_list_toutes[3]
                            else:
                                color = colors_list[3]
                        diskBar = self.listDiskCanevas[aa].create_rectangle(0.0, 3.0, diskx1 * zoom_ratio + 2,
                                                                        12 * zoom_ratio, fill=color)
                        if reglages_splited[3] == 'afficherLigneFree':
                            diskLabelFree = ttk.Label(self.listDiskFrame[i], text='...' + ' free',
                                                      font=(font_free, int(10 * zoom_ratio)), background=colors_list[0],
                                                      foreground=font_color_list[3])
                            diskLabelFree.grid(column=2, row=roww, sticky=tkinter.W)
                            roww += 1
                        else:
                            diskLabelFree = None
                        if '5' in colors_list_indices_toutes:
                            colors_list[5] = colors_list_toutes[5]
                        self.listDiskFrameWrite.append(tkinter.Frame(self.listDiskFrame[i], relief='ridge', borderwidth=2,
                                                       width=int(9 * zoom_ratio), background=colors_list[5]))
                        self.listDiskFrameWrite[can_count].grid(column=1, row=roww)
                        if '6' in colors_list_indices_toutes:
                            colors_list[6] = colors_list_toutes[6]
                        self.listDiskFrameRead.append(tkinter.Frame(self.listDiskFrame[i], relief='ridge', borderwidth=2,
                                                  width=int(9 * zoom_ratio), background=colors_list[6]))
                        self.listDiskFrameRead[can_count].grid(column=2, row=roww)

                        diskLabelWrite = ttk.Label(self.listDiskFrameWrite[can_count], text='W: ...', width=15,
                                                   font=(font_write, int(9 * zoom_ratio)),
                                                   background=colors_list[5], foreground=font_color_list[4])
                        diskLabelWrite.grid(column=1, row=1, sticky=tkinter.W)
                        diskLabelRead = ttk.Label(self.listDiskFrameRead[can_count], text='R: ...', width=15,
                                                  font=(font_read, int(9 * zoom_ratio)),
                                                  background=colors_list[6], foreground=font_color_list[5])
                        diskLabelRead.grid(column=2, row=1, sticky=tkinter.W)
                        frame_root.update()
                        row += 1
                        if not col_seter.valide_height(frame_root.winfo_height()):

                            if count_frame_gen == 0:
                                self.frame_col_2 = ttk.Frame(frame_root)
                                self.frame_col_2.grid(column=2, row=1, rowspan=30, sticky=tkinter.N)
                                self.diskframegeneral2 = tkinter.Frame(self.frame_col_2, relief='raised',
                                                                       borderwidth=4, background=color_princ)
                                self.diskframegeneral2.grid(column=1, row=1,
                                                            sticky=tkinter.N)
                                diskLabelGen2 = ttk.Label(self.diskframegeneral2, text="Disk Infos 2:", width=35,
                                                          font=(disk_inf_font, int(10 * zoom_ratio)),
                                                          background=color_princ, foreground=color_font_title)
                                diskLabelGen2.grid(column=1, row=1, sticky=tkinter.NW)
                                self.listDiskFrame[i].destroy()

                                diskCanevas2 = tkinter.Canvas(self.diskframegeneral2, width=int(10 * zoom_ratio),
                                                              background=colors_list[0])
                                diskCanevas2.grid(column=1, row=2, sticky=tkinter.W)
                                varcanevas = diskCanevas2

                                self.frame_pour_network = self.frame_col_2

                            coll += 1
                            self.row_pour_network = 3
                            row = 1

                            if count_frame_gen != 0:
                                if count_frame_gen == 1:
                                    frame_root.update()
                                    self.frame_col_3 = tkinter.Frame(frame_root)
                                    self.frame_col_3.grid(column=3, row=1, rowspan=30, sticky=tkinter.N)
                                    self.diskframegeneral3 = tkinter.Frame(self.frame_col_3, relief='raised',
                                                                           borderwidth=4,
                                                                           background=color_princ)
                                    self.diskframegeneral3.grid(column=1, row=1,
                                                                sticky=tkinter.N)
                                    diskLabelGen3 = ttk.Label(self.diskframegeneral3, text="Disk Infos 3:",
                                                              width=35, font=(disk_inf_font,
                                                                              int(10 * zoom_ratio)),
                                                              background=color_princ, foreground=color_font_title)
                                    diskLabelGen3.grid(column=1, row=1, sticky=tkinter.W)
                                    self.listDiskFrame[i].destroy()
                                    iFrameGen += 1

                                    diskCanevas3 = tkinter.Canvas(self.diskframegeneral3, height=0,
                                                          width=int(10 * zoom_ratio), background=colors_list[0])
                                    diskCanevas3.grid(column=1, row=2, sticky=tkinter.W)
                                    varcanevas = diskCanevas3
                                    self.frame_pour_network = self.frame_col_3
                                    self.row_pour_network = 3


                                elif count_frame_gen == 2:
                                    frame_root.update()
                                    self.frame_col_4 = tkinter.Frame(frame_root)
                                    self.frame_col_4.grid(column=4, row=1, sticky=tkinter.N)
                                    self.diskframegeneral4 = tkinter.Frame(self.frame_col_4, relief='raised',
                                                                           borderwidth=4,
                                                                           background=color_princ)
                                    self.diskframegeneral4.grid(column=1, row=1, rowspan=200,
                                                                sticky=tkinter.N)
                                    diskLabelGen4 = ttk.Label(self.diskframegeneral4, text="Disk Infos 4:",
                                                              width=35, font=(disk_inf_font, int(10 * zoom_ratio)),
                                                              background=color_princ, foreground=color_font_title)
                                    diskLabelGen4.grid(column=1, row=1, sticky=tkinter.W)
                                    self.listDiskFrame[i].destroy()

                                    iFrameGen += 1

                                    diskCanevas4 = tkinter.Canvas(self.diskframegeneral4, height=0,
                                                          width=int(10 * zoom_ratio), background=colors_list[0])
                                    diskCanevas4.grid(column=1, row=2, sticky=tkinter.W)
                                    self.frame_pour_network = self.frame_col_4
                                    self.row_pour_network = 3
                                    varcanevas = diskCanevas4

                            count_frame_gen += 1

                            self.listDiskFrame[i] = tkinter.Frame(varcanevas, width=14, relief="raised",
                                                             borderwidth=1, background=colors_list[0])
                            self.listDiskFrame[i].grid(column=1, columnspan=2, row=1, sticky=tkinter.W)
                            roww = 2
                            if reglages_splited[0] == 'devicemountp':
                                if sep == "\n":
                                    colspan = 2
                                    widt = 30
                                else:
                                    colspan = 1
                                    widt = 15
                                diskTitle = ttk.Label(self.listDiskFrame[i], width=widt, text=str(disque.device),
                                                      font=(font_nom_device, int(10 * zoom_ratio)),
                                                      background=colors_list[0], foreground=font_color_list[0])
                                diskTitle.grid(column=1, columnspan=colspan, row=roww, sticky=tkinter.W)
                                if sep == "\n":
                                    roww += 1
                                    coll = 1
                                else:
                                    coll = 2
                                diskTitle2 = ttk.Label(self.listDiskFrame[i], width=widt,
                                                      text=str(disque.mountpoint),
                                                      font=(font_mount_point, int(10 * zoom_ratio)),
                                                       background=colors_list[0], foreground=font_color_list[1])
                                diskTitle2.grid(column=coll, columnspan=colspan, row=roww, sticky=tkinter.W)
                                roww += 1

                            elif reglages_splited[0] == 'device':
                                diskTitle = ttk.Label(self.listDiskFrame[i], width=30, text=str(disque.device),
                                                      font=(font_nom_device, int(10 * zoom_ratio)),
                                                      background=colors_list[0], foreground=font_color_list[0])
                                diskTitle.grid(column=1, columnspan=2, row=roww, sticky=tkinter.W)
                                roww += 1
                            elif reglages_splited[0] == 'mountp':
                                diskTitle = ttk.Label(self.listDiskFrame[i], width=30, text=str(disque.mountpoint),
                                                      font=(font_mount_point, int(10 * zoom_ratio)),
                                                      background=colors_list[0], foreground=font_color_list[1])
                                diskTitle.grid(column=1, columnspan=2, row=roww, sticky=tkinter.W)
                                roww += 1
                            if reglages_splited[2] == 'afficherused':
                                diskLabel = ttk.Label(self.listDiskFrame[i], width=32, text='Disk ...% used / ...',
                                                      font=(font_used_et_total, int(10 * zoom_ratio)),
                                                      background=colors_list[0], foreground=font_color_list[2])
                                diskLabel.grid(column=1, columnspan=2, row=roww, sticky=tkinter.W)
                                roww += 1
                            else:
                                diskLabel = None

                            self.listDiskCanevas[can_count] = tkinter.Canvas(self.listDiskFrame[i], height=10 * zoom_ratio,
                                                                       width=int(100 * zoom_ratio), relief='raised',
                                                                       borderwidth=2, background=colors_list[1],
                                                                       highlightthickness=0)
                            self.listDiskCanevas[can_count].grid(column=1, row=roww, sticky=tkinter.W)
                            diskx1 = disk.percent
                            if diskx1 <= zone_1_max:
                                color = color1
                            elif diskx1 <= zone_2_max:
                                color = color2
                            else:
                                color = color3
                            diskBar = self.listDiskCanevas[can_count].create_rectangle(0.0, 3.0, diskx1 * zoom_ratio + 2,
                                                                            12 * zoom_ratio, fill=colors_list[2])
                            if reglages_splited[3] == 'afficherLigneFree':
                                diskLabelFree = ttk.Label(self.listDiskFrame[i], text='...' + ' free',
                                                          font=(font_free, int(10 * zoom_ratio)),
                                                          background=colors_list[0], foreground=font_color_list[3])
                                diskLabelFree.grid(column=2, row=roww, sticky=tkinter.W)
                                roww += 1
                            else:
                                diskLabelFree = None
                            self.listDiskFrameWrite[can_count] = tkinter.Frame(self.listDiskFrame[i], relief='ridge', borderwidth=2,
                                                           width=int(9 * zoom_ratio), background=colors_list[5])
                            self.listDiskFrameWrite[can_count].grid(column=1, row=roww)
                            self.listDiskFrameRead[can_count] = tkinter.Frame(self.listDiskFrame[i], relief='ridge', borderwidth=2,
                                                          width=int(9 * zoom_ratio), background=colors_list[6])
                            self.listDiskFrameRead[can_count].grid(column=2, row=roww)

                            diskLabelWrite = ttk.Label(self.listDiskFrameWrite[can_count], text='W: ...', width=15,
                                                       font=(font_write, int(9 * zoom_ratio)),
                                                       background=colors_list[5], foreground=font_color_list[4])
                            diskLabelWrite.grid(column=1, row=1, sticky=tkinter.W)
                            diskLabelRead = ttk.Label(self.listDiskFrameRead[can_count], text='R: ...', width=15,
                                                      font=(font_read, int(9 * zoom_ratio)),
                                                      background=colors_list[6], foreground=font_color_list[5])
                            diskLabelRead.grid(column=2, row=1, sticky=tkinter.W)
                            frame_root.update()
                            diskframerow = 2
                            self.colu_pour_network += 1

                        self.device = disque.device
                        try:
                            splitedParse = geter.get('disk_reglages', disque_mnt).split('=>')
                        except configparser.NoOptionError:
                            splitedParse = geter.get('disk_reglages', 'settings_all').split('=>')
                        dev = UNdisque.UnDisque()
                        dev.creer_disque(str(disque.mountpoint), conv, pond=splitedParse[6], lignes=splitedParse[1],
                                         afficher_used=splitedParse[2], ligne_free=splitedParse[3], disbar=diskBar,
                                         diskframe=listDiskFrameGen[iFrameGen], disklabe=diskLabel,
                                         disklabelfree=diskLabelFree, unit_w_r=splitedParse[4],
                                         adjuste=splitedParse[5], diskcanevas=self.listDiskCanevas,
                                         disk_laber_read=diskLabelRead, disk_label_write=diskLabelWrite,
                                         devisse=self.device)

                        liste_disk_afficher.append(dev)

                        aa += 1
                        can_count += 1
                        self.row_pour_network += 4
                        i += 1
                diskframerow += 1
                ii += 1
        if str(sep) == '\n':
            self.row_pour_network += row
        return liste_disk_afficher, self.colu_pour_network, self.row_pour_network, self.frame_pour_network, \
            self.frame_col_1, self.frame_col_2, self.frame_col_3, self.frame_col_4, self.list_disks

    def destroy_all_disk(self):
        try:
            self.diskframegeneral.destroy()
            self.diskframegeneral2.destroy()
            self.diskframegeneral3.destroy()
            self.diskframegeneral4.destroy()
        except TypeError:
            pass

    def v_update_style(self):
        geter_style = getter.accessToSettings('reliefs.ini')
        relief_widg = geter_style.get('disks', 'widg')
        relief_partitions = geter_style.get('disks', 'partition')
        relief_barre = geter_style.get('disks', 'barre')
        relief_write = geter_style.get('disks', 'write')
        relief_read = geter_style.get('disks', 'read')

        try:
            self.diskframegeneral.configure(relief=relief_widg)
            self.diskframegeneral2.configure(relief=relief_widg)
            self.diskframegeneral3.configure(relief=relief_widg)
            self.diskframegeneral4.configure(relief=relief_widg)
        except TypeError:
            pass
        for frame in self.listDiskFrame:
            frame.configure(relief=relief_partitions)
        for can in self.listDiskCanevas:
            can.configure(relief=relief_barre)
        for frame_read in self.listDiskFrameRead:
            frame_read.configure(relief=relief_read)
        for frame_write in self.listDiskFrameWrite:
            frame_write.configure(relief=relief_write)