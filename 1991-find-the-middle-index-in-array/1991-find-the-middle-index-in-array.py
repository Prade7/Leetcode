class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        right=0
        left=sum(nums)
        
        for index,ele in enumerate(nums):
            left-=ele
            if(left==right):
                return index
            right+=ele
        return -1
                
                