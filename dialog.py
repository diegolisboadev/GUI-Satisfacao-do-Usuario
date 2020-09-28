'''Classe com janela de dialogo Tkinter'''
from tkinter import *
import sys

class Dialog:

    def __init__(self, parent, title, desc, titulo2=''):
        self.fonteTitulo = ("Times New Roman", "16", "bold")
        self.fontTextos = ("Times New Roman", "14")
        self.descricao = desc
        self.title = title
        self.titulo2 = titulo2

        self.top = Toplevel(parent)
        if (sys.platform.startswith('win')): 
            self.top.iconbitmap("sorriso.ico")
        else:
            self.top.iconbitmap('@sorriso.xbm')
        self.top.configure(background='#fff')
        self.top.transient(parent)
        self.top.grab_set()
        self.top.title(self.title)
        Label(self.top, text=self.titulo2, font=self.fonteTitulo, background="#fff").pack(pady=15)
        self.top.bind("<Escape>", self.fecha_modal)
        self.e = Label(self.top, text=self.descricao, font=self.fontTextos)
        self.e.pack(padx=15)
        self.e.focus_set()
        self.sair = Button(self.top, text="Fechar", font=("Times New Roman", 13, "bold"), command=self.fecha_modal)
        self.sair.pack(padx=15, pady=15)

    def fecha_modal(self):
        self.top.destroy()