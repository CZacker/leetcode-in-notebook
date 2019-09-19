# # # coding=utf-8
# # import sys
# #
# #
# # def catchOne(atrs):
# #     n = len(atrs)
# #     cal = lambda ai, bi, j, ns: ai * (j - 1) + bi * (ns - j)
# #     por = lambda ai, bi: bi - ai
# #     pors = [por(atr[0], atr[1]) for atr in atrs]
# #
# #     por_sorted = pors.copy()
# #     por_sorted.sort()
# #     result = 0
# #     for ind, atr in enumerate(atrs):
# #         j = por_sorted.index(pors[ind])
# #         por_sorted.remove(pors[ind])
# #         result += cal(atr[0], atr[1], j, n)
# #     return result
# #
# #
# # if __name__ == "__main__":
# #     m = int(sys.stdin.readline().strip())
# #     ans = 0
# #     atrs = []
# #     for i in range(m):
# #         line = sys.stdin.readline().strip()
# #         a = list(map(int, line.split()))
# #         atrs.append(a)
# #     print(catchOne(atrs))
# #
# #
# # def reverse(text):
# #     """
# #     input: 'abcd'
# #     output: 'dcba'
# #     """
# #     alist = [i for i in text]
# #     result = []
# #     for i in range(len(alist)):
# #         result.append(alist.pop())
# #
# #     return ''.join(result)
#
#
# def find_the_path(data, value):
#     """
#     input: (data, 'data3')
#     output: ['d1', 'd2b', 'd3b', 'd4b']
#     """
#     if data is None or value == '':
#         return []
#
#     result = []
#     dfs(data, value)
#     pass
#
#
# def dfs(data, vuale):
#     for key, values in data.items():
#         try:
#             print(key)
#             dfs(value, values)
#         except AttributeError:
#             print(str(value))
#
#
#
#
# data = {
#         'a1': {
#             'a2': {
#                 'a3': 'data under a',
#                 },
#             },
#         'b1': None,
#         'c1': {
#             'c2':{
#                 'c2a': 'data1',
#                 'c2b': 'data2',
#                 }
#             },
#         'd1': {
#             'd2a': {
#                 'd2a1': 3,
#                 'd2a2': 4,
#                 },
#             'd2b': {
#                 'd3b': {
#                     'd4b': 'data3',  # the value need to find
#                     },
#                 'd3c': 12345,
#                 }
#             }
#         }
#
# find_the_path(data, 'data3')
#
#
# !/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


# def smallestRange():
#     K = int(input())
#     data_i = list(map(int, input().split(' ')))
#     results = []
#     current = max(data_i) - min(data_i)
#     for i in data_i:
#
#     return

# # ******************************结束写代码******************************
#
#
# res = smallestRange()
#
# print(str(res) + "\n")

# # !/bin/python
# # -*- coding: utf8 -*-
# import sys
# import os
# import re
#
#
# # 请完成下面这个函数，实现题目要求的功能
# # 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# # ******************************开始写代码******************************
#
#
# def find_longest_num_str(input):
#     results = re.findall('(\d+)', input)
#     return str(len(max(results))) + '/' + max(results)
#
# # ******************************结束写代码******************************
#
#
# try:
#     _input = input()
# except:
#     _input = None
#
# res = find_longest_num_str(_input)
#
# print(res + "\n")

# 找零钱
# changes = [10, 5, 1, 0.5]
#
#
# def cal_change(a, b):
#     res = b - a
#     results = []
#     while True:
#         if res <= 0:
#             break
#         for i in changes:
#             while res >= i:
#                 results.append(i)
#                 res -= i
#     result = ''
#     for i in changes:
#         cnt = results.count(i)
#         if cnt:
#             result += (str(i) + ':' + str(cnt) + ';')
#     return result
#
#
# line = list(map(float, input().split(' ')))
# print(str(line[1]-line[0])+' '+cal_change(line[0], line[1]))

#
# def find_seq(input):
#     results = [[] for _ in input]
#     plat_list = ['1', '2', '3']
#     for i, v in enumerate(input):
#         for j in plat_list:
#             vb = v + j
#             results[i].append(vb)
#     res = []
#
#     def get_p(lis, j=True):
#         if j:
#             lis = [[[i] for i in lis[0]]] + lis[1:]
#         if len(lis) > 2:
#             for i in lis[0]:
#                 for j in lis[1]:
#                     get_p([[i + [j]]] + list[2:], False)
#         elif len(lis) == 2:
#             for i in lis[0]:
#                 for j in lis[1]:
#                     res.append(i + [j])
#
#     get_p(results)
#
#     ress = ''
#     for i in res:
#         ress += ''.join(i) + ' '
#     return ress
#
#
# inp = input()
# print(find_seq(inp))


# #coding=utf-8
# # 本题为考试多行输入输出规范示例，无需提交，不计分。
# import sys
#
#
# def b_game(alist):
#     i = 0
#     j = 0
#     res = alist.count(-1)
#     if alist[i+1][0] and alist[0][j+1]:
#         return -1
#     for iv in alist:
#         if iv.count(-1) == len(iv):
#             return -1
#     for jv in range(len(alist)):
#         if sum([i[jv]] for i in alist) == -3:
#             return -1
#
#     if not alist[i+1][j+1] == -1:
#         return res - 1
#
#     return res
#
#
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = 3
#     ans = 0
#     monster_map = []
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(str, line.split()))
#         for i, v in enumerate(values):
#             if '-' == v:
#                 values[i] = '-1'
#         monster_map.append(list(map(int, values)))
#     print(b_game(monster_map))


# # coding=utf-8
# # 本题为考试多行输入输出规范示例，无需提交，不计分。
# import sys
#
#
# def car_num(alist, car_size):
#     res = 0
#     alist.sort(reverse=True)
#     i = 0
#     while True:
#         if not alist:
#             break
#         v = alist[0]
#         alist.pop()
#         if car_size == v:
#             res += 1
#         else:
#             while True:
#                 if v + alist[0] > car_size:
#                     alist.pop(0)
#                     res += 1
#                     break
#                 else:
#                     v += alist[0]
#
#     return res
#
#
# if __name__ == "__main__":
#     # 读取第一行的n
#     line = sys.stdin.readline().strip()
#     # 把每一行的数字分隔后转化成int列表
#     bags = list(map(int, line.split()))
#     car_size = int(sys.stdin.readline().strip())
#     print(car_num(bags, car_size))


# coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys


def str_top(alist, top_k):
    res = 0
    str_set = set(alist)
    str_list = list(str_set)
    len_list = [len(i) for i in str_list]
    if top_k > len(len_list):
        return len_list[-1]

    return len_list[top_k-1]


if __name__ == "__main__":
    # 读取第一行的n
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    str_list = list(map(str, line.split()))
    top_k = int(sys.stdin.readline().strip())
    print(str_top(str_list, top_k))
