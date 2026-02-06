# ABC-079 C - Train Ticket
# https://atcoder.jp/contests/abc079/tasks/abc079_c
#
def getString():
    return input()


def main():
    S = list(getString())

    # 000～111のパターンを全探索
    for i in range(8):
        mask = 1
        buf = []
        # ビットパターンを確認
        for tm in range(0, 3):
            flag = mask & i
            # ビットが立っていればバッファに格納
            if flag > 0:
                buf.append(tm + 1)
            mask = mask << 1

        # 計算と式の組み立て
        # 1桁目を初期値として設定
        calc = int(S[0])
        formula = S[0]
        # 2桁目以降を確認
        for j in range(1, len(S)):
            # バッファに格納されたインデックスを確認
            if j in buf:
                calc += int(S[j])
                formula += "+" + S[j]
            else:
                calc -= int(S[j])
                formula += "-" + S[j]

        if calc == 7:
            print(formula + "=7")
            return


if __name__ == "__main__":
    main()
