class Solution:
    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {}
        res = left = 0
        for i in range(len(s)):
            l = m.get(s[i])
            if l is None or 0 if l is None else l < left:
                res = max(res, i - left + 1)
                print(i, i - left - 1, m)
            else:
                left = l if l is not None else 0
            m[s[i]] = i + 1
        return res

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        b = []
        a = path.split('/')
        for i, value in enumerate(a):
            if value == '' and i != 0 or value == '.':
                continue
            else:
                if value == '..' and b != []:
                    print(b)
                    c = b.pop()
                    if c == '..':
                        b.append('..')
                    elif c == '':
                        b.append('')
                else:
                    b.append(value)

        a = '/'.join(b)
        if a == '..' or a == '':
            a = '/'
        return a

    def threeSum2(self, nums):
        mutnums = nums
        results = []
        mutnums.sort()
        print(mutnums)
        length = len(mutnums)
        zero = mutnums.count(0)
        if zero >= 3 and zero != 0:
            results.append([0, 0, 0])
        for i in range(length):
            if mutnums[i] >= 0:
                break
            elif i > 0 and mutnums[i] == mutnums[i - 1]:
                continue
            target = 0 - mutnums[i]
            if zero and mutnums.count(target):
                results.append([-target, 0, target])
            while i + 1 < length - 1:
                if mutnums[i+1:].count(target - mutnums[i + 1]) and mutnums[i + 1] < 0 and results.count([-target, mutnums[i + 1], target - mutnums[i + 1]]) == 0:
                    results.append([-target, mutnums[i + 1], target - mutnums[i + 1]])
                for j in range(i + 1, length - 1):
                    if mutnums[j] <= 0:
                        continue
                    elif mutnums[j] >= target:
                        break
                    elif mutnums[j+1:].count(target - mutnums[j]) and results.count([-target, mutnums[j], target - mutnums[j]]) == 0:
                        results.append([-target, mutnums[j], target - mutnums[j]])
                i += 1
        return results

    def threeSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 存储结果列表
        res_list = []
        # 对nums列表进行排序，无返回值，排序直接改变nums顺序
        nums.sort()
        for i in range(len(nums)):
            # 如果排序后第一个数都大于0，则跳出循环，不可能有为0的三数之和
            if nums[i] > 0:
                break
            # 排序后相邻两数如果相等，则跳出当前循环继续下一次循环，相同的数只需要计算一次
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 记录i的下一个位置
            j = i + 1
            # 最后一个元素的位置
            k = len(nums) - 1
            while j < k:
                # 判断三数之和是否为0
                if nums[j] + nums[k] == -nums[i]:
                    # 把结果加入数组中
                    res_list.append([nums[i], nums[j], nums[k]])
                    # 判断j相邻元素是否相等，有的话跳过这个
                    while j < k and nums[j] == nums[j + 1]: j += 1
                    # 判断后面k的相邻元素是否相等，是的话跳过
                    while j < k and nums[k] == nums[k - 1]: k -= 1
                    # 没有相等则j+1，k-1，缩小范围
                    j += 1
                    k -= 1
                # 小于-nums[i]的话还能往后取
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    k -= 1
        return res_list

    def threeSum(self, nums):
        # 创建一个存储结果的列表
        res = []
        # 创建一个字典用于存储nums中的元素及其出现的次数
        d = dict()
        for i in nums:
            if i not in d:
                d[i] = 0
            d[i] += 1
        # 创建两个列表分别用于存储正数和负数
        posnum = [i for i in d if i > 0]
        negnum = [i for i in d if i < 0]
        if d.get(0, 0) > 2:
            res.append([0, 0, 0])
        if negnum == [] or posnum == []:
            return res
        for i, x in enumerate(posnum):
            if d[x] >= 2 and -2 * x in d:
                res.append([x, x, -2 * x])
            for y in posnum[i + 1:]:
                if -(x + y) in d:
                    res.append([x, y, -x - y])
        for i, x in enumerate(negnum):
            if d[x] >= 2 and -2 * x in d:
                res.append([x, x, -2 * x])
            for y in negnum[i + 1:]:
                if -(x + y) in d:
                    res.append([x, y, -x - y])

        if 0 in d:
            for x in posnum:
                if -x in d:
                    res.append([x, 0, -x])
        return res
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ''
        mapping = s.split('')
        slow,minLen,index,matchNum = 0,float('inf'),0,0
        for fast in range(len(s)):
            char = s[fast]
            count = mapping.count(char)
            if count == None:
                continue
            mapping.remove()
            if count == 1:
                matchNum += 1
            while matchNum == len(mapping):
                if fast-slow+1 < minLen:
                    minLen = fast-slow+1
                    index = slow
                leftmost = s[slow]
                slow += 1
                leftmostCount = mapping.get(leftmost)
                if leftmostCount == None:
                    continue
                mapping[leftmost] += 1
                if leftmostCount == 0:
                    matchNum -= 1
        return '' if minLen == float('inf') else s[index:index+minLen]

a = Solution()
# print(a.simplifyPath("/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///"))
print(a.threeSum([2,-8,8,6,-14,-12,11,-10,13,14,7,3,10,-13,3,-15,7,3,-11,-8,4,5,9,11,7,1,3,13,14,-13,3,-6,-6,-12,-15,-12,-9,3,-15,-11,-6,-1,0,11,2,-12,3,-6,6,0,-6,-12,-10,-12,6,5,-4,-5,-5,-4,-11,13,5,-2,-13,-3,-7,-15,8,-15,12,-13,0,-3,6,9,-8,-6,10,5,9,-11,0,7,-15,-8,-3,-4,-6,7,7,-2,-2,-11,3,0,-6,12,0,-13,4,-3,11,-11,1,2,13,8,4,9,-1,-2,5,14,12,5,13,-6,-13,-8,9,1,5,-8,-2,-6,-1]))
