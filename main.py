from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *



# window = tkinter.Tk()
# def cadastro_produto():    
#     window.title('Cadastro de Produtos')

#     frame = tkinter.Frame(window)
#     frame.pack()

#     produto_info_frame = tkinter.LabelFrame(frame, text='Cadastro de Produtos')
#     produto_info_frame.grid(row=0, column=0, padx=20, pady=5)

#     tipo_label = tkinter.Label(produto_info_frame, text='Tipo de Carne')
#     tipo_label.grid(row=0, column=0)
#     tipo_combobox = ttk.Combobox(produto_info_frame, text='Tipo de Carne', values=['Carne 1', 'Carne 2'])
#     tipo_combobox.grid(row=1, column=0)


#     corte_label = tkinter.Label(produto_info_frame, text='Corte')
#     corte_label.grid(row=0, column=1)
#     corte_entry = tkinter.Entry(produto_info_frame)
#     corte_entry.grid(row=1, column=1)

#     sexo_label = tkinter.Label(produto_info_frame, text='Sexo')
#     sexo_label.grid(row=0, column=2)
#     sexo_combobox = ttk.Combobox(produto_info_frame, values=["F", "M"])
#     sexo_combobox.grid(row=1, column=2)

#     codigo_barras_label = tkinter.Label(produto_info_frame, text='Código Barras')
#     codigo_barras_label.grid(row=2, column=0)
#     codigo_barras_entry = tkinter.Entry(produto_info_frame)
#     codigo_barras_entry.grid(row=3, column=0)

#     for widget in produto_info_frame.winfo_children():
#         widget.grid_configure(padx=10, pady=5)

    
#     nutricional_frame = tkinter.LabelFrame(frame, text='Informação Nutricional')
#     nutricional_frame.grid(row=1, column=0, sticky='news', padx=20, pady=20)

#     cem_gramas_label = tkinter.Label(nutricional_frame, text='100g')
#     cem_gramas_label.grid(row=0, column=1)
#     valor_diario_label = tkinter.Label(nutricional_frame, text="% VD*")
#     valor_diario_label.grid(row=0, column=2)

#     valor_energetico_label = tkinter.Label(nutricional_frame, text='Valor energético (kcal)')
#     valor_energetico_label.grid(row=1, column=0)
#     valor_energetico_cem_gramas_entry = tkinter.Entry(nutricional_frame)
#     valor_energetico_cem_gramas_entry.grid(row=1, column=1)  
#     valor_energetico_diario_entry = tkinter.Entry(nutricional_frame)
#     valor_energetico_diario_entry.grid(row=1, column=2)

#     carboidratos_totais_label = tkinter.Label(nutricional_frame, text='Carboidratos Totais (g)')
#     carboidratos_totais_label.grid(row=2, column=0)
#     carboidratos_totais_cem_gramas_entry = tkinter.Entry(nutricional_frame)
#     carboidratos_totais_cem_gramas_entry.grid(row=2, column=1)  
#     carboidratos_totais_diario_entry = tkinter.Entry(nutricional_frame)
#     carboidratos_totais_diario_entry.grid(row=2, column=2)

#     acucares_totais_label = tkinter.Label(nutricional_frame, text='Açucares Totais (g)')
#     acucares_totais_label.grid(row=3, column=0)
#     acucares_totais_cem_gramas_entry = tkinter.Entry(nutricional_frame)
#     acucares_totais_cem_gramas_entry.grid(row=3, column=1)  
#     acucares_totais_diario_entry = tkinter.Entry(nutricional_frame)
#     acucares_totais_diario_entry.grid(row=3, column=2)

#     acucares_adicionados_label = tkinter.Label(nutricional_frame, text='Açucares Adicionados (g)')
#     acucares_adicionados_label.grid(row=4, column=0)
#     acucares_adicionados_cem_gramas_entry = tkinter.Entry(nutricional_frame)
#     acucares_adicionados_cem_gramas_entry.grid(row=4, column=1)  
#     acucares_adicionados_diario_entry = tkinter.Entry(nutricional_frame)
#     acucares_adicionados_diario_entry.grid(row=4, column=2)

#     proteinas_label = tkinter.Label(nutricional_frame, text='Proteínas (g)')
#     proteinas_label.grid(row=5, column=0)
#     proteinas_cem_gramas_entry = tkinter.Entry(nutricional_frame)
#     proteinas_cem_gramas_entry.grid(row=5, column=1)  
#     proteinas_diario_entry = tkinter.Entry(nutricional_frame)
#     proteinas_diario_entry.grid(row=5, column=2)

#     gorduras_totais_label = tkinter.Label(nutricional_frame, text='Gorduras totais (g)')
#     gorduras_totais_label.grid(row=6, column=0)
#     gorduras_totais_cem_gramas_entry = tkinter.Entry(nutricional_frame)
#     gorduras_totais_cem_gramas_entry.grid(row=6, column=1)  
#     gorduras_totais_diario_entry = tkinter.Entry(nutricional_frame)
#     gorduras_totais_diario_entry.grid(row=6, column=2)

#     gorduras_saturadas_label = tkinter.Label(nutricional_frame, text='Gorduras saturadas (g)')
#     gorduras_saturadas_label.grid(row=7, column=0)
#     gorduras_saturadas_cem_gramas_entry = tkinter.Entry(nutricional_frame)
#     gorduras_saturadas_cem_gramas_entry.grid(row=7, column=1)  
#     gorduras_saturadas_diario_entry = tkinter.Entry(nutricional_frame)
#     gorduras_saturadas_diario_entry.grid(row=7, column=2)

#     gorduras_trans_label = tkinter.Label(nutricional_frame, text='Gorduras trans (g)')
#     gorduras_trans_label.grid(row=8, column=0)
#     gorduras_trans_cem_gramas_entry = tkinter.Entry(nutricional_frame)
#     gorduras_trans_cem_gramas_entry.grid(row=8, column=1)  
#     gorduras_trans_diario_entry = tkinter.Entry(nutricional_frame)
#     gorduras_trans_diario_entry.grid(row=8, column=2)

#     fibra_alimentar_label = tkinter.Label(nutricional_frame, text='Fibra alimentar (g)')
#     fibra_alimentar_label.grid(row=9, column=0)
#     fibra_alimentar_cem_gramas_entry = tkinter.Entry(nutricional_frame)
#     fibra_alimentar_cem_gramas_entry.grid(row=9, column=1)  
#     fibra_alimentar_diario_entry = tkinter.Entry(nutricional_frame)
#     fibra_alimentar_diario_entry.grid(row=9, column=2)

#     sodio_label = tkinter.Label(nutricional_frame, text='Sódio (mg)')
#     sodio_label.grid(row=10, column=0)
#     sodio_cem_gramas_entry = tkinter.Entry(nutricional_frame)
#     sodio_cem_gramas_entry.grid(row=10, column=1)  
#     sodio_diario_entry = tkinter.Entry(nutricional_frame)
#     sodio_diario_entry.grid(row=10, column=2)

#     porcao_embalagem_label = tkinter.Label(nutricional_frame, text='Porção por Embalagem')
#     porcao_embalagem_label.grid(row=11, column=0)
#     porcao_embalagem_entry = tkinter.Entry(nutricional_frame)
#     porcao_embalagem_entry.grid(row=11, column=1)
#     porcao = tkinter.Label(nutricional_frame, text='Porção')
#     porcao.grid(row=11, column=2)
#     porcao_entry = tkinter.Entry(nutricional_frame)
#     porcao_entry.grid(row=11, column=3)

#     campo_adicional_label = tkinter.Label(nutricional_frame, text='Campo adicional')
#     campo_adicional_label.grid(row=12, column=0)
#     campo_adicional_entry = tkinter.Entry(nutricional_frame)
#     campo_adicional_entry.grid(row=13, column=0)

#     # btn_salvar = ttk.Button('Salvar')
#     # btn_salvar.grid(row=14, column=2)

# def cadastro_empresa():
#     window.title('Cadastro Empresa')
#     frame = tkinter.Frame()
#     frame.pack()


# def cadastro_tipo():
#     window.title('Tipo de Carne')
#     frame = tkinter.Frame()
#     frame.pack()


# class CadastroTipo(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.criar_widgets()

#     def criar_widgets(self):
#         self.label = tk.Label(self, text="Tela Cadastro Tipo")
#         self.label.grid(row=0, column=0, pady=10)


#         self.botao_proximo_tela = ttk.Button(self, text="Proxima Tela",
#             command=self.abrir_proxima_tela)
        
#         self.botao_proximo_tela.grid(row=0, column=0, pady=20)

#     def abrir_proxima_tela(self):
#         self.master.master.master.mudar_tela(CadastroProduto)
        













# class TelaSecundaria(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.criar_widgets()

#     def criar_widgets(self):
#         self.label = tk.Label(self, text="Tela Secundária")
#         self.label.grid(row=0, column=0, pady=10)

#         self.botao_tela_anterior = ttk.Button(self, text="Tela Anterior", command=self.voltar_tela_anterior)
#         self.botao_tela_anterior.grid(row=0, column=0)

#     def voltar_tela_anterior(self):
#         self.master.master.master.mudar_tela(Home)

