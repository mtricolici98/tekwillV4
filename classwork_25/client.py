import requests

mock_ua = "Marius Brain"

while True:
    response = requests.get(f'http://127.0.0.1:5000/convert/EUR/{input("Suma")}', headers={'User-Agent': mock_ua})
    print(response.content)
