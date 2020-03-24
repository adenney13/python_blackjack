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
        for suit in suits: #for every suit...
            for rank in ranks: #go through every rank and...
                self.deck.append(Card(suit,rank))#using the Card class, append and fill the self.deck with the ranks of every suit
    
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

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):#take in a "card" object
        #"card" is passed in
        #from class/method above, Deck.deal().... single Card(suit,rank)class instance
        self.cards.append(card) #add 'card' object grabbed to the self.cards list
        self.value += values[card.rank] #matching card rank with value from values dict...adjusting value to card just added to list self.cards
    
        #track aces
        
        if card.rank == 'Ace':
            self.aces += 1
        
    def adjust_for_ace(self):
        
        #if my total value is > 21, AND i still have an ace
        #change my ace to be a 1 instead of 11
        while self.value > 21 and self.aces: #self.aces ... truthyness... 0 value, will be treated as False, and a value is treated as True. BOOLEAN
            self.value -= 10
            self.aces -= 1

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input by passing argument (self, total=100)
        self.bet = 0
        
    def win_bet(self): #wins the bet, add the bet to the total
        self.total += self.bet
    
    def lose_bet(self): #loses the bet, subtract the bet from the total
        self.total -= self.bet

def take_bet(chips):
    
    while True:
        #logic/loop to prevent someone from making non-number bet, or betting more than they have left
        try:
            chips.bet = int(input("How many chips do you want to bet: "))
        except:
            print("Sorry, put in a number")
        else:
            if chips.bet > chips.total:
                print(f"Sorry, you don't have enough chips! You have {chips.total} chips left")
            else:
                break
