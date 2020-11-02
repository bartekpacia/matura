# zad 2.1
 
def binarny(x: float, k: int) -> str:
  tekst = ""

  tekst += "0."
  y = x
  for i in range(1, k + 1):
    print(f"{i=}, {y=}")
    if y >= (1 / 2):
      tekst += "1"
    else:
      tekst += "0"
    y *= 2
    if y >= 1:
      y -= 1

  return tekst


a = binarny(0.6, 5)
print(a)