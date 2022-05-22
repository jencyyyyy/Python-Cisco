# 4.1.6.13 PROJECT: Tic-Tac-Toefrom random import randrange

print("-------Tic-Tac-Toe-------")
#Updates the user my printing the board to the console
def display_board(board):
    #print(board)
    for i in range(0,len(board),3):
        print("+-------"*3 + "+")
        print("|       "*3 + "|")
        print("|   " + str(board[i]) + \
                 "   |   " + str(board[i + 1]) + \
                "   |   " + str(board[i + 2]) + "   |   ")
        print("|       "*3 + "|")
    print("+-------"*3 + "+")



# This function takes the users input and updates the board 
def EnterMove(board):
    FreeSpace = MakeListOfFreeSpace(board)
    position = int(input("Your turn:"))

    while(position < 1 or position > 9):
        print("Please enter number 1-9")
        position = int(input("Your turn:"))
        
    while True:
        if position in FreeSpace:
            board[position - 1] = 'O'
            break
        else:
            print('That spot has been taken')
            position = int(input("Your turn:"))
    display_board(board)

# This function checks to see if there are any free spaces and makes a list of the ones avalable
def MakeListOfFreeSpace(board):
    FreeSpace = []
    for i in range(len(board)):
            if board[i] != 'O' and board[i]!='X':
                FreeSpace.append(board[i])
    return FreeSpace


#Checks to see if the O or X player has won the game
def Victory(board, sign):
    arrangements = [[1, 2, 3], [4, 5, 6], [7, 8, 9],[1, 4, 7],  [2, 5, 8], [3, 6, 9],[1, 5, 9], [3, 5, 7]]
    for i in range(len(arrangements)):
        position1, position2, position3 = arrangements[i][0] - 1, arrangements[i][1] - 1, arrangements[i][2] - 1
        if (str(board[position1]) == sign) and (str(board[position2]) == sign) and (str(board[position3]) == sign):
            return True
    return False


# This function is how the computer makes the move and it updates the board
def draw_move(board):
    FreeSpace = MakeListOfFreeSpace(board)
    position = randrange(1,10)
    while True:
        if position in FreeSpace:
            board[position - 1] = 'X'
            break
        else:
            position = randrange(1, 10)
    display_board(board)

#This is the list for the board
board = [1, 2, 3, 4, 'X', 6, 7, 8, 9]

display_board(board)
while True:
#checks to see if the board is filled
    moves = 0
    for i in range(len(board)):
        if board[i] == 'O' or board[i] =='X':
            moves +=1
    if moves == len(board):
        print('Game is Tie')
        break

#When its the users turn 
    EnterMove(board)
    if Victory(board, 'O'):
        print('You won!!!')
        break
# When its the computers 
    draw_move(board)
    if Victory(board, 'X'):
        print('Computer won!!!')
        break
