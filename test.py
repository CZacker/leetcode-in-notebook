# # coding=utf-8
# import sys
#
#
# def catchOne(atrs):
#     n = len(atrs)
#     cal = lambda ai, bi, j, ns: ai * (j - 1) + bi * (ns - j)
#     por = lambda ai, bi: bi - ai
#     pors = [por(atr[0], atr[1]) for atr in atrs]
#
#     por_sorted = pors.copy()
#     por_sorted.sort()
#     result = 0
#     for ind, atr in enumerate(atrs):
#         j = por_sorted.index(pors[ind])
#         por_sorted.remove(pors[ind])
#         result += cal(atr[0], atr[1], j, n)
#     return result
#
#
# if __name__ == "__main__":
#     m = int(sys.stdin.readline().strip())
#     ans = 0
#     atrs = []
#     for i in range(m):
#         line = sys.stdin.readline().strip()
#         a = list(map(int, line.split()))
#         atrs.append(a)
#     print(catchOne(atrs))
#
#
# def reverse(text):
#     """
#     input: 'abcd'
#     output: 'dcba'
#     """
#     alist = [i for i in text]
#     result = []
#     for i in range(len(alist)):
#         result.append(alist.pop())
#
#     return ''.join(result)


def find_the_path(data, value):
    """
    input: (data, 'data3')
    output: ['d1', 'd2b', 'd3b', 'd4b']
    """
    if data is None or value == '':
        return []

    result = []
    dfs(data, value)
    pass


def dfs(data, vuale):
    for key, values in data.items():
        try:
            print(key)
            dfs(value, values)
        except AttributeError:
            print(str(value))




data = {
        'a1': {
            'a2': {
                'a3': 'data under a',
                },
            },
        'b1': None,
        'c1': {
            'c2':{
                'c2a': 'data1',
                'c2b': 'data2',
                }
            },
        'd1': {
            'd2a': {
                'd2a1': 3,
                'd2a2': 4,
                },
            'd2b': {
                'd3b': {
                    'd4b': 'data3',  # the value need to find
                    },
                'd3c': 12345,
                }
            }
        }

find_the_path(data, 'data3')


