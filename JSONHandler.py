import json

class JSONHandler:
    def __init__(self, json_data=None):
        if json_data:
            self.data = json.loads(json_data)
        else:
            self.data = {}
    def __getitem__(self, key):
        """
        Permite acessar valores usando a notação de colchetes, como num dicionário.
        Exemplo: handler['key']
        """
        return self.data.get(key, None)
    def __setitem__(self, key, value):
        """
        Permite definir valores usando a notação de colchetes, como num dicionário.
        Exemplo: handler['key'] = value
        """
        self.data[key] = value
    def __delitem__(self, key):
        """
        Permite deletar um item usando a notação de colchetes.
        Exemplo: del handler['key']
        """
        if key in self.data:
            del self.data[key]
    def __contains__(self, key):
        """
        Permite verificar se uma chave está no dicionário.
        Exemplo: 'key' in handler
        """
        return key in self.data
    def __add__(self, other):
        """
        Permite adicionar dois JSONHandlers juntos.
        Exemplo: handler1 + handler2
        """
        if isinstance(other, JSONHandler):
            new_data = {**self.data, **other.data}
            return JSONHandler(json.dumps(new_data))
        raise ValueError("Operação de soma só é permitida com outro JSONHandler.")
    def __repr__(self):
        """
        Define como a instância será representada ao ser impressa ou convertida em string.
        Exemplo: print(handler)
        """
        return json.dumps(self.data, indent=4)
    def add_to_list(self, key, value):
        """
        Adiciona um valor a uma lista em uma chave específica. Se a chave não existir, cria uma nova lista.
        """
        if key not in self.data:
            self.data[key] = []
        if not isinstance(self.data[key], list):
            raise ValueError(f"O valor em '{key}' não é uma lista.")
        self.data[key].append(value)
    def list_entries(self, key):
        """
        Retorna a lista associada à chave. Se a chave não for uma lista, lança um erro.
        """
        if key in self.data and isinstance(self.data[key], list):
            return self.data[key]
        else:
            raise ValueError(f"A chave '{key}' não contém uma lista.")
    def save_to_file(self, file_path):
        """
        Salva o JSON em um arquivo.
        """
        with open(file_path, 'w') as file:
            json.dump(self.data, file, indent=4)
    def load_from_file(self, file_path):
        """
        Carrega o JSON a partir de um arquivo.
        """
        with open(file_path, 'r') as file:
            self.data = json.load(file)
    def get(self):
        return self.data
    def stest(self, key):
        return self.__contains__(key)

        
        

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