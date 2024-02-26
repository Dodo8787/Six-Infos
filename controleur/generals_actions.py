import tkinter
import modele.m_access_to_settings as access
import controleur.c_fenetre_param as c_fen_param
import configparser

class General:

    def __init__(self):
        self.fen_param_isopen = False
        self.fen_param = c_fen_param.FenParam
        self.posx = 1
        self.posy = 1
        self.previewposx = 0
        self.previewposy = 0


    def store_position(self, x, y):
        accesseur = access.accessToSettings('theme.ini')
        accesseur.set('start', 'root_position', '+{}+{}'.format(x, y))
        acces_set = access.accessToSettings('settings.ini')
        acces_set.set('app_settings', 'update', 'True')

    def verif_root_position(self, root):
        self.posx, self.posy = (int(s) for s in root.geometry().split("+")[1:])
        if self.posx != self.previewposx or self.posy != self.previewposy:
            if self.previewposx != 0 or self.previewposy != 0:
                self.store_position(self.posx, self.posy)
            self.previewposx = self.posx
            self.previewposy = self.posy


    def get_theme(self):
        try:
            theme = self.accesseur.get('themes', 'theme_actuel')
        except configparser.NoOptionError:
            self.accesseur.set('themes', 'theme_actuel', 'breeze')
            theme = 'breeze'
        return theme

    def close_all_fen(self, root_frame, refresh_after_id, root, fen_param):
        self.on_closing_main_window(root_frame, refresh_after_id, root, fen_param=None)

    def ouvrir_fen_couleurs(self):  # dans vue non ??
        pass

    '''def instancier_obj_param_fen(self):
        try:
            self.fen_param.on_closing_fen_param()
        except:
            pass
        self.fen_param = FenParam(disk_partitions, diskFrameGeneral, liste_disques_affiches, root)
        self.fen_param.open_window()
        self.fen_param_isopen = True
        '''

    def verif_update(self, option):
        accesseur_verif = access.accessToSettings('settings.ini')
        list_updt = []
        do_app_updt = accesseur_verif.get('app_settings', option)
        if do_app_updt == 'True':
            list_updt.append('app')
            accesseur_verif.set('app_settings', option, 'False')
        return list_updt

    def on_closing_fen_param(self, fen_param):
        self.fen_param_isopen = False
        fen_param.destroy()

    def on_closing_main_window(self, root_frame, refresh_after_id, root, fen_param=None):
        root_frame.after_cancel(str(refresh_after_id))   # cancel mainloop
        if fen_param is not None and fen_param.fen_param_isopen:
            fen_param.fen_parame.destroy()
        root.destroy()
        exit()

    def get_zoom_ratio(self):
        accesseur = access.accessToSettings('settings.ini')
        zoom_rat = accesseur.get('app_settings', 'zoom')
        zoom_ratio = int(zoom_rat) / 100.0
        return zoom_ratio

    def update_zoom(self, root_frame):
        # ici nettoyer frame_root et appeler 'creer cpu', 'creer disk' et creer network avec le bon ratio zoom.
        tkinter.Widget.destroy(root_frame)

        '''global zoom_ratio
        global caneva
        global networkGraphFram
        global diskFrameGeneral
        global diskLabelGen
        global caneva_disque
        global frameRoot
        global affich_gen_disk
        global liste_disques_affiches
        global cpuFrame
        global diskFrameGeneral2
        global diskFrameGeneral3
        global diskFrameGeneral4
        global networkFrameUngrided
        global windo_height
        global frame_pour_network
        global networkTitle
        global network_up_down_frame
        global label2Up
        global label2Down
        global networkDownDebit
        global networkUpDebit
        global listepathtoforg
        global liste_dev




        try:
            networkFrame.grid_forget()
        except:
            pass
        i = 0
        cpuCol = 1
        cpuRow = 5
        while i < nbrCpuCore + 1:
            labName[str(i)].grid_forget()
            canvasName[str(i)].grid_forget()
            i += 1
        coreTempLab.grid_forget()
        i = 0
        while i < nbrCpuCore + 1:
            labName[str(i)].configure(font=('Arial', int(10 * zoom_ratio)), width=15)
            labName[str(i)].grid(column=cpuCol + 1, row=cpuRow, sticky=W)
            canvasName[str(i)].configure(width=int(100 * zoom_ratio), height=int(10 * zoom_ratio))
            canvasName[str(i)].grid(column=cpuCol, row=cpuRow, sticky=W)
            cpuRow += 1
            root.update()
            if col_setter.valide_height(root.winfo_height()) == False:
                cpuCol += 2
                cpuRow = 1
                labName[str(i)].grid(column=cpuCol + 1, row=cpuRow)
                canvasName[str(i)].grid(column=cpuCol, row=cpuRow)
                cpuRow += 1
            i += 1
        coreTempLab.grid(columnspan=2, column=cpuCol, row=cpuRow, sticky=EW)
        coreTempLab.configure(font=('Arial', int(10 * zoom_ratio)), width=int(10 * zoom_ratio))
        root.update()
        if col_setter.valide_height(root.winfo_height()) == False:
            coreTempLab.grid(columnspan=2, column=cpuCol + 2, row=1)

        if affich_gen_disk:
            if networkFrameUngrided == False:
                reaffichergraph = True
                networkFrame.grid_forget()
            else:
                reaffichergraph = False
            networkFrameUngrided = True
            caneva_disque.diskFrameGen.destroy()
            diskFrameGeneral.destroy()

            diskFrameGeneral = caneva_disque.diskFrameGen
            diskFrameGeneral = ttk.Frame(cpuFrame, relief='raised', borderwidth=4)
            rowdiskframgen = cpuRow + 1
            diskFrameGeneral.grid(column=col_for_frame_gen_disk, columnspan=2, row=rowdiskframgen)
            diskLabelGen = ttk.Label(diskFrameGeneral, text="Disk Infos:", width=30, font=('Arial', int(10 * zoom_ratio)))
            diskLabelGen.grid(column=1, row=1, sticky=W)
            root.update()

            listepathtoforg = parser_zoom.get('disk', 'to_forget').split('=>')

            caneva_disque = CanevasDisk.Canevasdisques(win_height, liste_dev, conv, 65, 85, zoom_ratio, diskFrameGeneral)
            liste_disques_affiches = caneva_disque.afficher_disks(liste_dev, conv, cpuFrame, cpuCol, rowdiskframgen, diskFrameGeneral,
                                                                  diskFrameGeneral2, diskFrameGeneral3, diskFrameGeneral4,
                                                                  nbrdedisqueaafficher,
                                                                  listepathtoforg, destroy=True)
            diskFrameGeneral = caneva_disque.diskframegeneral
            diskFrameGeneral2 = caneva_disque.diskframegeneral2
            diskFrameGeneral3 = caneva_disque.diskframegeneral3
            diskFrameGeneral4 = caneva_disque.diskframegeneral4
            rowNet = caneva_disque.row_pour_network + 1
            colNet = caneva_disque.colu_pour_network
            frame_net = caneva_disque.frame_pour_network
            frame_pour_network = frame_net
            if reaffichergraph:
                networkFrameUngrided = False
                create_widget_network(frameRoot, rowNet, colNet)


        if networkFrameUngrided == False:
            create_widget_network(frameRoot, 3, 1)
            place_graph_widget(3, 1)

        parser_zoom.set('app_settings', 'update', 'False')
        with open(str(directory) + '/settings.ini', 'w') as g:
            parser_zoom.write(g)
            '''
