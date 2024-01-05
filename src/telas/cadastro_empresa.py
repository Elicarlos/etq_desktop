import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style
from controllers import TkinterController

class CadastroEmpresa(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.criar_widgets()

        # Configurar o formulário com os dados da empresa existente, se houver
        self.configurar_com_dados_empresa()

    def criar_widgets(self):
        # Criação do formulário baseado na classe Empresa
        empresa_info_frame = tk.LabelFrame(self, text='Cadastro de Empresa', padx=50, pady=50)
        empresa_info_frame.grid(row=0, column=0, padx=20, pady=5)

        # Crie um objeto Style da ttkbootstrap
        style = Style(theme="flatly")  # Substitua "flatly" pelo tema desejado

        # Labels
        cnpj_label = ttk.Label(empresa_info_frame, text='CNPJ', style="TLabel")
        cnpj_label.grid(row=0, column=0, sticky=tk.E, pady=5)

        razao_social_label = ttk.Label(empresa_info_frame, text='Razão Social', style="TLabel")
        razao_social_label.grid(row=1, column=0, sticky=tk.E, pady=5)

        fantasia_label = ttk.Label(empresa_info_frame, text='Nome Fantasia', style="TLabel")
        fantasia_label.grid(row=2, column=0, sticky=tk.E, pady=5)

        numero_sif_label = ttk.Label(empresa_info_frame, text='Número SIF', style="TLabel")
        numero_sif_label.grid(row=3, column=0, sticky=tk.E, pady=5)

        registro_adapi_label = ttk.Label(empresa_info_frame, text='Registro ADAPI', style="TLabel")
        registro_adapi_label.grid(row=4, column=0, sticky=tk.E, pady=5)

        # Entry widgets
        self.cnpj_entry = ttk.Entry(empresa_info_frame, width=50, style="TEntry")  
        self.cnpj_entry.grid(row=0, column=1, pady=5)

        self.razao_social_entry = ttk.Entry(empresa_info_frame, width=50, style="TEntry")
        self.razao_social_entry.grid(row=1, column=1, pady=5)

        self.fantasia_entry = ttk.Entry(empresa_info_frame, width=50, style="TEntry")
        self.fantasia_entry.grid(row=2, column=1, pady=5)

        self.numero_sif_entry = ttk.Entry(empresa_info_frame, width=50, style="TEntry")
        self.numero_sif_entry.grid(row=3, column=1, pady=5)

        self.registro_adapi_entry = ttk.Entry(empresa_info_frame, width=50, style="TEntry")
        self.registro_adapi_entry.grid(row=4, column=1, pady=5)

        # Botão
        btn_salvar = ttk.Button(empresa_info_frame, text='Salvar', style="TButton", command=self.salvar_empresa)
        btn_salvar.grid(row=5, column=1, pady=10)

    def configurar_com_dados_empresa(self):
        # Verificar se há uma empresa existente
        empresa_existente = TkinterController.obter_empresas().first()

        if empresa_existente:
            # Preencher os campos com os dados da empresa existente
            self.cnpj_entry.insert(0, empresa_existente.cnpj)
            self.razao_social_entry.insert(0, empresa_existente.razao_social)
            self.fantasia_entry.insert(0, empresa_existente.fantasia)
            self.numero_sif_entry.insert(0, empresa_existente.numero_sif)
            self.registro_adapi_entry.insert(0, empresa_existente.registro_adapi)

    def salvar_empresa(self):
        # Obter valores dos campos
        cnpj = self.cnpj_entry.get()
        razao_social = self.razao_social_entry.get()
        fantasia = self.fantasia_entry.get()
        numero_sif = self.numero_sif_entry.get()
        registro_adapi = self.registro_adapi_entry.get()

        # Validar campos (adicionar validações conforme necessário)

        # Verificar se a empresa já existe
        empresa_existente = TkinterController.obter_empresas().first()

        try:
            if empresa_existente:
                # Atualizar a empresa existente
                TkinterController.atualizar_empresa(empresa_existente.id, cnpj, razao_social, fantasia, numero_sif, registro_adapi)
                messagebox.showinfo("Sucesso", "Empresa atualizada com sucesso!")
            else:
                # Criar uma nova empresa
                TkinterController.criar_empresa(cnpj, razao_social, fantasia, numero_sif, registro_adapi)
                messagebox.showinfo("Sucesso", "Empresa cadastrada com sucesso!")

            # Limpar os campos após o sucesso
            self.limpar_campos()

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar empresa: {str(e)}")

    def limpar_campos(self):
        # Limpar os campos
        self.cnpj_entry.delete(0, tk.END)
        self.razao_social_entry.delete(0, tk.END)
        self.fantasia_entry.delete(0, tk.END)
        self.numero_sif_entry.delete(0, tk.END)
        self.registro_adapi_entry.delete(0, tk.END)

    def abrir_proxima_tela(self):
        # Adicione a lógica para avançar para a próxima tela aqui
        pass