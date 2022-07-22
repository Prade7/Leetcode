class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count=0
        a=sorted(arr)
        # print(a)
        h=[]
        for ele in range(len(arr)):
            h.extend(sorted(arr[:ele]))
            h.extend(sorted(arr[ele::]))
            if(h==a):
                print(h)
                count+=1
            h=[]
        print(count)
        return count