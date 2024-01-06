import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from controllers import TkinterController
class CadastroProduto(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.controller = TkinterController()
        self.tipo_combobox = None  # Adicione esta linha
        self.criar_widgets()
        

    def criar_widgets(self):
        # style = Style(theme="lumen")  # Escolha o tema desejado

        notebook = ttk.Notebook(self)
        notebook.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

        produto_info_frame = ttk.Frame(notebook)
        notebook.add(produto_info_frame, text='Produto')

        # Labels e Combobox/Entries
        labels = ['Tipo de Carne', 'Corte', 'Sexo', 'Código Barras', 'Porção por Embalagem', 'Porção']
        for i, label_text in enumerate(labels):
            label = ttk.Label(produto_info_frame, text=label_text)
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
        
        tipos_corte = self.controller.obter_tipos()

        # Sempre cria o Combobox, mesmo que vazio
        self.tipo_combobox = ttk.Combobox(produto_info_frame, values=tipos_corte)
        self.tipo_combobox.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        adicona_tipo = ttk.Button(produto_info_frame, text="+ Adicionar", command=self.abrir_popup)
        adicona_tipo.grid(row=0, column=2, padx=10, pady=5, sticky="ew")

        # Adiciona o evento para lidar com a seleção no Combobox
        self.tipo_combobox.bind("<<ComboboxSelected>>", self.selecionar_tipo)


        corte_entry = ttk.Entry(produto_info_frame)
        corte_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        sexo_combobox = ttk.Combobox(produto_info_frame, values=["F", "M"])
        sexo_combobox.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        codigo_barras_entry = ttk.Entry(produto_info_frame)
        codigo_barras_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")
        porcao_embalagem_entry = ttk.Entry(produto_info_frame)
        porcao_embalagem_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")
        porcao_entry = ttk.Entry(produto_info_frame)
        porcao_entry.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

        campo_adicional_label = ttk.Label(produto_info_frame, text='Campo adicional')
        campo_adicional_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        campo_adicional_entry = tk.Text(produto_info_frame, height=4, width=40)
        campo_adicional_entry.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky="ew")


        # Adicionando a frame "Informação Nutricional"
        nutricional_frame = ttk.Frame(notebook)
        notebook.add(nutricional_frame, text="Informação Nutricional")

        # Titulos
        cem_gramas_label = ttk.Label(nutricional_frame, text='100g')
        cem_gramas_label.grid(row=0, column=1, padx=10, pady=5)
        valor_diario_label = ttk.Label(nutricional_frame, text="% VD*")
        valor_diario_label.grid(row=0, column=2, padx=10, pady=5)

        valor_energetico_label = ttk.Label(nutricional_frame, text='Valor energético (kcal)')
        valor_energetico_label.grid(row=1, column=0, padx=10, pady=5)
        valor_energetico_cem_gramas_entry = ttk.Entry(nutricional_frame)
        valor_energetico_cem_gramas_entry.grid(row=1, column=1, padx=10, pady=5)

        valor_energetico_diario_entry = ttk.Entry(nutricional_frame)
        valor_energetico_diario_entry.grid(row=1, column=2, padx=10, pady=5)

        carboidratos_totais_label = ttk.Label(nutricional_frame, text='Carboidratos Totais (g)')
        carboidratos_totais_label.grid(row=2, column=0, padx=10, pady=5)

        carboidratos_totais_cem_gramas_entry = ttk.Entry(nutricional_frame)
        carboidratos_totais_cem_gramas_entry.grid(row=2, column=1, padx=10, pady=5)  
        carboidratos_totais_diario_entry = ttk.Entry(nutricional_frame)
        carboidratos_totais_diario_entry.grid(row=2, column=2, padx=10, pady=5)

        acucares_totais_label = ttk.Label(nutricional_frame, text='Açucares Totais (g)')
        acucares_totais_label.grid(row=3, column=0, padx=10, pady=5)

        acucares_totais_cem_gramas_entry = ttk.Entry(nutricional_frame)
        acucares_totais_cem_gramas_entry.grid(row=3, column=1, padx=10, pady=5)  
        acucares_totais_diario_entry = ttk.Entry(nutricional_frame)
        acucares_totais_diario_entry.grid(row=3, column=2, padx=10, pady=5)

        acucares_adicionados_label = ttk.Label(nutricional_frame, text='Açucares Adicionados (g)')
        acucares_adicionados_label.grid(row=4, column=0, padx=10, pady=5)

        acucares_adicionados_cem_gramas_entry = ttk.Entry(nutricional_frame)
        acucares_adicionados_cem_gramas_entry.grid(row=4, column=1, padx=10, pady=5)  
        acucares_adicionados_diario_entry = ttk.Entry(nutricional_frame)
        acucares_adicionados_diario_entry.grid(row=4, column=2, padx=10, pady=5)

        proteinas_label = ttk.Label(nutricional_frame, text='Proteínas (g)')
        proteinas_label.grid(row=5, column=0, padx=10, pady=5)

        proteinas_cem_gramas_entry = ttk.Entry(nutricional_frame)
        proteinas_cem_gramas_entry.grid(row=5, column=1, padx=10, pady=5)  
        proteinas_diario_entry = ttk.Entry(nutricional_frame)          
        proteinas_diario_entry.grid(row=5, column=2, padx=10, pady=5)

        gorduras_totais_label = ttk.Label(nutricional_frame, text='Gorduras totais (g)')
        gorduras_totais_label.grid(row=6, column=0, padx=10, pady=5)

        gorduras_totais_cem_gramas_entry = ttk.Entry(nutricional_frame)
        gorduras_totais_cem_gramas_entry.grid(row=6, column=1, padx=10, pady=5)  
        gorduras_totais_diario_entry = ttk.Entry(nutricional_frame)
        gorduras_totais_diario_entry.grid(row=6, column=2, padx=10, pady=5)

        gorduras_saturadas_label = ttk.Label(nutricional_frame, text='Gorduras saturadas (g)')
        gorduras_saturadas_label.grid(row=7, column=0, padx=10, pady=5)
        gorduras_saturadas_cem_gramas_entry = ttk.Entry(nutricional_frame)
        gorduras_saturadas_cem_gramas_entry.grid(row=7, column=1, padx=10, pady=5)  
        gorduras_saturadas_diario_entry = ttk.Entry(nutricional_frame)
        gorduras_saturadas_diario_entry.grid(row=7, column=2, padx=10, pady=5)

        gorduras_trans_label = ttk.Label(nutricional_frame, text='Gorduras trans (g)')
        gorduras_trans_label.grid(row=8, column=0, padx=10, pady=5)
        gorduras_trans_cem_gramas_entry = ttk.Entry(nutricional_frame)
        gorduras_trans_cem_gramas_entry.grid(row=8, column=1, padx=10, pady=5)  
        gorduras_trans_diario_entry = ttk.Entry(nutricional_frame)
        gorduras_trans_diario_entry.grid(row=8, column=2, padx=10, pady=5)

        fibra_alimentar_label = ttk.Label(nutricional_frame, text='Fibra alimentar (g)')
        fibra_alimentar_label.grid(row=9, column=0, padx=10, pady=5)
        fibra_alimentar_cem_gramas_entry = ttk.Entry(nutricional_frame)
        fibra_alimentar_cem_gramas_entry.grid(row=9, column=1, padx=10, pady=5)  
        fibra_alimentar_diario_entry = ttk.Entry(nutricional_frame)
        fibra_alimentar_diario_entry.grid(row=9, column=2, padx=10, pady=5)

        sodio_label = ttk.Label(nutricional_frame, text='Sódio (mg)')
        sodio_label.grid(row=10, column=0, padx=10, pady=5)
        sodio_cem_gramas_entry = ttk.Entry(nutricional_frame)
        sodio_cem_gramas_entry.grid(row=10, column=1, padx=10, pady=5)  
        sodio_diario_entry = ttk.Entry(nutricional_frame)
        sodio_diario_entry.grid(row=10, column=2, padx=10, pady=5)

        salvar_produto = ttk.Button(nutricional_frame, text="Salvar")
        salvar_produto.grid(row=11, column=2, padx=10, pady=5, sticky="ew")


    def abrir_popup(self):
        popup = tk.Toplevel(self.master)
        popup.title("Adicionar Tipo de Carne")

        label = ttk.Label(popup, text="Novo Tipo de Carne:")
        label.pack(padx=10, pady=5)

        entry = ttk.Entry(popup)
        entry.pack(padx=10, pady=5)

        salvar_button = ttk.Button(popup, text="Salvar", command=lambda: self.salvar_tipo(entry.get(), popup))
        salvar_button.pack(padx=10, pady=10)

        largura_popup = 300
        altura_popup = 150
        largura_tela = self.master.winfo_screenwidth()
        altura_tela = self.master.winfo_screenheight()

        x = (largura_tela - largura_popup) // 2
        y = (altura_tela - altura_popup) // 2

        popup.geometry(f"{largura_popup}x{altura_popup}+{x}+{y}")
        popup.grab_set()

    def selecionar_tipo(self, event):
        tipo_selecionado = event.widget.get()

    def salvar_tipo(self, novo_tipo, popup):
        print("Funcao salvar tipo")
        if novo_tipo:
            print(novo_tipo)
            self.controller.criar_tipo(novo_tipo)
            CadastroProduto.tipos_carne = self.controller.obter_tipos()
            self.tipo_combobox['values'] = CadastroProduto.tipos_carne
            self.tipo_combobox.set(novo_tipo)

        popup.destroy()

    def salvar_produto(self):
        # Coletar dados do formulário
        tipo = self.tipo_combobox.get()
        corte = corte_entry.get()
        sexo = sexo_combobox.get()
        codigo_barras = codigo_barras_entry.get()
        porcao_embalagem = porcao_embalagem_entry.get()
        porcao = porcao_entry.get()
        campo_adicional = campo_adicional_entry.get("1.0", tk.END).strip()

        # Coletar dados do formulário de informação nutricional
        valor_energetico_cem_gramas = valor_energetico_cem_gramas_entry.get()
        valor_energetico_diario = valor_energetico_diario_entry.get()

        valor_energetico_diario = valor_energetico_diario_entry.get()

        carboidratos_totais_cem_gramas_entry = carboidratos_totais_cem_gramas_entry.get()
       
        carboidratos_totais_diario_entry = carboidratos_totais_diario_entry.get()
       
        acucares_totais_cem_gramas_entry = acucares_totais_cem_gramas_entry.get()
       
        acucares_totais_diario_entry = acucares_totais_diario_entry.get()

        acucares_adicionados_cem_gramas_entry = acucares_adicionados_cem_gramas_entry.get()
       
        acucares_adicionados_diario_entry = acucares_adicionados_diario_entry.get()
       
        proteinas_cem_gramas_entry = proteinas_cem_gramas_entry.get()
    
        proteinas_diario_entry = proteinas_diario_entry.get()

        gorduras_totais_cem_gramas_entry = gorduras_totais_cem_gramas_entry.get()
       
        gorduras_totais_diario_entry = gorduras_totais_diario_entry.get()


        gorduras_saturadas_cem_gramas_entry = gorduras_saturadas_cem_gramas_entry.get()
        
        gorduras_saturadas_diario_entry = gorduras_saturadas_diario_entry.get()

       
        gorduras_trans_cem_gramas_entry = gorduras_trans_cem_gramas_entry.get()
       
        gorduras_trans_diario_entry = gorduras_trans_diario_entry.get()

        
        fibra_alimentar_cem_gramas_entry = fibra_alimentar_cem_gramas_entry.get()
         
        fibra_alimentar_diario_entry = fibra_alimentar_diario_entry.get()

        sodio_cem_gramas_entry = sodio_cem_gramas_entry.get()
        
        sodio_diario_entry = sodio_diario_entry.get()
     
        
        
       
                
        

        

        # Coletar os outros dados da informação nutricional de maneira semelhante

        # Criar um dicionário com os dados do produto
        dados_produto = {
            "tipo": tipo,
            "corte": corte,
            "sexo": sexo,
            "digo_barras": codigo_barras,
            "porcao_embalagem": porcao_embalagem,
            "porcao": porcao,
            "campo_adicional": campo_adicional,
            "valor_energetico_cem_gramas": valor_energetico_cem_gramas,
            "valor_energetico_diario": valor_energetico_diario,
            # Adicione os outros campos da informação nutricional aqui

            "valor_energetico_cem_gramas": valor_energetico_cem_gramas,
            "valor_energetico_diario": valor_energetico_diario,

            "valor_energetico_diario": valor_energetico_diario,

            "carboidratos_totais_cem_gramas_entry": carboidratos_totais_cem_gramas,
        
            "carboidratos_totais_diario_entry": carboidratos_totais_diario,
        
            "acucares_totais_cem_gramas_entry": acucares_totais_cem_gramas,
        
            "acucares_totais_diario_entry": acucares_totais_diario,

            "acucares_adicionados_cem_gramas_entry" : acucares_adicionados_cem_gramas,
        
            "acucares_adicionados_diario_entry" : acucares_adicionados_diario,
        
            "proteinas_cem_gramas_entry" : proteinas_cem_gramas,
        
            "proteinas_diario_entry" : proteinas_diario,

            "gorduras_totais_cem_gramas_entry" : gorduras_totais_cem_gramas,
        
            "gorduras_totais_diario_entry" : gorduras_totais_diario,


            "gorduras_saturadas_cem_gramas_entry" : gorduras_saturadas_cem_gramas,
            
            "gorduras_saturadas_diario_entry" : gorduras_saturadas_diario,

        
            "gorduras_trans_cem_gramas_entry" : gorduras_trans_cem_gramas,
        
            "gorduras_trans_diario_entry" : gorduras_trans_diario,

            
            "fibra_alimentar_cem_gramas_entry" : fibra_alimentar_cem_gramas,
            
            "fibra_alimentar_diario_entry" : fibra_alimentar_diario,
                    
            "sodio_cem_gramas_entry" : sodio_cem_gramas,
            
            "sodio_diario_entry": sodio_diario,
     
        }

        # Salvar o produto usando o controller
        self.controller.salvar_produto(dados_produto)

        # Limpar os campos do formulário
        self.tipo_combobox.set('')
        corte_entry.delete(0, tk.END)
        sexo_combobox.set('')
        codigo_barras_entry.delete(0, tk.END)
        porcao_embalagem_entry.delete(0, tk.END)
        porcao_entry.delete(0, tk.END)
        campo_adicional_entry.delete("1.0", tk.END)
        valor_energetico_cem_gramas_entry.delete(0, tk.END)
        valor_energetico_diario_entry.delete(0, tk.END)
        # Limpar os outros campos da informação nutricional aqui

        # Adicione qualquer lógica adicional após salvar o produto

    def abrir_proxima_tela(self):
        self.master.master.master.mudar_tela(Home)
