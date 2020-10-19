import requests

hero1 = requests.get("https://superheroapi.com/api/2619421814940190/332/powerstats")
hero2 = requests.get("https://superheroapi.com/api/2619421814940190/149/powerstats")
hero3 = requests.get("https://superheroapi.com/api/2619421814940190/655/powerstats")

superhero = {}

superhero[hero1.json()["name"]] = int(hero1.json()["intelligence"])
superhero[hero2.json()["name"]] = int(hero2.json()["intelligence"])
superhero[hero3.json()["name"]] = int(hero3.json()["intelligence"])
print(superhero)

max = 0
key = ''
for hero, intelligence in superhero.items():
    if intelligence > max:
        max = intelligence
        key = hero
print(f'Самый умный из героев {key}, его интеллект {max}')