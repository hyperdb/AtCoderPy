# ABC-453 B - Sensor Data Logging
# https://atcoder.jp/contests/abc453/tasks/abc453_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    T, X = getIntMap()
    A = getIntList()

    # 基準値を保存して出力
    saved = A[0]
    print(f"0 {saved}")
    # 1つずつ基準値との差を比較して出力
    for i in range(1, T + 1):
        if abs(saved - A[i]) >= X:
            print(f"{i} {A[i]}")
            # 基準値を更新
            saved = A[i]


if __name__ == "__main__":
    main()
