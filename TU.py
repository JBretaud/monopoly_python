from classes.de import De
from classes.joueur import Joueur
import unittest

class DeTest(unittest.TestCase):
    def test__init__(self):
        self.assertRaises(Exception,De,-1)

    def test_launch(self):
        D2 = De(2)
        lance = D2.launch()
        self.assertTrue(lance < 3 and lance > 0)
        
class JoueurTest(unittest.TestCase):
    @mock.patch('classes.joueur.input', create=True)
    def test_Joueur_ask_Name(self, mocked_input):
        j = Joueur(1)
        joueur = ['xxx']
        result = j.ask_name()
        self.assertEqual(result, 'xxx')

unittest.main()