with open("liczby1.txt") as f:
    liczby1 = [int(l, 8) for l in f.readlines()]

low = float("inf")
high = -1
for i, num in enumerate(liczby1):
    if num < low:
        low = num

    if num > high:
        high = num

print("min: " + str(oct(low))[2:])
print("max: " + str(oct(high))[2:])
