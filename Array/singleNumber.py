class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = b = c = 0
        for x in nums:
            b |= (a & x)
            a ^= x
            c = a & b
            a ^= c
            b ^= c
        return a

    def singleNumber1(self, nums):
        a = b = 0
        for x in nums:
            a ^= x
            b ^= x
        return a ^ b