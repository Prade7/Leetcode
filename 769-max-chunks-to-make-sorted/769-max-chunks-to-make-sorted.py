class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count=0
        a=sorted(arr)
        h=[]
        for ele in range(len(arr)):
            h.extend(sorted(arr[:ele]))
            h.extend(sorted(arr[ele::]))
            if(h==a):
                count+=1
            h=[]
        return count