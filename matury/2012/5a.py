from typing import List


def gen_triangle(n: int) -> List[List[int]]:
    if n < 1:
        print("error: n < 1")
        return []

    triangle = [[1]]

    for i in range(1, n):
        triangle.append([])

        for j in range(i + 1):
            ii = i - 1
            jj = j - 1
            if jj >= 0 and ii >= 0:
                up_left = triangle[ii][jj]
            else:
                up_left = 0

            if ii >= 0:
                try:
                    up = triangle[ii][j]
                except IndexError:
                    up = 0
            else:
                up = 0

            triangle[i].append(up_left + up)

    return triangle


my_triangle = gen_triangle(10)
for i, _ in enumerate(my_triangle):
    print(f"row: {i + 1}", end="    ")
    for j, _ in enumerate(my_triangle[i]):
        print(my_triangle[i][j], end=" ")

    print("")
