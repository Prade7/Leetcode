class Solution:
    def fib(self, n: int) -> int:
        n1=0
        n2=1
        nth=n1
        if(n==0):
            nth=n1
        if(n==1):
             nth=n1+n2
        while(n>1):
            nth=n1+n2
            n1=n2
            n2=nth
            n-=1
        return nth
        
            
        