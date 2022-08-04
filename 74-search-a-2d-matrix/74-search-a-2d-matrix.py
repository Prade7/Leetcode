class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i=0
        l=len(matrix)-1
        q=-1
        while(i<=l):
            mid=(i+l)//2
            if(target in matrix[mid]):
                q=matrix[mid]
                break
            elif(target<matrix[mid][0]):
                l=mid-1
            else:
                i=mid+1
        print(q)
        
        if(q==-1):
            return False
        i=0
        l=len(q)
        while(i<l):
            mid=(i+l)//2
            if(target==q[mid]):
                return True
            elif(target<q[mid]):
                l=mid
            else:
                i=mid