
#Zoe Chow, 014

#importing chess.py
from chess import print_board

#list of letter rows from the chess.py file
letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
#current turn bool
turn = "Clear"
piece_moved = False

#~~~~~~~~~~~Part A~~~~~~~~~~~~~~
#piece dictionaries
clear_piece_locations = {
    "A1": "rook", "A2": "knight", "A3": "bishop", "A4": "queen",
    "A5": "king", "A6": "bishop", "A7": "knight", "A8": "rook",
    "B1": "pawn", "B2": "pawn", "B3": "pawn", "B4": "pawn",
    "B5": "pawn", "B6": "pawn", "B7": "pawn", "B8": "pawn"
    }

filled_piece_locations = {
    "H1": "rook", "H2": "knight", "H3": "bishop", "H4": "king",
    "H5": "queen", "H6": "bishop", "H7": "knight", "H8": "rook",
    "G1": "pawn", "G2": "pawn", "G3": "pawn", "G4": "pawn",
    "G5": "pawn", "G6": "pawn", "G7": "pawn", "G8": "pawn"
    }

#~~~~~~~~~~~~~~Part B~~~~~~~~~~~~~
#Function for getting piece at coordinate
def get_piece_at_coordinate(coordinate):
    #take the list of rows from print_board

    #coordinate[0] = letter row
    #coordinate[1:] = number
    
    #check if row and column are on the board
    if coordinate[0] in letters and int(coordinate[1:]) in range(1, 9):
        #check location dict of clear pieces
        if coordinate in clear_piece_locations.keys():
            #return the clear piece if occupied
            return "Clear " + clear_piece_locations[coordinate]
        #check location dict of filled pieces
        elif coordinate in filled_piece_locations.keys():
            #return filled piece if occupied
            return "Filled " + filled_piece_locations[coordinate]
        #if coord not in clear or filled dicts, the cell is empty
        else:
            return "empty"
    #if the coord is invalid, return empty
    else:
        return "empty"

#~~~~~~~~~~~~~~Part C~~~~~~~~~~~~~~~~
#function for checking legal coords
def is_legal_coordinate(coordinate):
    #the same thing but shorted from my prev function
    if coordinate[0] in letters and int(coordinate[1:]) in range(1, 9):
        return True
    else:
        return False

#~~~~~~~~~~~Part D~~~~~~~~~~~~~~~
#function for moving chess pieces
def move_piece(start, end):
    #check if the move is within bounds by using legal cord function on start and end
    if is_legal_coordinate(start) and is_legal_coordinate(end):
        #get piece to move by using the get_piece function at start
        piece_check = get_piece_at_coordinate(start)
        #get piece to remove by using get_piece function at end
        piece_remove = get_piece_at_coordinate(end)

        #check if there are pieces at the end pos
        #if "Clear" then remove from clear dict
        if "Clear" in piece_remove:
            del clear_piece_locations[end]
        #if "Filled" remove from filled dict
        elif "Filled" in piece_remove:
            del filled_piece_locations[end]

        #check which dict to update the position
        if "Clear" in piece_check:
            #if clear, extract the old pair and delete
            piece = clear_piece_locations.pop(start)
            #replace with updated pair
            clear_piece_locations[end] = piece
        #else if it is filled
        elif "Filled" in piece_check:
            #extract and del old pair
            piece = filled_piece_locations.pop(start)
            #update with new pair
            filled_piece_locations[end] = piece
        #if it is empty
        else:
            print("There is no piece to move at this position")
    #if it is invalid
    else:
        print("That is not a valid move")

#~~~~~~~~~~~~Part E~~~~~~~~~~~~
#function for checking friendly fire
def is_friendly_fire(start, end):
    #assign the values of the 2 pieces
    piece_1 = get_piece_at_coordinate(start)
    piece_2 = get_piece_at_coordinate(end)

    #if both are Clear or both are Filled, return true
    if "Clear" in piece_1 and "Clear" in piece_2 or "Filled" in piece_1 and "Filled" in piece_2:
        return True
    #if not its not friendly fire
    else:
        return False

#~~~~~~~~~~~~~Part F~~~~~~~~~~~~
#function for checking illegal jumps
def is_illegal_jump(start, end):
    #store the two pieces at the start and end
    piece_1 = get_piece_at_coordinate(start)
    piece_2 = get_piece_at_coordinate(end)
    
    #variable for checking legality
    illegal = False

    #generate list of columns (1-8) between start and end
    #convert the number half of coord into ints and find range between
    #if the start clumn is smaller than the end column
    if int(start[1:]) < int(end[1:]):
        in_between_columns = list(range(int(start[1:]), int(end[1:]) + 1))
    #else generate it in reverse
    else:
        in_between_columns = list(range(int(start[1:]), int(end[1:]) - 1, -1))
        #this process avoids the lists generating incorrectly
        
    #generate list of rows (A-H) between start and end
    #convert the first part of the coord into unicode and make a list
    #if the starting letter is smaller than the end row
    if start[0] < end[0]:
        in_between_rows = [chr(code) for code in range(ord(start[0]), ord(end[0]) + 1)]
    #else generate in reverse
    else:
        in_between_rows = [chr(code) for code in range(ord(start[0]), ord(end[0]) - 1, -1)]
        #needed to avoid incorrect generation

    #if the piece is a knight, illegal is false
    if "knight" in piece_1:
        return False
    #if it is not a knight
    else:
        #for every row in between start and end
        for row in in_between_rows:
            #and for every column between start and end on that row
            for column in in_between_columns:
                #the current coord joins the two momentarily
                current_pos = row + str(column)
                #if there is a piece in that coord when it is not the start or end, the jump is illegal
                if get_piece_at_coordinate(current_pos) != "empty" and current_pos != start and current_pos != end:
                    illegal = True

        #after the check, return appropriate value depending on illegal bool
        if illegal:
            return True
        else:
            return False

#~~~~~~~~~~~Part G~~~~~~~~~~~~~
#function for piece type movement
def piece_type_can_move(start, end):
    #find the piece at the start coord
    piece = get_piece_at_coordinate(start)

    #if it is a rook, it can only move if
    if "rook" in piece:
        #same row or same column
        if end[0] == start[0] or end[1:] == start[1:]:
            return True
        #else it cant
        else:
            return False

    #if it is a bishop, it can only move if
    if "bishop" in piece:
        #the absolute value of the difference between the start and end row
        #and the absolute val of the diff between start and end column are equal
        if abs(ord(start[0]) - ord(end[0])) == abs(int(start[1:]) - int(end[1:])):
            return True
        #else it cant
        else:
            return False

    #if it is a queen, it can move if
    if "queen" in piece:
        #in a straight line or if diagonal
        if end[0] == start[0] or end[1:] == start[1:] or abs(ord(start[0]) - ord(end[0])) == abs(int(start[1:]) - int(end[1:])):
            return True
        else:
            return False

    #if it is a king, it can move if
    if "king" in piece:
        #vertical by 1, horizontal by 1, or diagonal by 1
        if end[0] == start[0] and abs(int(start[1:]) - int(end[1:])) == 1 or end[1:] == start[1:] and abs(ord(start[0]) - ord(end[0])) == 1 or abs(ord(start[0]) - ord(end[0])) == abs(int(start[1:]) - int(end[1:])) and abs(ord(start[0]) - ord(end[0])) == 1:
            return True
        else:
            return False

    #if it is a knight, it can move if
    if "knight" in piece:
        #the abs value diff between rows = 2 and columns is 1 or when the abs value diff is 1 and 2
        if abs(ord(start[0]) - ord(end[0])) == 2 and abs(int(start[1:]) - int(end[1:])) == 1 or abs(ord(start[0]) - ord(end[0])) == 1 and abs(int(start[1:]) - int(end[1:])) == 2:
            return True
        else:
            return False

    #if it is a pawn
    if "pawn" in piece:
        #check if it is straight line or diagonal by 1 and there is enemy
        if end[1:] == start[1:] or abs(int(start[1:]) - int(end[1:])) == 1 and get_piece_at_coordinate(end) != "empty":
            #determine if it is clear or filled
            #if clear and end row is bigger unicode value
            #or if filled and end row is smaller unicode value
            if "Clear" in piece and ord(end[0]) == ord(start[0]) + 1 or "Filled" in piece and ord(end[0]) == ord(start[0]) - 1:
                #then it has moved forward 1 depending on clear or filled
                return True
            else:
                #prevents it from moving backwards
                return False
        #if its not diag or straight by 1
        else:
            #no bueno
            return False

#~~~~~~~~~~~~~~~Part H and J~~~~~~~~~~~~~~~~~
#the Avengers Assemble function of all the previous ones
#start coord, end coord, which side
def move_if_valid(start, end, turn):
    global piece_moved

    #variable for Turn status
    Turn = str.title(turn)
    #piece to reference
    piece = get_piece_at_coordinate(start)
    #bool to allow the move
    move_it = False
    piece_moved = False

    #if it is a valid turn
    if Turn == "Clear" or Turn == "Filled":
        #determine which side to move
        if Turn in piece:
            #if both coordinates are legal
            if is_legal_coordinate(start) and is_legal_coordinate(end):
                #if not friendly fire
                if not is_friendly_fire(start, end):
                    #if not illegal jump
                    if not is_illegal_jump(start, end):
                        #if it is the correct move type
                        if piece_type_can_move(start, end):
                            #set the bool to True           
                            move_it = True
                        #if the move is the wrong type
                        else:
                            print("Invalid move pattern")
                    #if illegal jump
                    else:
                        print("Illegal jump, can't move")
                #if friendly fire
                else:
                    print("You cannot take your own piece")
            #if not a valid coordinate
            else:
                print("Those are not valid coordinates")
        #if not a valid piece
        else:
            print("There is no piece on this coordinate")
    #if not a valid turn type
    else:
        print("Invalid turn type")

    #if all confitions are valid
    if move_it:
        #move the function
        move_piece(start, end)

        #if after the move it is checked
        if is_checked(Turn):
            #move it back
            move_piece(end, start)
            #inform the player
            print("Move results in king being checked")
        else:
            piece_moved = True
            print("Move successful")
            

#~~~~~~~~~~Part I~~~~~~~~~~~~~~~~
#king is checked function
def is_checked(side):
    #bool for seeing if checked
    checked = False

    #if the side chosen is clear
    if str.title(side) == "Clear":
        #for key values in clear piece dict
        for key, value in clear_piece_locations.items():
            #find the king
            if value == "king":
                #save the key coord
                king = key

        #for every piece in filled pieces dict
        for key, value in filled_piece_locations.items():
            #check for no illegal jumps and possible moves for each piece
            #between the fill key coord and the coord of the king
            if is_illegal_jump(key, king) == False and piece_type_can_move(key, king):
                #if there is, checked is true
                checked = True

    #repeat same thing for filled
    #if the side chosen is filled
    elif str.title(side) == "Filled":
        #for every pair in filled, find the king
        for key, value in filled_piece_locations.items():
            if value == "king":
                king = key
                
        #check every piece in clear
        for key, value in clear_piece_locations.items():
            #if no illegal jumps or possible moves
            if is_illegal_jump(key, king) == False and piece_type_can_move(key, king):
                checked = True

    #if any checks found, return true
    if checked:
        return True
    else:
        return False

#~~~~~~~~~~Part K~~~~~~~~~~~
#the win check function
def has_won(side):
    #bool for winning
    won = False

    #if the side is clear
    if str.title(side) == "Clear":
        #for key values in filled piece dict
        for key, value in filled_piece_locations.items():
            #check for king
            if value == "king":
                #if found, won is false
                won = False
                #stop iterating through
                break
            #if it is not found
            else:
                #won is true
                won = True

    #same thing for filled
    if str.title(side) == "Filled":
        #check clear dict
        for key, value in clear_piece_locations.items():
            #find the king
            if value == "king":
                #if found its false
                won = False
                break
            #else its won
            else:
                won = True

    #if it is not won, return false else true
    if won == False:
        return False
    else:
        return True

#~~~~~~~~~~Part L and M~~~~~~~~~~~
#function for playing the game
def play_game():
    #ensure the function is referencing the global vars
    global turn
    global piece_moved

    #list for pawns to be updated
    keys_to_update = []

    #loop until a valid move is made
    while True:
        #heading + text info
        print()
        print(f"Turn: {turn}")
        #inputs for coords
        start = input("Move start Coordinate: ")
        end = input("Move end Coordinate: ")

        #move according to the coords
        move_if_valid(start, end, turn)
        #print board
        print_board(clear_piece_locations, filled_piece_locations)

        #if the piece was successfully moved
        if piece_moved:
            #check for any clear pawns at row H
            for key, value in clear_piece_locations.items():
                if key[0] == "H" and value == "pawn":
                    #add to the update list
                    keys_to_update.append(key)

            #check for any filled pawns at row A
            for key, value in filled_piece_locations.items():
                if key[0] == "A" and value == "pawn":
                    #add to the update list
                    keys_to_update.append(key)

            # update the pawns to queens
            for key in keys_to_update:
                #update clear and fileld pawns
                clear_piece_locations[key] = "queen"
                filled_piece_locations[key] = "queen"
            
            #check for win con
            if has_won(turn):
                return f"{turn} has won!"
                #end function
                break
            else:
                #change the turn depending on clear or filled
                if turn == "Clear":
                    turn = "Filled"
                elif turn == "Filled":
                    turn = "Clear"












    
