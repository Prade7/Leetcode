class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        d=[[]]
        
        for ele in nums:
            f=[]
            for i in d:
                f.append(i+[ele])
                print(f)
            d+=f
        return d
        # print(d)