# ABC-190 B - Magic 3
# https://atcoder.jp/contests/abc190/tasks/abc190_b
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n, s, d = getIntMap()
    l = getIntListRow(n)

    a = False
    for x, y in l:
        if x < s and y > d:
            a = True
            break
    print('Yes' if a else 'No')


if __name__ == "__main__":
    main()
