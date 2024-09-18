# ABC-370 A - Raise Both Hands
# https://atcoder.jp/contests/abc370/tasks/abc370_a
#
def getIntMap():
    return map(int, input().split())


def main():
    L, R = getIntMap()

    h = L + R * 2

    print("Yes" if h == 1 else "No" if h == 2 else "Invalid")


if __name__ == "__main__":
    main()
