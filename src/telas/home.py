# from ttkbootstrap import ttk
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

import ttkbootstrap as bt
from ttkbootstrap.constants import *
from ttkbootstrap import Style

from controllers import TkinterController
from telas.cadastro_tipo import CadastroTipo
from telas.pre_impressao import PreImpressao
from .cadastro_produto import CadastroProduto

class Home(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.config(background="#FFFFFF")
        self.controller = TkinterController()
        self.criar_widgets()

    def criar_widgets(self):
        # Campo de pesquisa

        self.label_resultado = bt.Label(self, text="")
        self.label_resultado.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        self.campo_pesquisa = bt.Entry(self, width=120)
        self.campo_pesquisa.grid(row=0, column=0, padx=10, pady=10)

        # Botão de pesquisa
        btn_pesquisa = ttk.Button(self, text='Buscar', command=self.realizar_pesquisa)
        btn_pesquisa.grid(row=0, column=1, padx=10, pady=10)

        # Elementos para exibição dos resultados
        self.label_resultado = ttk.Label(self, text="")
        self.label_resultado.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.colunas = ("Corte", "Tipo", "Sexo","Imprimir")
        self.tree_resultados = bt.Treeview(self, columns=self.colunas, show="headings", selectmode="browse", style='light.Treeview')
        
        for coluna in self.colunas:
            self.tree_resultados.heading(coluna, text=coluna)

        self.tree_resultados.bind('<ButtonRelease-1>', self.on_tree_click)
    
    def on_tree_click(self, event):
        item_id = self.tree_resultados.identify_row(event.y)
        col_id = self.tree_resultados.identify_column(event.x)

        if item_id and col_id == '#4':  # Coluna "Ação"
            acao = self.tree_resultados.item(item_id, 'values')[3]             

            if acao == "Imprimir":
                # Obtenha o ID da linha clicada
                produto_data = self.tree_resultados.item(item_id, 'values')
                # print(produto_data)

                # Obtenha os dados do produto selecionado
                produto_data = self.tree_resultados.item(item_id, 'values')

                # Recupere o ID do produto da primeira coluna
                produto_id = produto_data[0]
                # print(produto_id)

                # Recupere os dados do produto do banco de dados usando o ID
                dados_do_banco = self.controller.obter_item_nutricional_por_id(produto_id)
             

                # Crie uma instância do CadastroProduto passando o Toplevel como mestre e os dados do produto
                cadastro_produto_popup = tk.Toplevel(self.master)
                cadastro_produto_popup.title("Impressão")

                # Chame o método para inicializar os campos com os dados do produto
                cadastro_produto_frame = PreImpressao(cadastro_produto_popup, dados_produto=dados_do_banco)
                cadastro_produto_frame.pack(expand=True, fill="both")

                # ... (se necessário, adicione outras configurações específicas)

                # Centralize o popup na tela principal
                largura_popup = 800
                altura_popup = 600
                largura_tela = self.master.winfo_screenwidth()
                altura_tela = self.master.winfo_screenheight()
                x = (largura_tela - largura_popup) // 2
                y = (altura_tela - altura_popup) // 2

                cadastro_produto_popup.geometry(f"{largura_popup}x{altura_popup}+{x}+{y}")

                # Impede interação com a tela principal enquanto o popup estiver aberto
                cadastro_produto_popup.grab_set()

                # Aguarde o fechamento do popup antes de continuar
                self.master.wait_window(cadastro_produto_popup)

                # Atualize os dados na Treeview após o fechamento do popup
                # self.adicionar_dados()

        # if item_id and col_id == '#6':  # Coluna "Ação"
        #     acao = self.tree.item(item_id, 'values')[5] 
        #     if acao == 'Excluir':  # Coluna "Ação" (índice 3 considerando 0 como o primeiro índice)
        #         acao = self.tree.item(item_id, 'values')[2]
        #         self.excluir_produto()


    def realizar_pesquisa(self):
        self.termo_pesquisa = self.campo_pesquisa.get()
        # Adicione a lógica necessária para a pesquisa
        resultados = self.controller.pesquisa(self.termo_pesquisa)
        # print(resultados)

        # Limpar a tabela de resultados
        for i in self.tree_resultados.get_children():
            self.tree_resultados.delete(i)

        if resultados:
            for resultado in resultados:
                corte = resultado.get('corte', '')
                tipo = resultado.get('tipo', '')
                sexo = resultado.get('sexo', '')
               

                self.tree_resultados.insert("", "end", values=(corte, tipo, sexo, 'Imprimir')) 
                self.tree_resultados.heading("Imprimir", text="")
                self.tree_resultados.column('Corte', width=100)
                self.tree_resultados.column("Tipo", width=100)
                self.tree_resultados.column('Sexo', width=50)
                self.tree_resultados.column("Imprimir", width=50)
         

            # Exibir Treeview apenas se houver resultados
            # self.tree_resultados.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
            self.tree_resultados.grid(row=2, column=0,  padx=10, pady=10, sticky="nsew")
            self.label_resultado.config(text="")
        else:
            # Ocultar Treeview se não houver resultados
            self.tree_resultados.grid_remove()
            self.label_resultado.config(text="Produto não encontrado")

    