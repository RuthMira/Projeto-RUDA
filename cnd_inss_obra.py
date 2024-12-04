import re

def extrair_afericao(texto):
    try:
        regex = r'(?<=Aferição: )(?P<chave>\d+.\d+.\d+/\d+-\d+)'
        resultado = re.search(regex,texto)
        # print(resultado.group())
        return resultado.group()
    except:
        return ''

def extrair_cep(texto):
    try:
        regex = r'(?<=SP, )\d+-\d+'
        resultado = re.search(regex,texto)
        # print(resultado.group())
        return resultado.group()
    except:
        return ''

def extrair_endereco(texto):
    try:
        #regex = r'(?<=Endereço:)[0-9A-Za-z ,./sáéíóúãõâêôàèìòùäëïöüçÁÉÍÓÚÃÕÂÊÔÀÈÌÒÙÄËÏÖÜÇ-]+'
        #regex = r'Endereço: (.+)$'
        regex = r'(?<=Endereço: )([^\n]+(?:\n[^\n]+)?)(\d+-)(\d+)'
        resultado = re.search(regex,texto)
        # print(resultado.group())
        return resultado.group()
    except:
        return ''
    
def extrair_hora(texto):
    try:
        regex = r'(?<=Emitida às )\d+:\d+:\d+'
        resultado = re.search(regex,texto)
        # print (resultado.group())
        return resultado.group()
    except:
        return ''
    
def extrair_emissão(texto):
    try:
        regex = r'(?<=Emitida às )(\d+:)+(\w+ )+(\d+/)+(\w+ )+'
        resultado = re.search(regex,texto)
        # print (resultado.group())
        return resultado.group()
    except:
        return ''
    
def extrair_validade(texto):
    try:
        regex = r'(?<=Válida até )\d+/\d+/\d+'
        resultado = re.search(regex,texto)
        # print (resultado.group())
        return resultado.group()
    except:
        return ''
    
def extrair_categoria(tabelas):
    try:
        tabela = tabelas[0] # retorna uma tabela dado sua posição no vetor
        #print(tabela)
        # tabela_filtrada = tabela.loc[:,["Categoria","Unnamed: 0","Unnamed: 1"]]
        # print(tabela_filtrada)
        # saida["descricao"] = tabela.iat[0,1]
        # saida["area"] = tabela.iat[0,4]
        resultado = tabela.iat[0,0] # [o,x] é a linha, [x,o] é a coluna
        # print(resultado)
        return resultado
    except:
        return ''

def extrair_destinação(tabelas):
    try:
        tabela = tabelas[0] # retorna uma tabela dado sua posição no vetor
        resultado = tabela.iat[0,1]
        # print(resultado)
        return resultado
    except:
        return ''

def extrair_area(tabelas):
    try:
        tabela = tabelas[0] # retorna uma tabela dado sua posição no vetor
        resultado = tabela.iat[0,4]
        # print(resultado)
        return resultado
    except:
        return ''

def extrair_dados(texto, tabelas):
    try:
        resultado = {
            "afericao":extrair_afericao(texto),
            "cep": extrair_cep(texto),
            "endereco": extrair_endereco(texto),
            "hora": extrair_hora(texto),
            "emissão": extrair_emissão(texto),
            "validade": extrair_validade(texto),
            "categoria":extrair_categoria(tabelas),
            "destinação": extrair_destinação(tabelas),
            "area": extrair_area(tabelas)
        }
        return resultado
    except:
        return None