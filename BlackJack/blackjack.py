from deck import Deck
from player import Player
from dealer import Dealer

print('Welcome to Black Jack!')

        
#Ready to play?
ready = input("Ready to play Black Jack? Enter Y or N:").upper()
initial_game = True
if ready == 'Y':
    game_on = True
else:
    game_on = False    

while game_on: 
    #prepare deck
    new_deck = Deck()

    new_deck.ShuffleDeck()

    #draw initial 2 cards for player and dealer  
    if initial_game:
        pl_hand = Player()
        pl_hand.CreateHand(new_deck)
        print(pl_hand)
    else:
        pl_hand.hand = []
        dealer_hand.hand = []
        pl_hand.CreateHand(new_deck)
        print(pl_hand)

    dealer_hand = Dealer(new_deck)
    dealer_hand.CreateHand()
    print(dealer_hand)

    pl_total = 0
    pl_total = pl_hand.CalculateTotal()
    print("Player Cards total: " + str(pl_total))
    #Note: we don't display dealer's card total at this time
    #since 1 of dealers card is hidden

    #Ask player to make a bet and check if amount 
    #not exceeding balance
    input_valid = False
    while not input_valid:
        try:
            bet_amount = int(input("Please enter bet amount:"))
            pl_hand.Bet(bet_amount)
            input_valid = True
        except:
            print("Invalid bet amount!")
            continue

    #Loop and Ask player to Hit(bet) or Stop - exits loop
    hit_stop = ''
    selection_valid = False  
    while not selection_valid and hit_stop != 'S':        
        hit_stop = input("Please enter H(for Hit) or S(for Stop):").upper()
        if hit_stop == 'H':
            #Draw another card
            pl_hand.DrawCard(new_deck)
            print(pl_hand)

            pl_total = pl_hand.CalculateTotal()
            print("Player Cards total: " + str(pl_total))
            if pl_total > 21:
                print("You are BUSTED. Game over!")
                game_on = False
                break
            else:
                continue

        elif hit_stop == 'S':
            selection_valid = True
        else:
            continue
            
    #If Player total > than dealer total, dealer drows more
    #cards until deler either bust or >= player total and <= 21
    dealer_total = dealer_hand.CalculateTotal()
    if dealer_total >= pl_total and pl_total <= 21:
        print("Dealer total: " + str(dealer_total))
        print("Dealer WON. Game over!")
        dealer_hand.PrintAll()
        pl_hand.DisplayBalance()
        
        game_on = False        
    else:
        while dealer_total < pl_total and pl_total <= 21:
            dealer_hand.DrawCard(new_deck)
            print(dealer_hand, True)

            dealer_total = dealer_hand.CalculateTotal()
            if dealer_total > 21:
                pl_hand.BetWon()
                pl_hand.DisplayBalance()
                print("You WON. Game over!")                          
                game_on = False
                break
            elif dealer_total >= pl_total:                
                print("You LOST. Game over!")
                dealer_hand.PrintAll()
                pl_hand.DisplayBalance()
                game_on = False
                break
            else:
                continue   
        
    replay = input("Do you want to play another game? Y(yes) or N(no):").upper() 
    if replay == 'Y':
        game_on = True 
        initial_game = False                  
        continue
    else:
        game_on = False
        break