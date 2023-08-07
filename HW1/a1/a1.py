""" A fancy tic-tac-toe game for CSSE1001/7030 A1. """
from constants import *

Board = list[list[str]]
Pieces = list[int]
Move = tuple[int, int, int]

def num_hours() -> float:
    return

def generate_initial_pieces(num_pieces: int) -> Pieces:
# generate initial pieces for both player in range of 5~9
    if num_pieces >= 5 and num_pieces <= 9:
        return list(range(1, num_pieces +1))

def initial_state() -> Board:
    ## generate the n * n playing white_board based on grid_size
    white_board = []
    for i in range(GRID_SIZE):
        white_board.append([])
        for j in range(GRID_SIZE):
            white_board[i].append(" ")
    return white_board
        
def place_piece(board: Board, player: str, pieces_available: Pieces, move: Move ) -> None:
    #put number on the board and delete the number in the available list
    if player == "NAUGHT":
        board[move[0]][move[1]] = "O" + str(move[2])
    else: # player == CROSS
         board[move[0]][move[1]] = "X" + str(move[2])
    del pieces_available[move[2]-1]
    return

def print_game(board: Board, naught_pieces: Pieces, cross_pieces: Pieces)-> None:
    # generate the player info
    str_list_O = ", ".join(map(str,naught_pieces))
    str_list_X = ", ".join(map(str,cross_pieces))
    sep_line = "  " + "---"* GRID_SIZE
    

    print("O has: " + str_list_O)
    print("X has: " + str_list_X)
    
    #generate the first and second line (not the board)
    first_row = "   "
    for i in range(1,GRID_SIZE + 1):
        first_row += (str(i) + "  ")

    print(first_row)
    print(sep_line)

    # show the board in 2D view
    for i,row in enumerate(board, start=1):
       formatted_row = [f"{item:2}" for item in row] # use item:2 to ensure the width equal to 2
       print(f"{i}|{'|'.join(formatted_row)}|")
       print(sep_line)

    return

def process_move(move: str) -> Move :
    error_message = ""
    if len(move) != 5 or move[1] != " " or move[3] != " " or move.count(" ") !=2:
        error_message = INVALID_FORMAT_MESSAGE
    else:
        for i,element in enumerate(move):
            if i == 0:
                if element.isdigit() == False:
                    error_message = INVALID_ROW_MESSAGE
                    break
                else: 
                    if int(element) > (GRID_SIZE +1) or int(element) ==0:
                        error_message = INVALID_ROW_MESSAGE
                        break
            if i == 2:
                if element.isdigit() == False:
                    error_message = INVALID_COLUMN_MESSAGE
                    break
                else:
                    if int(element) > (GRID_SIZE +1) or int(element) ==0:
                        
                        error_message = INVALID_COLUMN_MESSAGE
                        break
            if i == 4:
                if element.isdigit() == False:
                    error_message = INVALID_SIZE_MESSAGE
                else:
                    if int(element)> 6: #modify
                     error_message = INVALID_SIZE_MESSAGE
                     
    if error_message != "":
        return error_message
    else:
        strlist_move = move.split()
        intlist_move = [int(i) for i in strlist_move]
        intlist_move[0]-= 1
        intlist_move[1] -= 1
        tuple_move = tuple(intlist_move)
        
        return tuple_move
    
def get_player_move() -> Move:
    my_move = input("Enter your move:")
    if my_move == "h" or my_move == "H":
        print("Enter a row, column & piece size in the format: row col size")
    else:
        print(process_move(my_move))
    return

def main() -> None:
    # Write your main code here
    my_board = initial_state()
    player1 = "NAUGHT"
    player2 = "CROSS"
    my_naught_pieces = generate_initial_pieces(7)
    my_cross_pieces = generate_initial_pieces(7)
    
    # place_piece(my_board,player1,my_naught_pieces,(1,1,3))
    

    # print(print_game(my_board,my_naught_pieces,my_cross_pieces))

    # place_piece(my_board,player2,my_cross_pieces,(1,1,3))
    # print(print_game(my_board,my_naught_pieces,my_cross_pieces))
    get_player_move()
    
    pass


if __name__ == '__main__':
    main()
