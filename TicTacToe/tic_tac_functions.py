from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])  
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])
    
    pass

def player_input():    
    '''
    ('X', 'O') or ('O','X') - player1 and player2 markers
    '''
    marker = ''
    tup = ('#', '#')
    while marker != 'X' and marker != 'O':
        marker = input("Please enter 'X' or 'O'").upper()
        if marker == 'X':
            tup =  ('X', 'O')            
        elif marker == 'O':
            tup = ('O', 'X')
        else:
            pass
    
    return tup

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    if (board[1] == board[2] == board[3] == mark) or \
        (board[4] == board[5] == board[6] == mark) or \
        (board[7] == board[8] == board[9] == mark) or \
        (board[1] == board[4] == board[7] == mark) or \
        (board[2] == board[5] == board[8] == mark) or \
        (board[3] == board[6] == board[9] == mark) or \
        (board[1] == board[5] == board[9] == mark) or \
        (board[7] == board[5] == board[3] == mark):        
        return True
    else:
        return False

def choose_first():
    choice = random.randint(1,2)
    return choice

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    if ' ' not in board:
        return True
    else:
        return False
    pass

def player_choice(board):
    position = 0
    while not space_check(board, position) or position not in range(1,10):
        position = input("Please enter next position from 1 to 9:")
    
    return position

def replay():
    answer = input("Please enter Y if you want to play again")
    if answer.upper() == 'Y':
        return True
    else:
        return False
