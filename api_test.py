import requests
import json 
from raksha import prices

item_to_id = {"spirit weed seeds": 12176, 
"Carambola seeds": 48768, 
"golden dragonfruit seeds": 48764, 
"small blunt rune salvage": 47298, 
"medium spiky orikalkum salvage": 51103, 
"huge plated orikalkum salvage": 51105, 
"black dragonhide": 1747, 
"onyx dust": 42954, 
"dinosaur bones": 48075, 
"crystal keys": 989, 
"inert adrenaline crystals": 48575, 
"sirenic scales": 29863, 
"soul runes": 566, 
"dark/light animica stone spirits": 44815, 
"Greater ricochet ability codex": 51094, 
"Greater chain ability codex": 51096, 
"Divert ability codex": 51098, 
"Shadow spike": 51086, 
"Laceration boots": 48081, 
"Blast diffusion boots": 48085, 
"Fleeting boots": 51082}

for k, v in item_to_id.items():
    r = requests.get(f'https://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item={v}')
    price = str(r.json()['item']['current']['price']).rstrip()

    if 'k' in price:
        prices[k] = int(float(price[:-1]) * 10 ** 3)
        print(prices[k])
    elif 'm' in price:
        prices[k] = int(float(price[:-1]) * 10 ** 6)
        print(prices[k])
    elif 'b' in price:
        prices[k] = int(float(price[:-1]) * 10 ** 9)
        print(prices[k])
    else:
        prices[k] = int(''.join(x for x in price if x.isdigit()))
        print(prices[k])