class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sm=0
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                if((j-i)%2==0):
                    for k in range(i,j+1):
                        sm+=arr[k]
        print(sm)
        return sm
    
    