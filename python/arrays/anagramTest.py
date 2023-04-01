""" anagram tester """
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 
def countLetters(phrase):
  #build empty letterScore
  letterScore = {}
  for char in alpha:
    letterScore[char] = 0
    
  for letter in phrase:
    if letter in alpha:
      letterScore[letter] += 1
  
  return letterScore    

def main():
  wordList = open("wordList.txt")
  for line in wordList:
    line.rstrip()
    (a, b) = line.split(',')
    print "A: %s, B: %s" % (a, b),

    a = a.upper()
    b = b.upper()
    aScore = countLetters(a)
    bScore = countLetters(b)
    if aScore == bScore:
      print "ANAGRAM!"
    else:
      print "Not an anagram" 
    print
  
  wordList.close()
  
if __name__ == "__main__":
  main()
  
  
