# ABC-334 B - Christmas Trees
# https://atcoder.jp/contests/abc334/tasks/abc334_b
#
def getIntMap():
    return map(int, input().split())


def main():
    a, m, l, r = getIntMap()

    al = abs(l - a) // m
    ar = abs(r - a) // m

    ml = abs(l - a) % m
    mr = abs(r - a) % m

    if l <= a <= r:
        print(ar + al + 1)  # a地点を調整
    else:
        print(abs(ar - al) + (0 if ml != 0 or mr != 0 else 1))  # 開始点がmで割り切れるか


if __name__ == "__main__":
    main()
