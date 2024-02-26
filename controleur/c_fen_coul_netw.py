import tkinter

from modele import m_access_to_settings
from controleur import fenetre_select_color
from functools import partial
from pathlib import Path


class FenCoulNetw:
    def __init__(self, fen_param, frame_param, indice='gen'):
        self.indice = indice
        self.directory = Path(__file__).parent.parent
        self.bouton_color_img = tkinter.PhotoImage(file=str(self.directory) + '/Images/color_buton.png')
        if self.indice == 'gen':
            self.netw_getter = m_access_to_settings.accessToSettings('colors.ini')
            self.bg_principal = self.netw_getter.get('Network', 'principale')
            self.coul_down = self.netw_getter.get('Network', 'coul_down')
            self.coul_up = self.netw_getter.get('Network', 'coul_up')
            self.coul_down_curve = self.netw_getter.get('Network', 'down_curve')
            self.coul_up_curve = self.netw_getter.get('Network', 'up_curve')
            self.coul_fond_graph = self.netw_getter.get('Network', 'fond_graph')
            self.coul_contour_graph = self.netw_getter.get('Network', 'contour_graph')
            self.coul_axes_x_et_y = self.netw_getter.get('Network', 'axes_x_et_y')
            self.list_coul = [self.bg_principal, self.coul_down, self.coul_up, self.coul_down_curve, self.coul_up_curve,
                              self.coul_fond_graph, self.coul_contour_graph, self.coul_axes_x_et_y]
            self.list_text = ['Fond principal: ', 'Cadre débit down: ', 'Cadre débit up: ', 'Courbe débit down: ',
                              'Courbe débit up: ', 'Fond du graphique: ', 'Contour du graphique: ', 'Axes x et y: ']
            self.list_commands = ['NetwPrincipal', 'NetwDown', 'NetwUp', 'NetwCurveDown', 'NetwCurveUp', 'NetwGrFond',
                                  'NetwGrCont', 'netwGrAxes']
        else:
            self.netw_font_gett = m_access_to_settings.accessToSettings('color_font.ini')
            self.coul_font_title = self.netw_font_gett.get('Network_font', 'title')
            self.coul_font_down = self.netw_font_gett.get('Network_font', 'down')
            self.coul_font_up = self.netw_font_gett.get('Network_font', 'up')
            self.list_coul = [self.coul_font_title, self.coul_font_down, self.coul_font_up]
            self.list_text = ['Couleur titre: ', 'Couleur down: ', 'Couleur up: ']
            self.list_commands = ['NetwFontTitle', 'NetwFontDown', 'NetwFontUp']
        self.fen_param = fen_param
        self.frame_param = frame_param
        self.fen_coul = fenetre_select_color.fenSelectionColor
        self.can_principal = tkinter.Canvas
        self.lab_hexa_princ = tkinter.Label
        self.buton_coul_princ = tkinter.Button
        self.can_down = tkinter.Canvas
        self.lab_hexa_down = tkinter.Label
        self.buton_coul_down = tkinter.Button
        self.can_up = tkinter.Canvas
        self.lab_hexa_up = tkinter.Label
        self.buton_coul_up = tkinter.Button

        self.fen_coul = fenetre_select_color
        self.afficher_fen_coul_netw()

    def afficher_fen_coul_netw(self):
        lab_coul_princ = tkinter.Label(self.frame_param, text=self.list_text[0])
        lab_coul_princ.grid(column=1, row=2)
        self.can_principal = tkinter.Canvas(self.frame_param, width=45, height=20, relief='groove',
                                            borderwidth=2, background=self.list_coul[0])
        self.can_principal.grid(column=2, row=2)
        self.lab_hexa_princ = tkinter.Label(self.frame_param, text='Hexadecimal: ' + self.list_coul[0])
        self.lab_hexa_princ.grid(column=3, row=2)
        self.buton_coul_princ = tkinter.Button(self.frame_param, image=self.bouton_color_img,
                                               command=partial(self.afficher_palette, self.list_commands[0],
                                                               self.can_principal, self.lab_hexa_princ))
        self.buton_coul_princ.grid(column=4, row=2)

        lab_coul_down = tkinter.Label(self.frame_param, text=self.list_text[1])
        lab_coul_down.grid(column=1, row=3)
        self.can_down = tkinter.Canvas(self.frame_param, width=45, height=20, relief='groove',
                                       borderwidth=2, background=self.list_coul[1])
        self.can_down.grid(column=2, row=3)
        self.lab_hexa_down = tkinter.Label(self.frame_param, text='Hexadecimal: ' + self.list_coul[1])
        self.lab_hexa_down.grid(column=3, row=3)
        self.buton_coul_down = tkinter.Button(self.frame_param, image=self.bouton_color_img,
                                              command=partial(self.afficher_palette, self.list_commands[1],
                                                              self.can_down, self.lab_hexa_down))
        self.buton_coul_down.grid(column=4, row=3)

        lab_coul_up = tkinter.Label(self.frame_param, text=self.list_text[2])
        lab_coul_up.grid(column=1, row=4)
        self.can_up = tkinter.Canvas(self.frame_param, width=45, height=20, relief='groove',
                                     borderwidth=2, background=self.list_coul[2])
        self.can_up.grid(column=2, row=4)
        self.lab_hexa_up = tkinter.Label(self.frame_param, text='Hexadecimal: ' + self.list_coul[2])
        self.lab_hexa_up.grid(column=3, row=4)
        self.buton_coul_up = tkinter.Button(self.frame_param, image=self.bouton_color_img,
                                            command=partial(self.afficher_palette, self.list_commands[2],
                                                            self.can_up, self.lab_hexa_up))
        self.buton_coul_up.grid(column=4, row=4)

        if self.indice == 'gen':
            lab_coul_down_curve = tkinter.Label(self.frame_param, text=self.list_text[3])
            lab_coul_down_curve.grid(column=1, row=5)
            self.can_down_curve = tkinter.Canvas(self.frame_param, width=45, height=20, relief='groove',
                                                 borderwidth=2, background=self.list_coul[3])
            self.can_down_curve.grid(column=2, row=5)
            self.lab_hexa_down_curve = tkinter.Label(self.frame_param, text='Hexadecimal: ' + self.list_coul[3])
            self.lab_hexa_down_curve.grid(column=3, row=5)
            self.buton_coul_down_curve = tkinter.Button(self.frame_param, image=self.bouton_color_img,
                                                command=partial(self.afficher_palette, self.list_commands[3],
                                                                self.can_down_curve, self.lab_hexa_down_curve))
            self.buton_coul_down_curve.grid(column=4, row=5)

            lab_coul_up_curve = tkinter.Label(self.frame_param, text=self.list_text[4])
            lab_coul_up_curve.grid(column=1, row=6)
            self.can_up_curve = tkinter.Canvas(self.frame_param, width=45, height=20, relief='groove',
                                                 borderwidth=2, background=self.list_coul[4])
            self.can_up_curve.grid(column=2, row=6)
            self.lab_hexa_up_curve = tkinter.Label(self.frame_param, text='Hexadecimal: ' + self.list_coul[4])
            self.lab_hexa_up_curve.grid(column=3, row=6)
            self.buton_coul_up_curve = tkinter.Button(self.frame_param, image=self.bouton_color_img,
                                                command=partial(self.afficher_palette, self.list_commands[4],
                                                                self.can_up_curve, self.lab_hexa_up_curve))
            self.buton_coul_up_curve.grid(column=4, row=6)

            lab_coul_fond_graph = tkinter.Label(self.frame_param, text=self.list_text[5])
            lab_coul_fond_graph.grid(column=1, row=7)
            self.can_fond_graph = tkinter.Canvas(self.frame_param, width=45, height=20, relief='groove',
                                               borderwidth=2, background=self.list_coul[5])
            self.can_fond_graph.grid(column=2, row=7)
            self.lab_hexa_fond_graph = tkinter.Label(self.frame_param, text='Hexadecimal: ' + self.list_coul[5])
            self.lab_hexa_fond_graph.grid(column=3, row=7)
            self.buton_coul_fond_graph = tkinter.Button(self.frame_param, image=self.bouton_color_img,
                                                      command=partial(self.afficher_palette, self.list_commands[5],
                                                                      self.can_fond_graph, self.lab_hexa_fond_graph))
            self.buton_coul_fond_graph.grid(column=4, row=7)

            lab_coul_contour_graph = tkinter.Label(self.frame_param, text=self.list_text[6])
            lab_coul_contour_graph.grid(column=1, row=8)
            self.can_contour_graph = tkinter.Canvas(self.frame_param, width=45, height=20, relief='groove',
                                               borderwidth=2, background=self.list_coul[6])
            self.can_contour_graph.grid(column=2, row=8)
            self.lab_hexa_contour_graph = tkinter.Label(self.frame_param, text='Hexadecimal: ' + self.list_coul[6])
            self.lab_hexa_contour_graph.grid(column=3, row=8)
            self.buton_coul_contour_graph = tkinter.Button(self.frame_param, image=self.bouton_color_img,
                                                      command=partial(self.afficher_palette, self.list_commands[6],
                                                                      self.can_contour_graph, self.lab_hexa_contour_graph))
            self.buton_coul_contour_graph.grid(column=4, row=8)

            lab_coul_axes_x_et_y = tkinter.Label(self.frame_param, text=self.list_text[7])
            lab_coul_axes_x_et_y.grid(column=1, row=9)
            self.can_axes_x_et_y = tkinter.Canvas(self.frame_param, width=45, height=20, relief='groove',
                                               borderwidth=2, background=self.list_coul[7])
            self.can_axes_x_et_y.grid(column=2, row=9)
            self.lab_hexa_axes_x_et_y = tkinter.Label(self.frame_param, text='Hexadecimal: ' + self.list_coul[7])
            self.lab_hexa_axes_x_et_y.grid(column=3, row=9)
            self.buton_coul_axes_x_et_y = tkinter.Button(self.frame_param, image=self.bouton_color_img,
                                                      command=partial(self.afficher_palette, self.list_commands[7],
                                                                      self.can_axes_x_et_y, self.lab_hexa_axes_x_et_y))
            self.buton_coul_axes_x_et_y.grid(column=4, row=9)

    def afficher_palette(self, indice, canevas, lab_hexa):
        try:
            self.fen_coul.close_fen()
        except AttributeError:
            pass
        self.fen_coul = fenetre_select_color.fenSelectionColor(self.fen_param, canevas, lab_hexa, indice)
