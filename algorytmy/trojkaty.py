from typing import Optional


def skonstruuj_trojkat(a: float, b: float, c: float) -> Optional[tuple[float, float, float]]:
    """
    :return: Boki w kolejności od najkrótszego do najdłuższego
    """
    boki = [a, b, c]
    boki.sort()

    if boki[0] + boki[1] > boki[2]:
        return boki[0], boki[1], boki[2]

    return None


def czy_trojkat(a: float, b: float, c: float) -> bool:
    return skonstruuj_trojkat(a, b, c) is not None


def czy_prostokatny(a: float, b: float, c: float) -> bool:
    trojkat = skonstruuj_trojkat(a, b, c)

    if not trojkat:
        return False

    if trojkat[0] ** 2 + trojkat[1] ** 2 == trojkat[2] ** 2:
        return True

    return False


def czy_rownoboczny(a: float, b: float, c: float) -> bool:
    trojkat = skonstruuj_trojkat(a, b, c)

    if not trojkat:
        return False

    return all(bok == trojkat[0] for bok in trojkat)


def czy_ostrokatny(a: float, b: float, c: float) -> bool:
    trojkat = skonstruuj_trojkat(a, b, c)

    if not trojkat:
        return False

    if trojkat[0] ** 2 + trojkat[1] ** 2 > trojkat[2] ** 2:
        return True

    return False


def czy_rozwartokatny(a: float, b: float, c: float) -> bool:
    trojkat = skonstruuj_trojkat(a, b, c)

    if not trojkat:
        return False

    if trojkat[0] ** 2 + trojkat[1] ** 2 < trojkat[2] ** 2:
        return True

    return False
