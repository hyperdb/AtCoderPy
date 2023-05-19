# ABC-164 B - Battle
# https://atcoder.jp/contests/abc164/tasks/abc164_b
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, c, d = getIntMap()

    while a > 0 and c > 0:
        c -= b
        if c <= 0:
            print('Yes')
            break
        a -= d
        if a <= 0:
            print('No')
            break


if __name__ == "__main__":
    main()
