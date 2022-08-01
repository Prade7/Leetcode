class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        j=0
        for k in nums:
            temp=max(k+i,j)
            i=j
            j=temp
        return j