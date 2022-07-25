class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums=nums1+nums2
        nums.sort()
        n=len(nums)//2

        if(len(nums)%2==0):
            return (float(nums[n]+nums[n-1]))/2
        else:
            return float(nums[n])
            