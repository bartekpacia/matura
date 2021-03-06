from triangle import gen_triangle

my_triangle = gen_triangle(30)

max_in_10 = max(my_triangle[9])
max_in_20 = max(my_triangle[19])
max_in_30 = max(my_triangle[29])

print(f"{max_in_10=}, {max_in_20=}, {max_in_30=}")
