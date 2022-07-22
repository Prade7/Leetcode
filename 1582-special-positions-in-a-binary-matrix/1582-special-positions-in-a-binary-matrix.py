class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        a1=[0]*len(mat)
        b1=[0]*len(mat[0])
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                if(mat[x][y]==1):
                    a1[x]+=1
                    b1[y]+=1
        count=0    
        for x in range(len(a1)):
            for y in range(len(b1)):
                if(a1[x]==1 and b1[y]==1 and mat[x][y]==1):
                    count+=1
        return count