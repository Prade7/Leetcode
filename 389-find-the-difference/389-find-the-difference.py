class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for ele in s:
            # if(ele in s):
            t=t.replace(ele,"",1)
        return t