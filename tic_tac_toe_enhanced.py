"""
Course: Python for Scientist (Part-I)
"""
#%%
def author():
    return 'Laura Soto'
#%%
import random
import copy
# %%
def DrawBoard(Board):
    rows=len(Board)
    columns=len(Board[0])
    if rows!=3 or columns!=3:
        print('No valid')
    print(' --+--+--')
    for i in range(0,rows):
        for j in range(0,columns):
            print('|',Board[i][j], end='')
        print('|''\n --+--+--')
#%% 
def IsSpaceFree(Board, i ,j):
    try:
        if Board[i][j] == ' ':
            return True
        else:
            return False
    except:
        return False
#%%
def GetNumberOfChessPieces(Board):
    num=0
    for i in range(len(Board)):
        for j in range(len(Board)):
            if Board[i][j]=='X' or Board[i][j]=='O':
                num+=1 
    return num
#%%
def IsBoardFull(Board):
    num = GetNumberOfChessPieces(Board)
    if num == 9:
        return True
    else: 
        return False
#%%
def IsBoardEmpy(Board):
    num = GetNumberOfChessPieces(Board)
    if num == 0:
        return True
    else: 
        return False
#%%
def UpdateBoard(Board, Tag, Choice):
    i=Choice[0]
    j=Choice[1]
    Board[i][j]=Tag
#%%
def HumanPlayer(Tag, Board):
    print('Please enter the row and column:')
    choice=[0,0]
    while True:
        row=int(input('Row: '))
        column=int(input('Colum:'))
        if type(row)==int and type(column)==int:
            if row > 3 or column > 3 or row < 0 or column < 0:
                print('This position is invalid, please choose another spot:')
            elif IsSpaceFree(Board, row, column)==False:
                print('This position is occupied, please choose another spot:')
            else:
                choice[0]=row
                choice[1]=column
                break  
        else:
            print("Error. Please input a valid number")     
    return choice
#%%
def GenerateChildStates(Board):
    states=[]
    if IsBoardFull(Board) :
        return 0
    else:
        for i in range(len(Board)):
            for j in range(len(Board)):
                if IsSpaceFree(Board, i,j):
                    states.append([i,j])       
    return states 
#%%
def getUtility(Board, OTag):
    result=Judge(Board)
    if result==1 and OTag=='X' or result==2 and OTag=='O':
        return 1
    elif result==1 and OTag=='O' or result==2 and OTag=='X':
        return -1
    else:  
        return 0
#%%
def Recursion(N,Board, Tag, Max, OTag):
    if N == Max:
        return getUtility(Board, OTag)
    result=Judge(Board) 
    if result !=0:
        return getUtility(Board, OTag)
    scores=[]    
    BoardX=Board
    states=GenerateChildStates(Board)
    for state in states:
        BoardX[state[0]][state[1]]=Tag
        if Tag == 'X':
            scores.append(Recursion(N+1,BoardX,'O', Max, OTag))
        else:
            scores.append(Recursion(N+1,BoardX,'X', Max, OTag))
        BoardX[state[0]][state[1]]=' '
    
    if Tag != OTag:
        return min(scores)
    else:
        return max(scores)
#%%
def ComputerPlayerThink(Tag, Board):
    choice=[0,0]
    if IsBoardEmpy(Board):
        return choice
    scores=[]
    Max=int(input("Enter number of steps ahead (N>=2):"))
    states=GenerateChildStates(Board)
    BoardX=Board
    for state in states:
        BoardX[state[0]][state[1]]=Tag
        if Tag == 'X':
            scores.append(Recursion(1,BoardX,'O', Max, Tag))
        else:
            scores.append(Recursion(1,BoardX,'X', Max, Tag)) 
        BoardX[state[0]][state[1]]=' '
    for i in range(len(scores)):
        if scores[i] == max(scores):
            position=i
    choice[0]=states[position][0]
    choice[1]=states[position][1]
    return choice
#%%
def Judge(Board):
    if Board[0]==['X', 'X','X'] or Board[1]==['X', 'X','X'] or Board[2]==['X', 'X','X'] or [Board[0][0],Board[1][0],Board[2][0]]==['X', 'X','X'] or [Board[0][1],Board[1][1],Board[2][1]]==['X', 'X','X'] or [Board[0][2],Board[1][2],Board[2][2]]==['X', 'X','X'] or [Board[0][0],Board[1][1],Board[2][2]]==['X', 'X','X'] or [Board[0][2],Board[1][1],Board[2][0]]==['X', 'X','X']:
        return 1
    elif Board[0]==['O', 'O','O'] or Board[1]==['O', 'O','O'] or Board[2]==['O', 'O','O'] or [Board[0][0],Board[1][0],Board[2][0]]==['O', 'O','O'] or [Board[0][1],Board[1][1],Board[2][1]]==['O', 'O','O'] or [Board[0][2],Board[1][2],Board[2][2]]==['O', 'O','O'] or [Board[0][0],Board[1][1],Board[2][2]]==['O', 'O','O'] or [Board[0][2],Board[1][1],Board[2][0]]==['O', 'O','O']:
        return 2
    elif IsBoardFull(Board):
        return 3
    else:
        return 0      
#%%
def ShowOutcome(Outcome, NameX, NameO):
    print("Outcome:", Outcome)
    if Outcome==0:
        print('The game is still in progress')
    elif Outcome==1:
        print('The winner is ', NameX, '!')
    elif Outcome==2:
        print('The winner is ', NameO, '!')
    elif Outcome==3:
        print("Full board")
        print('Its a tie')
#%% read but do not modify this function
def Which_Player_goes_first():
    if random.randint(0, 1) == 0:
        print("Computer player goes first")
        PlayerX = ComputerPlayerThink
        PlayerO = HumanPlayer
    else:
        print("Human player goes first")
        PlayerO = ComputerPlayerThink
        PlayerX = HumanPlayer
    return PlayerX, PlayerO
#%% the game
def TicTacToeGame():
    #---------------------------------------------------    
    print("Wellcome to Tic Tac Toe Game")
    Board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    DrawBoard(Board)
    # determine the order
    PlayerX, PlayerO = Which_Player_goes_first()
    # get the name of each function object
    NameX = PlayerX.__name__
    NameO = PlayerO.__name__
    while True:
        ChoiceX=PlayerX('X',Board)
        UpdateBoard(Board, 'X', ChoiceX)
        DrawBoard(Board)
        Outcome=Judge(Board)
        ShowOutcome(Outcome, NameX, NameO)
        if Outcome!=0:
            break
        else:
            ChoiceO=PlayerO('O',Board)
            UpdateBoard(Board, 'O', ChoiceO)
            DrawBoard(Board)
            Outcome=Judge(Board)
            ShowOutcome(Outcome, NameX, NameO)
            if Outcome!=0:
                break
#%% play the game many rounds until the user wants to quit
# read but do not modify this function
def PlayGame():
    while True:
        TicTacToeGame()
        print('Do you want to play again? (yes or no)')
        if not input().lower().startswith('y'):
            break
    print("GameOver")
#%% do not modify anything below
if __name__ == '__main__':
    PlayGame()