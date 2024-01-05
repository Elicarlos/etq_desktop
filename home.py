import tkinter as tk
from ttkbootstrap import ttk, Style

def fazer_algo():
    # Adicione a lógica necessária para a opção do menu
    print("Fazendo algo...")

def realizar_pesquisa():
    termo_pesquisa = campo_pesquisa.get()
    # Adicione a lógica necessária para a pesquisa
    print(f"Realizando pesquisa: {termo_pesquisa}")

def cadastrar_produto_popup(nome, preco, popup):
    # Adicione a lógica necessária para cadastrar o produto com as informações fornecidas
    print(f"Cadastrando Produto - Nome: {nome}, Preço: {preco}")
    popup.destroy()

def abrir_popup_cadastro_produto():
    # Criar um popup de cadastro para produto
    popup = tk.Toplevel(janela)
    popup.title("Cadastro de Produto")

    # Adicionar campos de entrada (Entry) e rótulos (Label)
    tk.Label(popup, text="Nome do Produto:").grid(row=0, column=0, padx=10, pady=5)
    nome_produto = tk.Entry(popup)
    nome_produto.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(popup, text="Preço:").grid(row=1, column=0, padx=10, pady=5)
    preco_produto = tk.Entry(popup)
    preco_produto.grid(row=1, column=1, padx=10, pady=5)

    # Botão para confirmar o cadastro
    btn_confirmar = ttk.Button(popup, text="Confirmar", command=lambda: cadastrar_produto_popup(nome_produto.get(), preco_produto.get(), popup))
    btn_confirmar.grid(row=2, column=0, columnspan=2, pady=10)


def fechar_janela():
    janela.destroy()



# Criar a janela principal
janela = tk.Tk()
janela.title('Home')

# Barra de menus
barra_menu = tk.Menu(janela)
janela.config(menu=barra_menu)

# Menu Cadastro
menu_cadastro = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Cadastro", menu=menu_cadastro)

menu_cadastro.add_command(label="Empresa", command=abrir_popup_cadastro_produto)
menu_cadastro.add_command(label="Cadastro Produto", command=abrir_popup_cadastro_produto)
 
# Adicionando a opção "Sair" ao menu Cadastro
menu_cadastro.add_separator()
menu_cadastro.add_command(label="Sair", command=fechar_janela)

# Configuração da janela
largura_janela = 600
altura_janela = 450

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

x_pos = (largura_tela - largura_janela) // 2
y_pos = (altura_tela - altura_janela) // 2

janela.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

# Estilo do ttkbootstrap
style = Style()
style.theme_use('cosmo')

# Frame central
frame_central = ttk.Frame(janela)
frame_central.pack(expand=True)

# Campo de pesquisa
campo_pesquisa = ttk.Entry(frame_central, width=80)
campo_pesquisa.grid(row=0, column=0, padx=10, pady=10)

# Botão de pesquisa
btn_pesquisa = ttk.Button(frame_central, text='Buscar', command=realizar_pesquisa)
btn_pesquisa.grid(row=0, column=1, padx=10, pady=10)

# Iniciar o loop principal da interface gráfica
janela.mainloop()
