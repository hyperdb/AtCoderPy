# ABC-085 C - Otoshidama
# https://atcoder.jp/contests/abc085/tasks/abc085_c
#
def getIntMap():
    return map(int, input().split())


def main():
    N, Y = getIntMap()

    # 10000円札の枚数
    for x in range(N + 1):
        # 5000円札の枚数
        for y in range(N - x + 1):
            # 1000円札の枚数はxとyから決定
            z = N - x - y

            if 10000 * x + 5000 * y + 1000 * z == Y:
                print(x, y, z)
                return

    # 見つからなかった場合
    print(-1, -1, -1)


if __name__ == "__main__":
    main()
