'''Zapisz algorytm (w postaci listy kroków lub w wybranym języku programowania),
który dla danego łańcucha znaków zwraca liczbę różnych znaków.'''

# Problem: czy brać pod uwagę wielkość liter?

s = input("Podaj łańcuch znaków: ")
chars = {}

for char in s:
    if char not in chars:
        chars[char] = 1
    else:
        chars[char] += 1

r = len(chars)
print(r)

# Przydatne do debugowania


def printOccurrences(chars):
    for char in chars:
        occurences = str(chars[char])
        print(char + ": " + occurences)
