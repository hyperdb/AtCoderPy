# ABC-354 A - Exponential Plant
# https://atcoder.jp/contests/abc354/tasks/abc354_a
#
def getInt():
    return int(input())


def main():
    h = getInt()

    d = 0
    t = 0
    while h >= t:
        t += (2 ** d)
        d += 1
    print(d)


if __name__ == "__main__":
    main()
