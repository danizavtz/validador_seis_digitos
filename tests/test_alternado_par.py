import unittest
from main import verifica_alternado_em_par


class TestCepGothan(unittest.TestCase):

    def test_verifica_alternado_em_par_verdadeiro(self):
        self.assertTrue(verifica_alternado_em_par('121426'))

    def test_verifica_alternado_em_par_verdadeiro_2(self):
        self.assertTrue(verifica_alternado_em_par('552523'))

    def test_verifica_alternado_em_par_falso(self):
        self.assertFalse(verifica_alternado_em_par('523563'))
    
    def test_verifica_numero_com_menos_de_seis_digitos(self):
        self.assertFalse(verifica_alternado_em_par('0'))

    def test_verifica_numero_com_menos_de_seis_digitos2(self):
        self.assertFalse(verifica_alternado_em_par('99999'))
    
    def test_verifica_numero_com_sete_digitos(self):
        self.assertFalse(verifica_alternado_em_par('11111111'))
    
    def test_verifica_entrada_com_letras(self):
        self.assertFalse(verifica_alternado_em_par('101a00'))

    def test_verifica_entrada_com_caracteres_especiais(self):
        self.assertFalse(verifica_alternado_em_par('01111!'))
    
    def test_verifica_entrada_iniciando_com_zero(self):
        self.assertFalse(verifica_alternado_em_par('0111111'))
    
    def test_verifica_entrada_iniciando_com_zero_2(self):
        self.assertFalse(verifica_alternado_em_par('0000000'))

if __name__ == '__main__':
    unittest.main()