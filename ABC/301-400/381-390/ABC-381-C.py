# ABC-381 C - 11/22 Substring
# https://atcoder.jp/contests/abc381/tasks/abc381_c
#
def getInt():
    return int(input())


def getString():
    return input()


def main():
    N = getInt()
    S = getString()

    ch = S[0]
    cnt = 1
    d = []
    for i in range(1, N):
        if S[i] != ch:
            d.append([ch, cnt])
            ch = S[i]
            cnt = 1
        else:
            cnt += 1
    d.append([ch, cnt])

    r = 1
    for i in range(1, len(d) - 1):
        # "/"　かつ 連続していない
        if d[i][0] == "/" and d[i][1] == 1:
            # 前後が"1"と"2"
            if d[i - 1][0] == "1" and d[i + 1][0] == "2":
                w = min(d[i - 1][1], d[i + 1][1])
                r = max(r, w * 2 + 1)

    print(r)


if __name__ == "__main__":
    main()
