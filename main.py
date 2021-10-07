import os
import requests

API_KEY = os.environ['API_KEY']
WS_URL = "http://api.weatherstack.com/current"

ciudades = []

with open("ciudades.txt") as f:
  for line in f:
    ciudades.append(line.strip())

for ciudad in ciudades:
  params = {'access_key':API_KEY,'query':ciudad}
  req = requests.get(WS_URL,params)

  hora=req.json()['location']['localtime']
  temperatura=req.json()['current']['temperature']


  with open(f'{ciudad}.text','a') as f:
    f.write(f'en {ciudad} a las {hora} la temperatura es de {temperatura}°C')
    print(f'se creo un archivo txt con la temperatura de:{ciudad}')