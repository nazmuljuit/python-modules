import time
import os
while True:
  if os.path.exists("files/vegitables.txt"):
    with open("files/vegitables.txt") as file:
      print(file.read())
      
  else:
    print("file is not find!")
  time.sleep(10)