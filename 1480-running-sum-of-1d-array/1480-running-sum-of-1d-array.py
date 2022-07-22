class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d=0
        g=[]
        for i in range(len(nums)):
            d+=nums[i]
            g.append(d)
        print(g)
        return g