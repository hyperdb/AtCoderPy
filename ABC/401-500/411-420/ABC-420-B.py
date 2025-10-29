# ABC-420 B - Most Minority
# https://atcoder.jp/contests/abc420/tasks/abc420_b
#
def getIntMap():
    return map(int, input().split())


def getStringRow(N):
    return [list(input()) for _ in range(N)]


def main():
    N, M = getIntMap()
    S = getStringRow(N)

    point = [0 for _ in range(N)]
    r = [list(x) for x in zip(*S, strict=False)]

    for i in range(M):
        s = [r[i].count("0"), r[i].count("1")]
        if s[0] == 0 or s[1] == 0:
            for j in range(N):
                point[j] += 1
        elif s[0] < s[1]:
            for j in range(N):
                if r[i][j] == "0":
                    point[j] += 1
        elif s[0] > s[1]:
            for j in range(N):
                if r[i][j] == "1":
                    point[j] += 1

    ans = [i + 1 for i in range(N) if point[i] == max(point)]
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()
