from tkinter import Tk, Label, Entry, Button
from controllers.Usuario import Usuario
from views.Conexao import Conexao
from views.Records import Records
from views.Signup import Signup


class Login:

    def __init__(self):

        # Dimensões da janela
        largura = 1280
        altura = 720

        # meio da janela
        posx = largura / 2
        posy = altura / 2

        self.root = Tk()
        self.root.title('Login')
        self.root.geometry('1280x720')
        self.root.maxsize(1280, 720)
        self.root.minsize(1280, 720)

        # Title
        Label(self.root, text='Mineiríssima', font=('Arial', 20, 'bold')).place(x=posx - 25, y=(posy - 90))

        # Usuário
        Label(self.root, text='Usuário', font=('Arial', 12)).place(x=posx - 65, y=(posy - 32))
        self.login = Entry(self.root, font=('Arial', 12), width=15)
        self.login.grid(row=1, column=1)
        self.login.place(x=posx, y=(posy - 30))

        # Senha
        Label(self.root, text='Senha', font=('Arial', 12)).place(x=posx - 60, y=(posy - 2))
        self.senha = Entry(self.root, show='*', font=('Arial', 12), width=15)
        self.senha.grid(row=2, column=1)
        self.senha.place(x=posx, y=posy)

        # Buttons
        self.buttonLogin = Button(self.root, text='Login', bg='#88E497', width=10, font=('Arial', 10),
                                  command=lambda: Usuario.Logar(self))
        self.buttonLogin.place(x=posx - 60, y=(posy + 40))

        self.buttonCadastro = Button(self.root, text='Cadastrar', bg='#FF8368', width=10, font=('Arial', 10),
                                     command=lambda: Signup())
        self.buttonCadastro.place(x=posx + 50, y=(posy + 40))

        self.buttonVisualizarCadastros = Button(self.root, text='Visualizar cadastros', relief='flat', fg='#00A3FF',
                                                width=20, font=('Arial', 10),
                                                command=lambda: Records())
        self.buttonVisualizarCadastros.place(x=posx - 40, y=(posy + 90))

        self.ButtonConfigBd = Button(self.root, text='Configurações', relief='flat', fg='#00A3FF',
                                                width=10, font=('Arial', 10),
                                                command=lambda: Conexao())
        self.ButtonConfigBd.place(x=posx - 630, y=(posy - 350))

        self.root.mainloop()
