#!/usr/bin/env python
"""

"""

#imports
import os

__author__ = "Jens Vansteenvoort"
__email__ = "jens.vansteenvoort@student.kdg.be"
__status__ = "Development"

def main():
  print("Type 1 to update the os")
  print("Type 2 to install a program")
  print("Type 3 to reboot")
  print("Type 4 to shutdown")
  number = input("Type a mumber: ")


  def Execute(cmd):
    print(cmd)
    for line in os.popen(cmd).read().split("\n"):
      print("==> " + line.strip())


  if number == 1:
    Execute("sudo apt-get update")
    Execute("sudo apt-get upgrade")

  if number == 2:

    Execute("sudo apt-get install"+ input("name of progrom: "))

  if number == 3:
    Execute("sudo reboot")

  if number == 4:
     Execute("sudo shutdown")


if __name__ == '__main__':
    main()