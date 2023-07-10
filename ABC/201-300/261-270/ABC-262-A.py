# ABC-262 A - World Cup
# https://atcoder.jp/contests/abc262/tasks/abc262_a
#
def getInt():
    return int(input())


def main():
    n = getInt()

    o = (n + 2) % 4
    print(n if o == 0 else n + 4 - o)


if __name__ == "__main__":
    main()
