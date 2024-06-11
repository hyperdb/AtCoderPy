# ABC043 A - キャンディーとN人の子供イージー
# https://atcoder.jp/contests/abc043/tasks/abc043_a
#
def getInt():
    return int(input())


def main():
    N = getInt()
    print(int(((N + 1) * N) / 2))


if __name__ == "__main__":
    main()
