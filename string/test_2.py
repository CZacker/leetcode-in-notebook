class Solution(object):
    def checkInclusion(s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        sfan = s1[::-1]
        for i,str2 in enumerate(s2):
            print(str2==sfan[0])
            if str2 == sfan[0] or str2 == s1[0]:
                ss = s2[i:i+len(s1)]
                if ss == sfan or ss == s1:
                    return True
        return False
            
a = Solution
print(a.checkInclusion("ab","eidbaoo"))
