class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums.sort()
        hm={}
        for ele in nums:
            if(ele%2==0 and ele not in hm):
                hm[ele]=1
            else:
                if(ele%2==0):
                    hm[ele]+=1
        print(hm)
        if(len(set(list(hm.values())))==0):
            return -1
        hmVal=list(hm.values())
        print(hmVal)
        hmVal=max(hmVal)
        
        for i,j in hm.items():
            if(j==hmVal):
                return i
        
                