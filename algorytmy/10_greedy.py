nominaly = [200, 100, 50, 20, 10, 5, 2, 1]


def change(money: int):
    print(f"----- {money} -----")
    reszta = money

    for nominal in nominaly:
        if reszta == 0:
            break
        if reszta >= nominal:
            x = reszta // nominal
            print(nominal, "x", x)
            reszta = reszta - x * nominal


change(2)
change(10)
change(69)
change(101)
