# ABC-346 B - Piano
# https://atcoder.jp/contests/abc346/tasks/abc346_b
#
def getIntMap():
    return map(int, input().split())


def main():
    s = 'wbwbwwbwbwbw'
    w, b = getIntMap()
    wb = w + b

    # w + b -> max:200
    sa = s * 20

    r = False
    # 始点をずらして12パターン
    for i in range(12):
        sl = sa[i:i+wb]
        if w == sl.count('w') and b == sl.count('b'):
            r = True
            break

    print('Yes' if r else 'No')


if __name__ == "__main__":
    main()
