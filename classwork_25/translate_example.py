import requests

url = "https://text-translator2.p.rapidapi.com/translate"

key = open('API_KEY').read().strip()

headers = {
    "content-type": "application/x-www-form-urlencoded",
    "X-RapidAPI-Key": key,
    "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
}

# while True:
#     text = input("Text:")
#     payload = {
#         "source_language": "en",
#         "target_language": "ro",
#         "text": text
#     }
#     response = requests.post(url, data=payload, headers=headers)
#     print(response.json()['data']['translatedText'])


with open('C:\\Users\\mariu\\ProjectsTeaching\\tekwillV4\\final_project\\idei_proiect.md') as f:
    lines = []
    for line in f.readlines()[:5]:
        lines.append(line)
    text = ';'.join(lines)
    payload = {
        "source_language": "en",
        "target_language": "ro",
        "text": text
    }
    response = requests.post(url, data=payload, headers=headers)
    print(response.json())
    print(response.json()['data']['translatedText'])
