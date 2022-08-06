class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxi=nums[0]
        ind=0
        for i,ele in enumerate(nums):
            if(ele>maxi):
                maxi=ele
                ind=i
        print(maxi)
        for ele in range(len(nums)):
            if(nums[ele]*2 > maxi and ele!=ind):
                return -1
        return ind