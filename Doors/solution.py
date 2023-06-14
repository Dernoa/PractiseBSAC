Doors = ["Closed"] * 100

def Switch(Door):
    if Door == "Closed":
        Door = "Open"
    elif Door == "Open":
        Door = "Closed"
    return Door

for i in range(1,100):
    for k in range(0,100):
        if k % i == 0:
            Doors[k] = Switch(Doors[k])

def CreateArray(Doors):
    Array = []
    for i in range(0,100):
        if Doors[i] == "Open":
            Array.append(i)
    return Array

print(CreateArray(Doors))
