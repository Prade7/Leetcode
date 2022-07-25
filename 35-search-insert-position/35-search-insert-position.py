class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i=0
        l=len(nums)
        if(target in nums):
            while(i<l):
                mid=(i+l)//2

                if(nums[mid]==target):
                    return mid
                if(nums[mid]<target):
                    i=mid
                else:
                    l=mid
 # else:
        for i,ele in enumerate(nums):
            if(target<ele):
                return i
            if(target>nums[-1]):
                return len(nums)
                    
