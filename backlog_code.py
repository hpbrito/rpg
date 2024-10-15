# Exemplo de uso
#  json_handler = JSONHandler()
#  
#  # Usando a notação de colchetes para adicionar itens
#  json_handler['user'] = {'name': 'John Doe', 'age': 30}
#  json_handler['location'] = 'Brazil'
#  
#  # Verificar se uma chave existe
#  print('user' in json_handler)  # True
#  print('age' in json_handler)   # False
#  
#  # Adicionar itens a uma lista
#  json_handler.add_to_list('hobbies', 'reading')
#  json_handler.add_to_list('hobbies', 'coding')
#  
#  # Acessar valores com notação de colchetes
#  print(json_handler['user'])  # {'name': 'John Doe', 'age': 30}
#  
#  # Remover um item
#  del json_handler['location']
#  
#  # Soma de dois JSONHandlers
#  json_handler2 = JSONHandler()
#  json_handler2['project'] = 'Python JSON Manager'
#  combined_handler = json_handler + json_handler2
#  
#  # Exibir o JSON combinado
#  print(combined_handler)
#  
#  # Salvar o JSON em um arquivo
#  json_handler.save_to_file('data.json')
#  
#  # Carregar JSON de um arquivo
#  json_handler.load_from_file('data.json')
#  
#  # Exibir o JSON formatado
#  print(json_handler)
#  

# class Api(Rpg):
#     def __init__(self):
#         super().__init__()
#         self.app = Flask(__name__)
#         self.app.config['SERVER_NAME'] = '127.0.0.1:1617'
# 
#         # inicializar as rotas
#         self._routes_character_sheet()
# 
#     def run(self):
#         self.app.run(debug=True)
#   
#     # As rotas foram definidas desta forma para organização
#     def _routes_character_sheet(self):  
# 
#         # @self.app.route('/sheet/model/create', methods=['POST'])
#         # def create_sheet_model():
#         #     data = request.json
#         #     return data, 200
#         
#         @self.app.route('/sheet/model/select', methods=['POST'])
#         def select_sheet_model():
#             data = request.json             
#             return self.load_character(data['character_id'])
#         
#         @self.app.route('/sheet/model/create', methods=['POST'])
#         def create_sheet_model():
#             data             = request.json            
#             return  self.create_new_charactar(data['nome_jogador'], data['nome_personagem'], data['ficha_personagem'])             
# def main()->None:
#     # api = Api()
#     # api.run()
#     # rpg = Rpg()
#     # rpg.load_character(1)
#     pass
# 
# if __name__ == "__main__":
#   main()