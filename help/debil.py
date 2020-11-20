import math
import time

name = input("kto cie wkurza byczku? -->")
msg = f"{name} zamknij mordę"
l = 1
increasing = True
while True:
  for i in range(l):
    print(msg[i], end="")
  print("", end="\n")

  if increasing:
    l += 1
  else:
    l -= 1

  if l == len(msg):
    increasing = False
  if l == 1:
    increasing = True

  time.sleep(0.01)


