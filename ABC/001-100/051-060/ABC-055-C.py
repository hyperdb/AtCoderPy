# ABC-055 C - Scc Puzzle
# https://atcoder.jp/contests/abc055/tasks/arc069_a
#
def getIntMap():
    return map(int, input().split())


def main():
    N, M = getIntMap()

    # Sを使い切ってもCが余る場合
    if M > 2 * N:
        scc = N + (M - 2 * N) // 4
    # Cが足りない場合
    else:
        scc = M // 2

    print(scc)


if __name__ == "__main__":
    main()
