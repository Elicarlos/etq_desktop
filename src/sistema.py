from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk 
from ttkbootstrap import ttk as ttkbs
# from ttkbootstrap.constants import *
from ttkbootstrap import Style


from telas.home import Home
from telas.cadastro_produto import CadastroProduto
# from telas.cadastro_tipo import CadastroTipo
from telas.cadastro_empresa import CadastroEmpresa


import os

class Sistema(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.title('Etiquetário')
        # self.geometry("400x300")
        self.tela_atual = None
        # self.window = window
        self.title('Etiqutário')
        self.geometry('1366x768')
        self.state('zoomed')
        self.config(background="#eff5f6")

        style = Style(theme="darkly")
        

       
        
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        largura_janela = 1366  # Substitua pelo valor desejado
        altura_janela = 768  # Substitua pelo valor desejado

        posicao_x = largura_tela // 2 - largura_janela // 2
        posicao_y = altura_tela // 2 - altura_janela // 2

        self.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")

        # Cria um diretorio 
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, '..', 'images', 'profile.png')

        self.home_image = Image.open(image_path)
        icon = ImageTk.PhotoImage(self.home_image)
        self.iconphoto(True, icon)

        self.header = ttk.Frame(self)
        self.header.place(x=300, y=0, width=1070, height=70)
        # self.logout_text = ttk.Button(self.header, text='Sair', style='TButton', 
        #     font=('', 13, 'bold'), bd=0, fg='white',
        #     cursor='hand2', activebackground="#32cf8e" )
        
        # self.logout_text.place(x=950, y=15)

        self.sidebar = tk.Frame(self, bg='#ffffff')
        self.sidebar.place(x=0, y=0, width=300, height=750)

           

        
        # logo
        # self.logoImage = Image.open('images\\profile.png')
        # photo = ImageTk.PhotoImage(self.logoImage)
        # self.logo = tk.Label(self.sidebar, image=photo, bg="#ffffff")
        # self.logo.image = photo
        # self.logo.place(x=70, y=80)

        # Name of Brand
        # self.brand_name = tk.Label(self.sidebar, text="Elicarlos Ferreira",
        #      bg="#ffffff",font=("", 15, "bold"))
        # self.brand_name.place(x=80, y=200)


        # Dashboard
        # self.dashboard_image = Image.open('images\\profile.png')
        # photo = ImageTk.PhotoImage(self.dashboard_image)
        # self.dashboard = tk.Label(self.sidebar, image=photo, bg="#ffffff")
        # self.dashboard.image = photo
        # self.dashboard.place(x=35, y=289)

       

        # self.dashboard_text = ttk.Button(self.sidebar, text="Dasboard", bg="#ffffff",
        #     font=("", 13, 'bold'), bd=0, cursor='hand2', activebackground="#ffffff")
        
        # self.dashboard_text.place(x=80, y=291)


        
        # style = ttk.Style()
        # style.configure('TButton', background='#ffffff')



        # self.manage_text =ttk.Button(self.sidebar, text='Manage', style='TButton',
        #     font=("", 13, 'bold'), bd=0, cursor='hand2', activeforeground="#ffffff")
        # self.manage_text.place(x=80, y=345 )

        # Home
        image_path1 = os.path.join(script_dir, '..', 'images', 'profile1.png')
        self.home_image = Image.open(image_path1)
        photo = ImageTk.PhotoImage(self.home_image)

        self.home_label = tk.Label(self.sidebar, image=photo, bg="#ffffff")
        self.home_label.image = photo
        self.home_label.place(x=35, y=80)

        self.btn_home = ttk.Button(self.sidebar, text='Home', command=lambda: self.mudar_tela(Home))
        self.btn_home.place(x=70, y=80)    
        

        # Cadastro de Produtos
        # image_path2 = os.path.join(script_dir, '..','images', 'produto.png')
        # self.cadastro_produto_image = Image.open(image_path2)
        # photo = ImageTk.PhotoImage(self.cadastro_produto_image, height=10, width=10)

        # self.cadastro_label = tk.Label(self.sidebar, image=photo, bg="#ffffff")
        # self.cadastro_label.image = photo
        # self.cadastro_label.place(x=35, y=120)
        
        self.btn_cadastro_produto = ttk.Button(self.sidebar, 
            text='Cadastro Produtos', command=lambda: self.mudar_tela(CadastroProduto))
        self.btn_cadastro_produto.place(x=70, y=120)


        # Cadastro de Empresas
        # image_empresa = os.path.join(script_dir, '..', 'images', 'empresa.png')
        # self.cadastro_empresa_image = Image.open(image_empresa)
        # photo = ImageTk.PhotoImage(self.cadastro_empresa_image, height=10, width=10)

        # self.empresa_label = tk.Label(self.sidebar, image=photo, bg="#ffffff")
        # self.empresa_label.image = photo
        # self.empresa_label.place(x=35, y=160)

        
        self.btn_cadastro_empresa = ttk.Button(self.sidebar, 
            text='Cadastro Empresa', command=lambda: self.mudar_tela(CadastroEmpresa))
        self.btn_cadastro_empresa.place(x=70, y=160)


        # self.settings_text = ttk.Button(self.sidebar, text="Settings", 
        #                             font=('', 13, 'bold'),style='TButton',
        #     cursor="hand2",bd=0, activebackground='#ffffff')
        
        # self.settings_text.place(x=80, y=402)


        # exit
        # self.exit_image = Image.open('images\\profile.png')
        # photo = ImageTk.PhotoImage(self.exit_image)
        # self.exit = tk.Label(self.sidebar, image=photo, bg="#ffffff")
        # self.exit.image = photo
        # self.exit.place(x=25, y=452)

        # self.exit_text = ttk.Button(self.sidebar, text="Settings", 
        #                             font=('', 13, 'bold'),style='TButton',
        #     cursor="hand2",bd=0, activebackground='#ffffff')
        
        # self.settings_text.place(x=85, y=462)



        self.heading = tk.Label(self, text="Dasboard", 
            font=('', 13, 'bold'),
            fg="#0064d3", bg="#eff5f6")
        
        self.heading.place(x=325, y=70)

        
        # Meus frames devem redenrizar aqui
        self.bodyframe1 = tk.Frame(self, bg="#FF0000")
        self.bodyframe1.place(x=328, y=110, width=1060, height=540)

        self.background_frame = tk.Frame(self, bg="#CCCCCC")
        self.background_frame.place(x=328, y=110, width=1060, height=540)

        self.central_frame = tk.Frame(self.background_frame)
        self.central_frame.pack(expand=True, fill='both')

        

        self.frames = {}

        self.frames[Home] = Home(self.central_frame)
        self.frames[CadastroEmpresa] = CadastroEmpresa(self.central_frame)
        self.frames[CadastroProduto] = CadastroProduto(self.central_frame)
        # self.frames[TelaSecundaria] = TelaSecundaria(self.central_frame)

        # Inicialize a tela inicial
        self.mostrar_tela(Home)

    def mostrar_tela(self, tela):
        frame = self.frames[tela]
        if self.tela_atual:
            self.tela_atual.destroy()

        self.tela_atual = frame
        self.tela_atual.pack(expand=True, fill='both')

    def mudar_tela(self, tela_classe):
        nova_tela = tela_classe(self.central_frame)
        if self.tela_atual:
            self.tela_atual.destroy()

        self.tela_atual = nova_tela
        self.tela_atual.pack(expand=True, fill='both')

        # Chame o método para criar a interface da nova tela
        self.tela_atual.criar_widgets()

    # def mostrar_tela(self, tela):
    #     frame = self.frames[tela]
    #     if self.tela_atual:
    #         self.tela_atual.destroy()

    #     self.tela_atual = frame
    #     self.tela_atual.pack(expand=True, fill='both')




    #     self.mudar_tela(Home)

    # def mudar_tela(self, tela_classe):
    #     nova_tela = tela_classe(self.central_frame)
    #     if self.tela_atual:
    #         self.tela_atual.destroy()
        
    #     self.tela_atual = nova_tela
    #     self.tela_atual.pack(expand=True, fill='both')


       
if __name__ == "__main__":
    app = Sistema()
    app.mainloop()