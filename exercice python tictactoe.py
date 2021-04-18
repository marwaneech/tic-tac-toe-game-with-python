
from time import sleep
from random import randrange
def display_board(board):
    print('+-------+-------+-------+')
    print('+---'+board[0][0]+'---+---'+board[0][1]+'---+---'+board[0][2]+'---+')
    print('+-------+-------+-------+')
    print('+---'+board[1][0]+'---+---'+board[1][1]+'---+---'+board[1][2]+'----+')
    print('+-------+-------+-------+')
    print('+---'+board[2][0]+'---+---'+board[2][1]+'---+---'+board[2][2]+'---+')
    print('+-------+-------+-------+')
    return ""

def enter_move(board):
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.
    while True:
        
        move = int(input("entrer le nombre le l emlacement suivant : "))
        if move>=10 or move<=0:
            print("le nombre doit etre entre 1 et 9")
            continue
        else :
            col=0
            em=int(move)
            if em<=3:
                if board[0][em-1] not in["X","O"]:
                        board[0][em-1]='X'
                        break
                else :
                        print("l emplacement a ete deja saisi ")
                        continue
            else: 
                while em >3:
                    em-=3
                    col+=1
                if board[col][em-1] not in["X","O"]:
                        board[col][em-1]='X'
                        break
                else:
                        print("l emplacement a ete deja saisi ")
                        continue
 
def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column number
    
    free=[]
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ["X","O"]:
                free.append((row,col))
    print(free)

def victory_for(board, sign):
    
    if sign==board[0][0] and sign==board[0][1]and sign==board[0][2]:
        return True
    elif sign==board[1][0] and sign==board[1][1]and sign==board[1][2]:
        return True
    elif sign==board[2][0] and sign==board[2][1]and sign==board[2][2]:
        return True
    elif sign==board[0][0] and sign==board[1][0]and sign==board[2][0]:
        return True
    elif sign==board[0][1] and sign==board[1][1]and sign==board[2][1]:
        return True
    elif sign==board[0][2] and sign==board[1][2]and sign==board[2][2]:
        return True
    elif sign==board[0][0] and sign==board[1][1]and sign==board[2][2]:
        return True
    elif sign==board[0][2] and sign==board[1][1]and sign==board[2][0]:
        return True
    
                   
    
def draw_move(board):
    # The function draws the computer's move and updates the board.
    while True:
        movecom=randrange(1,10)
        if movecom>=10 or movecom<=0:
            print("le nombre doit etre entre 1 et 9")
            continue
        else:
            col=0
            em=int(movecom)
            if em<=3:
                if board[0][em-1] not in["X","O"]:
                    board[0][em-1]='O'
                    break
                else :
                   
                    continue
            else: 
                while em >3:
                    em-=3
                    col+=1
                if board[col][em-1] not in["X","O"]:
                    board[col][em-1]='O'
                    break
                else:
                    continue


board=[['1','2','3'],['4','O','6'],['7','8','9']]
nbmoves=0
print("TIC TAC TOE")
print("DEMARAGE",end="")
for i in range(10):
    print(".",end='')
    sleep(0.5)
print()
print("toi ta le sign 'X' et l ordinateur a le sign 'O' ")
sleep(0.3)
while nbmoves<8:
   
    player="X"
    display_board(board)
    print("ton tour ")
    enter_move(board)
    nbmoves+=1
    if victory_for(board, player)==True:
        display_board(board)
        print()
        print()
        print("player with sign X win the game ")
        break
    
    
    player="O"
    print("tour du l ordinateur")
    sleep(0.2)
    draw_move(board)
    nbmoves+=1
    if victory_for(board, player)==True:
        display_board(board)
        print()
        print()
        print("l ordinateur  with sign O win the game ")
        break
    
else:
    print("egalite")
    
