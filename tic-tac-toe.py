bord = []
def intil_bord():
    for i in range(3):
        bord.append([' - ',' - ' ,' - ',])

def print_bord():
    print(' ___ ___ ___ ')
    print('| 1 | 2 | 3 |')
    for row in bord:
        print('', end='|')
        for col in row:
            print(col, end='|')
        print()
        horisontal_check()

def horisontal_check():
    #across
    for row in range(2):
        for col in range(1):
            if bord[row][col] == bord[row][col + 1] == bord[row][col + 2]  and not bord[row][col + 2] == ' - ':
                print("win")
                break

PlayerCounter = 1 
intil_bord()
print_bord()


while True:
    token = ' X '
    if PlayerCounter % 2 == 0:
        token = ' O '


    print('')
    choice = int(input("where do you want to go: "))
    print('')
    choice -= 1

    for i in range (2, -1, -1):
        if bord[i][choice] == ' - ':
            bord[i][choice] = token
            PlayerCounter += 1
            break

    print_bord()