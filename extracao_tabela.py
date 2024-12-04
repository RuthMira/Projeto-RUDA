import tabula

def obter_tabelas(ext : str, caminho_arquivo : str):
    if not ext or not caminho_arquivo: # False OU None
        return None

    if "PDF" in ext.upper():
        try:
            print('extraindo a tabela ...')
            tabelas = tabula.read_pdf(caminho_arquivo, pages='all')
            return tabelas
        except:
            print('caiu aqui na excecao')
            return None
    else:
        print ("arquivo não encontrado")
        return None


