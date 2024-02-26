import tkinter
from tkinter import messagebox


class AfficherMessage:

    paren = tkinter.Toplevel

    def __init__(self, parent):
        self.paren = parent

    def afficher_mess(self, a, b, typee):
        if typee == 'error':
            messagebox.showerror(a, b, parent=self.paren)
        elif typee == 'yesno':
            rep = messagebox.askyesno(a, b, parent=self.paren)
            return rep
        elif typee == 'info':
            messagebox.showinfo(a, b, parent=self.paren)
