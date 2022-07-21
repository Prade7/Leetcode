# class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
class Solution:
    def maxSubArray(self, nums):
        q=nums[0]
        c=0
        for ele in nums:
            if(c<=0):
                c=0
            
            c+=ele
            q=max(c,q)
        return q
                