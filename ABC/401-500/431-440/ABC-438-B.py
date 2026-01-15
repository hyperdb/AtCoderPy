# ABC-438 B - Substring 2
# https://atcoder.jp/contests/abc438/tasks/abc438_b
#
def getIntMap():
    return map(int, input().split())


def getString():
    return input()


def main():
    N, M = getIntMap()
    S = getString()
    T = getString()

    result = M * 10
    for i in range(N - M + 1):
        s = S[i : i + M]
        c = 0
        for j in range(M):
            # 各桁を数値で比較
            x = int(s[j])
            y = int(T[j])
            # 桁ごとの差を加算
            c += x - y if x - y >= 0 else x - y + 10
        # 差の最小値を更新
        result = min(result, c)
    print(result)


if __name__ == "__main__":
    main()
