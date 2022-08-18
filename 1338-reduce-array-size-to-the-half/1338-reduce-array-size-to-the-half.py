class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        # arr.sort(key=lambda e:arr.count(e))
        print(arr)
        
        hm={}
        for e in arr:
            if(e not in hm):
                hm[e]=1
            else:
                hm[e]+=1
        
        values=list(hm.values())
        print(values)
        count=0
        values.sort(reverse=True)
        hald=len(arr)//2
        while(hald>0):
            hald-=values[count]
            count+=1
        return count
        
#         cnt = Counter(arr)      
#         num_freq = sorted(cnt.values(), reverse=True) 
#         print(num_freq)
#         half_size = len(arr) // 2
#         ans = 0
        
#         while half_size > 0:
#             half_size -= num_freq[ans]
#             ans += 1
        
#         return ans