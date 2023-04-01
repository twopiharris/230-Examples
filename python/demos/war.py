""" cardGame.py
    basic card game framework
    keeps track of card locations for as many hands as needed
"""
from random import *

NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2

cardLoc = [0] * NUMCARDS
suitName = ("hearts", "diamonds", "spades", "clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
            "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "computer")
cardCount = [0, 26, 26]  


def main():
  clearDeck()


  for i in range(26):
    assignCard(PLAYER)
    assignCard(COMP)

  showDeck()
  showHand(PLAYER)
  showHand(COMP)      

  print "+++++++++++++++++++++++++++++++++++++++++++"
  keepGoing = True
  i = 0
  while keepGoing:
    i += 1
    keepGoing = play()
    if keepGoing == False:
      print "Game Over in %d turns" % i
     
    if i > 1000:
      print "I give up... It took too long"
      keepGoing = False

def getCard(hand):
  #returns false if no cards left
  #or a card number

  #get a card from the given hand
  if cardCount[hand] <= 0:
    print "%s loses" % playerName[hand]
    result = False
  else:
    #try until you can find a card belonging to hand
    keepGoing = True
    while keepGoing:
      cn = randrange(NUMCARDS)
      if cardLoc[cn] == hand:
        result = cn
        keepGoing = False

  return result
  
def play():
  #play one hand
  result = True
  pCard = getCard(PLAYER)
  cCard = getCard(COMP)

  if pCard == False:
    result = False
  if cCard == False:
    result = False
    

  pRank = pCard % 13
  cRank = cCard % 13

  print "Player: %s, Comp: %s" % (getCardName(pCard), getCardName(cCard))  
  if pRank == cRank:
    print "Tie!"
  elif pRank > cRank:
    print "Player wins",
    #give computer card to player
    cardLoc[cCard] = PLAYER
    #reduce cards in computer hand
    cardCount[COMP] -= 1
    #increment cards in player hand
    cardCount[PLAYER] +=1
  else:
    print "Computer wins ",
    #give player card to computer
    cardLoc[pCard] = COMP
    #reduce cards in player hand
    cardCount[PLAYER] -= 1
    #increment cards in computer hand
    cardCount[COMP] += 1

  print "Card count- P: %d, C: %d" % (cardCount[PLAYER], cardCount[COMP])
  return result

def clearDeck():
  for cardPos in cardLoc:
    cardPos = DECK

def showDeck():
  for cn, cardPos in enumerate(cardLoc):
    print "%d) %s -  %s" % (cn, getCardName(cn), playerName[cardPos])

def assignCard(hand):
  #keepGoing until we get a card in the deck 
  keepGoing = True
  while keepGoing:
    #pick a random number 
    cn = randrange(NUMCARDS)
    
    if cardLoc[cn] == DECK:
      #this card is available, so pick it and get out
      cardLoc[cn] = hand
      keepGoing = False

def showHand(hand):
  print "%s hand" % playerName[hand]
  for cn, cardPos in enumerate(cardLoc):
    if cardPos == hand:
      print getCardName(cn)

  print


def getCardName(cn):
  suit = cn / 13
  rank = cn % 13

  return "%s of %s" % (rankName[rank], suitName[suit])

if __name__ == "__main__":
  main()
 
