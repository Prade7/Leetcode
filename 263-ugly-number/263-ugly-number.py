class Solution:
    def isUgly(self, n: int) -> bool:
        if(n==0):
            return False
        while(n%2==0):
            n//=2
            print(n)
        while(n%3==0):
            n//=3
        while(n%5==0):
            n//=5
        if(n==2 or n==3 or n==5 or n==1):
            return True
        return False