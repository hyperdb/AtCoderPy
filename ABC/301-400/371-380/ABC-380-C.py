# ABC-380 C - Move Segment
# https://atcoder.jp/contests/abc380/tasks/abc380_c
#
def getIntMap():
    return map(int, input().split())


def getString():
    return input()


def swap(a, b):
    return b, a


def main():
    N, K = getIntMap()
    S = getString()

    c = 0
    buf = S[0]
    sa = []
    for i in range(N):
        if S[i] == buf:
            c += 1
        else:
            sa.append((int(buf), c))
            buf = S[i]
            c = 1

    sa.append((int(buf), c))

    # '1'のK番目の位置
    idx = (K - 1) * 2 + (1 if S[0] == "0" else 0)
    # 1つ前と入れ替える
    sa[idx], sa[idx - 1] = swap(sa[idx], sa[idx - 1])

    r = ""
    for x, y in sa:
        r += str(x) * y
    print(r)


if __name__ == "__main__":
    main()
