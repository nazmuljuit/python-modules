import time
import os
import pandas
while True:
  if os.path.exists("files/temps_today.csv"):
      data = pandas.read_csv("files/temps_today.csv")
      print(data.mean()["st1"])
      
  else:
    print("file is not find!")
  time.sleep(10)