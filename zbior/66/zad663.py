def is_square_triangle(a: int, b: int, c: int) -> bool:
    boki = [a, b, c]
    przeciw = max(a, b, c)
    boki.remove(przeciw)

    if boki[0] ** 2 + boki[1] ** 2 == przeciw ** 2:
        return True

    return False


with open("trojki.txt") as file:
    last_square: tuple[int, int, int] | None = None
    for line in file:
        a, b, c = map(int, line.strip().split())

        current_square = (a, b, c)
        if is_square_triangle(a, b, c):
            if last_square:
                print(*last_square)
                print(*current_square)

            last_square = current_square
        else:
            last_square = None
