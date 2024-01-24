import requests

API_KEY = 'RGAPI-ca68bfba-152d-4e16-95d5-f642c985b6ae'
SUMMONER_NAME = 'Marin Kitagawa#WIN'  # Reemplaza con el nombre de invocador deseado

# Función para obtener el ID del invocador
def obtener_id_invocador(summoner_name):
    url = f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}'
    params = {'api_key': API_KEY}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        summoner_data = response.json()
        return summoner_data['id']
    else:
        print(f'Error al obtener el ID del invocador. Código de estado: {response.status_code}')
        return None

# Función para contar el número de partidas clasificatorias
def contar_partidas_clasificatorias(invocador_id):
    url = f'https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/{invocador_id}'
    params = {'api_key': API_KEY, 'queue': '420'}  # El código de cola '420' corresponde a partidas clasificatorias en la región NA

    response = requests.get(url, params=params)

    if response.status_code == 200:
        match_data = response.json()
        return len(match_data['matches'])
    else:
        print(f'Error al obtener las partidas clasificatorias. Código de estado: {response.status_code}')
        return None

# Ejemplo de uso
invocador_id = obtener_id_invocador(SUMMONER_NAME)

if invocador_id is not None:
    num_partidas_clasificatorias = contar_partidas_clasificatorias(invocador_id)

    if num_partidas_clasificatorias is not None:
        print(f'El invocador {SUMMONER_NAME} ha jugado {num_partidas_clasificatorias} partidas clasificatorias.')
