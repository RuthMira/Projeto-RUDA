import os
import pathlib
import ocr
import cnd_inss_obra
import extracao_tabela

print('> início da execução.')

caminho_modulo = os.path.dirname(__file__)
print(caminho_modulo)

# listagem dos arquivos
# método para listar os arquivos ainda não processados
import listagem_arquivos
res = listagem_arquivos.listar_arquivos_nao_processados(caminho_modulo + "/imagens/" )
print(res)

nome_arquivo = "00750889.PDF"
print(nome_arquivo)

# nome_arquivo = "00750403.TIF"
# print(nome_arquivo)

caminho_arquivo = caminho_modulo + "/imagens/" + nome_arquivo
print(caminho_arquivo)

# caminho_arquivo = caminho_modulo + "/imagens/habite-se/" + nome_arquivo
# print(caminho_arquivo)

extensao = pathlib.Path(caminho_arquivo).suffix
print(f'ext: {extensao}')

texto = ocr.obter_ocr(ext=extensao,caminho_arquivo=caminho_arquivo)
print(f'>> {texto}')

tabelas = extracao_tabela.obter_tabelas(ext=extensao,caminho_arquivo=caminho_arquivo)
print(f'>> {tabelas}')

resultado = cnd_inss_obra.extrair_dados(texto,tabelas)
