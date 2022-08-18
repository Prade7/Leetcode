class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        hm={}
        for e in arr:
            if(e not in hm):
                hm[e]=1
            else:
                hm[e]+=1
        
        values=list(hm.values())
        count=0
        values.sort(reverse=True)
        print(values)
        l=len(arr)
        g=len(arr)//2
        while(l>g):
            l-=values[count]
            count+=1
        return count
    