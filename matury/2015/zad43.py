with open("dane/liczby.txt") as f:
  nums = [int(l.strip(), 2) for l in f.readlines()]

wynik43 = open("wynik43.txt", "w")

smallest = nums.index(min(nums)) + 1
biggest = nums.index(max(nums)) + 1

wynik43.write(f"wiersz z najmniejsza liczba: {smallest}, najwieksza liczba: {biggest}")
wynik43.close()
