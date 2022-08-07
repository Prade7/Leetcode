class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        if(len(nums)==1):
            return 0
        diff=nums[1]-nums[0]
        for i in range(1,len(nums)-1):
            if(nums[i+1]-nums[i]>diff):
                diff=nums[i+1]-nums[i]
        return diff