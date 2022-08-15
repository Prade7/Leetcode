class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        temp=nums[0]
        
        while(left<=right):
            if(nums[left]<nums[right]):
                temp=min(temp,nums[left])
                break
            
            m=(left+right)//2
            temp=min(temp,nums[m])
            
            if(nums[left]<=nums[m]):
                left=m+1
            else:
                right=m-1
            
        return temp
        