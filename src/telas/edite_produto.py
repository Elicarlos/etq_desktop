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
        buscar_produtos.place(x=0, y=130)

        btn_adicionar_produto = ttk.Button(self, text="Buscar")
        btn_adicionar_produto.place(x=430, y=130)

        btn_adicionar_produto = ttk.Button(self, text="Adicionar Produto")
        btn_adicionar_produto.place(x=530, y=130)

        self.colunas = ('Corte', 'Tipo', 'Sexo')

        self.tree = ttk.Treeview(self, columns=self.colunas, show='headings')

        self.tree.heading("0", text="Corte", anchor=tk.CENTER)
        self.tree.heading("1", text="Tipo", anchor=tk.CENTER)
        self.tree.heading("2", text="Sexo", anchor=tk.CENTER)
        self.tree.place(x=0, y=230), 

    def carregar_produtos(self):
        # Limpar a Treeview antes de recarregar
        for item in self.tree.get_children():
            self.tree.delete(item)

        dados = self.controller.obter_itens_nutricionais()
        # print(dados)  

        # for produto in dados:
        #     self.tree.insert("", tk.END, values=(produto['corte'],produto['tipo'], produto['fibra_alimentar_100g']))

