# ABC-220 A - Find Multiple
# https://atcoder.jp/contests/abc220/tasks/abc220_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, c = getIntMap()

    d = a if a == c else (a // c + 1) * c

    print(d if d <= b else -1)


if __name__ == "__main__":
    main()
