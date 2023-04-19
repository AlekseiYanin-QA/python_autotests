import requests

base_url = 'https://pokemonbattle.me:9104/'
token = "7d29f07014f29ca79f812a8f2c20631d"

response_add_pokemons = requests.post(f'{base_url}pokemons', headers={'trainer_token': token, 'content-type': 'application/json'}, json={
    "name": "Bulka3",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})
print(response_add_pokemons.json())
# создание покемона

response_edit_pokemons = requests.put(f'{base_url}pokemons', headers={'trainer_token': token, 'content-type': 'application/json'}, json={
    "pokemon_id": "9346",
    "name": "Bublik",
    "photo": "https://dolnikov.ru/pokemons/albums/063.png"
})
print(response_edit_pokemons.json())
# изменение покемона

response_add_pokeball = requests.post(f'{base_url}trainers/add_pokeball', headers={'trainer_token': token, 'content-type': 'application/json'}, json={
    "pokemon_id": "9346"
})
print(response_add_pokeball.json())
# поймать покемона в покебол



