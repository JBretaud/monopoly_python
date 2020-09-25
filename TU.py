from classes.de import De
from classes.joueur import Joueur
import unittest

        
class JoueurTest(unittest.TestCase):
    @mock.patch('classes.joueur.input', create=True)
    def test_Joueur_ask_Name(self, mocked_input):
        j = Joueur(1)
        joueur = ['xxx']
        result = j.ask_name()
        self.assertEqual(result, 'xxx')

unittest.main()