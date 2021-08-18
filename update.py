import os

def Execute(cmd):
  print(cmd)
  for line in os.popen(cmd).read().split("\n"):
    print("==> " + line.strip())

Execute("sudo apt-get update")
Execute("sudo apt-get upgrade")