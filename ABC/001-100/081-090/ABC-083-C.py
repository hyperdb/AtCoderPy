# ABC083-C - Multiple Gift
# https://atcoder.jp/contests/abc083/tasks/arc088_a
#
def getIntMap():
    return map(int, input().split())


def main():
    X, Y = getIntMap()

    n = X  # 初期値はX
    result = 0
    # Yを超えるまで繰り返す
    while n <= Y:
        result += 1
        # 最小の倍数は2倍
        n *= 2

    print(result)


if __name__ == "__main__":
    main()
