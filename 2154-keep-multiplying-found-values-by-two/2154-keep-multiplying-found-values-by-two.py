class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        if(original not in nums):
            return original
        
        nums.sort()
        
        i=0
        l=len(nums)-1
        target=original
        while(i<=l):
            mid=(i+l)//2  
            if(nums[mid]==target):
                i=0
                l=len(nums)-1
                target*=2
            elif(nums[mid]>target):
                l=mid-1
            elif(nums[mid]<target):
                i=mid+1
        return target