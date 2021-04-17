from utils import to_num_system

with open("dane/dane.txt") as f:
    lines = [int(line.strip()) for line in f.readlines()]

print(to_num_system(15, 16))

for i in range(2, 17):
    print(to_num_system(100, i))
