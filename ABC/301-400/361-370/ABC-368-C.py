#
#
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    H = getIntList()

    T = 0
    for i in range(N):
        d, m = divmod(H[i], 5)
        T += d * 3
        while m > 0:
            T += 1
            m -= 3 if T % 3 == 0 else 1

    print(T)


if __name__ == "__main__":
    main()
