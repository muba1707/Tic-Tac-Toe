#Tic Tac Toe

import random


def draw_board(board):
    #This function import the board let you play

    #This let to pass into the board
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def inputplayerletter():
    #let the player choose what they are going to return
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print("Do you want to be X or O : ")
        letter = input().upper()

    # the first letter in the list is the player input and the second one is computer letter
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoisfirst():
    #this function define who go first
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return name
    
def playagain():
    #this function return want to play again return true or return false
    print("Do you want to play the game again? (yes or no): ")
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    #this function is used to find the possible of win.
    return((bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[3] == le and bo[6] == le and bo[9] == le) or
    (bo[2] == le and bo[5] == le and bo[8] == le) or
    (bo[1] == le and bo[4] == le and bo[7] == le) or
    (bo[1] == le and bo[5] == le and bo[9] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le))

def getBoardCopy(board):
    dulplicate = []

    for i in board:
        dulplicate.append(i)

    return dulplicate

def isSpaceFree(board, move):
    #this function return the true if the space is free
    return board[move] == ' '

def getPlayerMove(board):
    #let the player his move
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print("what is your next move(1-9): ")
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, moveList):
    #Return the possible list by passing the pass list in the passed board
    #Return the none
    possibleList =[]
    for i in moveList:
        if isSpaceFree(board, i):
            possibleList.append(i)

    if len(possibleList) != 0:
        return random.choice(possibleList)
    else:
        return None

def getcomputerMove(board, computerLetter):
    #Return the computer letter and make the move
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    #first check, if the next move to win
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    #check if the player could win in the next step and block them
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    #try to make one of the corner
    move = chooseRandomMoveFromList(board, [7, 9, 1, 3])
    if move != 0:
        return move

    #try to it center
    if isSpaceFree(board, 5):
        return 5

    #try on the otherside
    return chooseRandomMoveFromList(board, [8, 4, 6, 2])

def isBoardFull(board):
#Return true if hte every elements in the board are taken (or) return false
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print("Welcome to TIC TAC TOE")
name = input("enter the name: ")

while True:
    #reset the board
    the_board = [' '] * 10
    playerLetter, computerLetter = inputplayerletter()
    turn = whoisfirst()
    print(f"the {turn} will go first")
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == name:
            #player turn
            draw_board(the_board)
            move = getPlayerMove(the_board)
            makeMove(the_board, playerLetter, move)

            if isWinner(the_board, playerLetter):
                draw_board(the_board)
                print(f"congrats {name}, you won the game")
                gameIsPlaying = False
            else:
                if isBoardFull(the_board):
                    draw_board(the_board)
                    print("the game is tie")
                    break
                else:
                    turn = 'computer'

        else:
            #computer turn
            move = getcomputerMove(the_board, computerLetter)
            makeMove(the_board, computerLetter, move)
            
            if isWinner(the_board, computerLetter):
                draw_board(the_board)
                print("The computer has beaten you, you lose")
                gameIsPlaying = False
            else:
                if isBoardFull(the_board):
                    draw_board(the_board)
                    print("the game is tie")
                    break
                else:
                    turn = name

    if not playagain():
        break
