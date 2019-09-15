import unittest
from main import verifica_alternado_em_par


class TestAlternadoPar(unittest.TestCase):

    def test_verifica_alternado_em_par_verdadeiro(self):
        self.assertTrue(verifica_alternado_em_par('121426'))

    def test_verifica_alternado_em_par_verdadeiro_2(self):
        self.assertTrue(verifica_alternado_em_par('552523'))

    def test_verifica_alternado_em_par_no_fim_entrada(self):
        self.assertTrue(verifica_alternado_em_par('123454'))

    def test_verifica_alternado_em_par_falso(self):
        self.assertFalse(verifica_alternado_em_par('523563'))
    
    def test_verifica_entrada_somente_numeros(self):
        self.assertFalse(verifica_alternado_em_par('123456'))

    def test_verifica_alternado_em_par_verdadeiro_3(self):
        self.assertTrue(verifica_alternado_em_par('111111'))

    def test_verifica_alternado_em_par_falso_2(self):
        self.assertFalse(verifica_alternado_em_par('112233'))

if __name__ == '__main__':
    unittest.main()