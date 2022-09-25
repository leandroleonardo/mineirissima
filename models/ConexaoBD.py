from tkinter import messagebox

import pymysql.cursors


# Abre uma conexão com o banco de dados

class ConexaoBd:

    def __init__(self):
        usuario = ''
        senha = ''

    def AbreConexao(self):

        try:
            f = open('../controllers/conexao', 'r')
        except:
            with open('../controllers/conexao', 'x') as f:
                f.write('user\npass\n')
                f = open('../controllers/conexao', 'r')

        lista = []

        for line in f:
            lista.append(line)

        user = lista[0].replace('\n', '')
        passW = lista[1].replace('\n', '')

        try:
            self.conexao = pymysql.connect(
                host='localhost',
                user=user,
                password=passW,
                database='mineirissima',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            messagebox.showinfo('Error', 'Erro ao conectar com o banco de dados')
            return False

    def SalvaUsuario(self):

        if not self.userBD.get() or not self.passBD.get() or not self.chave.get():
            messagebox.showinfo('Erro', 'Preencha os campos')
            return

        if self.chave.get() != '123@':
            messagebox.showinfo('Erro', 'Chave de segurança inválida')
            return

        usuario = self.userBD.get()
        senha = self.passBD.get()

        with open('../controllers/conexao', 'w') as arquivo:
            arquivo.write(usuario + '\n' + senha)

        self.root_conexaoBD.destroy()

        ConexaoBd.AbreConexao(self)