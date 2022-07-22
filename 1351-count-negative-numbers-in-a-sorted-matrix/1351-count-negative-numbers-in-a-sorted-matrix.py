class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        c=0
        for ele in grid:
            for e in ele:
                if(e<0):
                    c+=1
        # print(c)
        return c