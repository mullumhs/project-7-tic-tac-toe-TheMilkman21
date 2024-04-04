bord = []

for i in range(6):
    bord.append(['-','-','-','-','-','-','-'])


while True:
    choice = int(input("where do you want to go: "))
    bord[5][choice] = "X"

    for row in bord:
        for col in row:
            print(col, end=" ")
        print()