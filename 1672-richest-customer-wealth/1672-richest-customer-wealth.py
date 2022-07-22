class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        d=[]
        for ele in accounts:
            d.append(sum(ele))
        return max(d)