from triangle import gen_triangle, print_triangle

triangle = gen_triangle(30)

for i, _ in enumerate(triangle):
    for j, _ in enumerate(triangle[i]):
        if triangle[i][j] % 3 == 0:
            triangle[i][j] = 7
        else:
            triangle[i][j] = 0

    print("")

print_triangle(triangle, show_index=False)
