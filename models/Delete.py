from tkinter import messagebox
from models import ConexaoBD as BD


class Delete:

    def RemoverID(self, tabela, campo, id):

        BD.ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('DELETE FROM {} WHERE {} = "{}"'.format(tabela, campo, id))
                self.conexao.commit()
        except:
            messagebox.showinfo('Erro', 'Erro ao remover dado!')