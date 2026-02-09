# ABC-443 B - Setsubun
# https://atcoder.jp/contests/abc443/tasks/abc443_b
#
def getIntMap():
    return map(int, input().split())


def main():
    N, K = getIntMap()

    x = 0  # 年数
    sum = N
    while sum < K:
        x += 1
        sum += N + x
    print(x)


if __name__ == "__main__":
    main()
