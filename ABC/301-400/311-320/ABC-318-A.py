# ABC-318 A - Full Moon
# https://atcoder.jp/contests/abc318/tasks/abc318_a
#
def getIntMap():
    return map(int, input().split())


def main():
    n, m, p = getIntMap()
    a = [i * p + m for i in range(n // p + 1) if i * p + m <= n]

    print(len(a))

if __name__ == "__main__":
    main()