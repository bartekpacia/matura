def jest_anagram(a: str, b: str) -> bool:
    # the fast way
    if a == b:
        return True

    a_chars: dict[str, int] = {}
    for char in a:
        if not a_chars.get(char):
            a_chars[char] = 1
        else:
            a_chars[char] += 1

    b_chars: dict[str, int] = {}
    for char in b:
        if not b_chars.get(char):
            b_chars[char] = 1
        else:
            b_chars[char] += 1

    return a_chars == b_chars


def jest_jednolity(a: str) -> bool:
    chars: set[str] = set()
    for char in a:
        chars.add(char)

    return len(chars) == 1
