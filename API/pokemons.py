import requests
import pytest 

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'bc934a5d465b13247d28220c148602bb'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '6912'
TRAINER_NAME = 'Smirka'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200 

def test_trainer_name():
     response_get = requests.get(url = f'{URL}/trainers', headers = HEADER, params = {'id' : TRAINER_ID, 'trainer_name' : TRAINER_NAME})
     assert response_get.json()["data"][0]["trainer_name"] == 'Smirka'