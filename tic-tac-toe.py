bord = []
def intil_bord():
    for i in range(3):
        bord.append([' - ',' - ' ,' - ',])

def print_bord():
    print(' ___ ___ ___ ')
    print('| 1 | 2 | 3 |')
    for row in bord:
        print('', end='|' )
        for col in row:
            print(col, end='|')
        print()
        horisontal_check()
        vertical_check()

def horisontal_check():
    #across
    for row in range(2):
        for col in range(1):
            if bord[row][col] == bord[row][col + 1] == bord[row][col + 2]  and not bord[row][col + 2] == ' - ':
                print("win")
                break

def vertical_check():
    #up
    for row in range(3):
        for col in range(6):
            if bord[row][col] == bord[row + 1][col] == bord[row + 2][col] == bord[row + 3][col] and not bord[row + 3][col] == ' - ':
                print("win")
                break

PlayerCounter = 1 
intil_bord()
print_bord()


while True:
    if PlayerCounter % 2 != 0:
        print("Player 1's go")
        token = ' X '
    else:
        print("Player 2's go")
        token = ' O '


    print('')
    choice = int(input("which row do you want to go: "))
    choice = int(input("which colum do you want to go: "))
    print('')
    choice -= 1

    for i in range (2, -1, -1):
        if bord[i][choice] == ' - ':
            bord[i][choice] = token
            PlayerCounter += 1
            break
    

    print_bord()