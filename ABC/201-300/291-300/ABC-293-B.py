# ABC-293 B - Call the ID Number
# https://atcoder.jp/contests/abc293/tasks/abc293_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    a = [0] + getIntList()
    b = [0 for _ in range(len(a))]

    for i in range(1, len(a)):
        if b[i] == 0:
            b[a[i]] = 1
    c = [i for i in range(1, len(b)) if b[i] == 0]

    print(len(c))
    print(" ".join(map(str, c)))


if __name__ == "__main__":
    main()
