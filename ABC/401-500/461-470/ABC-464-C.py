# ABC-464 C - Plumage Palette
# https://atcoder.jp/contests/abc464/tasks/abc464_c
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N, M = getIntMap()
    ADB = getIntListRow(N)

    # 色ごとの個数を管理する辞書
    base_color = dict()
    # 日にちごとの色の変化を管理する辞書
    change_color = dict()

    ADB.sort(key=lambda x: x[1])

    for a, b, d in ADB:
        # 色ごとの個数をカウント
        base_color.setdefault(a, 0)
        base_color[a] += 1
        # 日にちごとの色の変化（a -> d）を管理
        change_color.setdefault(b, [])
        change_color[b].append((a, d))

    # 0日目の個数をカウント
    all_color_count = len(base_color)

    # 1日目からM日目までの個数をカウント
    for day in range(1, M + 1):
        if day in change_color:
            for a, d in change_color[day]:
                # 置き換えられる色の個数を減らす
                base_color[a] -= 1
                # 個数が0になったら全体の個数を減らす
                if base_color[a] == 0:
                    # del base_color[a]
                    all_color_count -= 1
                # 置き換えた色の個数を増やす
                base_color[d] = base_color.get(d, 0) + 1
                # 新しい色（個数が1）なら全体の個数を増やす
                if base_color[d] == 1:
                    all_color_count += 1

        # 個数を出力
        print(all_color_count)


if __name__ == "__main__":
    main()
