import ocr
from PIL import Image
import pytesseract
import pdf2image
import os

# caminho_arquivo = "/workspaces/Projeto-RUDA/imagens/formal_partilha/00665735_editado.pdf"
# # dicionario_resultado = ocr.obter_ocr_paginado("PDF",caminho_arquivo)
# # print(dicionario_resultado)

# #Convertendo TIF em PDF
# tif_path = "imagens/formal_partilha/00665493.tif"
# img = Image.open(tif_path)
# pdf_path ="imagens/temp.pdf"
# img.save(pdf_path, save_all=True, append_imagens=[img])
# img.close()

# # Função para extrair informações usando OCR
# def extract_info_from_pdf(caminho_arquivo):
#     print('entrou no ocr do pdf')
#     imagens = pdf2image.convert_from_path(caminho_arquivo)
#     resultado = {}
#     for numero_pagina, pagina in enumerate(imagens):
#         texto = pytesseract.image_to_string(image=pagina,lang='por')
#         resultado[numero_pagina] = texto
#         print(resultado)
#     return resultado

# # Chama a função para extrair informações do PDF
# #result_dict = extract_info_from_pdf(pdf_path)

# # Exibe ou manipula o dicionário de resultados conforme necessário
# # print(result_dict)


#  Função para recortar bordas de um TIF e salvar em um novo arquivo
def recortar_bordas_salvar(input_path, output_path, margem):
    # Abre o arquivo TIF de várias páginas
    imagem_multipage = Image.open(input_path)

    # Cria uma lista para armazenar as páginas recortadas
    paginas_recortadas = []

    # Itera sobre todas as páginas
    for pagina_numero in range(imagem_multipage.n_frames):
        # Seleciona a página atual
        imagem_multipage.seek(pagina_numero)

        # Obtém as dimensões da página
        largura, altura = imagem_multipage.size

        # Calcula as coordenadas de recorte invertidas para manter apenas as bordas
        esquerda = 0
        superior = 0
        direita = largura
        inferior = altura

        # Subtrai a margem para manter apenas as bordas
        esquerda += margem
        superior += margem
        direita -= margem
        inferior -= margem

        # Recorta a imagem invertendo a lógica para manter apenas as bordas
        imagem_recortada = imagem_multipage.crop((esquerda, superior, direita, inferior))

        # Adiciona a página recortada à lista
        paginas_recortadas.append(imagem_recortada)

    # Salva as páginas recortadas como um arquivo multipage
    paginas_recortadas[0].save(output_path, save_all=True, append_images=paginas_recortadas[1:])

# Testando para um arquivo
input_path = '/workspaces/Projeto-RUDA/imagens/formal_partilha/00665493.tif'
output_path = '/workspaces/Projeto-RUDA/imagens'
margem = 50  # Ajuste 

recortar_bordas_salvar(input_path, output_path, margem)