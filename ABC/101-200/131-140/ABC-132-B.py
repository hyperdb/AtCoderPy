# ABC-132 B - Ordinary Number
# https://atcoder.jp/contests/abc132/tasks/abc132_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    p = getIntList()

    c = 0
    for i in range(len(p) - 2):
        q = p[i:i+3]
        if min(q) != q[1] and max(q) != q[1]:
            c += 1
    print(c)


if __name__ == "__main__":
    main()
