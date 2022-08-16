class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm={}
        
        for ele in s:
            if(ele not in hm):
                hm[ele]=1
            else:
                hm[ele]+=1
        print(hm)
        # res=list(hm.keys())
        for i,ele in hm.items():
            if(ele==1):
                return s.index(i)
        return -1