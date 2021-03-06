from triangle import gen_triangle

triangle = gen_triangle(30)
for i, _ in enumerate(triangle):
    ok = True

    for num in triangle[i]:
        if num % 5 == 0:
            ok = False

    if ok:
        print(f"row {i + 1} is OK")
