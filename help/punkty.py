x1, y1 = map(int, input("podaj współrzędne x i y punktu A: ").split())
x2, y2 = map(int, input("podaj współrzędne x i y punktu B: ").split())
x3, y3 = map(int, input("podaj współrzędne x i y punktu C: ").split())
print(f"{x1=}, {y1=}, {x2=}, {y2=}, {x3=}, {y3=}")


def czy_lezy_na_prostej(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> bool:
    """
    zwraca:
    -1 jeśli punkt leży pod prostą
    0 jeśli punkt leży na prostej
    1 jeśli punkt leży nad prostą
    """

    wyznacznik = (x1 * y2) + (x2 * y3) + (x3 * y1) - (x2 * y1) - (x1 * y3) - (x3 * y2)

    if wyznacznik != 0:
        print("punkt NIE należy do prostej i do odcinka")
        exit(0)

    if min(x1, x2) <= x3 and max(x1, x2) >= x3 and min(y1, y2) <= y3 and max(y1, y2) >= y3:
        print("punky C należy do prostej i do odcinka odcinka")
    else:
        print("punkt należy do prostej, ale NIE należy odcinka")


czy_lezy_na_prostej(x1, y1, x2, y2, x3, y3)
