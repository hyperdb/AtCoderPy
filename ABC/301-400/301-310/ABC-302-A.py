# ABC-302 A - Attack
# https://atcoder.jp/contests/abc302/tasks/abc302_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    c = a // b

    print(c if a % b == 0 else c + 1)


if __name__ == "__main__":
    main()
