x, y = map(int, input("podaj współrzędne x i y punktu: ").split())
a, b = map(int, input("podaj współrzędne a i b prostej: ").split())
print(f"{x=}, {y=}, {a=}, {b=}")


def czy_lezy_na_prostej(x: int, y: int, a: int, b: int) -> int:
    """
    zwraca:
    -1 jeśli punkt leży pod prostą
    0 jeśli punkt leży na prostej
    1 jeśli punkt leży nad prostą
    """

    wartosc_funkcji = a * x + b

    if wartosc_funkcji > y:
        return -1
    if wartosc_funkcji == y:
        return 0
    if wartosc_funkcji < y:
        return 1


result = czy_lezy_na_prostej(x, y, a, b)

if result == -1:
    print(f"punkt ({x}, {y}) leży pod prostą")

if result == 0:
    print(f"punkt ({x}, {y}) leży na prostej")

if result == 1:
    print(f"punkt ({x}, {y}) leży nad prostą")
