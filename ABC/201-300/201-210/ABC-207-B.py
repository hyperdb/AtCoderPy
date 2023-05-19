# ABC-207 B - Hydrate
# https://atcoder.jp/contests/abc207/tasks/abc207_b
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, c, d = getIntMap()

    r = -1
    for i in range(10 ** 5 + 1):
        if (a + b * i) <= (c * i) * d:
            r = i
            break
    print(r)


if __name__ == "__main__":
    main()
