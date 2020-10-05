pairs = []
with open("dane/pary.txt") as f:
  for line in f:
    parsed_line = line.strip().split()

    num = int(parsed_line[0])
    text = parsed_line[1]

    pairs.append(tuple([num, text]))

def is_prime(num: int) -> bool:
  for i in range(2, num):
    if num % i == 0:
      return False

  return True


def num_to_primes(num: int) -> (int, int):
  primes = []
  for i in range(2, num):
    if is_prime(i) and is_prime(num - i):
      primes.append(tuple([i, num - i]))

  # para z największą różnicą zawsze będzie pierwsza
  return primes[0]

output_file = open("wyniki_4_1.txt", "w")
for pair in pairs:
  num = pair[0]

  if num % 2 != 0:
    continue

  primes = num_to_primes(num)
  output_file.write(f"{num} {primes[0]} {primes[1]}\n")

output_file.close()