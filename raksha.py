from random import randint, choice
import requests
from item_to_id import item_to_id

#prices as of 26.09.2021
prices = {'spirit weed seeds': 6657, 
'Carambola seeds': 5369, 
'golden dragonfruit seeds': 30600, 
'small blunt rune salvage': 14700, 
'medium spiky orikalkum salvage': 73300, 
'huge plated orikalkum salvage': 123700, 
'black dragonhide': 2182, 
'onyx dust': 14400, 
'dinosaur bones': 6188, 
'crystal keys': 12600, 
'inert adrenaline crystals': 9531, 
'sirenic scales': 708500, 
'soul runes': 2231, 
'dark/light animica stone spirits': 950, 
'Greater ricochet ability codex': 1500000000, 
'Greater chain ability codex': 174800000, 
'Divert ability codex': 18000000, 
'Shadow spike': 188600000, 
'Laceration boots': 1200000, 
'Blast diffusion boots': 3000000, 
'Fleeting boots': 44000000}

def update_prices():
    progress = 0
    for k, v in item_to_id.items():
        r = requests.get(f'https://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item={v}')
        price = str(r.json()['item']['current']['price']).rstrip()

        if 'k' in price:
            prices[k] = int(float(price[:-1]) * 10 ** 3)
        elif 'm' in price:
            prices[k] = int(float(price[:-1]) * 10 ** 6)
        elif 'b' in price:
            prices[k] = int(float(price[:-1]) * 10 ** 9)
        else:
            prices[k] = int(''.join(x for x in price if x.isdigit()))

        progress += 100 / 21
        yield progress

def calculate_drop():
    drop = choice(main_droptable)

    if drop == "secondary_droptable":
        drop = choice(secondary_droptable)

    return drop
main_droptable = []

for _ in range(23):
    main_droptable.append("secondary_droptable")

while len(main_droptable) < 1000:
    if len(main_droptable) % 5 == 0:
        main_droptable.append(str(randint(75, 130)) + " onyx dust")
    else:
        main_droptable.append(str(randint(5, 10)) + " spirit weed seeds")
        main_droptable.append("5 Carambola seeds")
        main_droptable.append(str(randint(5, 10)) + " golden dragonfruit seeds")
        main_droptable.append("50 small blunt rune salvage")
        main_droptable.append(str(randint(12, 18)) + " medium spiky orikalkum salvage")
        main_droptable.append(str(randint(10, 15)) + " huge plated orikalkum salvage")
        main_droptable.append(str(randint(200, 300)) + " black dragonhide")
        main_droptable.append(str(randint(80, 120)) + " dinosaur bones")
        main_droptable.append(str(randint(25, 45)) + " crystal keys")
        main_droptable.append(str(randint(12, 18)) + " inert adrenaline crystals")
        main_droptable.append("3 sirenic scales")
        main_droptable.append(str(randint(125, 175)) + " soul runes")
        main_droptable.append(str(randint(60, 95) * 2) + " dark/light animica stone spirits")

if len(main_droptable) > 1000:
    main_droptable = main_droptable[:1000]
    

secondary_droptable = [] #Rare drops are here with a chace to roll on this table in the main droptable
for _ in range(5):
    secondary_droptable.append("Laceration boots")
    secondary_droptable.append("Blast diffusion boots")
    secondary_droptable.append("Fleeting boots")

for _ in range(2):
    secondary_droptable.append("Shadow spike")
    secondary_droptable.append("Greater ricochet ability codex")
    secondary_droptable.append("Greater chain ability codex")
    secondary_droptable.append("Divert ability codex")