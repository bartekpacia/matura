from typing import List


def read_nums() -> List[int]:
    nums: List[int] = []
    with open("dane/dane4.txt") as file:
        for line in file:
            sline = line.strip()
            nums.append(int(sline))

    return nums
