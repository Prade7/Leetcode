class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        if(len(mat)*len(mat[0])!=(r*c)):
            return mat
        f=0
        res=[]
        g=[]
        for ele in mat:
            for i in ele:
                res.append(i)
                f+=1
                
                if(f==c ):
                    g.append(res)
                    res=[]
                    f=0
        return g     
        
        
        
        
        