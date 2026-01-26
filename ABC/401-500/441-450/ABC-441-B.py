# ABC-441 B - Two Languages
# https://atcoder.jp/contests/abc441/tasks/abc441_b
#
def getIntMap():
    return map(int, input().split())


def getInt():
    return int(input())


def getString():
    return input()


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    N, M = getIntMap()
    S = getString()
    T = getString()
    Q = getInt()
    w = getStringRow(Q)

    s = set(S)
    t = set(T)

    for i in range(Q):
        lang = []
        # 部分集合のチェック
        if set(w[i]) <= s:
            lang.append("Takahashi")
        if set(w[i]) <= t:
            lang.append("Aoki")
        # 両方に該当しても”Unknown"
        print(lang[0] if len(lang) == 1 else "Unknown")


if __name__ == "__main__":
    main()
