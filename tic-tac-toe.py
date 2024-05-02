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
    

def horisontal_check():
    #across
    for row in range(1):
        if bord[0][row] == bord[1][row] == bord[2][row]  and not bord[2][row] == ' - ':
            print("win hori")
            break

def vertical_check():
    #up
    for col in range(3):
        if bord[col][0] == bord[col][1] == bord[col][2] and not bord[col][2] == ' - ':
            print("win vert")
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
    choice_row = int(input("which row do you want to go(1,2,3): ")) - 1
    choice_col = int(input("which colum do you want to go(1,2,3): ")) - 1
    print('')


    


    
    bord[choice_col][choice_row] = token 
    PlayerCounter += 1
    
    

    print_bord()
    horisontal_check()
    vertical_check()