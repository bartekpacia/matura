def jest_anagram(a: str, b: str) -> bool:
    # the fast way
    if a == b:
        return True

    a_chars = {}
    for char in a:
        if not a_chars.get(char):
            a_chars[char] = 1
        else:
            a_chars[char] += 1

    b_chars = {}
    for char in b:
        if not b_chars.get(char):
            b_chars[char] = 1
        else:
            b_chars[char] += 1

    return a_chars == b_chars


def jest_jednolity(a: str) -> bool:
    chars = set()
    for char in a:
        chars.add(char)

    return len(chars) == 1