punkty = []

with open("dane/punkty.txt") as f:
    punkty_raw = [l.strip() for l in f.readlines()]

    for p in punkty_raw:
        p = p.split()
        punkt = (int(p[0]), int(p[1]))

        punkty.append(punkt)

a = 200
b = 200
r = 200

### end boiler

punkty_w_brzegu = []
punkty_we_wnetrzu_pierwsze_100 = []
punkty_we_wnetrzu = []
for i, punkt in enumerate(punkty):
    if i == 100:
        punkty_we_wnetrzu_pierwsze_100 = punkty_we_wnetrzu.copy()

    x = punkt[0]
    y = punkt[1]

    if (x - a) ** 2 + (y - b) ** 2 == r ** 2:
        punkty_w_brzegu.append(punkt)

    if (x - a) ** 2 + (y - b) ** 2 < r ** 2:
        punkty_we_wnetrzu.append(punkt)

print(f"{punkty_w_brzegu=}")
print(f"{len(punkty_we_wnetrzu_pierwsze_100)=}")
print(f"{len(punkty_we_wnetrzu)=}")
