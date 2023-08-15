# ABC-284 B - Multi Test Cases
# https://atcoder.jp/contests/abc284/tasks/abc284_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    t = getInt()
    o = []
    for i in range(t):
        n = getInt()
        a = getIntList()
        m = [x % 2 for x in a]
        o.append(sum(m))
    for c in o:
        print(c)


if __name__ == "__main__":
    main()
