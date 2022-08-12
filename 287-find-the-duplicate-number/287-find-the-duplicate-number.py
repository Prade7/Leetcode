class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hm={}
        
        for ele in nums:
            if(ele not in hm):
                hm[ele]=1
            else:
                return ele