""" ants2.py
    classic counting song
    use parameters and return statements
    """


def chorus():
    output = """
    ...and they all go marching
    down-
    to the ground-
    to get out-
    of the rain.
    Boom boom boom boom boom boom boom
    """
    return output

def verse(verseNum):
    if verseNum == 1:
        distraction = "suck his thumb"
    elif verseNum == 2:
        distraction = "tie his shoe"
    else:
        distraction = "I have no idea"
        
        
    output = """
    The ants go marching {0} by {0} hurrah, hurrah.
    The ants go marching {0} by {0} hurrah, hurrah.
    The ants go marching {0} by {0}.
    The little one stops to {1}    
    """.format(verseNum, distraction)
    
    return output

print (verse(1))
print (chorus())
print (verse(2))
print (chorus())

