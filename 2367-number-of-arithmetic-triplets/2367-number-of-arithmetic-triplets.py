class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if(nums[j]-nums[i]==diff and nums[k]-nums[j]==diff):
                        count+=1
        return (count)
    
        i=0
        j=len(nums)-1
        count=0
        while(i<j):
            k=i+1
            while(k<j):
                if(nums[k]-nums[i]==diff and nums[j]-nums[k]==diff):
                    count+=1
                k+=1
            i+=1
            j-=1
        print(count)