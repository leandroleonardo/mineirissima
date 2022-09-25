from tkinter import messagebox, END

import pandas as pd

from models import ConexaoBD as BD
from models.Consulta import Consulta
from models.Delete import Delete
from models.Insert import Insert


class Venda:

    def __init__(self):

        # Atributos

        self.id_usuario = None
        self.id_produto = None
        self.quantidade = ''
        self.data = ''
        self.valor = ''

    def CadastrarVenda(self):

        quantidade = ""
        valor = ""
        data = ""

        try:
            nome = self.nome.get()
            quantidade = int(self.quantidade.get())
            data_vendas = str(self.data)
        except:
            messagebox.showinfo('Erro', 'Preencha todos os campos')
            return

        verificaProdutoCadastrado = ""

        # Verifica se produto está cadastrados

        verificaProdutoCadastrado = Consulta.TabelaParams(self, 'PRODUTOS', nome)

        try:
            self.id_produto = verificaProdutoCadastrado[0]['id_produto']
        except:
            messagebox.showinfo('Erro', 'Produto não cadastrado no sistema!')
            return

        if not verificaProdutoCadastrado:
            messagebox.showinfo('Erro', 'Produto não cadastrado no sistema!')
            return

        # campo vazio adiciona valor padrão

        valor_total = verificaProdutoCadastrado[0].get('preco')
        valor_total = quantidade * valor_total

        # Insere produto no banco de dados

        Insert.InsereVenda(self, self.id_usuario, self.id_produto, nome, quantidade, valor_total, data_vendas)

        Venda.MostrarVenda(self)

    def MostrarVenda(self):

        resultados = Consulta.Vendas(self)

        self.tree.delete(*self.tree.get_children())

        linhaV = []

        for linha in resultados:
            linhaV.append(linha['nome'])
            linhaV.append(linha['quantidade'])
            linhaV.append(linha['preco_total'])
            linhaV.append(linha['data_venda'])

            self.tree.insert('', END, values=linhaV, iid=linha['id_venda'], tag='1')

            linhaV.clear()

    def RemoverVenda(self):

        idDeletar = int(self.tree.selection()[0])
        Delete.RemoverID(self, 'VENDAS', 'ID_VENDA', idDeletar)
        Venda.MostrarVenda(self)

    def GerarExcel(self):
        BD.ConexaoBd.AbreConexao(self)

        try:
            dados = Consulta.ExcelVendas(self)
            dadosPd = pd.DataFrame(data=dados)
            dadosPd.to_csv('../Planilhas/dados_vendas.xlsx', index=False)
            messagebox.showinfo('Mensagem', 'Planilha gerada com sucesso')
        except:
            messagebox.showinfo('Erro', 'Erro ao gerar planilha')