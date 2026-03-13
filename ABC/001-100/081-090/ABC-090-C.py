# ABC-090 C - Flip,Flip, and Flip......
# https://atcoder.jp/contests/abc090/tasks/arc091_a
#
def getIntMap():
    return map(int, input().split())


def main():
    N, M = getIntMap()

    if N > M:
        N, M = M, N

    if N == 1:
        # 1x1なら1通り
        if M == 1:
            print(1)
        # 1xMならM-2通り（両端が偶数回で元に戻る）
        else:
            print(M - 2)
    else:
        # NxMなら(N-2)x(M-2)通り（それぞれの両端が偶数回で元に戻る）
        print((N - 2) * (M - 2))


if __name__ == "__main__":
    main()
