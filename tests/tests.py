import unittest
from main import verifica_alternado_em_par


class TestCepGothan(unittest.TestCase):

    def test_verifica_alternado_em_par_verdadeiro(self):
        self.assertTrue(verifica_alternado_em_par('121426'))

    def test_verifica_alternado_em_par_verdadeiro_2(self):
        self.assertTrue(verifica_alternado_em_par('552523'))

    def test_verifica_alternado_em_par_falso(self):
        self.assertFalse(verifica_alternado_em_par('523563'))

if __name__ == '__main__':
    unittest.main()