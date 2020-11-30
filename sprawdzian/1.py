from typing import List

def podzielniki(num: int) -> List[int]:
  podzielniki: List[int] = []

  for i in range(1, num + 1):
    if num % i == 0:
      podzielniki.append(i)

  return podzielniki


def fibonacci(n: int) -> int:
  if n == 0:
    return 0
  if n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

def decompose(num: int) -> []:
  factors = []
  k = 2

  while num > 1:
    while num % k == 0:
      factors.append(k)
      num = num // k

    k = k + 1

  return factors


def main():
  num_count = int(input("podaj liczbę wyrazów ciągu fibonacciego: "))

  for i in range(num_count):
    ith_element = fibonacci(i)

    podz = podzielniki(ith_element)
    print(f"element: {i}, wartość elementu: {ith_element}, podzielniki: {podz}")

    if ith_element != 0 and ith_element % 3 == 0:

      componenets = decompose(ith_element)
      how_many_times = componenets.count(3)
      print(f"element: {i}, wartość elementu: {ith_element} podzielnik 3 (powtarza się {how_many_times} razy)")

    if ith_element != 0 and ith_element % 5 == 0:
      components = decompose(ith_element)
      how_many_times = components.count(5)
      print(f"element: {i}, wartość elementu: {ith_element} podzielnik 5 (powtarza się {how_many_times} razy)")

main()