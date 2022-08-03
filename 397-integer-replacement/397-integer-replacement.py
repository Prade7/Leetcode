class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        m=0
        while(n>1):
            if(n%2==0):
                n=n//2
            elif(n==3 or n%4==1):
                n-=1
            else:
                n+=1
            m+=1
            
                
        return m 
    