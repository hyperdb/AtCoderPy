# ABC-440 B - Trifecta
# https://atcoder.jp/contests/abc440/tasks/abc440_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    _N = getInt()
    A = getIntList()

    d = {}
    i = 0
    for a in range(len(A)):
        d.setdefault(i + 1, A[a])
        i += 1

    sorted_list = sorted(d.items(), key=lambda x: x[1])
    print(" ".join(str(item[0]) for item in sorted_list[:3]))


if __name__ == "__main__":
    main()
