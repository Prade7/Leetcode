class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
            left=0
            sumOfElements=sum(nums)
            
            for i,n in enumerate(nums):
                if(left==(sumOfElements-left-n)):
                    return i
                left+=n
            return -1