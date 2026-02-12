# ABC043 A - キャンディーとN人の子供イージー
# https://atcoder.jp/contests/abc043/tasks/abc043_a
#
def getInt() -> int:
    return int(input())


def main():
    N: int = getInt()
    print(((N + 1) * N) // 2)


if __name__ == "__main__":
    main()
