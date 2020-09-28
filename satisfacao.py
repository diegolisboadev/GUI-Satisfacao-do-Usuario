
"""Software de Satisfação do Usuário - By Diego Lisboa and Python 3.7 and Tkinter"""
__author__ = "Diego Lisboa"
__copyright__ = "Copyright (C) 2019 Autor Diego Lisboa 2019"
__license__ = ""
__version__ = "1.0"

from tkinter import *
from tkinter import messagebox
import os, sys
from datetime import datetime
from dialog import Dialog
from PIL import Image, ImageTk

class Satisfacao:
    def __init__(self, master=None):
        #master.geometry('300x200+200+100')
        self.fontePadrao = ("Times New Roman", "14", "bold")
        self.fontImg = ("Times New Roman", 5, "bold")

        self.imagem1 = PhotoImage(file="ruim.png")
        self.imagem1.subsample(2, 2)
        self.imagem1.zoom(1,1)

        self.imagem2 = PhotoImage(file="regular.png")
        self.imagem2.subsample(2, 2)
        self.imagem2.zoom(1,1)

        self.imagem3 = PhotoImage(file="bom.png")
        self.imagem3.subsample(2, 2)
        self.imagem3.zoom(1,1)

        self.imagem4 = PhotoImage(file="otimo.png")
        self.imagem4.subsample(2, 2)
        self.imagem4.zoom(1,1)

        self.imagem5 = PhotoImage(file="excelente.png")
        self.imagem5.subsample(2, 2)
        self.imagem5.zoom(1,1)

        self.help = PhotoImage(file="ajudar.png")
        self.help.subsample(2,2)
        self.help.zoom(1,1)

        self.exitImg = PhotoImage(file="sair.png")
        self.exitImg.subsample(2, 2)
        self.exitImg.zoom(1, 1)

        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 15
        self.primeiroContainer.configure(background="#fff")
        self.primeiroContainer.grid(row=0, column=0, columnspan=5)

        self.helpContainer = Frame(master)
        self.helpContainer["padx"] = 5
        self.helpContainer.configure(background="#fff")
        self.helpContainer.grid(row=0, column=4, ipadx=50)

        self.exitContainer = Frame(master)
        self.exitContainer["pady"] = 5
        self.exitContainer.configure(background="#fff")
        self.exitContainer.grid(row=0, column=4, ipadx=1)

        self.segundoContainer = Frame(master)
        self.segundoContainer["pady"] = 20
        self.segundoContainer.configure(background="#fff")
        self.segundoContainer.grid(row=1, column=0)

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["pady"] = 20
        self.terceiroContainer.configure(background="#fff")
        self.terceiroContainer.grid(row=1, column=1)

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.configure(background="#fff")
        self.quartoContainer.grid(row=1, column=2)

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 20
        self.quintoContainer.configure(background="#fff")
        self.quintoContainer.grid(row=1, column=3)

        self.sextoContainer = Frame(master)
        self.sextoContainer["pady"] = 20
        self.sextoContainer.configure(background="#fff")
        self.sextoContainer.grid(row=1, column=4)

        self.setimoContainer = Frame(master)
        self.setimoContainer["pady"] = 20
        self.setimoContainer.configure(background="#fff")
        self.setimoContainer.grid(columnspan=5)

        # SEGUNDA PARTE DO CÓDIGO

        self.titulo = Label(self.primeiroContainer, text="SATISFAÇÃO")
        self.titulo["font"] = ("Times New Roman", "18", "bold")
        self.titulo.configure(background="#fff")
        self.titulo.grid(stick='nsew')

        self.titulo = Label(self.primeiroContainer, text="Bem Vindo Cliente que você acho do"+
        " nosso atendimento?\nAvalie-nos abaixo.")
        self.titulo["font"] = ("Times New Roman", "10", "bold")
        self.titulo.configure(background="#fff")
        self.titulo.grid(stick='nsew')

        self.ajudar = Button(self.helpContainer, image=self.help, bd=0, cursor="hand2")
        self.ajudar["font"] = ("Times New Roman", "18", "bold")
        self.ajudar.image = self.help
        self.ajudar['command'] = self.box_dialog
        self.ajudar.configure(background="#fff")
        self.ajudar.grid()

        self.exit = Button(self.exitContainer, image=self.exitImg, bd=0, cursor="hand2")
        self.exit["font"] = ("Times New Roman", "18", "bold")
        self.exit.image = self.help
        self.exit.configure(background="#fff")
        self.exit['command'] = self.sair
        self.exit.grid()

        self.btnIcon1 = Button(self.segundoContainer, image=self.imagem1,
        font=self.fontImg, bd="0", relief=GROOVE, width="150", height="100",
        activebackground="#fff", compound=CENTER, cursor="hand2", command=lambda: self.click_satisfacao(1))
        self.btnIcon1.image = self.imagem1
        self.btnIcon1.configure(background="#fff")
        self.btnIcon1.grid(row=0, column=1)

        self.textIcon = Label(self.segundoContainer, text="RUIM", font=self.fontePadrao)
        self.textIcon.configure(background="#fff")
        self.textIcon.grid(row=2, column=1, in_=self.segundoContainer, pady=20)

        self.btnIcon2 = Button(self.terceiroContainer, image=self.imagem2,
        font=self.fontImg, bd="0", relief=GROOVE, width="150", height="100",
        activebackground="#fff", compound=CENTER, cursor="hand2", command=lambda: self.click_satisfacao(2))
        self.btnIcon2.image = self.imagem2
        self.btnIcon2.configure(background="#fff")
        self.btnIcon2.grid(row=0, column=1)

        self.textIcon2 = Label(self.terceiroContainer, text="REGULAR", font=self.fontePadrao)
        self.textIcon2.configure(background="#fff")
        self.textIcon2.grid(row=2, column=1, in_=self.terceiroContainer, pady=20)

        self.btnIcon3 = Button(self.quartoContainer, image=self.imagem3,
        font=self.fontImg, bd="0", relief=GROOVE, width="150", height="100",
        activebackground="#fff", compound=CENTER, cursor="hand2", command=lambda: self.click_satisfacao(3))
        self.btnIcon3.image = self.imagem3
        self.btnIcon3.configure(background="#fff")
        self.btnIcon3.grid(row=0, column=1)

        self.textIcon3 = Label(self.quartoContainer, text="BOM", font=self.fontePadrao)
        self.textIcon3.configure(background="#fff")
        self.textIcon3.grid(row=2, column=1, in_=self.quartoContainer, pady=20)

        self.btnIcon4 = Button(self.quintoContainer, image=self.imagem4,
        font=self.fontImg, bd="0", relief=GROOVE, width="150", height="100",
        activebackground="#fff", compound=CENTER, cursor="hand2", command=lambda: self.click_satisfacao(4))
        self.btnIcon4.image = self.imagem4
        self.btnIcon4.configure(background="#fff")
        self.btnIcon4.grid(row=0, column=1)

        self.textIcon4 = Label(self.quintoContainer, text="ÓTIMO", font=self.fontePadrao)
        self.textIcon4.configure(background="#fff")
        self.textIcon4.grid(row=2, column=1, in_=self.quintoContainer, pady=20)

        self.btnIcon5 = Button(self.sextoContainer, image=self.imagem5,
        font=self.fontImg, bd="0", relief=GROOVE, width="150", height="100",
        activebackground="#fff", compound=CENTER, cursor="hand2", command=lambda: self.click_satisfacao(5))
        self.btnIcon5.image = self.imagem5
        self.btnIcon5.configure(background="#fff")
        self.btnIcon5.grid(row=0, column=1)

        self.textIcon5 = Label(self.sextoContainer, text="EXCELENTE", font=self.fontePadrao)
        self.textIcon5.configure(background="#fff")
        self.textIcon5.grid(row=2, column=1, in_=self.sextoContainer, pady=20)

        self.rodape = Label(self.setimoContainer, text="\xa9 Copyright 2019")
        self.rodape["font"] = ("Times New Roman", "11", "bold")
        self.rodape.configure(background="#fff")
        self.rodape.grid(stick='nsew')

    # FUNÇÕES PARA AS AÇÕES DE CLICK

    def sair(self):
        questao = messagebox.askokcancel("Sair", "Deseja Fechar a Aplicação?")
        if questao == True:
            root.quit()

    def box_dialog(self):
        '''modal com os informações do tutorial de ajudar'''
        dialog = Dialog(root, "Tutorial", "\n\n1 - Clique uma vez apenas um Emoji de Satisfação."
                                "\n\n2 - Após o clique você verá uma mensagem informando que seu clique foi validado."
                                "\n\n3 - Depois deixe a aplicação em aberto para que o próximo Cliente possa dar seu clique."
                                "\n\n4 - Caso ainda tenha alguma Dúvida, pergunte a(o) atendente mais próximo de você."
                                "\n\n Sem mais Agradecemos sua compreensão. Obrigado!!\n\n", "Sistema de Satisfação do Usuário")
        root.protocol("WM_DELETE_WINDOW", root.quit)
        root.geometry("+%d+%d" % (root.winfo_rootx() + 50,
                                  root.winfo_rooty() + 50))
        root.focus_set()
        root.iconbitmap("sorriso.ico")
        root.configure(background='#fff')
        root.wait_window(dialog.top)

    def click_satisfacao(self, click):
        '''pegar o click no button de satisfação
        correspondente ao emoji'''
        self.salvar_txt(click)
        self.salvar_total_txt()
        messagebox.showinfo("Voto", "Obrigado por Cliente pela sua opinião :)!\n\t Volte Sempre!!")

    def salvar_txt(self, click):
        '''salvar no log o clique de determinados butões da satisfação'''
        try:
            if os.path.exists("satisfacao_log.txt"):
                tipo_escrita = "a"
            else:
                tipo_escrita = "w"

            with open("satisfacao_log.txt", tipo_escrita, encoding='utf-8') as file_click:
                if click == 1:
                    texto = "Voto Ruim"
                elif click == 2:
                    texto = "Voto Regular"
                elif click == 3:
                    texto = "Voto Bom"
                elif click == 4:
                    texto = "Voto Ótimo"
                elif click == 5:
                    texto = "Voto Excelente"
                else:
                    pass

                file_click.write(str(datetime.strftime(datetime.today(), "[%d/%m/%Y %H:%M:%S]") + " -> " + texto) + "\n")

        except FileNotFoundError:
            print("Erro na criação do arquivo de LOG!")
            messagebox.showerror("Erro", "Erro na criação do arquivo de LOG!")

    def salvar_total_txt(self):
            '''salvar o total de cliques de cada satisfação button'''
            try:
                with open("satisfacao_log.txt", encoding='utf-8') as txt_read:
                    linhas = txt_read.readlines()

                    conta1 = conta2 = conta3 = conta4 = conta5 = 0
                    for l in linhas:
                        if "Ruim" in l:
                            conta1 += 1
                        elif "Regular" in l:
                            conta2 += 1
                        elif "Bom" in l:
                            conta3 += 1
                        elif "timo" in l:
                            conta4 += 1
                        elif "Excelente" in l:
                            conta5 += 1
                        else:
                            pass

                if os.path.exists("satisfacao_soma_log.txt"):
                    tipo_escrita = "w"
                else:
                    tipo_escrita = "w"

                with open("satisfacao_soma_log.txt", tipo_escrita, encoding='utf-8') as file_soma_click:
                    file_soma_click.write("ARQUIVO DE LOG - COM A SOMA DE CLIQUES DE SATISFAÇÕES\n\n")

                    file_soma_click.write(f"Há um total de {conta1} clicks em Satisfação Ruim!\n\n")
                    file_soma_click.write(f"Há um total de {conta2} clicks em Satisfação Regular!\n\n")
                    file_soma_click.write(f"Há um total de {conta3} clicks em Satisfação Bom!\n\n")
                    file_soma_click.write(f"Há um total de {conta4} clicks em Satisfação Ótimo!\n\n")
                    file_soma_click.write(f"Há um total de {conta5} clicks em Satisfação Excelente!\n\n")

            except FileNotFoundError:
                messagebox.showerror("Erro", "Houve um erro no click!")

root = Tk()
Satisfacao(root)
root.title("Satisfação do Usuário")
if (sys.platform.startswith('win')): 
    root.iconbitmap("sorriso.ico")
else:
    root.iconbitmap('@sorriso.xbm')
# root.iconbitmap(os.path.join(sys.path[0], 'sorriso.ico'))
# root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='sorriso.ico'))

root.configure(background='#fff')

wLarg = root.winfo_reqwidth()
wAltu = root.winfo_reqheight()

x = int(root.winfo_screenmmwidth() / 3 - wLarg / 2)
y = int(root.winfo_screenheight() / 3 - wAltu / 2)
root.geometry('+{}+{}'.format(x, y))
root.resizable(False, False)
#root.geometry('600x500+500+600')
root.mainloop()