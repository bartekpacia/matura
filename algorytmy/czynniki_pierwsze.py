def czynniki_pierwsze(num: int) -> []:
    factors = []
    k = 2

    while num > 1:
        while num % k == 0:
            factors.append(k)
            num = num // k

        k = k + 1

    return factors
