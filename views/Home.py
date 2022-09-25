import os
import sys
from datetime import date
from tkinter import Tk, Frame, Label, Button, Entry, NO, ttk, IntVar, Checkbutton, messagebox
from tkcalendar import Calendar

from controllers.Cadastro import Cadastro
from controllers.Estatistica import Estatistica
from controllers.Produto import Produto
from controllers.Venda import Venda


class Home:

    def __init__(self, usuarioMaster, id):

        self.id_usuario = None
        self.id = id

        self.root = Tk()
        self.root.title('ADMIN')

        # Dimensões da janela
        self.largura = 1280
        self.altura = 720

        # frame
        self.frame = Frame(self.root)
        self.frame.place(x=15, y=100)

        # title
        self.root.title('Cadastro de produtos')

        self.root.geometry('1280x720')
        self.root.maxsize(self.largura, self.altura)
        self.root.minsize(self.largura, self.altura)

        Label(self.root, text='Mineiríssima', font=('Arial', 20)).grid(row=1, column=1, padx=10, pady=10)

        Button(self.root, text='Vendas', width=20, command=lambda: Home.FrameVenda(self, self.root, self.id)) \
            .grid(row=1, column=2, padx=10, pady=10)
        Button(self.root, text='Produtos', width=20, command=lambda: Home.FrameProduto(self, self.root)) \
            .grid(row=1, column=3, padx=10, pady=10)
        Button(self.root, text='Estatísticas', width=20,
               command=lambda: Home.FrameEstatistica(self, self.root)) \
            .grid(row=1, column=4, padx=10, pady=10)
        Button(self.root, text='Sair', width=20, command=lambda: Home.Sair(self)) \
           .grid(row=1, column=6, padx=10, pady=10)
        if usuarioMaster:
            Button(self.root, text='Usuários', width=20, command=lambda: Home.FrameCadastro(self, self.root)) \
                .grid(row=1, column=5, padx=10, pady=10)

        Label(self.frame, text='Seja bem-vindo ao Mineiríssima!', font=('Arial', 20)).grid(row=2, column=0,
                                                                                           columnspan=4,
                                                                                           padx=5, pady=6, ipady=5)

        self.root.mainloop()

    def FrameVenda(self, tela, id_usuario):

        self.id_usuario = id_usuario

        # Calendario
        def calendario():

            self.calendario = Tk()
            self.calendario.title('Calendário')

            dataAtual = str(date.today()).split('-')
            cal = Calendar(self.calendario, selectmode='day', year=int(dataAtual[0]), month=int(dataAtual[1]),
                           day=int(dataAtual[2]))
            cal.grid(row=0, column=0, columnspan=2, pady=20, padx=10)

            def pegaData():
                self.data = cal.get_date()

                dataFormatado = str(self.data).split('/')

                ano = dataFormatado[2]
                dia = dataFormatado[1]
                mes = dataFormatado[0]

                dataFormatada = ano + '/' + mes + '/' + dia
                self.data = dataFormatada

                self.calendario.destroy()

            Button(self.calendario, text='confirmar', width=20, command=pegaData, bg='#60abe5', fg='white') \
                .grid(row=1, column=0, columnspan=2, pady=20, padx=10)

        # Tela
        self.root = tela

        try:
            self.frame.destroy()
        except:
            pass

        self.frame = Frame(self.root)
        self.frame.place(x=15, y=100)

        # title
        self.root.title('Cadastro de vendas')

        # Título
        Label(self.frame, text='Cadastrar vendas', font=('Arial', 14)).grid(row=5, column=0, columnspan=4, padx=15,
                                                                            pady=6, ipady=15)

        # Nome
        Label(self.frame, text='Nome').grid(row=6, column=0, columnspan=1, pady=5, padx=5)
        self.nome = Entry(self.frame)
        self.nome.grid(row=6, column=1, padx=5, pady=5)

        # Ingredientes
        Label(self.frame, text='Quantidade').grid(row=7, column=0, columnspan=1, pady=5, padx=5)
        self.quantidade = Entry(self.frame)
        self.quantidade.grid(row=7, column=1, padx=5, pady=5)

        # Valor total
        Label(self.frame, text='Data de venda', relief="flat", fg="#000").grid(row=8, column=0, pady=5, padx=5)
        self.dataB = Button(self.frame, text='Calendário', width=15, command=calendario, bg='#6ecef4')
        self.dataB.grid(row=8, column=1, padx=5, pady=5)

        Button(self.frame, text='Cadastrar', bg='#88E497', width=15,
               command=lambda: Venda.CadastrarVenda(self)).grid(row=12, column=0, padx=15, pady=5)
        Button(self.frame, text='Excluir', width=15, bg='#FF8368',
               command=lambda: Venda.RemoverVenda(self)).grid(row=12, column=1, padx=5, pady=5)
        Button(self.frame, text='Atualizar', width=15,
               command=lambda: Venda.MostrarVenda(self)).grid(row=13, column=0, padx=5, pady=5)
        Button(self.frame, text='Excel', width=15,
               command=lambda: Venda.GerarExcel(self)).grid(row=13, column=1, padx=5, pady=5)

        # Informações
        self.tree = ttk.Treeview(self.frame, selectmode="browse", columns=("c1", "c2", "c3", "c4"), show="headings")

        self.tree.column("c1", width=250, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='Nome')

        self.tree.column("c2", width=100, minwidth=500, stretch=NO)
        self.tree.heading('#2', text='Quantidade')

        self.tree.column("c3", width=100, minwidth=500, stretch=NO)
        self.tree.heading('#3', text='Valor')

        self.tree.column("c4", width=150, minwidth=500, stretch=NO)
        self.tree.heading('#4', text='Data')

        self.tree.grid(row=6, column=6, padx=25, pady=10, columnspan=3, rowspan=6)

        Venda.MostrarVenda(self)

        self.root.mainloop()

    def FrameProduto(self, tela):

        self.root = tela

        try:
            self.frame.destroy()
        except:
            pass

        self.frame = Frame(self.root)
        self.frame.place(x=15, y=100)

        # title
        self.root.title('Cadastro de produtos')

        # Título
        Label(self.frame, text='Cadastrar produto', font=('Arial', 14)).grid(row=5, column=0, columnspan=4, padx=15,
                                                                             pady=6, ipady=15)

        # Nome
        Label(self.frame, text='Nome').grid(row=6, column=0, columnspan=1, pady=5, padx=5)
        self.nome = Entry(self.frame)
        self.nome.grid(row=6, column=1, padx=5, pady=5)

        # Ingredientes
        Label(self.frame, text='Ingredientes').grid(row=7, column=0, columnspan=1, pady=5, padx=5)
        self.ingredientes = Entry(self.frame)
        self.ingredientes.grid(row=7, column=1, padx=5, pady=5)

        # Grupos
        Label(self.frame, text='Grupo').grid(row=8, column=0, columnspan=1, pady=5, padx=5)
        self.grupo = Entry(self.frame)
        self.grupo.grid(row=8, column=1, padx=5, pady=5)

        # Preco
        Label(self.frame, text='Preço').grid(row=9, column=0, columnspan=1, pady=5, padx=5)
        self.preco = Entry(self.frame)
        self.preco.grid(row=9, column=1, padx=5, pady=5)

        Button(self.frame, text='Cadastrar', bg='#88E497', width=15,
               command=lambda: Produto.CadastrarProduto(self)).grid(row=12, column=0, padx=15, pady=5)
        Button(self.frame, text='Excluir', width=15, bg='#FF8368',
               command=lambda: Produto.RemoverProduto(self)).grid(row=12, column=1, padx=5, pady=5)
        Button(self.frame, text='Atualizar', width=15,
               command=lambda: Produto.MostrarProduto(self)).grid(row=13, column=0, padx=5, pady=5)
        Button(self.frame, text='Excel', width=15,
               command=lambda: Produto.GerarExcel(self)).grid(row=13, column=1, padx=5, pady=5)

        # Informações
        self.tree = ttk.Treeview(self.frame, selectmode="browse", columns=("c1", "c2", "c3", "c4"), show="headings")

        self.tree.column("c1", width=150, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='Nome')

        self.tree.column("c2", width=300, minwidth=500, stretch=NO)
        self.tree.heading('#2', text='Ingredientes')

        self.tree.column("c3", width=100, minwidth=500, stretch=NO)
        self.tree.heading('#3', text='Grupo')

        self.tree.column("c4", width=100, minwidth=500, stretch=NO)
        self.tree.heading('#4', text='Preço')

        self.tree.grid(row=6, column=5, padx=10, pady=10, columnspan=3, rowspan=6)

        Produto.MostrarProduto(self)

        self.root.mainloop()

    def FrameEstatistica(self, tela):

        self.root = tela

        self.data = ''

        try:
            self.frame.destroy()
        except:
            pass

        self.frame = Frame(self.root)
        self.frame.place(x=15, y=100)

        # title
        self.root.title('Estatísticas')

        # Nome ou produto?
        Label(self.frame, text='Gerar estatística', font=('Arial', 15)) \
            .grid(row=0, column=1, columnspan=2, pady=40)

        Label(self.frame, text='Dados', font=('Arial', 13)) \
            .grid(row=2, column=0, columnspan=4)

        self.dinheiroEstatistica = IntVar()
        self.quantidadeUniEstatistica = IntVar()

        Checkbutton(self.frame, text='Dinheiro', variable=self.dinheiroEstatistica, bg='#32beff').grid(row=4, column=1)
        Checkbutton(self.frame, text='Quantidade unitária', variable=self.quantidadeUniEstatistica, bg='#32beff').grid(
            row=4, column=2)

        Button(self.frame, text='Gerar Estatística', bg='#88E497', width=13,
               command=lambda: Estatistica.GerarEstatistica(self), ).grid(row=6, column=1, pady=100)

        # Data
        Label(self.frame, text='Data', font=('Arial', 13)) \
            .grid(row=2, column=5)

        dataAtual = str(date.today()).split('-')
        cal = Calendar(self.frame, selectmode='day', year=int(dataAtual[0]), month=int(dataAtual[1]),
                       day=int(dataAtual[2]))
        cal.grid(row=3, column=5, padx=100, pady=25)

        def pegaData():
            data = cal.get_date()

            self.data = cal.get_date()

            dataFormatado = str(self.data).split('/')

            ano = dataFormatado[2]
            dia = dataFormatado[1]
            mes = dataFormatado[0]

            dataFormatada = ano + '/' + mes + '/' + dia
            self.data = dataFormatada

        def zeraData():
            self.data = ''

        Button(self.frame, text='Selecionar', bg='white', width=15,
               command=pegaData).grid(row=4, column=5, pady=5)

        Button(self.frame, text='Histórico', width=15, relief='flat', fg='#00A3FF',
               command=zeraData).grid(row=5, column=5)

        # Nome ou Grupo

        self.nomeEstatistica = IntVar()
        self.grupoEstatistica = IntVar()

        Checkbutton(self.frame, text='Nome', variable=self.nomeEstatistica, bg='#00bfbc').grid(row=3, column=1)
        Checkbutton(self.frame, text='Grupo', variable=self.grupoEstatistica, bg='#00bfbc').grid(row=3, column=2)

    def FrameCadastro(self, tela):

        try:
            self.root = tela

            try:
                self.frame.destroy()
            except:
                pass
        except:
            pass

        self.frame = Frame(self.root)
        self.frame.place(x=15, y=100)

        Label(self.frame, text='Usuários cadastrados', font=('Arial', 14)).grid(row=2, column=1)
        Label(self.frame, text='', font=('Arial', 14)).grid(row=3, column=1, pady=160, )

        self.tree = ttk.Treeview(self.root, selectmode="browse", columns=("c1", "c2", "c3", "c4"), show="headings")

        self.tree.column("c1", width=40, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='ID')

        self.tree.column("c2", width=40, minwidth=800, stretch=NO)
        self.tree.heading('#2', text='Usuário')

        self.tree.column("c2", width=40, minwidth=500, stretch=NO)
        self.tree.heading('#3', text='Senha')

        self.tree.column("c2", width=40, minwidth=500, stretch=NO)
        self.tree.heading('#4', text='Nível')

        self.tree.place(x=15, y=200)

        Button(self.frame, text='Atualizar', width=15,
               command=lambda: Cadastro.VisualizarCadastros(self)).grid(row=4, column=1)

        Button(self.frame, text='Excluir', width=15, bg="#FF8368",
               command=lambda: Cadastro.RemoverCadastro(self)).grid(row=4, column=2)

        Button(self.frame, text='Alterar Senha', width=15, bg="#84dcff",
               command=lambda: FrameUsuario()).grid(row=4, column=3, padx=25)

        Cadastro.VisualizarCadastros(self)

        def FrameUsuario():

            try:
                self.id_usuario = int(self.tree.selection()[0])
            except:
                messagebox.showinfo('Erro', 'Selecione um usuário!')
                return

            self.largura = 320
            self.altura = 400

            self.root_alterarUsuario = Tk()
            self.root_alterarUsuario.title('Atualizar cadastro de usuário')

            Label(self.root_alterarUsuario, text='Atualização de cadastro').grid(row=0, column=1, columnspan=2, pady=20)

            self.root_alterarUsuario.maxsize(self.largura, self.altura)
            self.root_alterarUsuario.minsize(self.largura, self.altura)

            # Nome
            Label(self.root_alterarUsuario, text='Nome').grid(row=1, column=0, pady=15)
            self.nome_altera = Entry(self.root_alterarUsuario)
            self.nome_altera.grid(row=1, column=1, padx=5, pady=5)

            # Senha
            Label(self.root_alterarUsuario, text='Senha').grid(row=2, column=0, pady=15)
            self.senha_altera = Entry(self.root_alterarUsuario, show='*')
            self.senha_altera.grid(row=2, column=1, padx=5, pady=5)

            # Senha
            Label(self.root_alterarUsuario, text='Confirmar senha').grid(row=3, column=0, pady=15)
            self.senha_confirma = Entry(self.root_alterarUsuario, show='*')
            self.senha_confirma.grid(row=3, column=1, padx=5, pady=5)

            # Senha
            Label(self.root_alterarUsuario, text='Chave de segurança').grid(row=4, column=0, pady=15)
            self.chave_seguranca = Entry(self.root_alterarUsuario, show='*')
            self.chave_seguranca.grid(row=4, column=1, padx=5, pady=5)

            Button(self.root_alterarUsuario, text='Alterar Senha', width=15, bg="#88E497",
                   command=lambda: Cadastro.AlterarCadastro(self, self.id_usuario)).grid(row=5, column=1, padx=50)

        self.frame.mainloop()

    def Sair(self):
        self.root.destroy()
        python = sys.executable
        os.execl(python, python, *sys.argv)