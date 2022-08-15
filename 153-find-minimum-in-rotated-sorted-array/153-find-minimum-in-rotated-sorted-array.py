class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        temp=nums[0]
        while(left<=right):
            if(nums[left]<nums[right]):
                temp=min(temp,nums[left])
                break            
            mid=(left+right)//2
            temp=min(temp,nums[mid])
            
            if(nums[left]<=nums[mid]):
                left=mid+1
            else:
                right=mid-1
                
        return temp
        
        
        