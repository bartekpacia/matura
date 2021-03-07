# checking my "whiteboard solution"

def skojarzona(a: int):
    suma_dzielnikow_a = 0
    for i in range(1, (a // 2) + 1):
        if a % i == 0:
            suma_dzielnikow_a += i

    suma_dzielnikow_b = 0
    b = suma_dzielnikow_a - 1
    for i in range(1, (b // 2) + 1):
        if b % i == 0:
            suma_dzielnikow_b += i

    if suma_dzielnikow_b == a + 1:
        print(f"{b=}")
    else:
        print("NIE")


for i in range(1, 100):
    skojarzona(i)
