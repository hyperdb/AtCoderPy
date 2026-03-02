# ABC-446 A - Handmaid
# https://atcoder.jp/contests/abc446/tasks/abc446_a
#
def getString():
    return input()


def main():
    S = getString()

    # 文字列を小文字に変換後、指定文字と結合して出力
    print(f"Of{S.lower()}")


if __name__ == "__main__":
    main()
