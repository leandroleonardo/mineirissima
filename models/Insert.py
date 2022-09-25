from tkinter import messagebox
from models import ConexaoBD as BD


class Insert:

    def InsereVenda(self, id_usuario, id_produto, nome, quantidade, valor_total, data_vendas):

        BD.ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('INSERT INTO VENDAS (ID_USUARIO, ID_PRODUTO, NOME, QUANTIDADE, PRECO_TOTAL, '
                               'DATA_VENDA) VALUES ({},{},"{}",{},{},"{}")'.format(id_usuario, id_produto,
                                                                                   nome, quantidade, valor_total,
                                                                                   data_vendas))
                self.conexao.commit()
                messagebox.showinfo('Mensagem', 'Produto cadastrado com sucesso!')
        except:
            messagebox.showinfo('Erro', 'Erro ao inserir pedido no banco de dados!')

    def InsereProduto(self, nome, ingredientes, grupo, preco):

        BD.ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('SELECT * FROM PRODUTOS WHERE NOME = %s', nome)
                check = cursor.fetchall()
                if check:
                    messagebox.showinfo('Erro', 'Produto já cadastrado')
                    return
        except:
            pass

        # Insere produto no banco de dados
        BD.ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('INSERT INTO PRODUTOS (NOME, INGREDIENTES, GRUPO, PRECO)'
                               'VALUES (%s,%s,%s,%s)', (nome, ingredientes, grupo, preco))
                self.conexao.commit()
                messagebox.showinfo('Mensagem', 'Produto cadastrado com sucesso!')
        except:
            messagebox.showinfo('Erro', 'Erro ao inserir produto no banco de dados')

    def InsereUsuario(self, novoNome, id_usuario, novaSenha):

        BD.ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute(
                    'SELECT * FROM USUARIOS WHERE NOME = "{}" AND ID_USUARIO != {}'.format(novoNome, id_usuario))
                verificarNome = cursor.fetchall()
        except:
            messagebox.showinfo('Erro', 'Erro ao atualizar usuário')

        if verificarNome:
            messagebox.showinfo('Erro', 'Nome de usuário já cadastro!')
            return

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('UPDATE USUARIOS SET NOME = "{}" WHERE ID_USUARIO = {}'.format(novoNome, id_usuario))
                self.conexao.commit()
        except:
            messagebox.showinfo('Erro', 'Erro ao atualizar usuário')
        #
        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('UPDATE USUARIOS SET SENHA = "{}" WHERE ID_USUARIO = {}'.format(novaSenha, id_usuario))
                self.conexao.commit()
        except:
            messagebox.showinfo('Erro', 'Erro ao atualizar usuário')

