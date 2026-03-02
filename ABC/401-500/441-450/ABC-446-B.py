# ABC-446 B - Greedy Draft
# https://atcoder.jp/contests/abc446/tasks/abc446_b
#
def getInt():
    return int(input())


def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    N, M = getIntMap()
    L = [0] * N
    X = [[] for _ in range(N)]

    # 売れた缶ジュースを記録するリスト
    sold = []

    for i in range(N):
        L[i] = getInt()
        X[i] = getIntList()
        found = False
        for x in X[i]:
            # すでに売れた缶ジュースであればスキップ、
            if x in sold:
                continue
            # そうでなければ売れた缶ジュースとして記録してループを抜ける
            else:
                sold.append(x)
                found = True
                break
        if found:
            continue
        # 希望の缶ジュースが売れ切れている場合は、水(0)を記録する
        sold.append(0)

    # 1行ずつ出力
    for i in sold:
        print(f"{i}")


if __name__ == "__main__":
    main()
