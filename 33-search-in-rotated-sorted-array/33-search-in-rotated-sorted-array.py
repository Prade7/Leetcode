class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i,ele in enumerate(nums):
            if(ele==target):
                return i
        return -1