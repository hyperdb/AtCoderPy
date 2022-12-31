# ABC-070 B - Two Switches
# https://atcoder.jp/contests/abc070/tasks/abc070_b
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, c, d = getIntMap()

    s = a if c < a else c
    e = b if d > b else d

    print(0 if b < c or d < a else e - s)


if __name__ == "__main__":
    main()
