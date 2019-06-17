from deck import Deck
from player import Player
from dealer import Dealer

new_deck = Deck()

new_deck.ShuffleDeck()

print(new_deck)

pl_hand = Player()
pl_hand.CreateHand(new_deck)

print(pl_hand)

pl_hand.Bet(3000) #Error - over balance
pl_hand.Bet(200)

pl_hand.DisplayBalance() # Should be 800
print("Player Cards total: " + str(pl_hand.CalculateTotal()))

dealer_hand = Dealer(new_deck)

dealer_hand.CreateHand()

print(dealer_hand)
print("dealer Cards total: " + str(dealer_hand.CalculateTotal()))

print("Dealer Full Hand:")
dealer_hand.PrintAll()




