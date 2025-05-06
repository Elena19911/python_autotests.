import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'aa2df2441dfce32084a8162455cb6b67'
HEADER = {'Content-Type':'application/json','trainer_token':TOKEN}
TRAINER_ID = '30572'
TRAINER_NAME = 'ELENA'

def test_status_code():
     response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
     assert response.status_code == 200

def test_part_of_response():
     response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
     assert response.json(),{'TRAINER_NAME'} == 'ELENA'