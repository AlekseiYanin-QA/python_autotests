import requests
import pytest

def test_status_code():
    token='7d29f07014f29ca79f812a8f2c20631d'
    response = requests.get('https://pokemonbattle.me:9104/trainers', params={'trainer_id' : 4060})
    assert response.status_code == 200
    # статус код 200

def test_name_trainer():
    response = requests.get('https://pokemonbattle.me:9104/trainers', params={'trainer_id' : 4060})
    assert response.json()['trainer_name'] == 'Alex'
    # строчка с именем тренера