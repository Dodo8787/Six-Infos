import tkinter

class afficherListeReliefs():
    def __init__(self, frame_param, liste_reliefs):
        self.frame_param = frame_param
        self.liste_reliefs = liste_reliefs
        i = 1
        self.frame_param2 = tkinter.Frame(self.frame_param, relief='solid', borderwidth=1)
        self.frame_param2.grid(column=1, row=1, columnspan=5, pady=10)
        liste_canvas = []
        for reliefs in self.liste_reliefs:
            if reliefs == 'unchange':
                continue
            liste_canvas.append(tkinter.Frame(self.frame_param2, relief=reliefs, borderwidth=3))
            liste_canvas[i - 1].grid(column=i, row=1, padx=15, pady=8)
            label_relief = tkinter.Label(liste_canvas[i - 1], text=reliefs)
            label_relief.grid()
            i += 1
