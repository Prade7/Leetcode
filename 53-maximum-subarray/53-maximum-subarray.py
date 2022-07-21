class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        c=nums[0]
        f=0
        for ele in nums:
            if(f<=0):
                f=0
            f+=ele
            c=max(f,c)
        return c
            