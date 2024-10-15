import unittest
import os
from JSONHandler import JSONHandler
from gamer import Gamer, Table


class TestGamer(unittest.TestCase):
    def setUp(self):
        self.sheet_table = JSONHandler()
        self.table_name = 'table_test.json'
        self.table = Table()

    def tearDown(self):
        if os.path.exists(self.table_name):
            os.remove(self.table_name)


    def test_get_section_id(self):
        self.table.set_section_id('test')
        self.assertEqual(self.table.get_section_id(),"9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08")
    
    def test_get_table_game(self):
        
        # Popular objeto de teste
        self.table.set_section_id('test')
        self.table.set_game_master('game_master')
        self.table.set_player('play_1')
        self.table.set_player('play_2')
        self.table.set_player('play_3')
        self.table.set_player('play_4')

        # Resultado esperado
        result = {
            "section_id":"9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
            "game_master":"game_master",
            "players":["play_1", "play_2", "play_3", "play_4"],

        }

        # Executa o teste de comparação
        self.assertDictEqual(self.table.get_table_game(), result)

    def test_do_save(self):
        # Popular objeto de teste
        self.table.set_section_id('test')
        self.table.set_game_master('game_master')
        self.table.set_player('play_1')
        self.table.set_player('play_2')
        self.table.set_player('play_3')
        self.table.set_player('play_4')

        # Resultado esperado
        result = {
            "section_id":"9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
            "game_master":"game_master",
            "players":["play_1", "play_2", "play_3", "play_4"]
        }

        # salva arquivo em disco
        self.table.do_save(self.table_name)

        # verifica se o arquivo foi salvo em disco
        self.assertTrue(os.path.exists(self.table_name))

        # Verifica o conteúdo do arquivo
        self.sheet_table.load_from_file(self.table_name)

        
        # verifica o conteudo do arquivo no formato dic
        self.assertEqual(self.sheet_table.get(), result)



if __name__ == '__main__':
    unittest.main()