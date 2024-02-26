from tkinter import *


def f1():
    print(var_dieu.get())
    pass


def f2():
    print(var_use_fps.get())
root = Tk()
frame_1 = Frame(root).grid()
var_dieu = IntVar()
dieu_ou_ = Checkbutton(frame_1, text="Mode  de  jeu  Créatif ",
                       variable=var_dieu, command=f1).grid(row=18, column=1)

var_use_fps = IntVar()
case_use_ = Checkbutton(frame_1, text="Utiliser la régulation des FPS",
                        variable=var_use_fps, command=f2).grid(row=20, column=1)

root.mainloop()