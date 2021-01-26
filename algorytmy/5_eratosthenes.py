from typing import List

# zwraca liczby pierwsze od 1 do n (włącznie)
def sito(n: 30) -> List[int]:
    if n < 2:
        return list()
    
    arr = [True] * (n + 1) # domyślnie wszystkie są True (czyli pierwsze)
    i = 2
    while i**2 <= n:    # tak długo aż kwadrat i < n
        if arr[i]:       # jeśli liczba nie została już "skreślona" wcześniej 
            j = i**2          # j = i do potęgi 2
            while j <= n:       # i jeśli to j <= n
                arr[j] = False  # to "skreśl" tą liczbę
                j = j + i # i zwiększ j o 1
        i += 1           # no i zwiększ i o 1

    result = list()
    for i in range(2, n+1):
        if arr[i]:
            result.append(i)

    return result
              
print(sito(10))
print(sito(20))
print(sito(30))
