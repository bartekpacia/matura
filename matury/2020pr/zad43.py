import operator

from reader import read_nums

nums = read_nums()

gaps: dict[int, int] = {}

for i in range(1, len(nums)):
    num1 = nums[i - 1]
    num2 = nums[i]

    gap = abs(num1 - num2)

    if not gaps.get(gap):
        gaps[gap] = 1
    else:
        gaps[gap] += 1

gap_list: list[tuple[int, int]] = []

max_occurences = 0
for gap, occurences in gaps.items():
    tuple_item = (gap, occurences)
    gap_list.append(tuple_item)

    if occurences > max_occurences:
        max_occurences = occurences

gap_list.sort(key=operator.itemgetter(1), reverse=True)

most_often_gaps: list[int] = []
for gap_tuple in gap_list:
    gap = gap_tuple[0]
    occurences = gap_tuple[1]

    if occurences == max_occurences:
        most_often_gaps.append(gap)

print("---")
print(f"krotność najczęstszej luki:", gap_list[0][1])
print(f"wartości najczęstszych luk:", *most_often_gaps)
