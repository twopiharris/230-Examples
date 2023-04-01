""" playWav.py
    play wav files using (ugh) system calls
    should work on any of the big three OS
    by using aplay for linux
    afplay for mac,
    and start for windows

    by Andy Harris

    this is a far from ideal solution (platform names may change)
    and it calls up the default media player for windows, which will
    be very slow.

    consider adding a dedicated audio player for windows
    like sounder.exe

    usage:  put this file in same directory as your program
    import playWav
    playWav.playSound("yourWavFile.wav")

    Might also work with other formats, but no guarantees.

"""

import os
import platform

def main():
  playSound("pew.wav")

def playSound(wavFile):
  sys = platform.system()
  
  #uncomment the following line to check for which 
  #platform you're on. You may have to modify this

  #print ("Current system: {}".format(sys))
  if sys == "Windows":
    command = "start %s" % wavFile
  elif sys == "Darwin":
    #most modern macs report Darwin, may need to 
    #change this for your version
    #mac command 
    command = "afplay %s" % wavFile
  else:
    #default is unix-like systems
    command = "aplay %s" % wavFile

  os.system(command)

if __name__ == "__main__":
  main()
