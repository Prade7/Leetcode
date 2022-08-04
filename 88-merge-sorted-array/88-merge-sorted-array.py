class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:]=nums2
        # for i in range(len(nums1)):
        #     a=min(nums1[i:])
        #     ind=nums1.index(a)
        #     nums1[i],nums1[ind]=nums1[ind],nums1[i]
        nums1.sort()
        print(nums1)
        
        
        
        