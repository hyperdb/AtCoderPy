# ABC-227 B - KEYENCE building
# https://atcoder.jp/contests/abc227/tasks/abc227_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def f(a, b):
    return 4 * a * b + 3 * a + 3 * b


def main():
    n = getInt()
    s = getIntList()

    a = []
    l = min(max(s), 1000) + 1
    for i in range(1, l):
        for j in range(1, l):
            k = f(i, j)
            if k > max(s):
                break
            if not k in a:
                a.append(k)
    c = 0
    for x in s:
        if x in a:
            c += 1
    print(len(s) - c)


if __name__ == "__main__":
    main()
