class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result=[]
        
        for ele in range(len(nums)):
            result.append(nums[nums[ele]])
        return result