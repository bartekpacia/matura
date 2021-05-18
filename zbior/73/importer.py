def read_file() -> list[str]:
    with open("tekst.txt") as f:
        text = f.readline().strip()

    words = text.split()
    return words
