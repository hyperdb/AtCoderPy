# ABC-190 A - Very Very Primitive Game
# https://atcoder.jp/contests/abc190/tasks/abc190_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, c = getIntMap()

    d = b - a
    print('Aoki' if d > 0 else 'Takahashi' if d <
          0 else 'Aoki' if c == 0 else 'Takahashi')


if __name__ == "__main__":
    main()
