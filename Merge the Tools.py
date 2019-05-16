def without_repetition(t):
    s = set()
    o = []
    for c in t:
        if c not in s:
            s.add(c)
            o.append(c)
    return ''.join(o)


def main():
    s = input()
    k = int(input())
    n = len(s)
    w = k
    for t in [s[i:i + w] for i in range(0, n, w)]:
        print(without_repetition(t))


main()

'''Hacker rank version'''

from collections import OrderedDict


def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        print(''.join(OrderedDict.fromkeys(string[i:i+k])))



if __name__=='__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

