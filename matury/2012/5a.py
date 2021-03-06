from typing import List


def gen_triangle(n: int) -> List[List[int]]:
    if n < 1:
        print("error: n < 1")
        return []

    triangle = []

    for i in range(n):
        triangle.append([])
        row_len = i + 1

        for j in range(row_len):
            triangle[i].append(1)

    return triangle


my_triangle = gen_triangle(10)
for i, _ in enumerate(my_triangle):
    for j, _ in enumerate(my_triangle[i]):
        print(my_triangle[i][j], end="")

    print("")
