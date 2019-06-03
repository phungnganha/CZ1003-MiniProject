from time import sleep
from random import randint
import board_init
import Ship_Placement_myway

GameState = 1  # 1 is on, 0 is off or game over
Player = 1
ComputerCarrierHealth = PlayerCarrierHealth = 4
ComputerSubHealth = PlayerSubHealth = 3


def ShowPlayerTurn (Player): # Function to print whose turn it is
    if (Player%2) == 1: # Player's turn
        print ("Your turn!")
        sleep(1)
    else:   # Even number indicates computer's turn
        print ("Computer's turn!")
        sleep(1)

def PlayerInput (Player): # Function to ask for input to fire
    if (Player%2) == 1:
        while True:
            try:
                print("Enter the coordinate to fire upon in the following format (row,col,depth). E.g. 3,E,0:")
                print("Note: depth 0 represents subsea level, depth 1 represents surface level")
                FirePoint = input("Enter the coordinate you wish to fire upon:")
                stry,strx,strz = FirePoint.split(',') #Split the string
                y,z = int(stry), int(strz)  #Change variable type to integer
                x = Ship_Placement_myway.ConvertColumn(strx)
                if CheckValidityPlayer(y,x,z) == 0:
                        print("Firing!")
                        return y, x, z
                elif CheckValidityPlayer(y,x,z) == 1:
                        print("Coordinate has already been hit. Please enter a different coordinate!")
                        return(PlayerInput(Player))
                elif CheckValidityPlayer(y,x,z) == 2:
                        print("Error! Please enter valid input!")
                        return(PlayerInput(Player))
                else:
                        print("Error! Check program")
            except ValueError:
                print("Invalid input! Enter numbers only in the following format, e.g. 3,E,0.")
    else: #Randomise input of computer
        y,x,z = randint(1,10), randint(1,10), randint(0,1)
        if CheckValidityCom(y,x,z) == 0:
            print("Firing!")
            return y, x, z
        elif CheckValidityCom(y,x,z) == 1: #coordinate already hit
            return(PlayerInput(Player))
        elif CheckValidityCom(y,x,z) == 2: #coordinate not in range (should not happen)
            return(PlayerInput(Player))
        else:
            print("Error! Check program")
def CheckValidityPlayer(y,x,z):

    #if  (y not in range [1,11]) or (x not in range [1,11]) or (z not in range [0,2]): #coordinate out of range (invalid)
    if  (y<1) or (y>10) or (x<1) or (x>10) or (z<0) or (z>1):
        return 2
    elif board_init.player_targeting_board[z][y][x] == 'H' or board_init.player_targeting_board[z][y][x] == 'X': #coordinate has already been hit
        return 1
    else: #coordinate checks out
        return 0
    
def CheckValidityCom(y,x,z):

    if  (y<1) or (y>10) or (x<1) or (x>10) or (z<0) or (z>1):
        return 2
    elif board_init.computer_targeting_board[z][y][x] == 'H' or board_init.computer_targeting_board[z][y][x] == 'X': #coordinate has already been hit
        return 1
    else: #coordinate checks out
        return 0
    
        
def CheckGame(): #Check if player or computer has won the game
    global ComputerCarrierHealth
    global ComputerSubHealth
    global PlayerCarrierHealth
    global PlayerSubHealth
    if ComputerCarrierHealth == 0 and ComputerSubHealth == 0:
        print("Victory! Congratulations!")
        sleep(5)
        quit()
        return 0
    elif PlayerCarrierHealth == 0 and  PlayerSubHealth == 0:
        print("Defeat! Better luck next time!")
        sleep(5)
        quit()
        return 0
    else:
        return 1

def PrintBoard(Player):
    if Player%2 == 1:
        board_init.printPlayerTargetingBoard()
    else:
        board_init.printPlayerPlacementBoard()
        
def FireCannons(y,x,z,Player): #Change S, C, and w to H and X where applicable --> S to H means sub health -1, --> C to H means ship health -1
    global ComputerCarrierHealth
    global ComputerSubHealth
    global PlayerCarrierHealth
    global PlayerSubHealth
    count = 0
    if Player%2 == 1: #Player's turn - Use variables for Player
        PlacementBoard = board_init.computer_placement_board
        TargetingBoard = board_init.player_targeting_board
        if y == 1:
            minY = 1
        else:
            minY = y-1
        if x == 1:
            minX = 1
        else:
            minX = x-1
        if y == 10:
            maxY = 11
        else:
            maxY = y+2
        if x == 10:
            maxX = 11
        else:
            maxX = x+2
        for i in range (minY, maxY):
            for j in range (minX, maxX):
                if PlacementBoard[z][i][j] == 'S':
                    TargetingBoard[z][i][j] = 'H'
                    PlacementBoard[z][i][j] = 'H'
                    ComputerSubHealth -= 1
                    count += 1
                elif PlacementBoard[z][i][j] == 'C':
                    TargetingBoard[z][i][j] = 'H'
                    PlacementBoard[z][i][j] = 'H'
                    ComputerCarrierHealth -= 1
                    count += 1
                elif PlacementBoard[z][i][j] == ' ':
                    TargetingBoard[z][i][j] = 'X'
                    PlacementBoard[z][i][j] = 'X'
        PrintBoard(Player)
        print ('You registered ', count,' hits on the computer!')
        print ('Computer Carrier condition:', ComputerCarrierHealth, '/4')
        print ('Computer Submarine condition:', ComputerSubHealth, '/3')
    else: #Computer's turn - Use variables for Computer

        PlacementBoard = board_init.player_placement_board
        TargetingBoard = board_init.computer_targeting_board
        if y == 1:
            minY = 1
        else:
            minY = y-1
        if x == 1:
            minX = 1
        else:
            minX = x-1
        if y == 10:
            maxY = 11
        else:
            maxY = y+2
        if x == 10:
            maxX = 11
        else:
            maxX = x+2
        for i in range (minY, maxY):
            for j in range (minX, maxX):
                if PlacementBoard[z][i][j] == 'S':
                    TargetingBoard[z][i][j] = 'H'
                    PlacementBoard[z][i][j] = 'H'
                    PlayerSubHealth -= 1
                    count += 1
                elif PlacementBoard[z][i][j] == 'C':
                    TargetingBoard[z][i][j] = 'H'
                    PlacementBoard[z][i][j] = 'H'
                    PlayerCarrierHealth -= 1
                    count += 1
                elif PlacementBoard[z][i][j] == ' ':
                    TargetingBoard[z][i][j] = 'X'
                    PlacementBoard[z][i][j] = 'X'
        PrintBoard(Player)
        print ('Computer registered ', count,' hits on you!')
        print ('Your Carrier condition:', PlayerCarrierHealth, '/4')
        print ('Your Submarine condition:', PlayerSubHealth, '/3')


def GamePlay():
    Ship_Placement_myway.PlayerPlacement()
    Ship_Placement_myway.ComPlace()
    global GameState
    global Player
    while GameState == 1:

        ShowPlayerTurn(Player)
        y, x, z = PlayerInput(Player)
        #stry,strx,strz = FirePoint.split(',')
        #y,x,z = int(stry), int(strx), int(strz) 
        FireCannons(y,x,z,Player)
        GameState = CheckGame()
        Player += 1

if __name__ == '__main__':
    GamePlay()
    
