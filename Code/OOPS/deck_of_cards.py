"""  Deck of Cards using OOPS """

from random import shuffle

class Card:
	
	def __init__(self,value,suit):
		self.suit=suit
		self.value=value
		
	def __repr__(self):
		return f"{self.value} of {self.suit}"	

class Deck:

	def __init__(self):
		suits=["Hearts","Diamonds","Clubs","Spades"]
		values=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
		self.cards=[Card(value,suit) for suit in suits for value in values]
	
	def __repr__(self):
		return f"Deck of {self.count()} cards"
		
	def __iter__(self):
		return iter(self.cards)
		
	def count(self):
		return len(self.cards)
		
	def _deal(self,num):
		count=self.count()
		actual = min([num,count])
		if count==0:
			raise ValueError("All cards have been dealt")
		cards=self.cards[-actual:]
		self.cards=self.cards[:-actual]
		return cards
		
	def shuffle(self):
		if self.count() < 52:
			raise ValueError("Only full decks can be shuffled")
		shuffle(self.cards)
		return self.cards
		
	def deal_card(self):
		return self._deal(1)[0]
		
	def deal_hand(self,hand_size):
		return self._deal(hand_size)
		

my_deck=Deck()
my_deck.shuffle()

for x in my_deck:
	print(x)

# card=my_deck.deal_card()
# print(card)
# hand=my_deck.deal_hand(3)
# print(hand)
# print(my_deck.count())

# c=Card("Hearts","K")
# c1=Card("Diamonds",2)
# print(c)
# print(c1)