# ABC-353 B - AtCoder Amusement Park
# https://atcoder.jp/contests/abc353/tasks/abc353_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, k = getIntMap()
    a = getIntList()

    b = [0]
    i = 0
    for x in a:
        if b[i] + x <= k:
            b[i] += x
        else:
            b.append(x)
            i += 1

    print(len(b))


if __name__ == "__main__":
    main()
