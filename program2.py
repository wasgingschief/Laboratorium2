import requests

response = requests.get("https://catfact.ninja/fact")

if response.status_code == 200:
    data = response.json()
    print("Fakt o kocie:", data['fact'])
else:
    print("Nie udało się pobrać faktu o kocie.")
