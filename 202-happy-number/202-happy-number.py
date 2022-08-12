class Solution:
    def isHappy(self, n: int) -> bool:
        while(True):
            d=0
            while(n!=0):
                q=n%10
                n//=10
                d+=(q*q)
                print(d)
            if(d==1):
                return True
            elif(d==4 or d==16):
                return False
            n=d
            
            
            
            
            
            