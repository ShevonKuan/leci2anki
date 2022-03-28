import os
import requests
import json
files = os.listdir()
for file in files:
    if 'json' in file:
        with open(file, 'r', encoding='utf8') as f:
            books = json.load(f)["data"]["dataVocabulary"]
            for book in books:
                try:
                    name = book["name"]
                    link = book["fileData"][0]["fileAdress"]
                    print(name, link)
                except:
                    continue
                re = requests.get(link, stream=True)
                open(name+'.zip', 'wb').write(re.content)
            