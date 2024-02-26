import tkinter


class fenCoulApp():
    def __init__(self, fen_param, frame_param):
        self.frame_gen = tkinter.Frame(frame_param)
        self.frame_gen.grid(column=1, row=1)

        self.label_rien = tkinter.Label(self.frame_gen, text='Désolé, il n\'y a rien ici...')
        self.label_rien.grid(column=1, row=1, sticky=tkinter.EW)
