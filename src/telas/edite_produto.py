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
        buscar_produtos.pack(side=tk.LEFT, padx=5)

        btn_adicionar_produto = ttk.Button(self, text="Buscar")
        btn_adicionar_produto.pack(side=tk.LEFT, padx=5)

        btn_adicionar_produto = ttk.Button(self, text="Adicionar Produto")
        btn_adicionar_produto.pack(side=tk.LEFT, padx=5)

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

        produtos = self.controller.obter_itens_nutricionais()

        # Consultar todos os produtos do banco de dados
        for i, item in enumerate(produtos):
            self.tree.insert("", tk.END, values=(item.corte, item.fibra_alimentar_100g))

            # Adiciona botões de edição, apagar e impressão fora do Treeview
            editar_button = tk.Button(self, text='Editar', command=lambda item=item: self.editar_item(item))
            apagar_button = tk.Button(self, text='Apagar', command=lambda item=item: self.apagar_item(item))
            imprimir_button = tk.Button(self, text='Imprimir', command=lambda item=item: self.imprimir_item(item))

            # Coloca os botões ao lado do Treeview
            editar_button.pack(side=tk.LEFT, padx=5)
            apagar_button.pack(side=tk.LEFT, padx=5)
            imprimir_button.pack(side=tk.LEFT, padx=5)

    # Funções de exemplo para edição, exclusão e impressão
    def editar_item(self, item):
        print(f'Editar: {item.corte}')

    def apagar_item(self, item):
        print(f'Apagar: {item.corte}')

    def imprimir_item(self, item):
        print(f'Imprimir: {item.corte}')