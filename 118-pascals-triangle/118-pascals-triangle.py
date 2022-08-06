class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a=[]
        
        for i in range(numRows):
            temp=[]
            for j in range(i+1):
                if(j==0 or j==i):
                    temp.append(1)
                else:
                    temp.append(a[i-1][j]+a[i-1][j-1])
            a.append(temp)
        return a