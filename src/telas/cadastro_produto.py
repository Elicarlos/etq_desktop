import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# from ttkbootstrap import Style
from controllers import TkinterController
class CadastroProduto(tk.Frame):
    tipos_carne = []
    def __init__(self, master=None,  dados_produto=None):
        super().__init__(master)
        self.master = master
        self.controller = TkinterController()
        self.dados_produto = dados_produto
        self.tipo_combobox = None  # Adicione esta linha
        self.criar_widgets()
        self.preencher_campos()
        

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
        self.tipo_combobox = ttk.Combobox(produto_info_frame, values=tipos_corte, state='readonly')
        self.tipo_combobox.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        adicona_tipo = ttk.Button(produto_info_frame, text="+ Adicionar", command=self.abrir_popup)
        adicona_tipo.grid(row=0, column=2, padx=10, pady=5, sticky="ew")

        # Adiciona o evento para lidar com a seleção no Combobox
        self.tipo_combobox.bind("<<ComboboxSelected>>", self.selecionar_tipo)


        self.corte_entry = ttk.Entry(produto_info_frame)
        self.corte_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        self.sexo_combobox = ttk.Combobox(produto_info_frame, values=["F", "M"], state='readonly' )
        self.sexo_combobox.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        self.codigo_barras_entry = ttk.Entry(produto_info_frame)
        self.codigo_barras_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")
        self.porcao_embalagem_entry = ttk.Entry(produto_info_frame)
        self.porcao_embalagem_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")
        self.porcao_entry = ttk.Entry(produto_info_frame)
        self.porcao_entry.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

        self.campo_adicional_label = ttk.Label(produto_info_frame, text='Campo adicional')
        self.campo_adicional_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.campo_adicional_entry = tk.Text(produto_info_frame, height=4, width=40)
        self.campo_adicional_entry.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky="ew")


        # Adicionando a frame "Informação Nutricional"
        nutricional_frame = ttk.Frame(notebook)
        notebook.add(nutricional_frame, text="Informação Nutricional")

        # Titulos
        self.cem_gramas_label = ttk.Label(nutricional_frame, text='100g')
        self.cem_gramas_label.grid(row=0, column=1, padx=10, pady=5)
        self.valor_diario_label = ttk.Label(nutricional_frame, text="% VD*")
        self.valor_diario_label.grid(row=0, column=2, padx=10, pady=5)

        self.valor_energetico_label = ttk.Label(nutricional_frame, text='Valor energético (kcal)')
        self.valor_energetico_label.grid(row=1, column=0, padx=10, pady=5)
        self.valor_energetico_cem_gramas_entry = ttk.Entry(nutricional_frame)
        self.valor_energetico_cem_gramas_entry.grid(row=1, column=1, padx=10, pady=5)

        self.valor_energetico_diario_entry = ttk.Entry(nutricional_frame)
        self.valor_energetico_diario_entry.grid(row=1, column=2, padx=10, pady=5)

        self.carboidratos_totais_label = ttk.Label(nutricional_frame, text='Carboidratos Totais (g)')
        self.carboidratos_totais_label.grid(row=2, column=0, padx=10, pady=5)

        self.carboidratos_totais_cem_gramas_entry = ttk.Entry(nutricional_frame)
        self.carboidratos_totais_cem_gramas_entry.grid(row=2, column=1, padx=10, pady=5)  
        self.carboidratos_totais_diario_entry = ttk.Entry(nutricional_frame)
        self.carboidratos_totais_diario_entry.grid(row=2, column=2, padx=10, pady=5)

        self.acucares_totais_label = ttk.Label(nutricional_frame, text='Açucares Totais (g)')
        self.acucares_totais_label.grid(row=3, column=0, padx=10, pady=5)

        self.acucares_totais_cem_gramas_entry = ttk.Entry(nutricional_frame)
        self.acucares_totais_cem_gramas_entry.grid(row=3, column=1, padx=10, pady=5)  
        self.acucares_totais_diario_entry = ttk.Entry(nutricional_frame)
        self.acucares_totais_diario_entry.grid(row=3, column=2, padx=10, pady=5)

        self.acucares_adicionados_label = ttk.Label(nutricional_frame, text='Açucares Adicionados (g)')
        self.acucares_adicionados_label.grid(row=4, column=0, padx=10, pady=5)

        self.acucares_adicionados_cem_gramas_entry = ttk.Entry(nutricional_frame)
        self.acucares_adicionados_cem_gramas_entry.grid(row=4, column=1, padx=10, pady=5)  
        self.acucares_adicionados_diario_entry = ttk.Entry(nutricional_frame)
        self.acucares_adicionados_diario_entry.grid(row=4, column=2, padx=10, pady=5)

        self.proteinas_label = ttk.Label(nutricional_frame, text='Proteínas (g)')
        self.proteinas_label.grid(row=5, column=0, padx=10, pady=5)

        self.proteinas_cem_gramas_entry = ttk.Entry(nutricional_frame)
        self.proteinas_cem_gramas_entry.grid(row=5, column=1, padx=10, pady=5)  
        self.proteinas_diario_entry = ttk.Entry(nutricional_frame)          
        self.proteinas_diario_entry.grid(row=5, column=2, padx=10, pady=5)

        self.gorduras_totais_label = ttk.Label(nutricional_frame, text='Gorduras totais (g)')
        self.gorduras_totais_label.grid(row=6, column=0, padx=10, pady=5)

        self.gorduras_totais_cem_gramas_entry = ttk.Entry(nutricional_frame)
        self.gorduras_totais_cem_gramas_entry.grid(row=6, column=1, padx=10, pady=5)  
        self.gorduras_totais_diario_entry = ttk.Entry(nutricional_frame)
        self.gorduras_totais_diario_entry.grid(row=6, column=2, padx=10, pady=5)

        self.gorduras_saturadas_label = ttk.Label(nutricional_frame, text='Gorduras saturadas (g)')
        self.gorduras_saturadas_label.grid(row=7, column=0, padx=10, pady=5)
        self.gorduras_saturadas_cem_gramas_entry = ttk.Entry(nutricional_frame)
        self.gorduras_saturadas_cem_gramas_entry.grid(row=7, column=1, padx=10, pady=5)  
        self.gorduras_saturadas_diario_entry = ttk.Entry(nutricional_frame)
        self.gorduras_saturadas_diario_entry.grid(row=7, column=2, padx=10, pady=5)

        self.gorduras_trans_label = ttk.Label(nutricional_frame, text='Gorduras trans (g)')
        self.gorduras_trans_label.grid(row=8, column=0, padx=10, pady=5)
        self.gorduras_trans_cem_gramas_entry = ttk.Entry(nutricional_frame)
        self.gorduras_trans_cem_gramas_entry.grid(row=8, column=1, padx=10, pady=5)  
        self.gorduras_trans_diario_entry = ttk.Entry(nutricional_frame)
        self.gorduras_trans_diario_entry.grid(row=8, column=2, padx=10, pady=5)

        self.fibra_alimentar_label = ttk.Label(nutricional_frame, text='Fibra alimentar (g)')
        self.fibra_alimentar_label.grid(row=9, column=0, padx=10, pady=5)
        self.fibra_alimentar_cem_gramas_entry = ttk.Entry(nutricional_frame)
        self.fibra_alimentar_cem_gramas_entry.grid(row=9, column=1, padx=10, pady=5)  
        self.fibra_alimentar_diario_entry = ttk.Entry(nutricional_frame)
        self.fibra_alimentar_diario_entry.grid(row=9, column=2, padx=10, pady=5)

        self.sodio_label = ttk.Label(nutricional_frame, text='Sódio (mg)')
        self.sodio_label.grid(row=10, column=0, padx=10, pady=5)
        self.sodio_cem_gramas_entry = ttk.Entry(nutricional_frame)
        self.sodio_cem_gramas_entry.grid(row=10, column=1, padx=10, pady=5)  
        self.sodio_diario_entry = ttk.Entry(nutricional_frame)
        self.sodio_diario_entry.grid(row=10, column=2, padx=10, pady=5)

        salvar_produto = ttk.Button(nutricional_frame, text="Salvar", command=self.salvar_produto)
        salvar_produto.grid(row=11, column=2, padx=10, pady=5, sticky="ew")

    def preencher_campos(self):
        if self.dados_produto:
            # Supondo que você tenha widgets como entry_corte, entry_tipo, entry_fibra, etc.
            produto = self.dados_produto
            
            tipo = produto.tipo_id         
            corte = produto.corte
            sexo = produto.sexo
            codigo_barras = produto.codigo_barras
            porcao_embalagem = produto.porcao_embalagem
            porcao = produto.porcao
            campo_adicional = produto.campo_adicional

            valor_energetico_cem_gramas = produto.valor_energetico_100g
            valor_energetico_diario = produto.valor_energetico_vd
            carboidratos_totais_cem_gramas = produto.carboidratos_totais_100g
            carboidratos_totais_diario = produto.carboidratos_totais_vd
            acucares_totais_cem_gramas = produto.acucares_totais_100g
            acucares_totais_diario = produto.acucares_totais_vd
            acucares_adicionados_cem_gramas = produto.acucares_adicionados_100g
            acucares_adicionados_diario = produto.acucares_adicionados_vd
            proteinas_cem_gramas = produto.proteinas_100g
            proteinas_diario = produto.proteinas_vd
            gorduras_totais_cem_gramas = produto.gorduras_totais_100g
            gorduras_totais_diario = produto.gorduras_totais_vd
            gorduras_saturadas_cem_gramas = produto.gorduras_saturadas_100g    
            gorduras_saturadas_diario  =   produto.gorduras_saturadas_vd   
            gorduras_trans_cem_gramas = produto.gorduras_trans_100g     
            gorduras_trans_diario =   produto.gorduras_trans_vd
            fibra_alimentar_cem_gramas =  produto.fibra_alimentar_100g
            fibra_alimentar_diario = produto.fibra_alimentar_vd
            sodio_cem_gramas =  produto.sodio_100g
            sodio_diario = produto.sodio_vd
              

            # Preencha os campos com os dados do produto selecionado
            self.tipo_combobox.set('')
            self.tipo_combobox.set(tipo)
            self.corte_entry.insert(0, corte)            
            # Para ComboBox
            # Limpe a seleção anterior, se houver
            self.sexo_combobox.set('')
            # Selecione o valor correto no ComboBox
            self.sexo_combobox.set(sexo)
            self.codigo_barras_entry.insert(0, codigo_barras)           
            self.porcao_embalagem_entry.insert(0, porcao_embalagem)       
            self.porcao_entry.insert(0, porcao) 
            self.campo_adicional_entry.insert('1.0', campo_adicional)
            self.valor_energetico_cem_gramas_entry.insert(0, valor_energetico_cem_gramas)
            self.valor_energetico_diario_entry.insert(0, valor_energetico_diario)
            self.carboidratos_totais_cem_gramas_entry.insert(0,carboidratos_totais_cem_gramas)            
            self.carboidratos_totais_diario_entry.insert(0, carboidratos_totais_diario)
            self.acucares_totais_cem_gramas_entry.insert(0, acucares_totais_cem_gramas)              
            self.acucares_totais_diario_entry.insert(0, acucares_totais_diario)
            self.acucares_adicionados_cem_gramas_entry.insert(0, acucares_adicionados_cem_gramas)            
            self.acucares_adicionados_diario_entry.insert(0, acucares_adicionados_diario) 
            self.proteinas_cem_gramas_entry.insert(0, proteinas_cem_gramas)            
            self.proteinas_diario_entry.insert(0, proteinas_diario)
            self.gorduras_totais_cem_gramas_entry.insert(0, gorduras_totais_cem_gramas)            
            self.gorduras_totais_diario_entry.insert(0, gorduras_totais_diario)

            self.gorduras_saturadas_cem_gramas_entry.insert(0, gorduras_saturadas_cem_gramas)        
            self.gorduras_saturadas_diario_entry.insert(0, gorduras_saturadas_diario)                 
            self.gorduras_trans_cem_gramas_entry.insert(0,gorduras_trans_cem_gramas)        
            self.gorduras_trans_diario_entry .insert(0, gorduras_trans_diario)           
            self.fibra_alimentar_cem_gramas_entry .insert(0, fibra_alimentar_cem_gramas)     
            self.fibra_alimentar_diario_entry.insert(0, fibra_alimentar_diario)     
            self.sodio_cem_gramas_entry.insert(0, sodio_cem_gramas)      
            self.sodio_diario_entry.insert(0, sodio_diario)
         



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

    def fechar_popup(self):
        self.master.destroy()

    def selecionar_tipo(self, event):
        tipo_selecionado = self.tipo_combobox.get()

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
        corte = self.corte_entry.get()
        sexo = self.sexo_combobox.get()
        codigo_barras = self.codigo_barras_entry.get()
        porcao_embalagem = self.porcao_embalagem_entry.get()
        porcao = self.porcao_entry.get()
        campo_adicional = self.campo_adicional_entry.get("1.0", tk.END).strip()

        # Coletar dados do formulário de informação nutricional
        valor_energetico_cem_gramas = self.valor_energetico_cem_gramas_entry.get()
        valor_energetico_diario = self.valor_energetico_diario_entry.get()
        carboidratos_totais_cem_gramas = self.carboidratos_totais_cem_gramas_entry.get()  
        carboidratos_totais_diario = self.carboidratos_totais_diario_entry.get()   
        acucares_totais_cem_gramas = self.acucares_totais_cem_gramas_entry.get()   
        acucares_totais_diario = self.acucares_totais_diario_entry.get()
        acucares_adicionados_cem_gramas = self.acucares_adicionados_cem_gramas_entry.get()       
        acucares_adicionados_diario = self.acucares_adicionados_diario_entry.get()
        proteinas_cem_gramas = self.proteinas_cem_gramas_entry.get()   
        proteinas_diario = self.proteinas_diario_entry.get()
        gorduras_totais_cem_gramas = self.gorduras_totais_cem_gramas_entry.get()      
        gorduras_totais_diario = self.gorduras_totais_diario_entry.get()
        gorduras_saturadas_cem_gramas = self.gorduras_saturadas_cem_gramas_entry.get()       
        gorduras_saturadas_diario = self.gorduras_saturadas_diario_entry.get()     
        gorduras_trans_cem_gramas = self.gorduras_trans_cem_gramas_entry.get()       
        gorduras_trans_diario = self.gorduras_trans_diario_entry.get()       
        fibra_alimentar_cem_gramas = self.fibra_alimentar_cem_gramas_entry.get()        
        fibra_alimentar_diario = self.fibra_alimentar_diario_entry.get()
        sodio_cem_gramas = self.sodio_cem_gramas_entry.get()
        sodio_diario = self.sodio_diario_entry.get()        

        # Coletar os outros dados da informação nutricional de maneira semelhante

        # Criar um dicionário com os dados do produto
        dados_produto = {
            "tipo": tipo,
            "corte": corte,
            "sexo": sexo,
            "codigo_barras": codigo_barras,
            "porcao_embalagem": porcao_embalagem,
            "porcao": porcao,
            "campo_adicional": campo_adicional,
            "valor_energetico_100g": valor_energetico_cem_gramas,
            "valor_energetico_vd": valor_energetico_diario,
            "carboidratos_totais_100g": carboidratos_totais_cem_gramas,
            "carboidratos_totais_vd": carboidratos_totais_diario,
            "acucares_totais_100g": acucares_totais_cem_gramas,
            "acucares_totais_vd": acucares_totais_diario,
            "acucares_adicionados_100g": acucares_adicionados_cem_gramas,
            "acucares_adicionados_vd": acucares_adicionados_diario,
            "proteinas_100g": proteinas_cem_gramas,
            "proteinas_vd": proteinas_diario,
            "gorduras_totais_100g": gorduras_totais_cem_gramas,
            "gorduras_totais_vd": gorduras_totais_diario,
            "gorduras_saturadas_100g": gorduras_saturadas_cem_gramas,
            "gorduras_saturadas_vd": gorduras_saturadas_diario,
            "gorduras_trans_100g": gorduras_trans_cem_gramas,
            "gorduras_trans_vd": gorduras_trans_diario,
            "fibra_alimentar_100g": fibra_alimentar_cem_gramas,
            "fibra_alimentar_vd": fibra_alimentar_diario,
            "sodio_100g": sodio_cem_gramas,
            "sodio_vd": sodio_diario,
        }

        # Salvar o produto usando o controller
        try:            
            self.controller.salvar_produto(dados_produto)
            messagebox.showinfo("Sucesso", "Empresa cadastrada com sucesso!")

            # Limpar os campos do formulário
            self.tipo_combobox.set('')
            self.corte_entry.delete(0, tk.END)
            self.sexo_combobox.set('')
            self.codigo_barras_entry.delete(0, tk.END)
            self.porcao_embalagem_entry.delete(0, tk.END)
            self.porcao_entry.delete(0, tk.END)
            self.campo_adicional_entry.delete("1.0", tk.END)
            self.valor_energetico_cem_gramas_entry.delete(0, tk.END)
            self.valor_energetico_diario_entry.delete(0, tk.END)
            self.valor_energetico_cem_gramas_entry.delete(0, tk.END)
            self.valor_energetico_diario_entry.delete(0, tk.END)
            self.carboidratos_totais_cem_gramas_entry.delete(0, tk.END)  
            self.carboidratos_totais_diario_entry.delete(0, tk.END)   
            self.acucares_totais_cem_gramas_entry.delete(0, tk.END)  
            self.acucares_totais_diario_entry.delete(0, tk.END)
            self.acucares_adicionados_cem_gramas_entry.delete(0, tk.END)       
            self.acucares_adicionados_diario_entry.delete(0, tk.END)
            self.proteinas_cem_gramas_entry.delete(0, tk.END)   
            self.proteinas_diario_entry.delete(0, tk.END)
            self.gorduras_totais_cem_gramas_entry.delete(0, tk.END)      
            self.gorduras_totais_diario_entry.delete(0, tk.END)
            self.gorduras_saturadas_cem_gramas_entry.delete(0, tk.END)       
            self.gorduras_saturadas_diario_entry.delete(0, tk.END)     
            self.gorduras_trans_cem_gramas_entry.delete(0, tk.END)       
            self.gorduras_trans_diario_entry.delete(0, tk.END)       
            self.fibra_alimentar_cem_gramas_entry.delete(0, tk.END)        
            self.fibra_alimentar_diario_entry.delete(0, tk.END)
            self.sodio_cem_gramas_entry.delete(0, tk.END)
            self.sodio_diario_entry.delete(0, tk.END)

            self.fechar_popup()      

        
        except Exception as e:
            print(e)
        # Limpar os outros campos da informação nutricional aqui

        # Adicione qualquer lógica adicional após salvar o produto

    def abrir_proxima_tela(self):
        self.master.master.master.mudar_tela(Home)
