# ABC-312 A - Chord
# https://atcoder.jp/contests/abc312/tasks/abc312_a
#
def getString():
    return input()


def main():
    s = getString()

    print('Yes' if s in ['ACE', 'BDF', 'CEG', 'DFA', 'EGB', 'FAC', 'GBD'] else 'No')


if __name__ == "__main__":
    main()
