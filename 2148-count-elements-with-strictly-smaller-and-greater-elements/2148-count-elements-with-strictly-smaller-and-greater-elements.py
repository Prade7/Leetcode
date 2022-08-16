class Solution:
    def countElements(self, nums: List[int]) -> int:
        # nums=len(nums)//2
        # return nums
        if(len(nums)==1):
            return 0
        if(len(set(nums))==1):
            return 0
        nums.sort()
        print(nums)
        first=nums[0]
        c=nums.count(first)
        
        while(c>1):
            nums.remove(first)
            c-=1
        print(nums)
        
        last=nums[-1]
        c=nums.count(last)
        while(c>1):
            nums.remove(last)
            c-=1
        return len(nums)-2
        
        