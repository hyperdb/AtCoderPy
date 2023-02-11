# ABC-125 A - Biscuit Generator
# https://atcoder.jp/contests/abc125/tasks/abc125_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, t = getIntMap()

    print(t // a * b)


if __name__ == "__main__":
    main()
