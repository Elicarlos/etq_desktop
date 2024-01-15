import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# from ttkbootstrap import Style
from controllers import TkinterController
class CadastroTipo(tk.Frame):
    tipos_carne = []
    def __init__(self, master=None,  dados_produto=None):
        super().__init__(master)
        self.master = master
        self.config(background="#FFFFFF")
        self.controller = TkinterController()
        self.dados_produto = dados_produto
        self.tipo_combobox = None  # Adicione esta linha
        self.criar_widgets()
        self.preencher_campos()
        

    def criar_widgets(self):
       
        self.tipo_entry = ttk.Entry(self)
        self.tipo_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
       
        salvar_produto = ttk.Button(self, text="Salvar", command=self.salvar_tipo)
        salvar_produto.grid(row=11, column=2, padx=10, pady=5, sticky="ew")

    def preencher_campos(self):
        if self.dados_produto:
            # Supondo que você tenha widgets como entry_corte, entry_tipo, entry_fibra, etc.
            produto = self.dados_produto            
            tipo = produto.tipo       
            self.tipo_entry.insert(0, tipo)           
           



    # def abrir_popup(self):
    #     popup = tk.Toplevel(self.master)
    #     popup.title("Adicionar Tipo de Carne")

    #     label = ttk.Label(popup, text="Novo Tipo de Carne:")
    #     label.pack(padx=10, pady=5)

    #     entry = ttk.Entry(popup)
    #     entry.pack(padx=10, pady=5)

    #     salvar_button = ttk.Button(popup, text="Salvar", command=lambda: self.salvar_tipo(entry.get(), popup))
    #     salvar_button.pack(padx=10, pady=10)

    #     largura_popup = 300
    #     altura_popup = 150
    #     largura_tela = self.master.winfo_screenwidth()
    #     altura_tela = self.master.winfo_screenheight()

    #     x = (largura_tela - largura_popup) // 2
    #     y = (altura_tela - altura_popup) // 2

    #     popup.geometry(f"{largura_popup}x{altura_popup}+{x}+{y}")
    #     popup.grab_set()

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

    def salvar_tipo(self):
       
        # Coletar dados do formulário       
        tipo = self.tipo_entry.get()
        
        # Coletar os outros dados da informação nutricional de maneira semelhante

        # Criar um dicionário com os dados do produto
        dados_produto = {
            "tipo": tipo,           
        }

        # Salvar o produto usando o controller
        if self.dados_produto:
            try:
                self.controller.atualizar_tipo(self.dados_produto.id, dados_produto)
                messagebox.showinfo('Sucesso', 'Tipo Atualizado com sucesso!')
                self.fechar_popup()
            
            except Exception as e:
                messagebox.showerror('Erro', f'Erro ao salvar o tipo: {e}')
        
        else:
            try:            
                self.controller.salvar_tipo(dados_produto)
                messagebox.showinfo("Sucesso", "Tipo cadastrado com sucesso!")          
                self.tipo_entry.delete(0, tk.END)           
                self.fechar_popup()      

            
            except Exception as e:
                print(e)
        # Limpar os outros campos da informação nutricional aqui

        # Adicione qualquer lógica adicional após salvar o produto

    def abrir_proxima_tela(self):
        self.master.master.master.mudar_tela(Home)
