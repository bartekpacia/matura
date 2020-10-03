input_file = open("dane/dane.txt")

bitmap = []
for line in input_file:
  pixels_str = line.strip().split()
  pixels_int = [int(p) for p in pixels_str]

  bitmap.append(pixels_int)

longest = 0

columns = []

longest_streaks = []
for i in range(320):
  streaks_in_column = []
  for j in range(0, 200):
    local_longest = 0
    for k in range(j, 200):
      pixel_1 = bitmap[j][i]  # 00 10 20 30 40  01 11 21 31 41  02 12 22 32
      pixel_2 = bitmap[k][i]

      if pixel_1 == pixel_2:
        local_longest += 1
      else:
        break

    streaks_in_column.append(local_longest)

  longest_streak_in_column = max(streaks_in_column)
  longest_streaks.append(longest_streak_in_column)


longest_streak = max(longest_streaks)
print(f"{longest_streak=}")
