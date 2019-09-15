import unittest
from main import verifica_cep_valido


class TestCepValido(unittest.TestCase):
    def test_cep_valido(self):
        self.assertTrue(verifica_cep_valido("123456"))
    
    def test_cep_valido_2(self):
        self.assertTrue(verifica_cep_valido("123455"))
    
    def test_cep_invalido_por_tamanho_da_cadeia_menor(self):
        self.assertFalse(verifica_cep_valido("12345"))
    
    def test_cep_invalido_com_letras(self):
        self.assertFalse(verifica_cep_valido("123a45"))
    
    def test_cep_invalido_com_caracteres_especiais(self):
        self.assertFalse(verifica_cep_valido("12345!"))
    
    def test_cep_invalido_por_tamanho_da_cadeia_maior(self):
        self.assertFalse(verifica_cep_valido("1234567"))

    def test_cep_valido_3(self):
        self.assertTrue(verifica_cep_valido("998877"))

    def test_cep_valido_parametro_tipo_integer(self):
        self.assertTrue(verifica_cep_valido(123456))

if __name__ == '__main__':
    unittest.main()