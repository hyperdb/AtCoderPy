# ABC-231 B - Election
# https://atcoder.jp/contests/abc231/tasks/abc231_b
#
def getInt():
    return int(input())


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    n = getInt()
    s = getStringRow(n)
    t = list(set(s))

    if len(t) == 1:
        print(t[0])
    else:
        r = {}
        for p in t:
            r[p] = s.count(p)
        sr = sorted(r.items(), key=lambda x: x[1], reverse=True)
        print(sr[0][0])


if __name__ == "__main__":
    main()
