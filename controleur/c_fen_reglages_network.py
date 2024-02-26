import configparser
import tkinter
from tkinter import ttk
from tkinter import *
from modele import m_access_to_settings
from pathlib import Path
from controleur.message import AfficherMessage


class FenetreReglagesNetwork:
    frameGeneral = ttk.Frame
    fen_parametres = tkinter.Toplevel
    y_entry = tkinter.StringVar
    x_entry = tkinter.StringVar
    values_up_down = ['auto', 'o', 'ko', 'mo', 'go']
    combo_up_down = tkinter.StringVar
    directory = ''
    var_affich_debit = StringVar
    aff_graph = StringVar
    var_aff_net_inf = StringVar
    liste_ponder = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    combo_ponder = StringVar
    messa = AfficherMessage

    def __init__(self, fen_para, frame_gen):
        self.directory = Path(__file__).parent.parent
        self.parser_defaut = m_access_to_settings.accessToSettings('settings.ini')
        self.frameGeneral = frame_gen
        self.fen_parametres = fen_para
        self.y_entry = tkinter.StringVar(value=self.parser_defaut.get('network_reglages', 'axe_y'))
        self.x_entry = tkinter.StringVar(value=self.parser_defaut.get('network_reglages', 'axe_x'))
        self.combo_up_down = tkinter.StringVar(value=self.parser_defaut.get('network_reglages', 'unite_up_down'))
        self.var_affich_debit = StringVar(value=self.parser_defaut.get('network_reglages', 'afficher_debit'))
        self.aff_graph = StringVar(value=self.parser_defaut.get('network_reglages', 'afficher_graph'))
        self.var_aff_net_inf = StringVar(value=self.parser_defaut.get('network_reglages', 'afficher_net_inf'))
        self.combo_ponder = StringVar(value=self.parser_defaut.get('network_reglages', 'ponderation'))
        self.messa = AfficherMessage(self.fen_parametres)

    def appliquer_reglages(self):
        aff_gra = self.aff_graph.get()
        aff_debit = self.var_affich_debit.get()
        aff_net_inf = self.var_aff_net_inf.get()
        pond = self.combo_ponder.get()
        aff_widg = self.var_aff_net_inf.get()
        if pond not in self.liste_ponder:
            self.messa.afficher_mess('erreur', 'Le choix de ponderation n\'est pas disponible.', 'error')
            return
        try:
            axe_y = self.y_entry.get()
            if axe_y != 'auto':
                try:
                    axe_y = int(axe_y)
                except ValueError:
                    self.messa.afficher_mess('erreur', 'Paramétre axe y semble ne pas être un nombre ni \'auto\'!', 'error')
                    return

        except:
            self.messa.afficher_mess('erreur', 'Il y a un probleme avec la valeur de l\'axe y', 'error')

        axe_x = self.x_entry.get()
        if axe_x == 'auto':
            pass
        else:
            try:
                axe_x = int(axe_x)
            except ValueError:
                self.messa.afficher_mess('erreur', 'Paramétre axe x semble ne pas être un nombre ni \'auto\'!', 'error')
                return
        if axe_y == 'auto':
            pass
        elif axe_y > 5000000000:
            self.messa.afficher_mess('erreur', 'Paramétre axe y superieur a 5 000 000 000!', 'error')
            return
        if axe_x != 'auto' and int(axe_x) < 0:
            self.messa.afficher_mess('erreur', 'Le paramétre axe x en secondes ne peut pas être inferieur a 0 secondes!',
                                  'error')
            return
        elif axe_x != 'auto' and int(axe_x) > 301:
            reponse = self.messa.afficher_mess('Vraiment?', 'Souhaitez-vous vraiment un historique de plus de 5 minutes'
                                                         ' sur le graphique? (5min.=300secondes)', 'yes/no')
            if reponse == False:
                return
        unite = self.combo_up_down.get()
        if (unite in self.values_up_down):
            pass
        else:
            self.messa.afficher_mess('Oups', 'Il semble que "{}" n\'est pas dans la liste des possibilitées pour '
                                          'l\'échelle Up et Down.'.format(unite), 'error')
            return
        if aff_widg == 'True':
            aff_widget = 'True'
        else:
            aff_widget = 'False'
        try:
            self.parser_defaut.set('network_reglages', 'axe_x', str(self.x_entry.get()))
        except configparser.NoSectionError:
            self.parser_defaut.add_section('network_reglages')
            self.parser_defaut.set('network_reglages', 'axe_x', str(self.x_entry.get()))
        try:
            self.parser_defaut.set('network_reglages', 'axe_y', str(self.y_entry.get()))
        except configparser.NoSectionError:
            print('line 34 c_fen_reglages_network.py no section error (network_reglages(axe_y))')
        try:
            self.parser_defaut.set('network_reglages', 'unite_up_down', str(self.combo_up_down.get()))
        except configparser.NoSectionError:
            print('line 38 c_fen_reglages_network.py no section error (network_reglages (unite_up_down))')
        self.parser_defaut.set('network_reglages', 'afficher_debit', aff_debit)
        self.parser_defaut.set('network_reglages', 'afficher_graph', aff_gra)
        self.parser_defaut.set('network_reglages', 'afficher_net_inf', aff_net_inf)
        self.parser_defaut.set('network_reglages', 'ponderation', pond)
        self.parser_defaut.set('app_settings', 'update', 'True')
        self.parser_defaut.set('network_reglages', 'afficher_widget', str(aff_widget))
        self.messa.afficher_mess('Tout est ok.', 'Vos choix ont bien été appliqués!', 'info')

    def afficher_reglages_net(self):
        frame_afficher_networkinfos = ttk.Frame(self.frameGeneral)
        frame_afficher_networkinfos.grid(column=1, row=1, pady=15)
        aff_lab = ttk.Label(frame_afficher_networkinfos, text='Afficher informations network?')
        aff_lab.grid(column=1, columnspan=2, row=1)
        aff_lab_rad_oui = ttk.Radiobutton(frame_afficher_networkinfos, text='oui', variable=self.var_aff_net_inf,
                                          value='True')
        aff_lab_rad_oui.grid(column=3, row=1)
        aff_lab_rad_non = ttk.Radiobutton(frame_afficher_networkinfos, text='non', variable=self.var_aff_net_inf,
                                          value='False')
        aff_lab_rad_non.grid(column=4, row=1)

        frame_set_y = ttk.Frame(self.frameGeneral)
        frame_set_y.grid(column=1, row=2, pady=15)
        label_y = ttk.Label(frame_set_y, text="Maximum a afficher sur l'axe des ordonnées (axe y)\n"
                                              "(selon le choix d'unité du 'débit par secondes' (ko, mo, etc.))."
                                              " Ou \"auto\":\nSi unité débit = auto, Maximum est en kbps")
        label_y.grid(column=1, columnspan=3, row=1, sticky=E)
        label_y_entry = ttk.Entry(frame_set_y, textvariable=self.y_entry)
        label_y_entry.grid(column=4, row=1, sticky=W)

        frame_set_x = ttk.Frame(self.frameGeneral)
        frame_set_x.grid(column=1, row=3)
        label_x = ttk.Label(frame_set_x, text="Maximum a afficher sur l'axe des abscisses (axe x), en secondes. Ou \"auto\":")
        label_x.grid(column=1, columnspan=3, row=2, sticky=E)
        label_x_entry = ttk.Entry(frame_set_x, textvariable=self.x_entry)
        label_x_entry.grid(column=4, row=2, sticky=W, pady=15)

        affich_graph_frame = ttk.Frame(self.frameGeneral)
        affich_graph_frame.grid(column=1, row=4)
        aff_graph_label = ttk.Label(affich_graph_frame, text='Afficher le graphique?')
        aff_graph_label.grid(column=1, columnspan=2, row=1)
        radio_graph_oui = ttk.Radiobutton(affich_graph_frame, text='oui', variable=self.aff_graph, value='True')
        radio_graph_oui.grid(column=3, row=1)
        radio_graph_non = ttk.Radiobutton(affich_graph_frame, text='non', variable=self.aff_graph, value='False')
        radio_graph_non.grid(column=4, row=1)

        frame_Afficher_Debit = ttk.Frame(self.frameGeneral)
        frame_Afficher_Debit.grid(column=1, row=5)
        label_afficher_debit = ttk.Label(frame_Afficher_Debit, text='Afficher débit network up et down?')
        label_afficher_debit.grid(column=1, columnspan=2, row=1)
        checkbox_afficher_debit = ttk.Radiobutton(frame_Afficher_Debit, text="oui", variable=self.var_affich_debit,
                                                  value='True')
        checkbox_afficher_debit.grid(column=3, row=1)
        checkbox_cacher_debit = ttk.Radiobutton(frame_Afficher_Debit, text='non', variable=self.var_affich_debit,
                                                value='False')
        checkbox_cacher_debit.grid(column=4, row=1)

        frame_up_down = ttk.Frame(self.frameGeneral)
        frame_up_down.grid(column=1, row=6)
        label_unite_up_down = ttk.Label(frame_up_down, text="Choix unité debit descendant et ascendant (bps ou auto):")
        label_unite_up_down.grid(column=1, columnspan=3, row=3, sticky=E)
        combo_unite_up_down = ttk.Combobox(frame_up_down, values=self.values_up_down,
                                           textvariable=self.combo_up_down, width=5)
        combo_unite_up_down.grid(column=4, row=3, sticky=W)
        frame_ponder = ttk.Frame(self.frameGeneral)
        frame_ponder.grid(column=1, row=7)
        ponder_label = ttk.Label(frame_ponder, text='Choix pondération débit:')
        ponder_label.grid(column=1, columnspan=2, row=1)
        ponder_combo = ttk.Combobox(frame_ponder, values=self.liste_ponder, textvariable=self.combo_ponder,
                                    width=5)
        ponder_combo.grid(column=3, row=1)
        bouton_appliquer = ttk.Button(self.frameGeneral, text='Appliquer', command=self.appliquer_reglages)
        bouton_appliquer.grid(column=1, row=8, pady=15)
