# ABC-315 B - The Middle Day
# https://atcoder.jp/contests/abc315/tasks/abc315_b
#
def getInt():
    return int(input())

def getIntList():
    return list(map(int, input().split()))

def main():
    m = getInt()
    d = getIntList()

    c = (sum(d) + 1) // 2

    r = []
    for i in range(m):
        if sum(d[:i]) > c:
            break
        r.append(sum(d[:i]))

    n = len(r)
    if c == max(r):
        # previous month
        n -= 1
        print(n, d[n - 1])
    else:
        print(n, c - max(r))


if __name__ == "__main__":
    main()