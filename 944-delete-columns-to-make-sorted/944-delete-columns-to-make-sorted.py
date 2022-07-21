class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        count=0
        for ele in zip(*strs):
            if(list(ele)!=sorted(ele)):
                count+=1
        return count
            