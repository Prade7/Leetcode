class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dict1={}
        for ele in arr:
            if(ele not in dict1):
                dict1[ele]=1
            else:
                dict1[ele]+=1
        sorted_values=sorted(dict1.values())
        print(sorted_values)
        length=len(sorted_values)
        for ele in sorted_values:
            if(ele<=k):
                print(k)
                k-=ele
                length-=1
            
            
        return length

