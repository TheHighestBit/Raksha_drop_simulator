from random import randint, choice

#prices as of 25.09.2021
prices = {"spirit weed seeds": 7377, 
"Carambola seeds": 5277, 
"golden dragonfruit seeds": 29981, 
"small blunt rune salvage": 14533, 
"medium spiky orikalkum salvage": 75000, 
"huge plated orikalkum salvage": 125000, 
"black dragonhide": 2215, 
"onyx dust": 14797, 
"dinosaur bones": 6542, 
"crystal keys": 12441, 
"inert adrenaline crystals": 9458, 
"sirenic scales": 723602, 
"soul runes": 2290, 
"dark/light animica stone spirits": 1069, 
"Greater ricochet ability codex": 1800000000, 
"Greater chain ability codex": 170049626, 
"Divert ability codex": 18000000, 
"Shadow spike": 190000000, 
"Laceration boots": 1184180, 
"Blast diffusion boots": 3010545, 
"Fleeting boots": 41000000}

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