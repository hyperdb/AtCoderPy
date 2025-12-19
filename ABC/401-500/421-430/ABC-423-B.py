# ABC-423 B - Locked Rooms
# https://atcoder.jp/contests/abc423/tasks/abc423_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def count_door(L):
    count = 0
    for stat in L:
        count += 1
        if stat == 1:
            break
    return count


def main():
    N = getInt()
    L = getIntList()

    p1 = count_door(L)
    r1 = [i for i in range(p1, N)]

    L.reverse()

    p2 = N - count_door(L)
    r2 = [i for i in range(p2, 0, -1)]

    print(len(set(r1) & set(r2)))


if __name__ == "__main__":
    main()
