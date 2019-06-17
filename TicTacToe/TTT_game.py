from  tic_tac_functions import *
print('Welcome to Tic Tac Toe!')
continue_game = True
while continue_game:    
    
    # Set the game up here; empty board, who's first and markers choice
    board = [' ']*10
    display_board(board)
    #select which player goes 1st
    choice = choose_first()    
    print("Player " + str(choice) + " selected to go 1st")
    #Ready to play?
    ready = input("Ready to play? Enter Y or N").upper()
    if ready == 'Y':
        game_on = True
    else:
        game_on = False
        continue_game = False
        break
    
    #get markers
    player1_marker = ''
    player2_marker = ''
    player1_marker,player2_marker = player_input()   
            
    #game_on = True
    while game_on:
        if choice == 1:
            
            #Player 1 Turn
            position = int(input("Please enter position from 1 to 9"))
            if not space_check(board, position):
                print("Position already taken")
                continue            
            else:
                #mark the position
                board[int(position)] = player1_marker 
                display_board(board)                
                #check if P1 won
                if win_check(board, player1_marker):
                    print("Player 1. Game over")
                    game_on = False
                    break
                #check for TIE GAME
                elif full_board_check(board):
                    print("TIE GAME")
                    game_on = False
                    break
                else:
                    #Switch to P2 and continue
                    choice = 2 
                    continue
                        
        # Player2's turn.
        else:
            position = int(input("Please enter position from 1 to 9"))
            if not space_check(board, position):
                print("Position already taken")
                continue            
            else:
                #mark the position
                board[int(position)] = player2_marker 
                display_board(board)                
                #check if P2 won
                if win_check(board, player2_marker):
                    print("Player 2. Game over")
                    game_on = False
                    break
                #check for TIE GAME
                elif full_board_check(board):
                    print("TIE GAME")
                    game_on = False
                    break
                else:
                    #Switch to P2 and continue
                    choice = 1 
                    continue                                

        if not replay():  
            continue_game = False      
            break
        else:
            game_on = True
            continue
