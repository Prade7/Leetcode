class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a=nums[-1]
        b=0
        for ele in nums:
            if(b<=0):
                b=0    
            b+=ele
            a=max(b,a)
        
        print(b)
        return a