class PlayingCard:
    """playing card object where numeric rank, suit values are stored"""
    
    def __init__(self,rank,suit):
        """instance variables are rank and suit."""
        self.rank = rank
        self.suit = suit
        
    def getRank(self):
        """returns the rank of the card"""
        return self.rank
    
    def getSuit(self):
        """returns the suit of the card"""
        return self.suit

    
    def byValue(self):
        """returns the value of the card, valuing each face card at 10"""
        if self.rank > 10:
            val = 10
        else:
            val = self.rank
        return val

    def __str__(self):
        """creates a list of every card rank and a list of all 4 suits"""
        ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        suits = {"d":"Diamonds","c":"Clubs","h":"Hearts", "s":"Spades"}
        return ranks[self.rank-1] + " of " + suits[self.suit]

if __name__ == '__main__':
    main()
        



        
