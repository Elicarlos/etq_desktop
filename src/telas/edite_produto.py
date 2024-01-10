import tkinter as tk
from tkinter import ttk
from controllers import TkinterController


class  EditeProduto(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.controller = TkinterController()
        self.criar_widgets()
        self.carregar_produtos()

    
    def criar_widgets(self):
        buscar_produtos = ttk.Entry(self, width=80)
        buscar_produtos.place(x=0, y=30)

        btn_adicionar_prodotus = ttk.Button(self,text="Buscar")
        btn_adicionar_prodotus.place(x=500, y=30)

        btn_adicionar_prodotus = ttk.Button(self,text="Adicionar Produto")
        btn_adicionar_prodotus.place(x=950, y=30)

        self.colunas = ('Corte', 'Tipo', 'Sexo')

        self.tree = ttk.Treeview(self, columns=self.colunas, show='headings')
  
        self.tree.heading("0", text="Corte")
        self.tree.heading("1", text="Tipo")
        self.tree.heading("2", text="Sexo")
        self.tree.pack(pady=10)
       

    def carregar_produtos(self):
        # Limpar a Treeview antes de recarregar
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        lista_produtos = self.controller.obter_itens_nutricionais()
        print(lista_produtos)

        # Consultar todos os produtos do banco de dados
        for produto in lista_produtos:
            self.tree.insert("", tk.END, values=produto)
    

        # Adicionar produtos ao Treeview
        # for produto in produtos:
        #     # tipo_nome = produto.tipo.tipo
        #     tipo_nome = 'Teste'
        #     corte = produto.corte
        #     sexo = produto.sexo
        #     self.tree.insert("", tk.END, values=(tipo_nome, corte, sexo))


