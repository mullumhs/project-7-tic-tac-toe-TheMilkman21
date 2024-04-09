bord = []
def intil_bord():
    for i in range(6):
        bord.append(['-','-','-','-','-','-','-'])

def print_bord():
    print('|1|2|3|4|5|6|7|')
    for row in bord:
        print('', end='|')
        for col in row:
            print(col, end='|')
        print()

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

    
    for row in range(6):
        for col in range(4):
            if bord[row][col] == bord[row][col + 1] == bord[row][col + 2] == bord[row][col + 3] and not bord[row][col + 3] == '-':
                print("win")
                break
    
    
    for i in range (5, -1, -1):
        if bord[i][choice] == ' - ':
            bord[i][choice] = token
            PlayerCounter += 1
            break
    print_bord()


    












