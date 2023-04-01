"""

   mac - afplay
   windows - start
   linux aplay
"""

import platform, os

class Sound(object):
  def __init__(self, fileName):
    object.__init__(self)
    self.__fileName = fileName
    print (platform.system())

  def play(self):
    if platform.system() == "Darwin":
      command = "afplay {}".format(self.__fileName)

    os.system(command)

def main():
  sound = Sound("evillaugh.wav")
  sound.play()

if __name__ == "__main__":
  main()



