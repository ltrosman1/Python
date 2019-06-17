'''Create Player Hand
Automatically draw 1st two cards from deck
Pass initial amount to keep track of player betting balance
'''
from deck import Deck
class Player(Deck):
    balance = 0
    initial_balance = 1000
    hand = []
    player_deck = Deck()
    last_bet = 0

    def __init__(self):
        self.balance = self.initial_balance    

    def CreateHand(self, deck):
        self.player_deck = deck
            #Draw 1st two cards
        self.hand.append(self.player_deck.DrawCard())
        self.hand.append(self.player_deck.DrawCard())
      
    def DrawCard(self, player_deck):
        self.hand.append(player_deck.DrawCard())

      #Print Hand
    def __str__(self):    	
        print("Player hand")
        for card1 in self.hand:                  
            self.PrintCard(card1)
        return ""

    def CalculateTotal(self):
        hand_total = 0        
        val = 0
        ace_count = 0
        for card in self.hand:            
            val = self.player_deck.card_values.get(card[0])            
            hand_total += val

            if card[0] == "A":
                ace_count += 1
                continue

        if hand_total > 21:
            while ace_count > 0 and hand_total > 21:
                hand_total -= 10
                ace_count -= 1

        return hand_total

    def Bet(self, amount):
    	if amount > self.balance:
    		print("You can not bet more than available balance of {}".format(self.balance))
    		return False
    	else:
            self.balance = self.balance - amount
            self.last_bet = amount
            print("balance: " + str(self.balance))
            print("last bet: " + str(self.last_bet))
            return True

    def DisplayBalance(self):
        print("Player balance: " + str(self.balance))

    def BetWon(self):
    	print("Last bet: " + str(self.last_bet))
    	self.balance = self.balance + 2 * self.last_bet
    	print("New balance: " + str(self.balance))





