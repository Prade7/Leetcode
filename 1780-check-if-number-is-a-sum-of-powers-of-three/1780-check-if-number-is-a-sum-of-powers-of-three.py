class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # return n%3==0
        
        while(n>0):
            rem=n%3
            if(rem>1):
                return False
            n//=3
        return True
        
        
        
        
        