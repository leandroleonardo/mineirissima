from tkinter import *
from tkinter import messagebox
from models.Consulta import Consulta
from models.Delete import Delete
from models.Insert import Insert


class Cadastro:

    def __init__(self):
        self.conexao = None
        self.root = None
        self.frame = None
        self.tree = None
        self.nome = ''

    def VisualizarCadastros(self):

        resultados = Consulta.Tabela(self, 'USUARIOS')

        self.tree.delete(*self.tree.get_children())

        linhaV = []

        for linha in resultados:
            linhaV.append(linha['id_usuario'])
            linhaV.append(linha['nome'])
            linhaV.append(linha['senha'])
            linhaV.append(linha['nivel'])

            self.tree.insert("", END, values=linhaV, iid=linha['id_usuario'], tag='1')
            linhaV.clear()

    def RemoverCadastro(self):

        idDeletar = int(self.tree.selection()[0])

        Delete.RemoverID(self, 'USUARIOS', 'ID_USUARIO', idDeletar)

        Cadastro.VisualizarCadastros(self)

    def AlterarCadastro(self, id_usuario):

            novoNome = ''
            novaSenha = ''
            ConfirmaSenha = ''

            try:
                novoNome = self.nome_altera.get()
                novaSenha = self.senha_altera.get()
                confirmaSenha = self.senha_confirma.get()
                chaveSeguranca = self.chave_seguranca.get()
            except:
                messagebox.showinfo('Erro', 'Insira todos os dados')
                return

            if novoNome == '' or novaSenha == '' or confirmaSenha == '':
                messagebox.showinfo('Erro', 'Insira todos os dados')
                return
            elif novaSenha != confirmaSenha:
                messagebox.showinfo('Erro', 'Senhas diferentes')
                return
            elif chaveSeguranca != '123@':
                messagebox.showinfo('Erro', 'Chave de segurança inválida!')
                return

            Insert.InsereUsuario(self, novoNome, id_usuario, novaSenha)

            self.root_alterarUsuario.destroy()

            Cadastro.VisualizarCadastros(self)