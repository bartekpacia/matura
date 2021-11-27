def read_nums(debug: bool = False) -> list[int]:
    if debug:
        # from problem listing
        return [4, 11, 4, 1, 4, 7, 11, 12, 13, 14, 7, 0, 3]

    nums: list[int] = []
    with open("dane/dane4.txt") as file:
        for line in file:
            sline = line.strip()
            nums.append(int(sline))

    return nums
