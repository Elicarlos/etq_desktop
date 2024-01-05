import tkinter as tk
from tkinter import ttk

class CadastroTipo(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.criar_widgets()
    
    def criar_widgets(self):
        # Criação do formulário baseado na classe Empresa
        empresa_info_frame = tk.LabelFrame(self, text='Cadastro de Empresa', padx=50, pady=50)
        empresa_info_frame.grid(row=0, column=0, padx=20, pady=5)

        cnpj_label = tk.Label(empresa_info_frame, text='CNPJ')
        cnpj_label.grid(row=0, column=0)
        cnpj_entry = tk.Entry(empresa_info_frame, width=50)
        cnpj_entry.grid(row=0, column=1)

        razao_social_label = tk.Label(empresa_info_frame, text='Razão Social')
        razao_social_label.grid(row=1, column=0)
        razao_social_entry = tk.Entry(empresa_info_frame, width=50)
        razao_social_entry.grid(row=1, column=1)

        fantasia_label = tk.Label(empresa_info_frame, text='Nome Fantasia')
        fantasia_label.grid(row=2, column=0)
        fantasia_entry = tk.Entry(empresa_info_frame, width=50)
        fantasia_entry.grid(row=2, column=1)

        numero_sif_label = tk.Label(empresa_info_frame, text='Número SIF')
        numero_sif_label.grid(row=3, column=0)
        numero_sif_entry = tk.Entry(empresa_info_frame, width=50)
        numero_sif_entry.grid(row=3, column=1)

        registro_adapi_label = tk.Label(empresa_info_frame, text='Registro ADAPI')
        registro_adapi_label.grid(row=4, column=0)
        registro_adapi_entry = tk.Entry(empresa_info_frame, width=50)
        registro_adapi_entry.grid(row=4, column=1)

        btn_salvar = ttk.Button(empresa_info_frame, text='Salvar')
        btn_salvar.grid(row=5, column=5)

        # Botão para avançar para a próxima tela
        botao_proxima_tela = ttk.Button(self, text="Próxima Tela", command=self.abrir_proxima_tela)
        botao_proxima_tela.grid(row=6, column=1, pady=20)

    def abrir_proxima_tela(self):
        # Adicione a lógica para avançar para a próxima tela aqui
        pass

