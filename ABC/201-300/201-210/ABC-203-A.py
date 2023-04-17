# ABC-203 A - Chinchirorin
# https://atcoder.jp/contests/abc203/tasks/abc203_a
#
def getIntList():
    return list(map(int, input().split()))


def main():
    l = getIntList()

    l.sort()
    c = len(set(l))

    if c == 3:
        print(0)
    elif c == 1:
        print(l[0])
    else:
        print(l[2] if l[0] == l[1] else l[0])


if __name__ == "__main__":
    main()
