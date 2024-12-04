import unittest
import cnd_inss_obra
import ocr
import extracao_tabela
import os

class Test_CND_INSS_OBRA(unittest.TestCase):
    def test_extrair_afericao_01(self):
        ext = 'PDF'
        caminho_modulo = os.path.dirname(__file__)
        nome_arquivo ='00750889.PDF'
        caminho_arquivo = caminho_modulo + '/imagens/' + nome_arquivo
        texto = ocr.obter_ocr(ext, caminho_arquivo)
        self.assertEqual(cnd_inss_obra.extrair_afericao(texto), '60.011.39012/68-001')

    def test_extrair_CEP_01(self):
        ext = 'PDF'
        caminho_modulo = os.path.dirname(__file__)
        nome_arquivo ='00750889.PDF'
        caminho_arquivo = caminho_modulo + '/imagens/' + nome_arquivo
        texto = ocr.obter_ocr(ext, caminho_arquivo)
        self.assertEqual(cnd_inss_obra.extrair_cep(texto), '12220-057')

    # def test_extrair_endereco_01(self):
    #     ext = 'PDF'
    #     caminho_modulo = os.path.dirname(__file__)
    #     nome_arquivo ='00750950.PDF'
    #     caminho_arquivo = caminho_modulo + '/imagens/' + nome_arquivo
    #     texto = ocr.obter_ocr(ext, caminho_arquivo)
    #     self.assertEqual(cnd_inss_obra.extrair_endereco(texto), 'RUA OLINDA, 335, PARQUE INDUSTRIAL, SÃO JOSÉ DOS CAMPOS/SP, 12235-830')
            
    def test_extrair_endereco_02(self):
        ext = 'PDF'
        caminho_modulo = os.path.dirname(__file__)
        nome_arquivo ='00750889.PDF'
        caminho_arquivo = caminho_modulo + '/imagens/' + nome_arquivo
        texto = ocr.obter_ocr(ext, caminho_arquivo)
        self.assertEqual(cnd_inss_obra.extrair_endereco(texto), 'RUA RUA OLIVIO AUGUSTO DO AMARAL 141, 141, casa, RES. VISTA LINDA, SÃO JOSÉ''\n'
                          'DOS CAMPOS/SP, 12220-057')

    def teste_extrair_hora_01(self):
        ext = 'PDF'
        caminho_modulo = os.path.dirname(__file__)
        nome_arquivo ='00750889.PDF'
        caminho_arquivo = caminho_modulo + '/imagens/' + nome_arquivo
        texto = ocr.obter_ocr(ext, caminho_arquivo)
        self.assertEqual(cnd_inss_obra.extrair_hora(texto), '19:49:43')

    def teste_extrair_emissão_01(self):
        ext = 'PDF'
        caminho_modulo = os.path.dirname(__file__)
        nome_arquivo ='00750889.PDF'
        caminho_arquivo = caminho_modulo + '/imagens/' + nome_arquivo
        texto = ocr.obter_ocr(ext, caminho_arquivo)
        self.assertEqual(cnd_inss_obra.extrair_emissão(texto), '19:49:43 do dia 06/10/2023 ')

    def teste_extrair_validade_01(self):
        ext = 'PDF'
        caminho_modulo = os.path.dirname(__file__)
        nome_arquivo ='00750889.PDF'
        caminho_arquivo = caminho_modulo + '/imagens/' + nome_arquivo
        texto = ocr.obter_ocr(ext,caminho_arquivo)
        self.assertEqual(cnd_inss_obra.extrair_validade(texto), '03/04/2024')

    def test_extrair_categoria(self):
        ext = 'PDF'
        caminho_modulo = os.path.dirname(__file__)
        nome_arquivo ='00750889.PDF'
        caminho_arquivo = caminho_modulo + '/imagens/' + nome_arquivo
        tabelas = extracao_tabela.obter_tabelas(ext, caminho_arquivo)
        self.assertEqual(cnd_inss_obra.extrair_categoria(tabelas), 'Obra Nova')

    def test_extrair_destinação(self):
        ext = 'PDF'
        caminho_modulo = os.path.dirname(__file__)
        nome_arquivo ='00750889.PDF'
        caminho_arquivo = caminho_modulo + '/imagens/' + nome_arquivo
        tabelas = extracao_tabela.obter_tabelas(ext, caminho_arquivo)
        self.assertEqual(cnd_inss_obra.extrair_destinação(tabelas), 'Residencial unifamiliar')

    def test_extrair_area(self):
        ext = 'PDF'
        caminho_modulo = os.path.dirname(__file__)
        nome_arquivo ='00750889.PDF'
        caminho_arquivo = caminho_modulo + '/imagens/' + nome_arquivo
        tabelas = extracao_tabela.obter_tabelas(ext, caminho_arquivo)
        self.assertEqual(cnd_inss_obra.extrair_area(tabelas), '187,93')

    def test_extrair_dados(self):
        ext = 'PDF'
        caminho_modulo = os.path.dirname(__file__)
        nome_arquivo ='00750889.PDF'
        caminho_arquivo = caminho_modulo + '/imagens/' + nome_arquivo
        texto = ocr.obter_ocr(ext, caminho_arquivo)
        tabelas = extracao_tabela.obter_tabelas(ext, caminho_arquivo)
        valor_esperado = {
            'afericao':'60.011.39012/68-001',
            'cep': '12220-057',
            'endereco': 'RUA RUA OLIVIO AUGUSTO DO AMARAL 141, 141, casa, RES. VISTA LINDA, SÃO JOSÉ''\n''DOS CAMPOS/SP, 12220-057',
            'hora': '19:49:43',
            'emissão': '19:49:43 do dia 06/10/2023 ',
            'validade': '03/04/2024',
            'categoria': 'Obra Nova',
            'destinação': 'Residencial unifamiliar',
            'area': '187,93'
        }
        self.assertEqual(cnd_inss_obra.extrair_dados(texto, tabelas), valor_esperado)

if __name__ == '__main__':
    unittest.main()