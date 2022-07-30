class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=0
        d=1
        for ele in range(1,len(nums)):
            if(nums[ele]!=nums[ele-1]):
                nums[d]=nums[ele]
                d+=1
        return d