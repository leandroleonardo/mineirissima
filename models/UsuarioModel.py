from tkinter import messagebox
from models import ConexaoBD as BD

class UsuarioModel:

    def __init__(self):
        self.conexao = None

    def login(self, usuario, senha, autenticado, usuarioMaster):

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('SELECT * FROM USUARIOS')
                resultados = cursor.fetchall()
        except:
            return

        for linha in resultados:
            if usuario == linha['nome'] and senha == linha['senha']:

                self.id = linha['id_usuario']

                if linha['nivel'] == 2:
                    usuarioMaster = True
                autenticado = True
                break

        return usuarioMaster, autenticado

    def Cadastro(self, nome, senha):

        BD.ConexaoBd.AbreConexao(self)

        try:
            self.conexao.cursor()
        except:
            return

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('SELECT * FROM USUARIOS WHERE NOME = "{}"'.format(nome))
                checarCadastro = cursor.fetchall()
                if checarCadastro:
                    messagebox.showinfo('Erro', 'Usuário já cadastrado')
                    return
        except:
            messagebox.showinfo('Erro', 'Erro de verificação')

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('INSERT INTO USUARIOS (NOME,SENHA,NIVEL) VALUES (%s, %s, %s)',
                               (nome, senha, 1))
                self.conexao.commit()
            messagebox.showinfo('Cadastro', 'Usuário cadastrado com sucesso')
        except:
            messagebox.showinfo('Erro', 'Erro ao inserir Usuário')
            return