import os
import tkinter as tk
from tkinter import ttk, messagebox
from  . cadastro_produto import CadastroProduto
from controllers import TkinterController



class EditeProduto(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.controller = TkinterController()
        self.criar_widgets()
        self.adicionar_dados()

    def criar_widgets(self):
        self.script_dir = os.path.dirname(os.path.abspath(__file__))

        buscar_produtos = ttk.Entry(self, width=80)
        buscar_produtos.place(x=0, y=130)

        btn_buscar_produto = ttk.Button(self, text="Buscar")
        btn_buscar_produto.place(x=430, y=130)

        btn_adicionar_produto = ttk.Button(self, text="Adicionar Produto", command=self.adicionar_produtos)
        btn_adicionar_produto.place(x=530, y=130)

        if not hasattr(self, 'tree'):
            self.tree = ttk.Treeview(self, columns=("Corte", "Tipo", "Fibra", "Ação"), show="headings")

            self.tree.heading("Corte", text="Corte")
            self.tree.heading("Tipo", text="Tipo")
            self.tree.heading("Fibra", text="Fibra")
            self.tree.heading("Ação", text="Ação")

            self.tree.column("Corte", width=200)
            self.tree.column("Tipo", width=100)
            self.tree.column("Fibra", width=200)
            self.tree.column("Ação", width=50)  # Ajuste a largura conforme necessário

            self.tree.place(x=0, y=230)

        # Adicionando atributos para armazenar referências às imagens
        self.editar_icon = None

        # Configurar evento de clique na coluna de Ação
        self.tree.bind('<ButtonRelease-1>', self.on_tree_click)

    def adicionar_dados(self):
        dados = self.controller.obter_itens_nutricionais()

        for item in self.tree.get_children():
            self.tree.delete(item)

        for dado in dados:
            corte = dado.get('corte', '')
            tipo = dado.get('tipo', '')
            fibra_alimentar_100g = dado.get('fibra_alimentar_100g', '')

            # Adicionar dados à Treeview, incluindo a coluna de ícones
            item = self.tree.insert("", tk.END, values=(corte, tipo, fibra_alimentar_100g, "Editar"))
            
            # Adicionar tags para os botões
            self.tree.tag_configure('editar', background='lightblue')

    def on_tree_click(self, event):
        item_id = self.tree.identify_row(event.y)
        col_id = self.tree.identify_column(event.x)

        if item_id and col_id == '#4':  # Coluna "Ação"
            acao = self.tree.item(item_id, 'values')[3]

            if acao == "Editar":
                # Obtenha os dados do produto selecionado
                produto_data = self.tree.item(item_id, 'values')
                
                # Recupere o ID do produto do banco de dados (supondo que a posição 0 seja o ID)
                produto_id = produto_data[0]

                # Recupere os dados do produto do banco de dados usando o ID
                dados_do_banco = self.controller.obter_dados_do_produto_por_id(produto_id)

                # Crie uma instância do CadastroProduto passando o Toplevel como mestre e os dados do produto
                cadastro_produto_popup = tk.Toplevel(self.master)
                cadastro_produto_popup.title("Editar Produto")

                # Chame o método para inicializar os campos com os dados do produto
                cadastro_produto_frame = CadastroProduto(cadastro_produto_popup, dados_produto=dados_do_banco)
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
                self.adicionar_dados()


    def adicionar_produtos(self):
        try:
            cadastro_produto_popup = tk.Toplevel(self.master)
            cadastro_produto_popup.title("Cadastro de Produto")

            # Crie uma instância do CadastroProduto passando o Toplevel como mestre
            cadastro_produto_frame = CadastroProduto(cadastro_produto_popup)
            cadastro_produto_frame.pack(expand=True, fill="both")  # Adicione o frame à janela

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
            self.adicionar_dados()

        except Exception as e:
            print(f"Erro ao abrir o popup: {e}")
