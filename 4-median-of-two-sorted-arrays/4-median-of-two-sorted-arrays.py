class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        # nums=nums1
        nums1.sort()
        n=len(nums1)//2

        if(len(nums1)%2==0):
            return (float(nums1[n]+nums1[n-1]))/2
        else:
            return float(nums1[n])
            