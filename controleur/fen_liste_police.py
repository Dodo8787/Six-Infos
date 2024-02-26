import tkinter


class fenListePolice():
    def __init__(self):
        self.fen = tkinter.Toplevel()
        self.fen.title('Liste des polices')
        self.list_font = list(tkinter.font.families())
        self.list_font.append('Arial')
        self.frame_gen = tkinter.Frame
        self.page_actuelle = 1
        self.pages_total = 0
        self.debut = 0
        self.fin = 0
        self.frame_list = tkinter.Frame

    def afficher_liste(self, debut, fin):
        self.list_font.sort()
        i = 0
        x = 1
        y = 1
        for police in self.list_font:
            if debut <= i < fin:
                if x == 7:
                    x = 1
                    y += 1

                lab_polices = tkinter.Label(self.frame_list, text=str(police), font=(str(police), 11))
                lab_polices.grid(column=x, row=y)
                x += 1
            i += 1

    def liste_precedente(self):
        if self.page_actuelle == 1:
            pass
        else:
            self.frame_list.destroy()
            self.frame_list = tkinter.Frame(self.frame_gen, borderwidth=3, relief='groove')
            self.frame_list.grid(column=1, row=1, columnspan=5)
            self.debut -= 30
            self.fin -= 30
            self.page_actuelle -= 1
            self.afficher_liste(self.debut, self.fin)
            self.label_page.configure(text='Page {}/{}'.format(self.page_actuelle, self.pages_total))

    def liste_suivante(self):
        if self.page_actuelle == self.pages_total:
            pass
        else:
            self.frame_list.destroy()
            self.frame_list = tkinter.Frame(self.frame_gen, borderwidth=3, relief='groove')
            self.frame_list.grid(column=1, row=1, columnspan=5)
            self.debut += 30
            self.fin += 30
            self.page_actuelle += 1
            self.afficher_liste(self.debut, self.fin)
            self.label_page.configure(text='Page {}/{}'.format(self.page_actuelle, self.pages_total))

    def afficher_fen(self):
        self.frame_gen = tkinter.Frame(self.fen)
        self.frame_gen.grid(column=1, row=1)
        self.frame_list = tkinter.Frame(self.frame_gen, borderwidth=3, relief='groove')
        self.frame_list.grid(column=1, row=1, columnspan=5)
        self.pages_total = (len(self.list_font) // 30) + 1
        self.page_actuelle = 1
        self.list_font.sort()
        self.debut = 0
        self.fin = 30
        self.afficher_liste(self.debut, self.fin)
        buton_precedent = tkinter.Button(self.frame_gen, text="Précédent", command=self.liste_precedente)
        buton_precedent.grid(column=2, row=2)
        self.label_page = tkinter.Label(self.frame_gen, text='Page {}/{}'.format(self.page_actuelle, self.pages_total))
        self.label_page.grid(column=3, row=2)
        buton_suivant = tkinter.Button(self.frame_gen, text="Suivant", command=self.liste_suivante)
        buton_suivant.grid(column=4, row=2)