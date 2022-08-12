class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        hm={}
        for ele in nums:
            if(ele not in hm):
                hm[ele]=1
            else:
                hm[ele]+=1
        for key,value in hm.items():
            if(value==1):
                return key