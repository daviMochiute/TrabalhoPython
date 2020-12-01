import requests
import json
from urllib.request import urlopen




hero_input = input('Digite o nome de algum personagem: ')

request = requests.get('https://www.superheroapi.com/api.php/1687915884717809/search/{}'.format(hero_input))

dados = request.json()

# print(dados)

with open('dados.json', 'w') as json_file:
    json.dump(dados, json_file, indent=4)

