import requests

#mapeado
def _map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


r = requests.get('http://192.168.1.100/status/list.php?estado=now') 

data = r.json()

print(data) 

print("\n\n")

coreTemp = data[1]['coreTemp']

print(coreTemp)

print(_map(float(coreTemp),40,70,0,255))
