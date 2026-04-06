# ABC-451 B - Personnel Change
# https://atcoder.jp/contests/abc451/tasks/abc451_b
#


def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N, M = getIntMap()
    AB = getIntListRow(N)
    current = [0] * M
    next = [0] * M
    # それぞれの部署を数える
    for a, b in AB:
        current[a - 1] += 1
        next[b - 1] += 1
    # 差分を出力
    for i in range(M):
        print(next[i] - current[i])


if __name__ == "__main__":
    main()
