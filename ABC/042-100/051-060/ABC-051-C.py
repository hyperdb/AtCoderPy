# ABC-051 C - Back and Forth
# https://atcoder.jp/contests/abc051/tasks/abc051_c
#
def getIntMap():
    return map(int, input().split())


def main():
    sx, sy, tx, ty = getIntMap()

    # １周目は二点を対角とする長方形の辺を移動する

    w = tx - sx
    h = ty - sy

    m = 'R' * w + 'U' * h + 'L' * w + 'D' * h

    # ２周目は１周目の外周を移動する
    # そのため移動する幅・高さは１つ増える

    w += 1
    h += 1

    m += 'D' + 'R' * w + 'U' * h + 'L' + 'U' + 'L' * w + 'D' * h + 'R'

    print(m)


if __name__ == "__main__":
    main()
