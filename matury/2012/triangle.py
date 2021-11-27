def gen_triangle(n: int) -> list[list[int]]:
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


def print_triangle(triangle: list[list[int]], show_index: bool = False):
    for i, _ in enumerate(triangle):
        if show_index:
            print(f"row: {i + 1}", end="    ")

        for j, _ in enumerate(triangle[i]):
            print(triangle[i][j], end=" ")

        print("")
