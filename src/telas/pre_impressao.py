import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap import Style
import os
from pathlib import Path
import importlib.util
from tkinter import ttk, filedialog
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


# from ttkbootstrap import Style
from controllers import TkinterController
class PreImpressao(tk.Frame):
    tipos_carne = []
    def __init__(self, master=None,  dados_produto=None):
        super().__init__(master)
        self.master = master
        self.controller = TkinterController()
        self.dados_produto = dados_produto
        self.temperatura_combobox = None  # Adicione esta linha
        self.etiquetas_disponiveis = []
        self.criar_widgets()
        self.carregar_etiquetas()


        

       
        
    def criar_widgets(self):
        temperatura = self.controller.obter_temperatura()
        self.data_fabricacao_label = tb.Label(self, text='Data Fabricação')
        self.data_fabricacao_label.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        self.data_fabricacao_entry = tb.DateEntry(self, bootstyle="primary")
        self.data_fabricacao_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        # Rótulo e entrada para Validade
        self.validade_label = tb.Label(self, text='Validade')
        self.validade_label.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.data_validade_entry = tb.DateEntry(self, bootstyle="primary")
        self.data_validade_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        self.temperatura_label = tb.Label(self, text='Temperatura')
        self.temperatura_label.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        self.temperatura_combobox = tb.Combobox(self, values=temperatura, state='readonly')
        self.temperatura_combobox.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        
        self.escolha_etiqueta_label = tb.Label(self, text='Etiqueta')
        self.escolha_etiqueta_label.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

        self.escolha_etiqueta_combobox = tb.Combobox(self, values=self.etiquetas_disponiveis, state='readonly')
        self.escolha_etiqueta_combobox.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        

        # Rótulo e entrada para Quantidade
        self.quantidade_label = tb.Label(self, text='Quantidade')
        self.quantidade_label.grid(row=4, column=0, padx=10, pady=5, sticky="ew")

        self.quantidade_entry = tb.Entry(self)
        self.quantidade_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

        

        # Botão para imprimir os valores
        salvar_produto = tb.Button(self, text="Imprimir", command=self.imprimir)
        salvar_produto.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

    def carregar_etiquetas(self):
        p = Path(__file__).parent
        diretorio_etiquetas = file=p/'../etiquetas'
        if diretorio_etiquetas:
            arquivos_python = [f for f in os.listdir(diretorio_etiquetas) if f.endswith('.py') and f != '__init__.py']

            print(arquivos_python)
            self.etiquetas_disponiveis = [f[:-3] for f in arquivos_python]

            # atualiza combobox
            self.escolha_etiqueta_combobox['values'] = self.etiquetas_disponiveis

        else:
            print("Sem diretorio")

    def imprimir(self):
        # Ação a ser executada ao pressionar o botão Imprimir
        data_fabricacao = self.data_fabricacao_entry.entry.get()        
        data_validade = self.data_validade_entry.entry.get()


        quantidade = self.quantidade_entry.get()

        print("Data de Fabricação:", data_fabricacao)
        print("Validade:", data_validade)
        print("Quantidade:", quantidade)

        etiqueta_selecionada = self.escolha_etiqueta_combobox.get()

        if etiqueta_selecionada:
            pdf_path = f"{etiqueta_selecionada.replace(' ', '_').lower()}_reportlab.pdf"
            self.criar_tabela_etiqueta(pdf_path)

    def criar_tabela_etiqueta(self, pdf_path):
        # Importa o módulo da etiqueta selecionada
        etiqueta_module = importlib.import_module(self.escolha_etiqueta_combobox.get())


        # Chama a função criar_tabela do módulo da etiqueta
        etiqueta_module.criar_tabela(pdf_path)


    def abrir_popup(self):
        popup = tk.Toplevel(self.master)
        popup.title("Impressão") 

        label = ttk.Label(popup, text="Impressão:")
        label.pack(padx=10, pady=5)

        entry = ttk.Entry(popup)
        entry.pack(padx=10, pady=5)

        salvar_button = ttk.Button(popup, text="Salvar", command=lambda: self.salvar_tipo(entry.get(), popup))
        salvar_button.pack(padx=10, pady=10)

        largura_popup = 50
        altura_popup = 150
        largura_tela = self.master.winfo_screenwidth()
        altura_tela = self.master.winfo_screenheight()

        x = (largura_tela - largura_popup) // 2
        y = (altura_tela - altura_popup) // 2

        popup.geometry(f"{largura_popup}x{altura_popup}+{x}+{y}")
        popup.grab_set()

    def fechar_popup(self):
        self.master.destroy()

    # def selecionar_tipo(self, event):
    #     tipo_selecionado = self.tipo_combobox.get()

    # def salvar_tipo(self, novo_tipo, popup):
    #     print("Funcao salvar tipo")
    #     if novo_tipo:
    #         print(novo_tipo)
    #         self.controller.criar_tipo(novo_tipo)
    #         CadastroProduto.tipos_carne = self.controller.obter_tipos()
    #         self.tipo_combobox['values'] = CadastroProduto.tipos_carne
    #         self.tipo_combobox.set(novo_tipo)

    #     popup.destroy()
        
   

    # def salvar_tipo(self):
       
    #     # Coletar dados do formulário       
    #     tipo = self.tipo_entry.get()
        
    #     # Coletar os outros dados da informação nutricional de maneira semelhante

    #     # Criar um dicionário com os dados do produto
    #     dados_produto = {
    #         "tipo": tipo,           
    #     }

    #     # Salvar o produto usando o controller
    #     if self.dados_produto:
    #         try:
    #             self.controller.atualizar_tipo(self.dados_produto.id, dados_produto)
    #             messagebox.showinfo('Sucesso', 'Tipo Atualizado com sucesso!')
    #             self.fechar_popup()
            
    #         except Exception as e:
    #             messagebox.showerror('Erro', f'Erro ao salvar o tipo: {e}')
        
    #     else:
    #         try:            
    #             self.controller.salvar_tipo(dados_produto)
    #             messagebox.showinfo("Sucesso", "Tipo cadastrado com sucesso!")          
    #             self.tipo_entry.delete(0, tk.END)           
    #             self.fechar_popup()      

            
    #         except Exception as e:
    #             print(e)
    #     # Limpar os outros campos da informação nutricional aqui

        # Adicione qualquer lógica adicional após salvar o produto


