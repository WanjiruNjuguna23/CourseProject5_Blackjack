# Day Baez
# Programming Assignment 5
# "Deck" Class

from PlayingCard import *
from random import randrange

class Deck:
    """Deck is a class to input a deck of cards"""
    
# constructor: Creates a new deck of 52 cards in a standard order.
    def __init__(self):
        self.cardList = [] # initalizes the list for the 52 cards
        for suit in ["d", "c", "h", "s"]: # sets the four suit
            for rank in range(1,14): # goes from 1 to 13 to set every number in every suit
                card = PlayingCard(rank,suit) # calls the playing card class and takes every
                                            # rank and suit to set it as one card
                self.cardList.append(card) # adds all 52 cards to the list 
        
# shuffle: Randomizes the order of the cards.
    def shuffle(self): # shuffle  function
        n = len(self.cardList) # sets n as the length of the card list
        for i in range(n): # goes through the length of the list
            card = randrange(1,n) # grabs a random card from the list 
            previous = self.cardList[i] # sets the old card as previous
            self.cardList[i] = self.cardList[card] # sets that card as the new one
            self.cardList[card] = previous # switches the two cards positons, shuffling them
        
# dealCard: Returns a single card from the top of the deck and removes the card from the deck.
    def dealCard(self): # deal card function
        topCard = self.cardList.pop() # takes the first "card" in the list and sets it as top
                                        # card and then removes it from the list
        return topCard # returns the card
        
# cardsLeft: Returns the number of cards remaining in the deck.
    def cardsLeft(self): # cards left function
        return len(self.cardList) # returns the length of the new list

def main():
    deck = Deck()
    deck.shuffle()
    for card in deck.cardList:
        print(card)

if __name__ == "__main__":
    main()
