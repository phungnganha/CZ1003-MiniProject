import random
import board_init
CarrierCount = 1
SubCount = 1
def PlayerPlacement():
    print("Welcome!")
    print("There is 1x Submarine: 3 units")
    print("There is 1x carrier: 4 units")
    print("depth of 0: surface")
    print("depth of 1: subsea")
    board_init.printPlayerPlacementBoard()
    global CarrierCount, SubCount
    while CarrierCount == 1 or SubCount == 1:
        try:
            if CarrierCount == 1 and SubCount == 1:
                choose = int(input("Carrier(0) or Submarine(1)? : "))
                if choose == 0:
                    print("You choose Carrier")
                    pos = input("Horizontal(H) or Vertical(V)? ")
                    if pos == 'H' or pos =='h':
                        UserPlaceHorizontalCarrier()
                        CarrierCount -= 1
                    elif pos == 'V' or pos =='v':
                        UserPlaceVerticalCarrier()
                        CarrierCount -= 1
                    else:
                        print("Error! Try again")
                        continue
                elif choose == 1:
                    print("You choose Submarine")
                    pos = input("Horizontal(H) or Vertical(V)? ")
                    if pos == 'H' or pos =='h':
                        UserPlaceHorizontalSub()
                        SubCount -= 1
                    elif pos == 'V' or pos =='v':
                        UserPlaceVerticalSub()
                        SubCount -= 1
                    else:
                        print("Error! Try again")
                        continue
                else:
                    print("Error! Invalid input")
                    PlayerPlacement()
            elif CarrierCount == 0 and SubCount == 1:
                print("Now, choose the direction of submarine.")
                pos = input("Horizontal(H) or Vertical(V)? ")
                if pos == 'H' or pos =='h':
                    UserPlaceHorizontalSub()
                    SubCount -= 1
                elif pos == 'V' or pos =='v':
                    UserPlaceVerticalSub()
                    SubCount -= 1
                else:
                    print("Error! Try again")
                    continue
            elif CarrierCount == 1 and SubCount == 0:
                print("Now, choose the direction of carrier.")
                pos = input("Horizontal(H) or Vertical(V)? ")
                if pos == 'H' or pos =='h':
                    UserPlaceHorizontalCarrier()
                    CarrierCount -= 1
                elif pos == 'V' or pos =='v':
                    UserPlaceVerticalCarrier()
                    CarrierCount -= 1
                else:
                    print("Error! Try again")
                    continue
        except ValueError:
            print("Invalid input! Enter numbers only")
    
def UserPlaceHorizontalCarrier():
    running = True
    while running:
        print("Choose coordinates to place your Carrier. Format is row,start_col,depth (i.e. 5,E,0). Start column is limited from A to G, Carrier can only be placed at depth 0.")
        user = input("Enter Coordinates: ")
        row,start_col,depth = user.split(',')
        row,depth = int(row),int(depth)
        start_col = ConvertColumn(start_col)
        pos = 'h'
        if CheckValidityPlacementCarrier(row,start_col,depth,pos) == 3:
            print("Error! Invalid Coordinates!")
            return UserPlaceHorizontalCarrier()
        elif CheckValidityPlacementCarrier(row,start_col,depth,pos) == 2:
            print("Error! Coordinates overlap with Submarine! Try again")
            return UserPlaceHorizontalCarrier()
        else:
            for x in range(4):
                board_init.player_placement_board[depth][row][start_col] = 'C'
                start_col +=1
            board_init.printPlayerPlacementBoard()
            return 0
        

def UserPlaceVerticalCarrier():
    running = True
    while running:
        print("Choose coordinates to place your Carrier. Format is start_row,column,depth (i.e. 5,E,0). Start row is limited from 1 to 7, Carrier can only be placed at depth 0.")
        user = input("Enter Coordinates: ")
        start_row,col,depth = user.split(',')
        start_row,depth = int(start_row),int(depth)
        col = ConvertColumn(col)
        pos = 'v'
        if CheckValidityPlacementCarrier(start_row,col,depth,pos) == 3:
            print("Error! Invalid Coordinates!")
            return UserPlaceVerticalCarrier()
        elif CheckValidityPlacementCarrier(start_row,col,depth,pos) == 2:
            print("Error! Coordinates overlap with Submarine! Try again")
            return UserPlaceVerticalCarrier()
        else:
            for x in range(4):
                board_init.player_placement_board[depth][start_row][col] = 'C'
                start_row += 1
            board_init.printPlayerPlacementBoard()
            return 0

def UserPlaceHorizontalSub():
    running = True
    while running:
        print("Choose coordinates to place your Submarine. Format is  row,start_col,depth (i.e. 5,E,1). Start column is limited from A to H, Sub can be placed at depth 0 or 1.")
        user = input("Enter Coordinates: ")
        row,start_col,depth = user.split(',')
        row,depth = int(row),int(depth)
        start_col = ConvertColumn(start_col)
        pos = 'h'
        if CheckValidityPlacementSub(row,start_col,depth,pos) == 3:
            print("Error! Invalid Coordinates!")
            return UserPlaceHorizontalSub()
        elif CheckValidityPlacementSub(row,start_col,depth,pos) == 2:
            print("Error! Coordinates overlap with Carrier! Try again")
            return UserPlaceHorizontalSub()
        else:
            for x in range(3):
                board_init.player_placement_board[depth][row][start_col] = 'S'
                start_col +=1
            board_init.printPlayerPlacementBoard()
            return 0
def UserPlaceVerticalSub():
    running = True
    while running:
        print("Choose coordinates to place your Submarine. Format is start_row,column,depth (i.e. 5,E,1). Start row is limited from 1 to 8, Sub can be placed at depth 0 or 1.")
        user = input("Enter Coordinates: ")
        start_row,col,depth = user.split(',')
        start_row,depth = int(start_row),int(depth)
        col = ConvertColumn(col)
        pos = 'v'
        if CheckValidityPlacementSub(start_row,col,depth,pos) == 3:
            print("Error! Invalid Coordinates!")
            return UserPlaceVerticalSub()
        elif CheckValidityPlacementSub(start_row,col,depth,pos) == 2:
            print("Error! Coordinates overlap with Carrier! Try again")
            return UserPlaceVerticalSub()
        else:
            for x in range(3):
                board_init.player_placement_board[depth][start_row][col] = 'S'
                start_row += 1
            board_init.printPlayerPlacementBoard()
            return 0

def CheckValidityPlacementCarrier(y,x,z,pos):
    if pos == 'v':
        for i in range (4):
            if (y not in range(1,11)) or (x not in range(1,11)) or (z!=0):
                return 3
            elif board_init.player_placement_board[z][y][x] == 'S':
                return 2
            y += 1
        else:
            return 0
    elif pos == 'h':
        for i in range (4):
            if (y not in range(1,11)) or (x not in range(1,11)) or (z!=0):
                return 3
            elif board_init.player_placement_board[z][y][x] == 'S':
                return 2
            x += 1
        else:
            return 0
        
def CheckValidityPlacementSub(y,x,z,pos):
    if pos == 'v':
        for i in range (3):
            if (y not in range(1,11)) or (x not in range(1,11)) or (z not in range (2)):
                return 3
            elif board_init.player_placement_board[z][y][x] == 'C':
                return 2
            y += 1
        else:
            return 0
    elif pos == 'h':
        for i in range (3):
            if (y not in range(1,11)) or (x not in range(1,11)) or (z not in range (2)):
                return 3
            elif board_init.player_placement_board[z][y][x] == 'C':
                return 2
            x += 1
        else:
            return 0

def ComValidityPlacementSub(y,x,z,pos):
    if pos == 'v':
        for i in range (3):
            if (y not in range(1,11)) or (x not in range(1,11)) or (z not in range (2)):
                return 3
            elif board_init.computer_placement_board[z][y][x] == 'C':
                return 2
            y += 1
        else:
            return 0
    elif pos == 'h':
        for i in range (3):
            if (y not in range(1,11)) or (x not in range(1,11)) or (z not in range (2)):
                return 3
            elif board_init.computer_placement_board[z][y][x] == 'C':
                return 2
            x += 1
        else:
            return 0
def ComPlaceCarrier():
    pos = random.randint(0,1)
    if pos == 0: #Horizontal placement
        row,col,depth = random.randint(1,10),random.randint(1,7),0
        for x in range(4):
            board_init.computer_placement_board[depth][row][col] = 'C'
            col += 1
        return 0
    elif pos ==1: #Vertical placement
        row,col,depth = random.randint(1,7),random.randint(1,10),0
        for x in range(4):
            board_init.computer_placement_board[depth][row][col] = 'C'
            row += 1
        return 0

def ComPlaceSub():
    pos = random.randint(0,1)
    if pos == 0: #Horizontal placement
        pos = 'h'
        row,col,depth = random.randint(1,10),random.randint(1,8),random.randint(0,1)
        if ComValidityPlacementSub(row,col,depth,pos)==3:
            print("Error! Invalid Coordinates!")
            return ComPlaceSub()
        elif ComValidityPlacementSub(row,col,depth,pos) == 2:
            #Error! Coordinates overlap with Carrier! Try again
            return ComPlaceSub()
        else:
            for x in range(3):
                board_init.computer_placement_board[depth][row][col] = 'S'
                col += 1
            return 0

    elif pos ==1: #Vertical placement]
        pos = 'v'
        row,col,depth = random.randint(1,8),random.randint(1,10),random.randint(0,1)
        if ComValidityPlacementSub(row,col,depth,pos)==3:
            print("Error! Invalid Coordinates!")
            return ComPlaceSub()
        elif ComValidityPlacementSub(row,col,depth,pos) == 2:
            print("Error! Coordinates overlap with Carrier! Try again")
            return ComPlaceSub()
        else:
            for x in range(3):
                board_init.computer_placement_board[depth][row][col] = 'S'
                row += 1
            return 0
def ConvertColumn(col):
    try:
        i = col.upper()
        convert = ord(i)-ord('A') +1
        return convert
    except:
        return 13

def ComPlace():
    while True:
        ComPlaceCarrier()
        ComPlaceSub()
        return 0
if __name__ == '__main__':

    PlayerPlacement()
    ComPlace()
