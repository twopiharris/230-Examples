""" cardGame.py
    basic card game framework
    keeps track of card locations for as many hands as needed
"""
from random import *

cardLoc = [1] * 52
suitName = ("hearts", "diamonds", "spades", "clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
        "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "computer")

DECK = 0
PLAYER = 1
COMP = 2

def main():
  clearDeck()
  #showDeck()

  for i in range(5):
    assignCard(PLAYER)
    assignCard(COMP)

  showDeck()
  showHand(PLAYER)
  showHand(COMP)          


def clearDeck():
  #assigns all elements of cardLoc to 0 (DECK)
  for cardNum in range(len(cardLoc)):
    cardLoc[cardNum] = DECK

def showDeck():
  """show the position of every card"""
  print "Location of all cards"
  print "# \t card \t \t location"
  for cardNum in range(52):
    #print "%d \t %s \t %s" % (cardNum, getCardName(cardNum), playerName[cardLoc[cardNum]])
    print "{0:<5}{1:<20}{2:<20}".format(cardNum, getCardName(cardNum), playerName[cardLoc[cardNum]])
  print

def assignCard(hand):
  #try to assign a card
  keepGoing = True
  while(keepGoing):
    #generate a random number between 0 and 51
    cardNum = randint(0, len(cardLoc) -1)
    #if the card at that position is blank
    if cardLoc[cardNum] == 0:
      #add the card 
      cardLoc[cardNum] = hand
      keepGoing = False

def showHand(hand):
  #goes through card list and displays cards in given hand
  print "Displaying %s hand:" % playerName[hand]
  for i in range(len(cardLoc)):
    if cardLoc[i] == hand:
      print getCardName(i)
  print
  
def getCardName(cardNum):
  suit= cardNum / 13
  rank = cardNum % 13
  cardName = "%s of %s" % (rankName[rank], suitName[suit])
  return cardName

if __name__ == "__main__":
  main()
    

