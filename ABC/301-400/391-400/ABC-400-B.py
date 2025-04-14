# ABC-400 B - Sum of Geometric Series
# https://atcoder.jp/contests/abc400/tasks/abc400_b
#
def getIntMap():
    return map(int, input().split())


def main():
    N, M = getIntMap()

    X = 0
    z = 10**9
    r = True
    for i in range(M + 1):
        X += N**i
        if X > z:
            r = False
            break
    print(X if r else "inf")


if __name__ == "__main__":
    main()
