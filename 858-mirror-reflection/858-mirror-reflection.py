class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        while(p%2==0 and q%2==0):
            p/=2
            q/=2
            print(p)
            print(q)
        
        
        if(p%2==0 and q%2!=0):
            return 2
        elif(p%2!=0 and q%2!=0):
            return 1
        elif(p%2!=0 and q%2==0):
            return 0
        
        