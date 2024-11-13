# ABC-035 B - ドローン
# https://atcoder.jp/contests/abc035/tasks/abc035_b
#
def getInt():
    return int(input())


def getString():
    return input()


def main():
    S = list(getString())
    T = getInt()

    x = S.count(("R")) - S.count("L")
    y = S.count(("U")) - S.count("D")
    q = S.count("?")

    for i in range(q):
        if T == 1:
            if x >= 0:
                x += 1
            else:
                x -= 1
        else:
            if x > 0:
                x -= 1
            elif x < 0:
                x += 1
            elif y > 0:
                y -= 1
            elif y < 0:
                y += 1
            else:
                x += 1

    r = abs(x) + abs(y)
    print(r)


if __name__ == "__main__":
    main()
