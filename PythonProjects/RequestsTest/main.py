import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'aa2df2441dfce32084a8162455cb6b67'
HEADER = {'Content-Type':'application/json','trainer_token':TOKEN}

body_create = {
    "name": "Кисик",
    "photo_id": 1
    }

body_name_change = {
    "pokemon_id": "309471",
    "name": "Кисик МЯУ",
    "photo_id": 2
}

body_add_pokeball = {
    "pokemon_id": "309471"
}


'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_name_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name_change)
print(response_name_change.text)'''

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)



