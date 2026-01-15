# ABC-439 B - Happy Number
# https://atcoder.jp/contests/abc439/tasks/abc439_b
#
def getInt():
    return int(input())


# nを数値にして二乗する
def int_square(n):
    return int(n) ** 2


# 二乗和を求める
def squares(N):
    n = list(map(int_square, list(str(N))))
    return sum(n)


def main():
    N = getInt()
    buf = set()

    n = squares(N)
    buf.add(n)

    result = True
    # 初回が1でなければループ
    if n != 1:
        while True:
            n = squares(n)
            if n == 1:
                break
            # nが既出ならループ終了
            elif n in buf:
                result = False
                break
            else:
                buf.add(n)

    print("Yes" if result else "No")


if __name__ == "__main__":
    main()
