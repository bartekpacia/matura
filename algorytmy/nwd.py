def nwd_i(a: int, b: int) -> int:
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def nwd_r(a: int, b: int) -> int:
    if b == 0:
        return a
    return nwd_r(b, a % b)


def nww(a: int, b: int) -> int:
    return (a * b) // nwd_i(a, b)
