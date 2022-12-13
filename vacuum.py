import random

def display(room):
    print(room)

room = [0, 0]

x = 0

while x < 2:
    room[x] = random.choice([0,1])
    x += 1

display(room)

x = 0

while x < 2:
    if room[x] == 1:
        print(f"Room {x} is dirty")
        room[x] = 0
    else:
        print(f"Room {x} is clean")
    x += 1       

display(room)