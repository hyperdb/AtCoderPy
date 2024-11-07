# ABC-376 A - Candy Button
# https://atcoder.jp/contests/abc376/tasks/abc376_a
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    N, C = getIntMap()
    T = getIntList()

    # 初回は貰える
    t = T[0]
    r = 1

    for i in range(1, N):
        if T[i] - t >= C:
            t = T[i]
            r += 1
    print(r)


if __name__ == "__main__":
    main()
