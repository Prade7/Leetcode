class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d=set()
        if(len(nums1)>len(nums2)):
            for ele in nums1:
                if(ele in nums2):
                    d.add(ele)
        for ele in nums2:
            if(ele in nums1):
                d.add(ele)
        return (d)