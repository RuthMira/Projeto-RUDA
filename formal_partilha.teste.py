import unittest
import formal_partilha
import ocr
import os

class Test_FORMAL_PARTILHA(unittest.TestCase):
    def test_processo(self):
        ext = 'PDF'
        caminho_modulo = os.path.dirname(__file__)
        nome_arquivo ='00665735_editado.pdf'
        caminho_arquivo = caminho_modulo + '/imagens/formal_partilha/' + nome_arquivo
        texto = ocr.obter_ocr_paginado(ext, caminho_arquivo)
        self.assertEqual(formal_partilha.extrair_processo(texto), '1014433-51.2016.8.26.0577')

if __name__ == '__main__':
    unittest.main()