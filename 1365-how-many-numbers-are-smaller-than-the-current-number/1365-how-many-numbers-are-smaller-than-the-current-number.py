class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        i=0
        l=len(nums)
        out=[]
        while(i<l):
            count=0
            for k in range(len(nums)):
                if(k!=i):
                    if(nums[i]>nums[k]):
                        count+=1
            out.append(count)
            i+=1
        # print(out)
        return out