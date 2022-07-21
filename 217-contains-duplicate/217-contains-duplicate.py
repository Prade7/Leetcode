class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        e=set(nums)
        if(sorted(list(e))!=sorted(nums)):
            return True
        else:
            return False
        # print(list(e))