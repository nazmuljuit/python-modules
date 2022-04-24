import time
while True:
  with open("files/vegitables.txt") as file:
    print(file.read())
    time.sleep(10)
