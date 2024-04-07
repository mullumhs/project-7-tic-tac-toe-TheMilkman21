bord = []

for i in range(6):
    bord.append(['-','-','-','-','-','-','-'])


while True:
    for row in bord:
        for col in row:
            print(col, end=" ")
        print()

    choice = int(input("where do you want to go: "))
    bord[5][choice] = "X"

    

    for row in range(6):
        for col in range(4):
            if bord[row][col] == bord[row][col + 1] == bord[row][col + 2] == bord[row][col + 3] and not bord[row][col + 3] == '-':
                print("win")
                break

    










