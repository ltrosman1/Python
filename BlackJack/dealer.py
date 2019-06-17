'''Create Dealer Hand
Automatically draw 1st two cards from deck
Don't display 2nd card (show 'X')
Pass initial amount to keep track of player betting balance
'''
from deck import Deck
class Dealer(Deck):	
	hand = []
	dealer_deck = Deck()

	def __init__(self, deck):
		self.dealer_deck = deck
		self.hand = []

	def CreateHand(self):		
		#Draw 1st two cards
		self.hand.append(self.dealer_deck.DrawCard())
		self.hand.append(self.dealer_deck.DrawCard())
	
	def DrawCard(self, dealer_deck):
		self.hand.append(self.dealer_deck.DrawCard())

	#Print Hand
	def __str__(self):
		#for dealer 2nd card is blind
		print("Dealer hand:")
		index = 0
		for card1 in self.hand:	
			index += 1
			if index == 2 and len(self.hand) == 2:
				print('X')	
			else:	
				self.PrintCard(card1)
		return ""

	def PrintAll(self):
		for card in self.hand:
			self.PrintCard(card)

	def CalculateTotal(self):
		hand_total = 0		
		val = 0
		ace_count = 0
		for card in self.hand:
			val = self.dealer_deck.card_values.get(card[0])
			hand_total += val

			if card[0] == "A":				
				ace_count += 1
				continue

		if hand_total > 21:
			while ace_count > 0 and hand_total > 21:
				hand_total -= 10
				ace_count -= 1

		return hand_total

		#def Bet(amount):