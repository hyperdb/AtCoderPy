# ABC-141 A - Weather Prediction
# https://atcoder.jp/contests/abc141/tasks/abc141_a
#
def getString():
    return input()


def main():
    s = getString()
    l = ['Sunny', 'Cloudy', 'Rainy']
    i = l.index(s) + 1
    i = i if i < len(l) else 0

    print(l[i])


if __name__ == "__main__":
    main()
