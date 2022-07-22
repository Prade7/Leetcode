class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if(m*n !=len(original)):
            return []
        q=[]
        g=[]
        c=0
        for ele in original:
            if(c<n):
                q.append(ele)
                c+=1
            if(c==n):
                g.append(q)
                # print(11111)
                c=0
                q=[]
        print(g)
        return g