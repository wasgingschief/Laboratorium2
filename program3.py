import requests

city = input("Podaj nazwę miasta: ")

url = f"https://api.api-ninjas.com/v1/city?name={city}"
headers = {'X-Api-Key': 'Twój_klucz_API'}  # <-- tutaj wpisz swój darmowy klucz API

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    if data:
        print(f"Miasto: {data[0]['name']}")
        print(f"Państwo: {data[0]['country']}")
        print(f"Liczba ludności: {data[0]['population']}")
    else:
        print("Nie znaleziono miasta.")
else:
    print("Błąd zapytania:", response.status_code)
