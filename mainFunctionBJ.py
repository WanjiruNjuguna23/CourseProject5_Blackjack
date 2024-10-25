# Main Function for BlackJack Game

from deckClass import *
import PlayingCard
from graphics import *
from ButtonClass import Button
from BlackjackClass import *
# imports previously made classes 

def main():

    win = GraphWin("BlackJack Game", 1000,500) # makes the blackjack window
    win.setBackground("green")

    xPosP = 400 # sets the positions for the x coord for the player hand cards
    xPosD = 400 # sets the positions for the x coord for the dealer hand cards
    end = Text(Point(675,250),"") # sets the end text to an epty string to use 'setText' later
    end.setStyle("bold")
    end.setSize(17)
    end.draw(win)

    end.setText("Hello! Welcome to our BlackJack Game. Click 'hit' or 'stand' to get started.")
        # introduces the program to the user and what to click to continue

    hitButton = Button(win,Point(190,250),100,50,"Hit")
    hitButton.activate()
    # makes and activates the hit button

    standButton = Button(win,Point(310,250),100,50,"Stand")
    standButton.activate()
    # makes and activates the stand button

    quitButton = Button(win,Point(925,450),100,50,"Quit")
    quitButton.deactivate()
    # makes and deactivates the quit button
    
    game = BlackJack()
    game.initDeal(win,200,100,200,400)
    # makes a Blackjack game and sets the cards at those coords

    coverCard = Image(Point(200,100), "img/b1fv.gif")
    coverCard.draw(win)
    # sets the back of a card on top the dealt card to the dealer so it is
        # covered but the value of the card is still taken into account
    
    Dtotal = game.evalutateHand(game.dealerHand)
    Ptotal = game.evalutateHand(game.playerHand)
    # gets the value of each hand as an interger 

    dealerLabel = Text(Point(85,85),"Dealer's Total:") # label for dealer's total
    dealerTotal = Text(Point(85,110),"") # dealer's total, but as an empty string to not tell
                                            # the player the total

    dealerTotal.setSize(20)
    dealerTotal.draw(win) 

    dealerLabel.setSize(20)
    dealerLabel.draw(win)

    playerLabel = Text(Point(85,385),"Player's Total:") # label for dealer's total
    playerTotal = Text(Point(85,410),str(Ptotal)) # players total shown on screen

    playerTotal.setSize(20)
    playerTotal.draw(win) 

    playerLabel.setSize(20)
    playerLabel.draw(win)
    

    pt = win.getMouse()

    while not quitButton.isClicked(pt): # while the quit button is NOT clicked
        
        if hitButton.isClicked(pt): # if hit button is clicked
            
            end.setText("Click hit/stand depending on your total!") # sets the text to this
            game.hit(win,xPosP,400) # sets the hit card at 400,400
            quitButton.activate() # activates the quit button 
            xPosP = xPosP + 100 # adds 100 to the x coord so the next card is 100 away, no overlap
            Ptotal = game.evalutateHand(game.playerHand) # evaluates the new player total
            playerTotal.setText(Ptotal)

            if game.evalutateHand(game.playerHand) > 21: # if the player's total is over 21
                end.setText("You busted, dealer wins!") # dealer wins
                end.setFill("red")
                hitButton.deactivate() # deactivates the hit button
                standButton.deactivate() # deactivates the stand button
                coverCard.undraw() # uncovers the dealer's card at the end of the game
                dealerTotal.setText(str(Dtotal)) # sets the dealer's total
                
            pt = win.getMouse()
            
        elif standButton.isClicked(pt): # if the stand is clicked
            
            quitButton.activate() 
            game.dealerPlays(win,xPosD,100) # sets the hit card for the dealer at 400,400
            Dtotal = game.evalutateHand(game.dealerHand) # evaluates the new dealer total
            dealerTotal.setText(Dtotal) 
            hitButton.deactivate()
            standButton.deactivate()

            if game.evalutateHand(game.dealerHand) > 21: # if the dealer busts
                end.setText("Dealer busted, you win!") # player wins
                end.setFill("light green")
                hitButton.deactivate() # deactivates hit button
                standButton.deactivate() # deactivates the stand button
                dealerTotal.setText(str(Dtotal)) # sets the dealer's total
                coverCard.undraw() # uncovers the dealer's card at the end of the game

            elif 17 <= game.evalutateHand(game.dealerHand) <= 21 and \
                 game.evalutateHand(game.playerHand) < game.evalutateHand(game.dealerHand):
                # if the dealer is at a soft 17, but their total is larger than the players, we lose
                end.setText("Dealer's total is higher than yours, you lose!") # player loses
                end.setFill("red")
                hitButton.deactivate() # deactivates hit button
                standButton.deactivate() # deactivates the stand button
                dealerTotal.setText(str(Dtotal)) # sets the dealer's total
                coverCard.undraw() # uncovers the dealer's card at the end of the game

            elif 17 <= game.evalutateHand(game.dealerHand) <= 21 and \
                 game.evalutateHand(game.playerHand) > game.evalutateHand(game.dealerHand):
                # if the dealer is at a soft 17, but the player's total is higher than the dealer's,
                    # they lose
                end.setText("Your total is higher than the Dealer's, you win!") # player wins
                end.setFill("light green")
                hitButton.deactivate() # deactivates hit button
                standButton.deactivate() # deactivates the stand button
                dealerTotal.setText(str(Dtotal)) # sets the dealer's total
                coverCard.undraw() # uncovers the dealer's card at the end of the game

            elif 17 <= game.evalutateHand(game.dealerHand) <= 21 and \
                 game.evalutateHand(game.playerHand) == game.evalutateHand(game.dealerHand):
                # if the dealer is at a soft 17, and the two totals are tied
                end.setText("You both have the same total, stand-off!") # tie
                hitButton.deactivate() # deactivates hit button
                standButton.deactivate() # deactivates the stand button
                dealerTotal.setText(str(Dtotal)) # sets the dealer's total
                coverCard.undraw() # uncovers the dealer's card at the end of the game
    
            pt = win.getMouse()

    win.close() # closes the window
    
main()
