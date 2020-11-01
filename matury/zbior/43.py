def silnia_zapis(x):
  silnia = 1
  k = 1
  while silnia < x:
    k = k + 1
    silnia = silnia * k

  if silnia > x:
    silnia = silnia // k
    k = k - 1

  s = " "
  while k > 0:
    cyfra = x // silnia
    s = s + str(cyfra)
    x = x % silnia
    silnia = silnia // k
    k = k - 1

  return s
  

w = silnia_zapis(5489)
print(w)