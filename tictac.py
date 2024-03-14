p1 = input('Enter Player 1 Name : ')
p2 = input('Enter Player 2 Name : ')
currMove = 'X'
dash = '-'
winPlay = False
movesCount = int(0)

board = [['-' , '-' , '-' ],
['-' , '-' , '-' ],
['-' , '-' , '-' ]]

def gameBoard(board):
    print(f' {board[0][0]} | {board[0][1]} | {board[0][2]} ')
    print('---|---|---')
    print(f' {board[1][0]} | {board[1][1]} | {board[1][2]} ')
    print('---|---|---')
    print(f' {board[2][0]} | {board[2][1]} | {board[2][2]} ')
    
    
def playerInput(board,currMove):
    row = int(input('Please enter the row value :'))
    col = int(input('Please enter the col value :'))
    
    if board[row-1][col-1] == '-':
        board[row-1][col-1] = currMove
        checkRow(board,currMove)
        checkCol(board,currMove)
        checkDia(board,currMove)
        playerMove()  
    else:
        print ("Please make another move as it is already filled")    
    
def playerMove():
    global currMove
    global movesCount
    if currMove == 'X':
        currMove = "O"
        movesCount = movesCount + 1
    else:
        currMove = 'X'
        

def winner():
    print("Game Over")
    if currMove == 'X':
        print(f'Player 1 "{p1}" is the Winner ') 
    else:
        print(f'Player 2 "{p2}" is the Winner ') 


def checkCol(board,currMove,row = 0):
    global winPlay
    for col in range(3):

        if board[row][col] == board[row+1][col] == board[row+2][col] == currMove:
            winPlay = True

def checkRow(board,currMove,col = 0):
    global winPlay
    for row in range(3):

        if board[row][col] == board[row][col+1] == board[row][col+2] == currMove:
            winPlay = True

def checkDia(board,currMove,col=0,row=0):
    global winPlay
   
    if (board[0][0] == board[1][1] == board[2][2] == currMove) or (board[0][2] == board[1][1] == board[2][0] == currMove):
        winPlay = True


def main():
    
    while movesCount < 5:
        if winPlay == False:
            gameBoard(board)
            playerInput(board,currMove)
            
        else:
            winner()
            break
    gameBoard(board)            
    if movesCount == 5:
        print("Game Over !!! Its a Tie")
    
main()
        
