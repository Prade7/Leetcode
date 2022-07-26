class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for ele in nums:
            if(ele in d):
                d[ele]=d[ele]+1
            else:
                d[ele]=1
            
        for i,k in d.items():
            if(k==1):
                return i