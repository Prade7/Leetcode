class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        d=0
        for ele in accounts:
            if(sum(ele)>d):
                d=sum(ele)
        return (d)