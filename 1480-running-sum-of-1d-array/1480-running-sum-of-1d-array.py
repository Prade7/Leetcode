class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d=0
        for i in range(len(nums)):
            d+=nums[i]
            nums[i]=d
        print(nums)
        return nums