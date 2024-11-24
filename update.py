import requests

URL = 'https://raw.githubusercontent.com/hokuspookus/ssh-game/refs/heads/main/game.py'

game = requests.get(URL).text

print(game)

with open('test.py', 'w') as f:
    f.write(game)