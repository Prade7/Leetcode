class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # a=set(s)
        # a=list(a)
        for i in range(len(s)):
            if(s.count(s[i])==1):
                return i
        return -1