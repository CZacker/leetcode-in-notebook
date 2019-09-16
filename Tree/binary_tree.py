# import sys
#
#
# def checkVersion(v1, v2):
#         v1_split = v1.split('.')
#         v2_split = v2.split('.')
#         v1_len, v2_len = len(v1_split), len(v2_split)
#         maxLen = max(v1_len, v2_len)
#         for i in range(maxLen):
#             temp1, temp2 = 0, 0
#             if i < v1_len:
#                 temp1 = int(v1_split[i])
#             if i < v2_len:
#                 temp2 = int(v2_split[i])
#             if temp1 > temp2:
#                 print('true')
#         print('false')
#
#
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     result = []
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(str, line.split()))
#         checkVersion(values[0],values[1])
#
#     for i in result:
#         print(i)


# -------------------------------------------------------------------------------
#
# #coding=utf-8
# import sys
#
# def catchOne(n):
#     mem = set()
#     while n != 1:
#         n = sum([int(i) ** 2 for i in str(n)])
#         if n not in mem:
#             mem.add(n)
#         else:
#             return False
#     return True
#
#
# if __name__ == "__main__":
#
#     m = int(sys.stdin.readline().strip())
#     ans = 0
#     for i in range(m):
#         line = sys.stdin.readline().strip()
#         values = list(map(int, line.split()))
#         print(catchOne(values[0]))

# # coding=utf-8
# import sys
#
#
# def catchOne(treasures, keys):
#     result = 0
#     for t in treasures:
#         for k in keys:
#             if (k+t % 2) == 0:
#                 pass
#             else:
#                 keys.remove(k)
#                 result += 1
#     return result
#
#
# if __name__ == "__main__":
#     count = sys.stdin.readline().strip()
#     n, m = list(map(int, count.split()))
#     line1 = sys.stdin.readline().strip()
#     treasures = list(map(int, line1.split()))
#     line2 = sys.stdin.readline().strip()
#     keys = list(map(int, line2.split()))
#     result = catchOne(treasures, keys)
#     if result >= m:
#         if result >= n:
#             print(n)
#         else:
#             print(m)
#     else:
#         if result >= n:
#             print(n)
#         else:
#             print(result)


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

# # coding=utf-8
# import sys
#
#
# def maxProduct(self, nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     # temp记录整个数组的子序列最大连乘积
#     temp = nums[0]
#     length = len(nums)
#
#     # M数组记录包含当前位置的最大连乘值
#     M = [0 for i in range(length)]
#     # m数组记录包含当前位置的最小连乘值
#     m = [0 for i in range(length)]
#
#     for i in range(length):
#         if i == 0:
#             M[i] = nums[i]
#             m[i] = nums[i]
#         else:
#             # 包含当前位置的最大连乘值从：当前位置和到第i-1个元素的最大连乘值的乘积、当前元素中选出
#             M[i] = max(max(M[i - 1] * nums[i], m[i - 1] * nums[i]), nums[i])
#             m[i] = min(min(M[i - 1] * nums[i], m[i - 1] * nums[i]), nums[i])
#
#         temp = max(temp, M[i])
#
#     return temp
#
#
# def cal(arr):
#     arr.sort()
#     lo = arr[0]
#     result = 0
#     for i in arr:
#         result += lo * i
#     return result
#
#
# if __name__ == "__main__":
#     m = int(sys.stdin.readline().strip())
#     ans = 0
#     line = sys.stdin.readline().strip()
#     score = list(map(int, line.split()))
#     print(cal(score))

# # 机器人排队
# # coding=utf-8
# import sys
#
#
# def get_height(alist):
#     results = [0 for i in alist]
#     alist.reverse()
#     for i,v in enumerate(alist):
#         m = i
#         while True:
#             if not v > alist[m]:
#                 results[alist.index(v)] += 1
#                 break
#             else:
#                 m += 1
#     return alist[max(results)]
#
#
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     line = sys.stdin.readline().strip()
#     # 把第二行的数字分隔后转化成int列表
#     values = list(map(int, line.split()))
#     results = [0 for i in values]
#     values.reverse()
#     for i, v in enumerate(values):
#         m = i + 1
#         while True:
#             if m > n - 1:
#                 break
#             if not v > values[m]:
#                 results[values.index(values[m])] += 1
#                 break
#             else:
#                 m += 1
#     if sum(results) == 0:
#         print(0)
#     else:
#         print(values[results.index(max(results))])

# 解密问题
# import sys
#
# code_book = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F', '7': 'G', '8': 'H', '9': 'I', '10': 'J',
#              '11': 'K', '12': 'L', '13': 'M', '14': 'N', '15': 'O', '16': 'P', '17': 'Q', '18': 'R', '19': 'S',
#              '20': 'T', '21': 'U', '22': 'V', '23': 'W', '24': 'X', '25': 'Y', '26': 'Z'}
# if __name__ == "__main__":
#     # 读取第一行的n
#     line = sys.stdin.readline().strip()
#     code_input = [i for i in line]
#     results = ['']
#     for i in code_input:
#         results[0] += code_book[i]
#     m = '0'
#     i = 1
#     por = []
#
#     while i < len(code_input):
#         m = line[i-1:i+1]
#         if not int(m) > 26:
#             por.append(m)
#             i += 2
#         else:
#             por.append(line[i-1])
#             i += 1
#     result = ''
#
#     for i in por:
#         result += code_book[i]
#     results.append(result)
#
#     for i in results:
#         print(i)

# 取水问题
# import sys
#
# if __name__ == "__main__":
#     # 读取第一行的n
#     line = sys.stdin.readline().strip()
#     # 把第二行的数字分隔后转化成int列表
#     values = list(map(int, line.split()))
#     bottles = values[:3]
#     water = values[3]
#

# #coding=utf-8
# import sys
#
#
# def find_int(num):
#     if num < 2:
#         return 1
#     count = 0
#     for i in range(1, num):
#         s = i*(i+1)//2
#         if s < num:
#             if (num-s)%i == 0:
#                 count += 1
#         elif s == num:
#             count += 1
#             break
#         else:
#             break
#     return count
#
#
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = find_int(n)
#     print(ans)

# #coding=utf-8
# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     a = sys.stdin.readline().strip()
#     b = sys.stdin.readline().strip()
#     count = 0
#     for i, iv in enumerate(a):
#         for j, jv in enumerate(a):
#             if a[i:i + j] in b:
#                 continue
#             else:
#                 count += 1
#                 break
#     print(count - 1)