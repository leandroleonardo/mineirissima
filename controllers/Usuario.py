from tkinter import messagebox
from models import ConexaoBD as BD
from models.UsuarioModel import UsuarioModel
from views.Home import Home


class Usuario:

    def __init__(self):
        self.senha_cadastro = None
        self.login_cadastro = None
        self.codigoSeguranca = None
        self.login = ''
        self.senha = ''
        self.usuario = ''
        self.id = ''

    # Cadastro
    def Cadastrar(self):

        codigoPadrao = '123@'

        if self.codigoSeguranca.get() == codigoPadrao:

            if len(self.login_cadastro.get()) <= 20:

                if len(self.senha_cadastro.get()) <= 20:

                    nome = self.login_cadastro.get()
                    senha = self.senha_cadastro.get()

                    if nome == "" or senha == "":
                        messagebox.showinfo('Erro', 'Preencha todos os campos!')
                        return

                    UsuarioModel.Cadastro(self, nome, senha)

                    self.root_cadastro.destroy()
                else:
                    messagebox.showinfo('Erro', 'Por favor inseria uma senha com menos caracteres')
            else:
                messagebox.showinfo('Erro', 'Por favor inseria um nome com menos caracteres')
        else:
            messagebox.showinfo('Erro', 'Erro no codigo de seguranca')

    # Login
    def Logar(self):

        BD.ConexaoBd.AbreConexao(self)

        autenticado = False
        usuarioMaster = False
        usuario = self.login.get()
        senha = self.senha.get()

        dados = UsuarioModel.login(self, usuario, senha, autenticado, usuarioMaster)

        try:
            usuarioMaster = dados[0]
            autenticado = dados[1]
        except:
            return

        if not autenticado:
            messagebox.showinfo('login', 'Usuário ou Senha inválido')
        if autenticado:
            try:
                self.root.destroy()
            except:
                pass

            Home(usuarioMaster, self.id)