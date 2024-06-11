# ARC-104 A - Plus Minus
# https://atcoder.jp/contests/arc104/tasks/arc104_a
#
def getIntMap():
    return map(int, input().split())


def main():
    A, B = getIntMap()

    # x + y + x - y = A + B
    # 2x = A + B
    x = (A + B) // 2
    y = x - B

    print(x, y)


if __name__ == "__main__":
    main()
