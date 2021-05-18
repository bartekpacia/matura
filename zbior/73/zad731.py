from importer import read_file
words = read_file()

num = 0
for word in words:

    one_after_another = False
    for i in range(len(word) - 1):
        char1 = word[i]
        char2 = word[i + 1]

        if char1 == char2:
            one_after_another = True

    if one_after_another:
        num += 1

print(num)
