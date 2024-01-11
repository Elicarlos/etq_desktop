import tkinter as tk
from tkinter import ttk
from controllers import TkinterController
import os
from PIL import Image, ImageTk

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, '..', 'images', 'profile.png')
class EditeProduto(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.controller = TkinterController()
        self.criar_widgets()
        self.adicionar_dados()

    def criar_widgets(self):
        

        buscar_produtos = ttk.Entry(self, width=80)
        buscar_produtos.place(x=0, y=130)

        btn_buscar_produto = ttk.Button(self, text="Buscar")
        btn_buscar_produto.place(x=430, y=130)

        btn_adicionar_produto = ttk.Button(self, text="Adicionar Produto", command=self.adicionar_dados)
        btn_adicionar_produto.place(x=530, y=130)

        # Verificar se o Treeview já foi criado
        if not hasattr(self, 'tree'):
            self.tree = ttk.Treeview(self, columns=("Corte", "Tipo", "Fibra"), show="headings")

            # Configurar cabeçalhos
            self.tree.heading("Corte", text="Corte")
            self.tree.heading("Tipo", text="Tipo")
            self.tree.heading("Fibra", text="Fibra")

            # Configurar largura das colunas
            self.tree.column("Corte", width=200)
            self.tree.column("Tipo", width=100)
            self.tree.column("Fibra", width=200)

            # Adicionar Treeview à janela
            self.tree.place(x=0, y=230)

    def adicionar_dados(self):
        dados = self.controller.obter_itens_nutricionais()

        for item in self.tree.get_children():
            self.tree.delete(item)

        # Adicionar dados à Treeview
        for dado in dados:
            corte = dado.get('corte', '')
            tipo = dado.get('tipo', '')
            fibra_alimentar_100g = dado.get('fibra_alimentar_100g', '')
            self.tree.insert("", tk.END, values=(corte, tipo, fibra_alimentar_100g))
        
         # Configurar ícones para tags 'editar' e 'deletar'
        self.tree.tag_configure('editar', image=self.obter_icone_editar())
        self.tree.tag_configure('deletar', image=self.obter_icone_deletar())

    def obter_icone_editar(self):
        # Substitua 'caminho_para_icone_editar.png' pelo caminho do seu ícone de editar
        # Certifique-se de ter o arquivo de imagem no mesmo diretório do seu script ou forneça o caminho completo
        editar = os.path.join(script_dir, '..','..','images', 'editar.png')
        self.editar_image = Image.open(editar)
        photo = ImageTk.PhotoImage(self.editar_image, height=10, width=10)
        return photo

    def obter_icone_deletar(self):
        # Substitua 'caminho_para_icone_deletar.png' pelo caminho do seu ícone de deletar
        # Certifique-se de ter o arquivo de imagem no mesmo diretório do seu script ou forneça o caminho completo
        deletar = os.path.join(script_dir, '..','..','images', 'deletar.png')
        self.deletar_image = Image.open(deletar)
        photo = ImageTk.PhotoImage(self.deletar_image, height=10, width=10)
        return photo
