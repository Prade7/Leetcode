class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        d=[]
        if(len(nums1)>len(nums2)):
            for ele in nums2:
                if(ele in nums1):
                    d.append(ele)
                    nums1.remove(ele)
            return d
        for ele in nums1:
            if(ele in nums2):
                d.append(ele)
                nums2.remove(ele)
        return d