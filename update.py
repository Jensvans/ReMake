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
  number = input("Type a mumber: ")

  def Execute(cmd):
    print(cmd)
    for line in os.popen(cmd).read().split("\n"):
      print("==> " + line.strip())


  if number == 1:
    Execute("sudo apt-get update")
    Execute("sudo apt-get upgrade")

if __name__ == '__main__':
    main()