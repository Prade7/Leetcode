class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        for i in range(len(nums)-1,0,-1):
            result=[]
            for j in range(i):
                if(nums[j]+nums[j+1]>9):
                    result.append((nums[j]+nums[j+1])%10)
                else:
                    result.append(nums[j]+nums[j+1])
            nums=result
        return nums[0]
                
