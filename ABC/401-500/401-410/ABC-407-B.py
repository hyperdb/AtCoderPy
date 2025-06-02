# ABC-407 B - P(X or Y)
# https://atcoder.jp/contests/abc407/tasks/abc407_b
#
def getIntMap():
    return map(int, input().split())


def main():
    X, Y = getIntMap()

    r = set()
    for i in [i + 1 for i in range(6)]:
        for j in [i + 1 for i in range(6)]:
            if i + j >= X:
                r.add((i, j))
            if abs(i - j) >= Y:
                r.add((i, j))

    print(len(r) / 36)


if __name__ == "__main__":
    main()
