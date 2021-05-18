from importer import read_file

words = read_file()

num_chars = 0
letters_dict = dict()
for word in words:
    for char in word:
        num_chars += 1
        if not letters_dict.get(char):
            letters_dict[char] = 1
        else:
            letters_dict[char] += 1

for k, v in letters_dict.items():
    percent = v / num_chars * 100
    percent_str = str(percent)
    percent_str = percent_str[:4]

    print(f"{k}: {v} ({percent_str}%)")
