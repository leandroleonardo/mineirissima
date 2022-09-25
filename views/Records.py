from tkinter import END, Toplevel, ttk, NO
from models.Consulta import Consulta


class Records:

    # Visualizar Cadastros
    def __init__(self):

        def geraViewCadastros(self):

            resultados = ''
            resultados = Consulta.Tabela(self, 'USUARIOS')

            self.tree.delete(*self.tree.get_children())

            linhaV = []
            cont = 0

            if resultados:
                for linha in resultados:
                    if linha['nivel'] != 2:
                        linhaV.append(linha['nome'])
                        self.tree.insert("", END, values=linhaV, iid=linha['id_usuario'], tag='1')
                        linhaV.clear()

        self.vc = Toplevel()
        self.vc.resizable(False, False)
        self.vc.title('Visualizar cadastros')

        # dimensoes da janela
        largura = 1280
        altura = 720

        # meio da janela
        posx = largura / 2
        posy = altura / 2

        self.tree = ttk.Treeview(self.vc, selectmode="browse", columns="c1", show="headings")

        self.tree.column("c1", width=500, minwidth=800, stretch=NO)
        self.tree.heading('#1', text='Usuários')

        self.tree.grid(row=0, column=0, padx=10, pady=10)

        geraViewCadastros(self)

        self.vc.mainloop()