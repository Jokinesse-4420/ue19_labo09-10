import requests

api = "https://punapi.rest/api/pun"

response = requests.get(api)

if response.status_code == 200:
    print(response.json()['pun'])
else:
    print(f"Erreur {response.status_code}: une erreur est survenue")