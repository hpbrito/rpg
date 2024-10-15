import websockets
import asyncio
import json
import sys
from typing import Any
from flask import Flask, request
from JSONHandler import JSONHandler
import argparse


# Função principal para o cliente
async def start_client(msg):
    uri = "ws://localhost:8765/chat"  # Path '/chat'
    async with websockets.connect(uri) as websocket:
        # Recebe uma mensagem do servidor
        response = await websocket.recv()
        print(f"Recebido do servidor: {response}")  

# Definindo uma classe de ação personalizada que herda de argparse.Action
class CustomAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        #print(f"Ação personalizada com valores: {values}")
        start_client(values)
        # Armazena o valor no namespace
        setattr(namespace, self.dest, values)

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
        return json.loads(json.dumps(self.data, indent=4))
class Rpg(JSONHandler):
    def __init__(self, character_name):               
        super().__init__()
        self.character = character_name
        # json para manipular respostas de output         
        self.sheet = JSONHandler()
        self.sheet.load_from_file('sheet_model_d&d.json')
        # inicia a instancia do objeto para receber o nome do personagem
        self.sheet["character"]["character_name"] = self.character        
            
    def show_sheet(self):
        print(self.sheet)
        return self.sheet
    
    def get(self):        
        return self.sheet
class serverWs():
    
    def __init__(self) -> None:
        pass
    
    # Função que lida com cada conexão de cliente
    async def handle_connection(self, websocket, path):
        print("Novo cliente conectado")
        try:
            # Loop para receber mensagens do cliente
            async for message in websocket:
                print(f"Mensagem recebida: {message}")
                # Enviando de volta a mensagem recebida
                await websocket.send(f"Servidor recebeu: {message}")
        except websockets.exceptions.ConnectionClosed as e:
            print("Conexão encerrada")

    # Função principal para iniciar o servidor WebSocket
    async def start_server(self):
        server = await websockets.serve(self.handle_connection, "localhost", 8765)
        print("Servidor WebSocket iniciado")
        
        # Mantém o servidor rodando
        await server.wait_closed()

def main()->None:
    
    ws = serverWs()
    asyncio.run(ws.start_server())

    # rpg = Rpg("rickyworion")    
    # rpg.get()['character']['player_name'] = "henrique"
    # rpg.get()['inventory']['itens'] = {"item":"espada longa", "description": "espada de duas mão", "value": "25 moedas" }
    # rpg.show_sheet()

    pass




if __name__ == "__main__":
    main()
  