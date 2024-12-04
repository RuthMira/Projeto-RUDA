import rocketry
import sys
import json
import listagem_arquivos
import cnd_inss_obra
import habite_se
import ocr
import extracao_tabela
import os

# parametriza o agendamento / define intervalo entre duas execuções da função
timer = sys.argv[2]

#Função responsável por processar todos os arquivos. 
#recebe da f()= verificar_arquivo _nao_processado os arquivos que precisam ser processados novamente
#Função responsável por salvar as informações dos arquivos em um JSON
def processar(arquivos_encontrados : list, caminho_arquivos_processados : str, tipo_arquivo : str, diretorio_resultado : str):
    print('>> carregando arquivos processados...')
    arquivo = open(caminho_arquivos_processados,"r")
    arquivos_processados = json.load(arquivo)
    print(arquivos_processados)
    print('>> carregamento finalizado.')
    # vamos checar os arquivos encontrados
    for _, caminho_arquivo in enumerate(arquivos_encontrados):
        precisa_processar = listagem_arquivos.verificar_arquivo_nao_processado(arquivos_processados, caminho_arquivo=caminho_arquivo) # a passagem de valor para a função pode ocorrer de duas formas
        if precisa_processar:
            print(f'>>>> processando arquivo: {caminho_arquivo} ...') # substituir pela extração e gravação do resultado
            _, ext = os.path.splitext(caminho_arquivo)
            nome_arquivo = os.path.basename(caminho_arquivo)
            dados_extraidos = extrair_dados(tipo_arquivo, ext, caminho_arquivo)
            salvar_dados_extraidos(dados_extraidos, diretorio_resultado + '/' + nome_arquivo + '.json')
            arquivos_processados[caminho_arquivo] = os.path.getmtime(caminho_arquivo)
        else:
            print(f'>>>> o arquivo não foi reprocessado: {caminho_arquivo} ...') # substituir pela extração e gravação do resultado
    print(arquivos_processados)
    print('>> salvando arquivos processados...')
    arquivo = open(caminho_arquivos_processados, 'w')
    json.dump(arquivos_processados, arquivo, indent=4)
    print('>> gravação concluída.')

# Extração de dados dos módulos (no caso, CND INSS Obra e Habite-se). Mas poderíamos incluir aqui outros módulos de modelos de documentos para extração de dados.
def extrair_dados(tipo_arquivo, ext, caminho_arquivo):
    texto = ocr.obter_ocr(ext, caminho_arquivo)
    tabelas = extracao_tabela.obter_tabelas(ext, caminho_arquivo)
    if 'CND_INSS_OBRA' == tipo_arquivo:
        # substituir por chamada para a função do módulo de extração
        dados_extraidos = cnd_inss_obra.extrair_dados(texto, tabelas)
        print(dados_extraidos)
    elif 'HABITE-SE' == tipo_arquivo:
        # substituir por chamada para a função do módulo de extração
        dados_extraidos = habite_se.extrair_dados(texto, tabelas)
    return dados_extraidos

# depois iremos modificar essa função para salvar no banco de dados.
def salvar_dados_extraidos(dados_extraidos, caminho_destino):
    if dados_extraidos:
        print(caminho_destino) 
        f = open(caminho_destino, 'w')
        print(f)
        print(dados_extraidos)
        json.dump(dados_extraidos, f, indent=4)
    else:
        print('>> não foi possível extrair dados do arquivo.')

# Rocketry é uma estrutura de agendamento baseada em declarações para Python. É possível ajustar a sessão de tempo do agendador de tarefas.   
app = rocketry.Rocketry()

# vide a documentação do rocketry 
# https://pypi.org/project/rocketry/
# https://rocketry.readthedocs.io/en/stable/
@app.task(f'every {timer} sec')
def executar_tarefa_agendada():
    print('\n> início da tarefa.')
    tipo_arquivo = sys.argv[1]
    diretorio_monitorado = "/workspaces/Projeto-RUDA/pasta-monitorada"
    diretorio_resultado = "/workspaces/Projeto-RUDA/resultado"
    caminho_arquivos_processados = diretorio_resultado + "/arquivos_processados.json"
    print('>> listando arquivos da pasta monitorada')
#    Para evitar que strings, dos tipos de extensão, sofram influência quando em uppercase ou lowercase, consideramos ambos os caso. Por exemplo, PDF e pdf.
    arquivos_encontrados_pdf = listagem_arquivos.listar_arquivos_recursivamente(diretorio_monitorado, 'pdf')
    arquivos_encontrados_PDF = listagem_arquivos.listar_arquivos_recursivamente(diretorio_monitorado, 'PDF')
    arquivos_encontrados_tif = listagem_arquivos.listar_arquivos_recursivamente(diretorio_monitorado, 'tif')
    arquivos_encontrados_TIF = listagem_arquivos.listar_arquivos_recursivamente(diretorio_monitorado, 'TIF')
    arquivos_encontrados = []
    arquivos_encontrados.extend(arquivos_encontrados_pdf)
    arquivos_encontrados.extend(arquivos_encontrados_PDF)
    arquivos_encontrados.extend(arquivos_encontrados_tif)
    arquivos_encontrados.extend(arquivos_encontrados_TIF)
    print(arquivos_encontrados)
    print('>> iniciando o processamento...')
    processar(arquivos_encontrados, caminho_arquivos_processados, tipo_arquivo, diretorio_resultado)
    print('\n> fim da tarefa.')
    
app.run()