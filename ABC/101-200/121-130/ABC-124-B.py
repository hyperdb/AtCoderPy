# ABC-124 B - Great Ocean View
# https://atcoder.jp/contests/abc124/tasks/abc124_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    h = getIntList()

    c = 1
    for i in range(1, len(h)):
        x = max(h[:i])
        if x <= h[i]:
            c += 1
    print(c)


if __name__ == "__main__":
    main()