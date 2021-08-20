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
  print("Type 5 to install teamviewer")
  number = input("Type a mumber: ")


  def Execute(cmd):
    print(cmd)
    for line in os.popen(cmd).read().split("\n"):
      print("==> " + line.strip())


  if number == 1:
    Execute("sudo apt-get update")
    Execute("sudo apt-get upgrade")

  if number == 2:
    prgm = input("type the name of the progrom between"": ")
    Execute("sudo apt-get install {}".format(prgm))

  if number == 3:
    Execute("sudo reboot")

  if number == 4:
     Execute("sudo shutdown")

  if number == 5:
    Execute("wget -P /home/pi/Downloads https://download.teamviewer.com/download/linux/teamviewer-host_armhf.deb")
    Execute("sudo apt-get install /home/pi/Downloads/teamviewer-host_armhf.deb")
    Execute("sudo teamviewer setup")

if __name__ == '__main__':
    main()