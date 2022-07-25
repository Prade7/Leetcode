class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums=nums1[::]+(nums2[::])
        nums.sort()
        print(nums)
        n=len(nums)//2

        if(len(nums)%2==0):
            # n=len(nums)//2
            print(n)
            return (float(nums[n]+nums[n-1]))/2
            # return float(2)
        else:
            return float(nums[n])
            