# ABC-037 A - 饅頭
# https://atcoder.jp/contests/abc037/tasks/abc037_a
#
def getIntMap():
    return map(int, input().split())


def main():
    A, B, C = getIntMap()

    print(C // min(A, B))


if __name__ == "__main__":
    main()
