from tkinter import messagebox
import matplotlib.pyplot as plt

from models.Consulta import Consulta


class Estatistica:

    def __init__(self):

        self.nome = ''
        self.quantidade = ''
        self.data = ''
        self.valor = ''

    def GerarEstatistica(self):

        nomeProdutos = []
        nomeProdutos.clear()
        plt.rcParams['figure.figsize'] = (10.0, 6.0)

        vendas = Consulta.DadosEstatisticas(self)

        if not vendas:
            messagebox.showinfo('Error', 'Sem vendas cadastrada nesse dia')
            return

        if self.nomeEstatistica.get() and self.grupoEstatistica.get():
            messagebox.showinfo('Error', 'Escolha apenas um campo')
            return
        elif self.nomeEstatistica.get():
            estado = 1
        elif self.grupoEstatistica.get():
            estado = 2
        else:
            messagebox.showinfo('Error', 'Escolha apenas um campo')
            return

        if estado == 1:

            if self.dinheiroEstatistica.get() and self.quantidadeUniEstatistica.get():
                messagebox.showinfo('Error', 'Escolha apenas um campo')
                return
            if self.dinheiroEstatistica.get():
                decisao3 = 1
            elif self.quantidadeUniEstatistica.get():
                decisao3 = 2
            else:
                messagebox.showinfo('Error', 'Escolha apenas um campo')
                return

            if decisao3 == 1:

                for i in vendas:
                    nomeProdutos.append(i['nome'])

                valores = []
                valores.clear()

                produtoVendido = []

                for i in vendas:
                    produtoVendido.append(i['nome'])

                nomeProdutos = sorted(set(produtoVendido))  # elemento repetido

                valores = []
                valores.clear()

                for i in nomeProdutos:
                    preco = 0.00
                    for j in vendas:
                        if j['nome'] == i:
                            preco += float(j['preco_total'])
                    valores.append(preco)

                titulo = "Porcentagem de lucro"
                tipo = "d"

                Estatistica.GerarGrafico(self, valores, nomeProdutos, titulo, tipo)

            if decisao3 == 2:
                grupoUnico = []
                grupoUnico.clear()

                for i in vendas:
                    grupoUnico.append(i['nome'])

                grupoUnico = sorted(set(grupoUnico))  # elemento repetido

                qntFinal = []
                qntFinal.clear()

                for i in grupoUnico:
                    qntVendida = 0
                    for j in vendas:
                        if j['nome'] == i:
                            qntVendida += j['quantidade']
                    qntFinal.append(qntVendida)

                titulo = "Porcentagem de produtos mais vendidos"
                tipo = ""

                Estatistica.GerarGrafico(self, qntFinal, grupoUnico, titulo, tipo)

        elif estado == 2:

            if self.dinheiroEstatistica.get() and self.quantidadeUniEstatistica.get():
                messagebox.showinfo('Error', 'Escolha apenas campo')
                return
            elif self.dinheiroEstatistica.get():
                decisao3 = 1
            elif self.quantidadeUniEstatistica.get():
                decisao3 = 2
            else:
                messagebox.showinfo('Error', 'Escolha um campo')
                return

            if decisao3 == 1:

                nomeGrupo = []

                for i in vendas:
                    nomeGrupo.append(i['grupo'])

                nomeGrupo = sorted(set(nomeGrupo))

                valores = []
                valores.clear()

                for i in nomeGrupo:
                    somaValor = 0

                    for v in vendas:
                        if i == v['grupo']:
                            somaValor += v['preco_total']

                    valores.append(somaValor)

                titulo = "Porcentagem de vendas em dinheiro"
                tipo = "d"

                Estatistica.GerarGrafico(self, valores, nomeGrupo, titulo, tipo)

            elif decisao3 == 2:

                grupoUnico = []
                grupoUnico.clear()

                for i in vendas:
                    grupoUnico.append(i['grupo'])
                grupoUnico = sorted(set(grupoUnico))  # elemento repetido

                qntFinal = []
                qntFinal.clear()

                for h in range(0, len(grupoUnico)):
                    qntUnitaria = 0
                    for i in vendas:
                        if grupoUnico[h] == i['grupo']:
                            qntUnitaria += i['quantidade']
                    qntFinal.append(qntUnitaria)

                titulo = "Porcentagem de vendas por grupo"
                tipo = ""

                Estatistica.GerarGrafico(self, qntFinal, grupoUnico, titulo, tipo)

    def GerarGrafico(self, valor, grupo, titulo, tipo):

        if tipo == 'd':
            string = "{:.1f}%\n(R${:.1f})"
        else:
            string = "{:.1f}%\n({:d})"

        def pctLambda(pct, qntFinal):
            conta = float(sum(qntFinal)*pct/100)
            conta = round(conta)
            return string.format(pct, conta)

        fig, ax = plt.subplots()
        wedges, texts, autotexts = ax.pie(valor, textprops=dict(color='w'),
                                          autopct=lambda pct: pctLambda(pct, valor)
                                          , startangle=90)
        ax.axis('equal')
        ax.legend(wedges, grupo,
                  title="Produtos",
                  loc="center left",
                  bbox_to_anchor=(0.8, 0, 0, 1))
        ax.set_title(titulo)
        plt.show()