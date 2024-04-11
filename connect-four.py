bord = []
def intil_bord():
    for i in range(6):
        bord.append([' - ',' - ' ,' - ',' - ',' - ',' - ',' - '])
    

def print_bord():
    print('| 1 | 2 | 3 | 4 | 5 | 6 | 7 |')
    for row in bord:
        print('', end='|')
        for col in row:
            print(col, end='|')
        print()
    horisontal_check()
    vertical_check()
    diagonal_check()

def horisontal_check():
    #across
    for row in range(6):
        for col in range(4):
            if bord[row][col] == bord[row][col + 1] == bord[row][col + 2] == bord[row][col + 3] and not bord[row][col + 3] == ' - ':
                print("win")
                break

def vertical_check():
    #up
    for row in range(3):
        for col in range(6):
             if bord[row][col] == bord[row + 1][col] == bord[row + 2][col] == bord[row + 3][col] and not bord[row + 3][col] == ' - ':
                print("win")
                break

def diagonal_check(): 
    #diagonal   
    for row in range(3):
            for col in range(4):
                # diag L
                if bord[row][col] == bord[row + 1][col + 1] == bord[row + 2][col + 2] == bord[row + 3][col + 3] and not bord[row + 3][col + 3] == ' - ':
                    print("win")
                    break
                # diag R
                elif bord[row][col] == bord[row + 1][col - 1] == bord[row + 2][col - 2] == bord[row + 3][col - 3] and not bord[row + 3][col - 3] == ' - ':
                    print("win")
                    break

PlayerCounter = 1 
intil_bord()
print_bord()



while True:
    token = ' X '
    if PlayerCounter % 2 == 0:
        token = ' O '
    
    #player input

    print('')
    choice = int(input("where do you want to go: "))
    print('')
    choice -= 1

    #place token
    for i in range (5, -1, -1):
        if bord[i][choice] == ' - ':
            bord[i][choice] = token
            PlayerCounter += 1
            break



                
    
    print_bord()


    












