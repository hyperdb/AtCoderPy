# ABC-031 A - ゲーム
# https://atcoder.jp/contests/abc031/tasks/abc031_a
#
def getIntMap():
    return map(int, input().split())


def main():
    A, D = getIntMap()

    print(A * D + max(A, D))


if __name__ == "__main__":
    main()
