class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        t0=0
        t1=1
        t2=1
        if(n==0):
            return 0
        if(n==1):
            return 1
        if(n==2):
            return 1
        # for i in range(n-2):
        #     t0,t1,t2=t1,t2,(t0+t1+t2)
        # return t2
        
        while(n>=3):
            
            t0,t1,t2=t1,t2,(t0+t1+t2)

            n-=1
        return t2
            
            
            