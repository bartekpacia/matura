from typing import Optional


def skonstruuj_trojkat(a: float, b: float, c: float) -> Optional[tuple[float, float, float]]:
    """
    :return: Boki w kolejności od najkrótszego do najdłuższego
    """
    bok_max = max(a, b, c)
    bok_min = min(a, b, c)

    if bok_min + b > bok_max:
        return bok_min, b, bok_max

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
