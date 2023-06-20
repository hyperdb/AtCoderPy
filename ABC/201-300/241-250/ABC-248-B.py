# ABC-248 B - Slimes
# https://atcoder.jp/contests/abc248/tasks/abc248_b
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, k = getIntMap()

    i = 0
    while b > a:
        a *= k
        i += 1
    print(i)


if __name__ == "__main__":
    main()
