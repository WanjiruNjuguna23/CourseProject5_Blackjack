# programming assignemt 5
# black jack class

from deckClass import *
import PlayingCard
from graphics import *
from ButtonClass import Button


class BlackJack:

    def __init__(self, dHand=[], pHand=[]):
        """creates two empty lists, dHand and pHand, which will hold the cards drawn"""
        """for the dealer and player and also gives the deck an initial shuffle"""
        self.dealerHand = dHand
        self.playerHand = pHand
        self.playingDeck = Deck()
        self.playingDeck.shuffle()

    def initDeal(self,gwin,xposD,yposD,xposP,yposP):
        """takes in initial x and y values for the dealer and player cards"""
        """then, draws two cards for the dealer and two for the player"""
        """d stands for dealer and p stands for player"""
        for i in range(2):
            dCard = self.playingDeck.dealCard()
            self.dealerHand.append(dCard)
            
            suit = dCard.getSuit()
            rank = dCard.getRank()
            dCardImg = Image(Point(xposD,yposD),"img/"+suit+str(rank)+".gif")
            dCardImg.draw(gwin)
            xposD = xposD + 100

            pCard = self.playingDeck.dealCard()
            self.playerHand.append(pCard)
            suit = pCard.getSuit()
            rank = pCard.getRank()
            pCardImg = Image(Point(xposP,yposP),"img/"+suit+str(rank)+".gif")
            pCardImg.draw(gwin)
            xposP = xposP + 100#prevents overlapping of cards
            
    def hit(self,gwin, xPos, yPos):
        """draws cards for the player and adds them to their hand when they play(hit)"""
        newPCard = self.playingDeck.dealCard()
        self.playerHand.append(newPCard)
        suit = newPCard.getSuit()
        rank = newPCard.getRank()
        newPCardImg = Image(Point(xPos, yPos),"img/"+suit+str(rank)+".gif")
        newPCardImg.draw(gwin)

    def evalutateHand(self, hand):
        """evaluates the total value of a hand, counting an ace as either 1 or 11"""
        """depending on the rest of the cards in the hand"""
        points = 0
        hasAce = False
        
        for card in hand:            
            if card.byValue() == 1:# card value=1 
                hasAce = True#there is an ace
            points = points + card.byValue()
            if hasAce and (17 <= points + 10 <= 21):#if total with Ace = 11 is less than 21
                points = points + 10#then count the ace as 11
            
        return points

    def dealerPlays(self,gwin,xPos,yPos):
        """as long as the dealer's hand value is less than 17, it will draw cards"""
        """for them and add them to the hand"""
        points = self.evalutateHand(self.dealerHand)
        while points < 17:
            newDCard = self.playingDeck.dealCard()
            points = self.evalutateHand(self.dealerHand)
            self.dealerHand.append(newDCard)
            suit = newDCard.getSuit()
            rank = newDCard.getRank()
            newDCardImg = Image(Point(xPos,yPos),"img/"+suit+str(rank)+".gif")
            newDCardImg.draw(gwin)
            xPos = xPos + 100#prevents overlapping of cards
            points = self.evalutateHand(self.dealerHand)

if __name__ == "__main__":
    main()
