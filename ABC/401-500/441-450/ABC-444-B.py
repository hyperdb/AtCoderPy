# ABC-444 B - Digit Sum
# https://atcoder.jp/contests/abc444/tasks/abc444_b
#
def getIntMap():
    return map(int, input().split())


def main():
    N, K = getIntMap()

    result = 0
    for n in range(1, N + 1):
        if sum(map(int, list(str(n)))) == K:
            result += 1

    print(result)


if __name__ == "__main__":
    main()
