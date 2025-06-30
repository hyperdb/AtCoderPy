# ABC-411 A - Required Length
# https://atcoder.jp/contests/abc411/tasks/abc411_a
#
def getString():
    return input()


def getInt():
    return int(input())


def main():
    P = getString()
    L = getInt()

    print("Yes" if L <= len(P) else "No")


if __name__ == "__main__":
    main()
