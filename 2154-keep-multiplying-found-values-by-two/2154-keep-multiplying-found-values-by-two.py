class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        if(original not in nums):
            return original
        
        for i in nums:
            if(original*2 not in nums):
                return original*2
            else:
                original*=2
                