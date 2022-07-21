class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        D=0
        count=0
        for ele in s:
            if(ele=="R"):
                count+=1
            else:
                count-=1
            if not count:
                D+=1
        return D