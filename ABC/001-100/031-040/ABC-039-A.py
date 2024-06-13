# ABC-039 A - 高橋直体
# https://atcoder.jp/contests/abc039/tasks/abc039_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, c = getIntMap()

    print((a * b + b * c + c * a) * 2)


if __name__ == "__main__":
    main()
