class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm={}
        for ele in nums:
            if(ele not in hm):
                hm[ele]=1
            else:
                hm[ele]+=1
        print(hm)
        
        val=list(hm.values())
        i=val[0]
        for ele in range(1,len(val)):
            if(i<val[ele]):
                i=val[ele]
        print(i)
        for key,j in hm.items():
            if(j==i):
                return key
        
        
        
        