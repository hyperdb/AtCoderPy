# ABC-356 A - Subsegment Reverse
# https://atcoder.jp/contests/abc356/tasks/abc356_a
#
def getIntMap():
    return map(int, input().split())


def main():
    N, L, R = getIntMap()

    a = [i + 1 for i in range(L - 1)]
    b = [i for i in range(R, L - 1, -1)]
    c = [i for i in range(R + 1, N + 1)]

    print(" ".join(map(str, a + b + c)))


if __name__ == "__main__":
    main()
