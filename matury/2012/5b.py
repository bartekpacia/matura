from triangle import gen_triangle

triangle = gen_triangle(30)

for i, _ in enumerate(triangle):
    char_count = 0
    for num in triangle[i]:
        char_count += len(str(num))

    print(f"row: {i + 1}, {char_count=}")
