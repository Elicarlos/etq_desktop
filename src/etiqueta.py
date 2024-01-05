from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def criar_tabela(pdf_path):
    c = canvas.Canvas(pdf_path, pagesize=letter)

    # Configurações de fonte
    c.setFont("Helvetica", 10)

    # Dados da tabela
    dados_tabela = [
        ["", " 100 g ", "% VD* "],      
        ["Valor energético (kcal)", "", ""],
        ["Carboidratos totais (g)", "", ""],
        ["Açúcares totais (g)", "", ""],
        ["Açúcares adicionados (g)", "", ""],
        ["Proteínas (g)", "", ""],
        ["Gorduras totais (g)", "", ""],
        ["Gorduras saturadas (g)", "", ""],
        ["Gorduras trans (g)", "", ""],
        ["Fibra alimentar (g)", "", ""],
        ["Sódio (mg)", "", ""]
    ]

    # Configurações da tabela
    largura_coluna_0 = 150  # Largura da coluna 0 ("")
    largura_coluna_1 = 60   # Largura da coluna 1 ("100 g")
    largura_coluna_2 = 60   # Largura da coluna 2 ("% VD*")
    altura_linha = 20
    altura_cabecalho = 30
    margem_esquerda = 50
    margem_inferior = 50

    # Desenhar contorno da tabela
    c.rect(margem_esquerda, margem_inferior, largura_coluna_0 + largura_coluna_1 + largura_coluna_2, altura_cabecalho + altura_linha * len(dados_tabela))

    # Desenhar linhas horizontais
    for i in range(len(dados_tabela) + 1):
        y = margem_inferior + i * altura_linha
        c.line(margem_esquerda, y, margem_esquerda + largura_coluna_0 + largura_coluna_1 + largura_coluna_2, y)

    # Desenhar linhas verticais
    c.line(margem_esquerda + largura_coluna_0, margem_inferior, margem_esquerda + largura_coluna_0, margem_inferior + altura_cabecalho + altura_linha * len(dados_tabela))
    c.line(margem_esquerda + largura_coluna_0 + largura_coluna_1, margem_inferior, margem_esquerda + largura_coluna_0 + largura_coluna_1, margem_inferior + altura_cabecalho + altura_linha * len(dados_tabela))

    # Preencher os dados na tabela
    for i, linha in enumerate(dados_tabela):
        for j, dado in enumerate(linha):
            if j == 0:
                largura_coluna = largura_coluna_0
            elif j == 1:
                largura_coluna = largura_coluna_1
            else:
                largura_coluna = largura_coluna_2

            x = margem_esquerda + sum((largura_coluna_0, largura_coluna_1, largura_coluna_2)[:j])
            y = margem_inferior + (len(dados_tabela) - i) * altura_linha
            c.drawString(x + 5, y - 15, dado)

    c.save()

# Exemplo de uso
pdf_path = "tabela_reportlab_modificada.pdf"
criar_tabela(pdf_path)
