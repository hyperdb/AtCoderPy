# ABC-134 B - Golden Apple
# https://atcoder.jp/contests/abc134/tasks/abc134_b
#
def getIntMap():
    return map(int, input().split())


def main():
    n, d = getIntMap()

    c = 2 * d + 1

    print(n // c + (0 if n % c == 0 else 1))


if __name__ == "__main__":
    main()
