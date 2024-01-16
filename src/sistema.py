from PIL import Image, ImageTk
import tkinter as tk
from ttkbootstrap import ttk as bt
from ttkbootstrap import Style
import os

from telas.home import Home
from telas.cadastro_produto import CadastroProduto
from telas.cadastro_empresa import CadastroEmpresa
from telas.edite_produto import EditeProduto
from telas.edite_tipo import EditeTipo
from telas.edite_temperatura import EditeTemperatura
from controllers import TkinterController


class Sistema(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Etiquetário')
        self.state('zoomed')
        style = Style(theme="litera")
        self.config(background="#F0F1F6")

        self.tela_atual = None
        self.controller = TkinterController

        self.setup_geometry()

        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, '..', 'images', 'profile.png')
        self.setup_icon(image_path)

        self.setup_header()
        self.setup_sidebar()
        self.setup_footer()

        self.central_frame = bt.Frame(self, bootstyle="dark")
        self.central_frame.pack(side='left', expand=True, fill='both', padx=10, pady=10)  # Ajuste o tamanho conforme necessário

        self.frames = {
            Home: Home(self.central_frame),
            CadastroEmpresa: CadastroEmpresa(self.central_frame),
            CadastroProduto: CadastroProduto(self.central_frame),
            EditeProduto: EditeProduto(self.central_frame),
            EditeTipo: EditeTipo(self.central_frame),
            EditeTemperatura: EditeTemperatura(self.central_frame)
        }

        self.mostrar_tela(Home)

    def setup_geometry(self):
        largura_janela = 1366
        altura_janela = 768

        self.geometry(f"{largura_janela}x{altura_janela}+0+0")

    def setup_icon(self, image_path):
        home_image = Image.open(image_path)
        icon = ImageTk.PhotoImage(home_image)
        self.iconphoto(True, icon)

    def setup_header(self):
        header = bt.Frame(self)
        header.pack(side='top', fill='x')

        # Adicione elementos ao header conforme necessário
        label_header = tk.Label(header, text="Header", font=("", 15, "bold"))
        
        label_header.pack(pady=10)

    def setup_sidebar(self):
        sidebar = bt.Frame(self, bootstyle="dark")
        sidebar.pack(side='left', fill='y')

        brand_name = tk.Label(sidebar, text="Elicarlos Ferreira", bg="#ffffff", font=("", 15, "bold"))
        brand_name.pack(pady=10)

        # Adicione outros elementos da sidebar conforme necessário
        btn_home = bt.Button(sidebar, text='Home', bootstyle="darky", command=lambda: self.mostrar_tela(Home))
        btn_home.pack(pady=10)

        btn_cadastro_produto = bt.Button(sidebar, bootstyle="darky", text='Produtos', command=lambda: self.mostrar_tela(EditeProduto))
        btn_cadastro_produto.pack(pady=10)

        btn_cadastro_empresa = bt.Button(sidebar, bootstyle="darky", text='Tipo', command=lambda: self.mostrar_tela(EditeTipo))
        btn_cadastro_empresa.pack(pady=10)

        btn_cadastro_temperatura = bt.Button(sidebar, bootstyle="darky", text='Temperatura', command=lambda: self.mostrar_tela(EditeTemperatura))
        btn_cadastro_temperatura.pack(pady=10)

        btn_cadastro_empresa = bt.Button(sidebar, bootstyle="darky", text='Cadastro Empresa', command=lambda: self.mostrar_tela(CadastroEmpresa))
        btn_cadastro_empresa.pack(pady=10)

    def setup_footer(self):
        footer = bt.Frame(self)
        footer.pack(side='bottom', fill='x')

        # Adicione elementos ao footer conforme necessário
        # empresa = self.controller
        label_footer = tk.Label(footer, text="Footer", font=("", 15, "bold"))
        label_footer = tk.Label(footer, text=f"2023 © Cajuina Code     v1.0     Cliente:    Licença de Uso     Política de Privacidade")
        label_footer.pack(pady=10)

    def mostrar_tela(self, tela):
        frame = self.frames[tela]
        if self.tela_atual:
            self.tela_atual.pack_forget()  # Use pack_forget para esconder, não destruir
        self.tela_atual = frame
        self.tela_atual.pack(side='left', expand=True, fill='both')


if __name__ == "__main__":
    app = Sistema()
    app.mainloop()
