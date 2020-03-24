'''
Blackjack!
'''
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True

class Card: #creates cards and return the string to label them
    
    def __init__(self, suit, rank):
        
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    
    def __init__(self):
        self.deck = []  #start with empty deck
        for suit in suits:
            for rank in ranks: #these three cycle through every rank for every suit then appends/adds a new Card() to the empty deck above
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        the_deck = '' #stringify the deck
        for card in self.deck:
            the_deck += '\n' + card.__str__()
        return 'Cards in the deck: ' +the_deck

    def shuffle(self):
        random.shuffle(self.deck) #no return needed, does it in place
        
    def deal(self):
        single_card = self.deck.pop() #pops off the last card in the shuffled deck, sets it to single_card variable
        return single_card

test_deck = Deck()
print(test_deck)