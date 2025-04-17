import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

if response.status_code == 200:
    print("Dane pobrane poprawnie:")
    print(response.json())
else:
    print("Błąd podczas pobierania danych:", response.status_code)
