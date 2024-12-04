import re

def extrair_processo(texto):
    try:
        regex = r'(?<=processo: )(\d+-\d+.)'
        resultado = re.search(regex,texto)
        # print(resultado.group())
        return resultado.group()
    except:
        return ''