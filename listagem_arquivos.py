import os
import glob

#Funçao responsável por verificar se o arquivo foi modificado e sinlaiza se precisa ser processado novamente.
def verificar_arquivo_nao_processado(arquivos_processados : dict, caminho_arquivo : str):
    if caminho_arquivo in arquivos_processados.keys():
        datahora_ultima_modificacao = arquivos_processados[caminho_arquivo]
        if os.path.getmtime(caminho_arquivo) == datahora_ultima_modificacao:
            print("o arquivo já foi inserido, porém não foi modificado.")
            return False # o arquivo será processado novamente
        else:
            print("o arquivo já foi inserido e modificado.")
    return True

#Função responsável por listar os arquivos dos diretórios de forma recursiva.
def listar_arquivos_recursivamente(diretorio : str, ext : str) -> [str]:
    caminhos_arquivos_encontrados = glob.glob(diretorio + f'/**/*.{ext}', recursive=True)
    # remover para produção print / deixar como documentação
    for indice, caminho_arquivo in enumerate(caminhos_arquivos_encontrados):
        print(f'{indice} -> caminho do arquivo: {caminho_arquivo}')
    return caminhos_arquivos_encontrados