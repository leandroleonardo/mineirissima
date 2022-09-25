from tkinter import Tk, Label, Entry, Button
from models.ConexaoBD import ConexaoBd


# from models.ConexaoBD import ConexaoBd


class Conexao:

    def __init__(self):

        self.root_conexaoBD = Tk()
        self.root_conexaoBD.title('Configuração do banco de dados')
        self.root_conexaoBD.geometry('1280x720')
        self.root_conexaoBD.maxsize(1280, 720)
        self.root_conexaoBD.minsize(1280, 720)

        # Dimensões da janela
        largura = 1280
        altura = 720

        # meio da janela
        posx = largura / 2
        posy = altura / 2

        # Title
        Label(self.root_conexaoBD, text='Configuração de banco de dados', font=('Arial', 20, 'bold')).place(x=posx - 165,
                                                                                               y=(posy - 150))
        # Usuário
        Label(self.root_conexaoBD, text='Password', font=('Arial', 12)).place(x=posx - 85, y=(posy - 32))
        self.passBD = Entry(self.root_conexaoBD, show='*', font=('Arial', 12), width=15)
        self.passBD.place(x=posx, y=(posy - 30))

        Label(self.root_conexaoBD, text='User', font=('Arial', 12)).place(x=posx - 85, y=(posy - 64))
        self.userBD = Entry(self.root_conexaoBD, font=('Arial', 12), width=15)
        self.userBD.place(x=posx, y=(posy - 60))

        Label(self.root_conexaoBD, text='Chave', font=('Arial', 12)).place(x=posx - 85, y=(posy - 0))
        self.chave = Entry(self.root_conexaoBD, show='*', font=('Arial', 12), width=15)
        self.chave.place(x=posx, y=(posy - 0))

        self.ButtonSave = Button(self.root_conexaoBD, text='Confirmar', bg='#88E497', width=10, font=('Arial', 10), command=lambda: ConexaoBd.SalvaUsuario(self))
        self.ButtonSave.place(x=posx, y=(posy + 30))

        self.root_conexaoBD.mainloop()