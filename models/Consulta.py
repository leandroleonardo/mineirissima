from tkinter import messagebox

from models import ConexaoBD as BD


class Consulta:

    # Select básico

    def Tabela(self, nome):

        BD.ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('SELECT * FROM ' + nome)
                resultados = cursor.fetchall()
        except:
            return

        return resultados

    # Select básico com params

    def TabelaParams(self, tabela, conteudo):

        BD.ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('SELECT * FROM {} WHERE NOME = "{}"'.format(tabela, conteudo))
                resultados = cursor.fetchall()
        except:
            return

        return resultados

    # Select na tabela vendas formatado

    def Vendas(self):

        BD.ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute(
                    'SELECT id_venda, nome, quantidade, preco_total, DATE_FORMAT (`data_venda`,"%d/%m/%Y") as '
                    'data_venda FROM VENDAS;')
                resultados = cursor.fetchall()
                return resultados
        except:
            return

    # Select na tabela produtos formatado

    def Produtos(self):

        BD.ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('SELECT * FROM PRODUTOS')
                resultados = cursor.fetchall()
                return resultados
        except:
            messagebox.showinfo('Erro', 'Erro ao consultar banco de dados')

    # ExcelVendas

    def ExcelVendas(self):

        BD.ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('SELECT nome, quantidade, preco_total, DATE_FORMAT (`data_venda`,"%d/%m/%Y") as '
                               'data_venda FROM VENDAS;')
                dados = cursor.fetchall()
                return dados
        except:
            messagebox.showinfo('Erro', 'Erro ao gerar planilha')

    # ExcelProdutos

    def ExcelProdutos(self):

        BD.ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('SELECT NOME, INGREDIENTES, GRUPO, PRECO FROM PRODUTOS')
                dados = cursor.fetchall()
                return dados
        except:
            messagebox.showinfo('Erro', 'Erro ao gerar planilha')

    # Dados estatísticas

    def DadosEstatisticas(self):

        BD.ConexaoBd.AbreConexao(self)

        if not self.data:
            try:
                with self.conexao.cursor() as cursor:
                    cursor.execute('SELECT * FROM VENDAS V INNER JOIN PRODUTOS PR ON PR.nome = V.nome')
                    vendas = cursor.fetchall()
                    return vendas
            except:
                messagebox.showinfo('Erro', 'Erro ao fazer consulta no banco de dados')
        else:
            try:
                with self.conexao.cursor() as cursor:
                    cursor.execute('SELECT * FROM VENDAS V INNER JOIN PRODUTOS PR ON PR.nome = V.nome WHERE  V.DATA_VENDA = "{}"'.format(self.data))
                    vendas = cursor.fetchall()
                    return vendas
            except:
                messagebox.showinfo('Erro', 'Erro ao fazer consulta no banco de dados')
