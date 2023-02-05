with open("level.txt") as f:
    level = f.read()

lines = level.split("\n")

line_level = lines[0]
line_enemies = lines[1]
line_pickups = lines[2]

level_number = line_level.split(":")[1]
enemies = line_enemies.split(":")[1]
pickups = line_pickups.split(":")[1].split(",")

print(f"Welcome to level {level_number}. There are {enemies} enemies to beat.")
print(f"On this level there are {len(pickups)} things to find:")

for pickup in pickups:
    print(pickup)

print("Good luck")