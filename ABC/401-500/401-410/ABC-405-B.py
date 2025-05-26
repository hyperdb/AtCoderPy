# ABC-405 B - Not All
# https://atcoder.jp/contests/abc405/tasks/abc405_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    N, M = getIntMap()
    A = getIntList()

    r = 0
    for _ in range(N):
        if len(set(A)) == M:
            A.pop()
            r += 1
            continue
        break
    print(r)


if __name__ == "__main__":
    main()
