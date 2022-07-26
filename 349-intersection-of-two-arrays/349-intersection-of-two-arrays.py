class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d=[]
        if(len(nums1)>len(nums2)):
            for ele in nums1:
                if(ele in nums2):
                    d.append(ele)
        for ele in nums2:
            if(ele in nums1):
                d.append(ele)
        return set(d)