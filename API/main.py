import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'bc934a5d465b13247d28220c148602bb'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "generate",
    "photo_id": -1
}
body_rename = {
    "pokemon_id": "47777",
    "name": "generate"
}
body_catch = {
    "pokemon_id": "47777"
}
body_delete = {
    "pokemon_id": "47777"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_rename = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)

'''response_delete = requests.post(url = f'{URL}/pokemons/knockout', headers = HEADER, json = body_delete)
print(response_delete.text)'''