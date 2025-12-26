# ABC-047 C - 一次元リバーシ
# https://atcoder.jp/contests/abc047/tasks/arc063_a
#
def getString():
    return input()


def main():
    S = getString()

    print(S.count("WB") + S.count("BW"))


if __name__ == "__main__":
    main()
