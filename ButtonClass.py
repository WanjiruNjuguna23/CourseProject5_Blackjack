# 04/05/22
# creating our own class
from graphics import *

class Button:
    # constructor method
    def __init__(self,win,center,width,height,label):
        """Creates a rectangular button, where: win is the GraphWin where the
            button will be drawn, center will be in Point object where the
            button is centered, width is an integer that is the wifth of the
            button in pixels, height is an integer that is the height of the
            button in pixels, and label is a string text that will appear on the
            button"""
        x,y = center.getX(), center.getY() 
        self.xmin = x-width/2 # instance variable for left boarder of button
        self.xmax = x+width/2 # instance variable for right boarder
        self.ymin = y-height/2 # instance variable for top boarder
        self.ymax = y+height/2 # instance variable for bottom boarder
        pt1 = Point(self.xmin,self.ymin) 
        pt2 = Point(self.xmax,self.ymax)
        self.rect = Rectangle(pt1,pt2) # instance variable for creating the rectange of button
        self.rect.draw(win)
        self.words = Text(center,label) # instance variable for the text/words on the button 
        self.words.draw(win) 

    def deactivate(self):
        """sets this button to be deactivated so it is not clickable"""
        # set the color text grey
        self.words.setFill("dark grey")
        # set the outline to be thinner
        self.rect.setWidth(1)
        # set the boolean flag self.activate to False
        self.active = False
        
    def activate(self):
        """sets this button to be actiavted, which means it can be clicked"""

        # set the color of the back to be "black"
        self.words.setFill("black")
        # set the outline to look bolder
        self.rect.setWidth(2)
        # set the boolean flag self.activate to True
        self.active = True

    def isClicked(self,pt):
        """returns True if pt is within the boundaries of the button, false otherwise"""
        if self.active and \
        self.xmin <= pt.getX() <= self.xmax and \
        self.ymin <= pt.getY() <= self.ymax:
            return True
        else:
            return False
        
def main():
    gwin = GraphWin("Button Test", 200,200)
    # instantiate the Button Class
    # i.e. create a button object
    myButton = Button(gwin, Point(100,100),50,25,"Quit")
    p = gwin.getMouse()
    if myButton.isClicked(p):
        print("button was clicked")
    else:
        print("button was not clicked")

if __name__ == "__main__":
    main()
