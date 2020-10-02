import math

wszystkie_punkty = []

P = 400 * 400

with open("dane/punkty.txt") as f:
  punkty_raw = [l.strip() for l in f.readlines()]

  for p in punkty_raw:
    p = p.split()
    punkt = (int(p[0]), int(p[1]))

    wszystkie_punkty.append(punkt)

a = 200
b = 200
r = 200

### end boiler

punkty_w_kwadracie = []
punkty_w_kole = []

pi_total = 0
pi_100 = 0
pi_1000 = 0
pi_5000 = 0
bledy_pi = []
for i, punkt in enumerate(wszystkie_punkty):
  if i == 100:
    pi_100 = pi_total

  if i == 1000:
    pi_1000 = pi_total

  if i == 5000:
    pi_5000 = pi_total


  x = punkt[0]
  y = punkt[1]

  punkty_w_kwadracie.append(punkt)

  if (x - a) ** 2 + (y - b) ** 2 <= r ** 2: # "<=" bo brzeg koła też się liczy
    punkty_w_kole.append(punkt)

  pi_total = (P * len(punkty_w_kole)) / (len(punkty_w_kwadracie) * r ** 2)

  blad = abs(math.pi - pi_total)
  bledy_pi.append(blad)


print(f"{round(pi_100, 4)=}")
print(f"{round(pi_1000, 4)=}")
print(f"{round(pi_5000, 4)=}")
print(f"{round(pi_total, 4)=}")
print(f"{len(punkty_w_kole)=}")

print(f"{round(bledy_pi[1000], 4)=}")
print(f"{round(bledy_pi[1700], 4)=}")