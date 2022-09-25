from tkinter import *
from tkinter import messagebox

from models.Consulta import Consulta
from models.Delete import Delete
from models.Insert import Insert
import pandas as pd


class Produto:

    def __init__(self):
        nome = ''
        ingrediente = ''
        grupo = ''
        preco = ''

    def CadastrarProduto(self):

        nome = self.nome.get()
        ingredientes = self.ingredientes.get()
        grupo = self.grupo.get()
        preco = self.preco.get()

        Insert.InsereProduto(self, nome, ingredientes, grupo, preco)

        Produto.MostrarProduto(self)

    def MostrarProduto(self):

        resultados = Consulta.Produtos(self)

        self.tree.delete(*self.tree.get_children())

        linhaV = []

        for linha in resultados:
            linhaV.append(linha['nome'])
            linhaV.append(linha['ingredientes'])
            linhaV.append(linha['grupo'])
            linhaV.append(linha['preco'])

            self.tree.insert('', END, values=linhaV, iid=linha['id_produto'], tag='1')

            linhaV.clear()

    def RemoverProduto(self):

        id_produto = int(self.tree.selection()[0])
        Delete.RemoverID(self, 'PRODUTOS', 'ID_PRODUTO', id_produto)
        Produto.MostrarProduto(self)

    def GerarExcel(self):

        try:
            dados = Consulta.ExcelProdutos(self)
            dadosPd = pd.DataFrame(data=dados)
            dadosPd.to_csv('../Planilhas/dados_produtos.xlsx', index=False)
            messagebox.showinfo('Mensagem', 'Planilha gerada com sucesso')
        except:
            messagebox.showinfo('Erro', 'Erro ao gerar planilha')