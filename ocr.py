import pytesseract
import pdf2image

def obter_ocr(ext : str, caminho_arquivo : str) -> str:
    print('entrou no ocr geral')
    if not ext or not caminho_arquivo: # False OU None
        print('false or null')
        return ''

    if "PDF" in ext.upper():
        print('entrou no ocr do pdf')
        imagens = pdf2image.convert_from_path(caminho_arquivo)

        texto_completo = ''
        for numero_pagina, pagina in enumerate(imagens):
            texto = pytesseract.image_to_string(image=pagina,lang='por')
            texto_completo += texto
            # print(f'> página {numero_pagina}:')
            # print(texto)
    elif "TIF" in ext.upper():
        texto_completo = pytesseract.image_to_string(caminho_arquivo,'por')
    else:
        print ("arquivo não encontrado")
    return texto_completo