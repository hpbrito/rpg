import hashlib
import json
from JSONHandler import JSONHandler

class Table():
    def __init__(self) -> None:
        self.sheet_table = JSONHandler()
        self.sheet_table.load_from_file('sheet_table_model.json')
        pass

    def set_section_id(self, section_id):
        self.sheet_table['section_id'] = hashlib.sha256(bytes([ord(char) for char in section_id])).hexdigest() 
    
    def set_game_master(self, game_master ):
        self.sheet_table['game_master'] = game_master 
    
    def set_player(self, player):
        self.sheet_table.add_to_list('players', player)

    def do_save(self, name_file):
        self.sheet_table.save_to_file(name_file)

    def get_section_id(self):
        return self.sheet_table['section_id'] 
    
    def get_section_game_master(self):
        return self.sheet_table['game_master'] 
    
    def get_section_players(self):
        return self.sheet_table['players'] 
    
    def get_table_game(self):
        return self.sheet_table.get() 
    

class Sheet_player():
    def __init__(self, sheet_player, sheet_model='sheet_model_d&d.json') -> None:
        self.sheet_player = sheet_player
        self.sheet = JSONHandler() 
        self.sheet.load_from_file(sheet_model)
        self.sheet['player_name'] = sheet_player
        self.sheet_file_name = sheet_player + '.json'
        self.sheet.save_to_file(self.sheet_file_name)
        pass

    def toset(self, key, value):
        to = self.sheet.stest(key)
        print(to) 
    
        

class Gamer(Table):
    def __init__(self) -> None:
        super().__init__()

    pass


sheet_player_1 = Sheet_player('player_1')
sheet_player_1.toset('character_status', 'mago')



#sheet_player_1['character']['character_name'] = 'lord_of_fire'

print(sheet_player_1)
