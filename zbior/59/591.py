def main():
  with open("liczby.txt", "r") as f:
    liczby = [int(line.strip()) for line in f.readlines()]

  for l in liczby:
    print(l)


main()