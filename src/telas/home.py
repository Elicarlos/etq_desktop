from ttkbootstrap import ttk
import tkinter as tk
from tkinter import messagebox
from .cadastro_produto import CadastroProduto

class Home(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.criar_widgets()

    def criar_widgets(self):
        # Campo de pesquisa
        self.campo_pesquisa = ttk.Entry(self, width=80)
        self.campo_pesquisa.grid(row=0, column=0, padx=10, pady=10)

        # Botão de pesquisa
        btn_pesquisa = ttk.Button(self, text='Buscar', command=self.realizar_pesquisa)
        btn_pesquisa.grid(row=0, column=1, padx=10, pady=10)

        # Elementos para exibição dos resultados
        self.label_resultado = ttk.Label(self, text="")
        self.label_resultado.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.colunas = ("Produto", "Detalhes", "Preço", "Estoque")
        self.tree_resultados = ttk.Treeview(self, columns=self.colunas, show="headings", selectmode="browse")
        for coluna in self.colunas:
            self.tree_resultados.heading(coluna, text=coluna)

    def realizar_pesquisa(self):
        self.termo_pesquisa = self.campo_pesquisa.get()
        # Adicione a lógica necessária para a pesquisa
        resultados = self.simular_pesquisa(self.termo_pesquisa)

        # Limpar a tabela de resultados
        for i in self.tree_resultados.get_children():
            self.tree_resultados.delete(i)

        if resultados:
            for resultado in resultados:
                self.tree_resultados.insert("", "end", values=resultado)

            # Exibir Treeview apenas se houver resultados
            self.tree_resultados.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
            self.label_resultado.config(text="")
        else:
            # Ocultar Treeview se não houver resultados
            self.tree_resultados.grid_remove()
            self.label_resultado.config(text="Produto não encontrado")

    def simular_pesquisa(self, termo_pesquisa):
        # Essa função deve ser substituída pela lógica real de pesquisa no seu banco de dados
        # Aqui, ela apenas simula alguns resultados
        if termo_pesquisa.lower() == "produto1":
            return [("Produto1", "Detalhes", "$10.00", "50 unidades")]
        elif termo_pesquisa.lower() == "produto2":
            return [("Produto2", "Detalhes", "$15.00", "30 unidades")]
        else:
            return []

    def abrir_proxima_tela(self):
        self.master.master.master.mudar_tela(CadastroProduto)
