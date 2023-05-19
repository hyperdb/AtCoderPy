# ABC-217 B - AtCoder Quiz
# https://atcoder.jp/contests/abc217/tasks/abc217_b
#
def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    s = getStringRow(3)
    t = ['ABC', 'ARC', 'AGC', 'AHC']

    for w in t:
        if w in s:
            continue
        print(w)
        break


if __name__ == "__main__":
    main()
