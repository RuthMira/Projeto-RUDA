import re
import os
import pytesseract

# para executar o pytesseract é necessário instalar o tesseract na máquina local.

# no linux, use o comando: 
# sudo apt-get install tesseract-ocr -y && apt-get install libtesseract-dev -y

# no windows, siga o passo-a-passo disponível em: 
# https://stackoverflow.com/questions/46140485/tesseract-installation-in-windows

# caso não funcione após a instalação, 
# adicione C:\Program Files\Tesseract-OCR\tesseract.exe no PATH das variáveis de ambiente do windows.

caminho_modulo = os.path.dirname(__file__)
print(caminho_modulo)

nome_arquivo = "00750024.PDF"
print(nome_arquivo)

caminho_arquivo = caminho_modulo + "\\imagens\\CND_INSS_OBRA\\" + nome_arquivo
print(caminho_arquivo)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

txt = pytesseract.image_to_string(caminho_arquivo,'por')
print(txt)

# Para o habite-se

# regex = r'(?<=Chave para validação: )(?P<chave>\w{5}.\w{5}.\w{5}.)'
# resultado = re.search(regex, txt)
# print(resultado.group('chave'))

# regex = r'(?<=Chave para validação: )\w+.\w+.\w+.'
# regex = r'(?<=Chave para validação: )(\w+.)+'
# resultado = re.search(regex, txt)
# print(resultado.group())

# regex = r'(?<=Documento emitido via internet em )(\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2})'
# resultado = re.search(regex, txt)
# print(resultado.group())

# regex = r' '
# resultado = re.split(regex, txt)
# print(resultado)

# Certidão Negativa de débitos

regex = r'(?<=Aferição: )(?p<chave>\d+.\d+.\d+/\d+-\d+)'
resultado = re.search(regex,txt)
print(resultado.group())

regex = r'(?<=SP, )\d+-\d+'
resultado = re.search(regex,txt)
print(resultado.group())

regex = r'(?<=Emitida às  )(\d+:\d+:\d+)'
resultado = re.search(regex, txt)
print(resultado.group())

regex = r'(?<=Emitida às )(\d+:\d+:\d+)(?<=do dia )(\d+/\d+/\d+)'
resultado = re.serach(regex, txt)

print(resultado.group())

# regex = r'^Endereço: ([\w\sáéíóúãõâêôàèìòùäëïöüçÁÉÍÓÚÃÕÂÊÔÀÈÌÒÙÄËÏÖÜÇ,.-]+)$'



def extrair_endereco(texto):
    # print("estou aqui!")
    regex = r'(?<=Endereço:)[0-9A-Za-z ,./sáéíóúãõâêôàèìòùäëïöüçÁÉÍÓÚÃÕÂÊÔÀÈÌÒÙÄËÏÖÜÇ-]+'
    # regex = r'^Endereço: (.+)$'
    resultado = re.search(regex,texto)
    print(resultado)
    print(resultado.group())
    return None

texto='Endereço:  RUA RUA OLIVIO AUGUSTO DO AMARAL 141, 141, casa, RES. VISTA LINDA, SÃO JOSÉ DOS CAMPOS/SP, 12220-057' 
extrair_endereco(texto)


#Condição. agendamento, manipulação 
# from rocketry.conds import crontime

# #Função para recortar bordas de um TIF e salvar em um novo arquivo
# def recortar_bordas_salvar(input_path, output_path, margem):
#     # Abre o arquivo TIF de várias páginas
#     imagem_multipage = Image.open(input_path)

#     # Cria uma lista para armazenar as páginas recortadas
#     paginas_recortadas = []

#     # Itera sobre todas as páginas
#     for pagina_numero in range(imagem_multipage.n_frames):
#         # Seleciona a página atual
#         imagem_multipage.seek(pagina_numero)

#         # Obtém as dimensões da página
#         largura, altura = imagem_multipage.size

#         # Calcula as coordenadas de recorte invertidas para manter apenas as bordas
#         esquerda = 0
#         superior = 0
#         direita = largura
#         inferior = altura

#         # Subtrai a margem para manter apenas as bordas
#         esquerda += margem
#         superior += margem
#         direita -= margem
#         inferior -= margem

#         # Recorta a imagem invertendo a lógica para manter apenas as bordas
#         imagem_recortada = imagem_multipage.crop((esquerda, superior, direita, inferior))

#         # Adiciona a página recortada à lista
#         paginas_recortadas.append(imagem_recortada)

#     # Salva as páginas recortadas como um arquivo multipage
#     paginas_recortadas[0].save(output_path, save_all=True, append_images=paginas_recortadas[1:])

# # Testando para um arquivo
# input_path = '/workspaces/Projeto-RUDA/imagens/formal_partilha/00665493.tif'
# output_path = '/workspaces/Projeto-RUDA/imagens'
# margem = 10  # Ajuste 

# recortar_bordas_salvar(input_path, output_path, margem)
