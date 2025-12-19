# ABC-424 B - Perfect
# https://atcoder.jp/contests/abc424/tasks/abc424_b
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N, M, K = getIntMap()
    AB = getIntListRow(K)

    ans = [0] + [0 for _ in range(N)]
    p = []
    for a, _ in AB:
        ans[a] += 1
        if ans[a] == M:
            p.append(a)

    if len(p) > 0:
        print(" ".join(map(str, p)))


if __name__ == "__main__":
    main()
