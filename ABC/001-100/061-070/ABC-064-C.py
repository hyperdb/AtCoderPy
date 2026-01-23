# ABC-064 C - Colorful Leaderboard
# https://atcoder.jp/contests/abc064/tasks/abc064_c
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    _N = getInt()
    a = getIntList()

    c = [0] * 8
    multi = 0

    for v in a:
        if v >= 3200:
            multi += 1
        else:
            c[v // 400] += 1

    used_c = sum([1 for x in c if x > 0])
    # 色は8色ではなく、8色＋自由に選べる色なので以下のように修正
    # unused_c = sum([1 for x in c if x == 0])
    # max_c = used_c + min(multi, unused_c)
    max_c = used_c + multi
    min_c = used_c if used_c > 0 else 1

    print(min_c, max_c)


if __name__ == "__main__":
    main()
