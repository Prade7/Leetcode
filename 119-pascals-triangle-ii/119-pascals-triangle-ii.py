class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        l1=[]
        for i in range(rowIndex+1):
            res=[]
            for j in range(i+1):
                if(j==0 or j==i):
                    res.append(1)
                else:
                    res.append(l1[i-1][j]+l1[i-1][j-1])
            l1.append(res)
        return l1[rowIndex]
                    