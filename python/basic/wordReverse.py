""" wordReverse.py
    demonstrates how to use loops
    for string manipulation
    3/30/06 """

inWord = raw_input("Please type a word or phrase: ")
outWord = ""

# remember, I want to count backwards to character zero,
# so negative one is the boundary

firstChar = -1

# The length of the word is how many characters are in it
# The last character is word length minus one.

maxIndex = len(inWord) - 1


# Go backwards from the last character to the first character
# counting by negative one each time through the loop

for charPos in range (maxIndex, firstChar, -1):

    # Add the current character to the output string 
    outWord = outWord + inWord[charPos]

# After the loop is finished, print out the results
print outWord




