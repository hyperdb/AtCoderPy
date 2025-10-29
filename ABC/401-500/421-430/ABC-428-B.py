# ABC-428 B - Most Frequent Substrings
# https://atcoder.jp/contests/abc428/tasks/abc428_b
#
def getIntMap():
    return map(int, input().split())


def getString():
    return input()


def main():
    N, K = getIntMap()
    S = getString()

    d = dict()
    for i in range(N - K + 1):
        ps = S[i : i + K]
        d.setdefault(ps, 0)
        d[ps] += 1

    maxv = max(d.values())
    items = [k for k, v in d.items() if v == maxv]
    items.sort()

    print(maxv)
    print(" ".join(items))


if __name__ == "__main__":
    main()
