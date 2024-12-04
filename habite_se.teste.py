import unittest
import habite_se
import ocr
import os

class Test_HABITE_SE(unittest.TestCase):
    def test_extrair_chave_01(self):
        ext = 'TIF'
        caminho_modulo = os.path.dirname(__file__)
        nome_arquivo ='00750403.TIF'
        caminho_arquivo = caminho_modulo + '/imagens/habite-se/' + nome_arquivo
        texto = ocr.obter_ocr(ext, caminho_arquivo)
        self.assertEqual(habite_se.extrair_chave(texto), 'PCLXJ.QZY96.PXG63.')

    def test_extrair_emissao_01(self):
        ext = 'TIF'
        caminho_modulo = os.path.dirname(__file__)
        nome_arquivo ='00750403.TIF'
        caminho_arquivo = caminho_modulo + '/imagens/habite-se/' + nome_arquivo
        texto = ocr.obter_ocr(ext, caminho_arquivo)
        self.assertEqual(habite_se.extrair_emissao(texto), '02/10/2023 10:23:48')

    def test_extrair_dados(self):
        ext = 'TIF'
        caminho_modulo = os.path.dirname(__file__)
        nome_arquivo ='00750403.TIF'
        caminho_arquivo = caminho_modulo + '/imagens/habite-se/' + nome_arquivo
        texto = ocr.obter_ocr(ext, caminho_arquivo)
        valor_esperado = {
            'chave para validação':'PCLXJ.QZY96.PXG63.',
            'Documento emitido via internet em': '02/10/2023 10:23:48'
        }
        self.assertEqual(habite_se.extrair_dados(texto), valor_esperado)

if __name__ == '__main__':
    unittest.main()