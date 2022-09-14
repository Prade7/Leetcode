class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        left=0
        right=sum(nums)
        
        for index,ele in enumerate(nums):
            right-=ele
            if(right==left):
                return index
            left+=ele
        return -1
                