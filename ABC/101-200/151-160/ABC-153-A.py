# ABC-153 A - Serval vs Monster
# https://atcoder.jp/contests/abc153/tasks/abc153_a
#
def getIntMap():
    return map(int, input().split())


def main():
    h, a = getIntMap()

    c = 0
    while h > 0:
        h -= a
        c += 1
    print(c)


if __name__ == "__main__":
    main()
