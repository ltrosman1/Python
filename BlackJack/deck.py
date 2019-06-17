'''Create 52 card deck
Deck shouls have methods for shuffling curds
and for drawing card
'''
#Declare global lists used to create deck; card face  - value in BJ game
import random
import colorama
class Deck():
	card_faces=["2","3","4","5","6","7","8","9", \
              "10","J","Q","K","A"]
	card_shades=["Spades", "Hearts", "Diamonds", "Clubs"]
	#dictionary of card values by faces
	card_values={"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9, \
				"10":10,"J":10,"Q":10,"K":10,"A":11}
	deck = []


	def __init__(self):
		#Create deck
		for card in self.card_faces:
			for shade in self.card_shades:
				tup = (card, shade)
				self.deck.append(tup)
				
	def ShuffleDeck(self):
		random.shuffle(self.deck)

	def DrawCard(self):
		return self.deck.pop()

	#this is for test printing deck
	def __str__(self):
		for card1 in self.deck:
			self.PrintCard(card1)
		return ""

	def PrintCard(self, card1):
		value, shade = card1
		print(self.GetSymbol(value, shade))

	def GetSymbol(self, value, shade):		    
		colorama.init(autoreset=True) # that's important to use colorama
		#Choose colors depending on cmd line or ipython
		cmd_white = colorama.Fore.WHITE
		cmd_red = colorama.Fore.RED
		wnd_blk = "\x1b[30m"
		wnd_red = "\033[91m"		
		color1 = "\x1b[30m"
		color2 = "\x1b[91m"
		try:
			get_ipython
			color2 = "\033[91m"
		except:
			color1 = cmd_white
			color2 = cmd_red

		if shade == "Clubs":
			return color1 + value + "\u2663" #Windows black "\x1b[30m"
		elif shade == "Spades":
			return  color1 + value + "\u2660" 
		elif shade == "Diamonds":
			return  color2 + value + "\u2666" #Windows red "\033[91m"
		elif shade == "Hearts":
			return  color2 + value + "\u2665" 
		else:
			return value + shade









