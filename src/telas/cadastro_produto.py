import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
class CadastroProduto(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
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

        tipo_combobox = ttk.Combobox(produto_info_frame, values=['Carne 1', 'Carne 2'])
        tipo_combobox.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        adicona_tipo = ttk.Button(produto_info_frame, text="+ Adicionar", )
        adicona_tipo.grid(row=0, column=2, padx=10, pady=5, sticky="ew")

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
        # Criar a janela popup
        popup = tk.Toplevel(self)
        popup.title("Adicionar Tipo de Carne")

        # Adicionar widgets ao popup
        label = ttk.Label(popup, text="Novo Tipo de Carne:")
        label.pack(padx=10, pady=5)

        entry = ttk.Entry(popup)
        entry.pack(padx=10, pady=5)

        salvar_button = ttk.Button(popup, text="Salvar", command=popup.destroy)
        salvar_button.pack(padx=10, pady=10)

        # Configurar para que a janela principal fique inativa enquanto o popup estiver aberto
        popup.grab_set()

        # Centralizar o popup na tela
        popup.update_idletasks()
        w = popup.winfo_width()
        h = popup.winfo_height()
        x = (popup.winfo_screenwidth() - w) // 2
        y = (popup.winfo_screenheight() - h) // 2
        popup.geometry('{}x{}+{}+{}'.format(w, h, x, y))

        
    def abrir_proxima_tela(self):
        self.master.master.master.mudar_tela(Home)

