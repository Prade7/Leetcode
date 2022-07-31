class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(nums[0]==0 and len(nums)==1):
            return 0
        nums.sort()
        print(nums)
        if(len(nums)==1):
            return 1
        a=0
        nums=set(nums)
        if(0 in nums):
            nums.remove(0)
        nums=list(nums)
        if(nums==[]):
            return 0
        if(len(nums)==1):
            return 1
        count=0
        while(True):
            a=nums[0]
            for i in range(0,len(nums)):
                nums[i]-=a
            count+=1
            nums=set(nums)
            nums=list(nums)
            nums.remove(0)
            if(len(nums)<=1):
                count+=1
                break
            
        return count
            