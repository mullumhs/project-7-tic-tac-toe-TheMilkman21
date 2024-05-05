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
    #up
    for row in range(3):
        if bord[0][row] == bord[1][row] == bord[2][row] and not bord[2][row] == ' - ':
            print("win ")
            return True

def vertical_check():
    #across
    for col in range(3):
        if bord[col][0] == bord[col][1] == bord[col][2] and not bord[col][2] == ' - ':
            print("win ")
            return True

def diag_check():
    if bord[0][0] == bord[1][1] == bord[2][2] and not bord[0][0] == ' - ':
        print("win")
        return True
    if bord[2][0] == bord[1][1] == bord[0][2] and not bord[0][2] == ' - ':
        print("win")
        return True


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
       
    
    if (choice_col >= 0 and choice_col < 3) and (choice_row >= 0 and choice_row < 3):

        if bord[choice_col][choice_row] == ' - ':
            bord[choice_col][choice_row] = token
            PlayerCounter += 1
        else:
            print("error thing there")
    else:
        print("error not a place")
    
    if PlayerCounter == 9:
        print("draw")
        break
    
    

    print_bord()
    if horisontal_check() or vertical_check() or diag_check():
        break
       
        
    
    
   
