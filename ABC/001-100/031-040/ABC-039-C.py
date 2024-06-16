# ABC-039 C - ピアニスト高橋君
# https://atcoder.jp/contests/abc039/tasks/abc039_c
#
def getString():
    return input()


def main():
    S = getString()
    kb = "WBWBWBW"
    map = {0: "Fa", 1: "Mi", 3: "Re", 5: "Do", 6: "Si", 8: "La", 10: "So"}

    i = S.index(kb)

    print(map[i])


if __name__ == "__main__":
    main()
