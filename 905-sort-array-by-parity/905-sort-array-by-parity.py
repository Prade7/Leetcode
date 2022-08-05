class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        d=[]
        h=[]
        for ele in nums:
            if(ele%2==0):
                d.append(ele)
        for ele in nums:
            if(ele%2!=0):
                h.append(ele)
        d.extend(h)
        return d