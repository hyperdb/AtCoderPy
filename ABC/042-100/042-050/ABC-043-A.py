# ABC043 A - キャンディーとN人の子供イージー
# https://atcoder.jp/contests/abc043/tasks/abc043_a
#
def getInt():
    return int(input())


def main():
    param = getInt()
    print(int(((param + 1) * param) / 2))


if __name__ == "__main__":
    main()
