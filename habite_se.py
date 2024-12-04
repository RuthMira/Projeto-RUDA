import re

def extrair_chave(texto):
    # regex = r'(?<=Chave para validação: )(?P<chave>\w+.\w+.\w+'
    regex = r'(?<=Chave para validação: )(\w+.)+'
    resultado = re.search(regex, texto)
    # print(resultado.group())
    return resultado.group()

def extrair_emissao(texto):
    regex = r'(?<=Documento emitido via internet em )(\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2})'
    resultado = re.search(regex, texto)
    # print(resultado.group())
    return resultado.group()

def extrair_dados(texto):
    return {
        "chave para validação":extrair_chave(texto),
        "Documento emitido via internet em": extrair_emissao(texto)
    }
