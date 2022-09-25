from tkinter import Tk, Label, Entry, Button
from controllers.Usuario import Usuario


class Signup:

    def __init__(self):

        # dimensões da janela
        largura = 1280
        altura = 720

        # meio da janela
        posx = largura / 2
        posy = altura / 2

        # Config tela
        self.root_cadastro = Tk()
        self.root_cadastro.title('Cadastro')
        self.root_cadastro.geometry('1280x720')
        self.root_cadastro.maxsize(1280, 720)
        self.root_cadastro.minsize(1280, 720)

        # Title
        Label(self.root_cadastro, text='Cadastro', font=('Arial', 22, 'bold')).place(x=posx - 20, y=(posy - 100))

        # Usuário
        Label(self.root_cadastro, text='Usuário', font=('Arial', 12)).place(x=posx - 60, y=(posy - 30))
        self.login_cadastro = Entry(self.root_cadastro, font=('Arial', 12))
        self.login_cadastro.grid(row=1, column=1)
        self.login_cadastro.place(x=posx, y=(posy - 30))

        # Senha
        Label(self.root_cadastro, text='Senha', font=('Arial', 12)).place(x=posx - 60, y=(posy))
        self.senha_cadastro = Entry(self.root_cadastro, show='*', font=('Arial', 12))
        self.senha_cadastro.grid(row=2, column=1)
        self.senha_cadastro.place(x=posx, y=posy)

        # Buttons
        self.buttonVisualizarCadastros = Button(self.root_cadastro, text='Confirmar Cadastro', bg='#88E497', width=20,
                                                command=lambda: Usuario.Cadastrar(self), font=('Arial', 10))
        self.buttonVisualizarCadastros.place(x=posx - 40, y=(posy + 80))

        Label(self.root_cadastro, text='Chave de segurança', font=('Arial', 12)).place(x=posx - 150, y=(posy + 30))
        self.codigoSeguranca = Entry(self.root_cadastro, show='*', font=('Arial', 12))
        self.codigoSeguranca.place(x=posx, y=(posy + 30))

        self.root_cadastro.mainloop()
