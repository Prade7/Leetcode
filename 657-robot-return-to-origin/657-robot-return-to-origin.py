class Solution:
    def judgeCircle(self, moves: str) -> bool:
    
        L=0
        R=0
        U=0
        D=0
        for ele in moves:
            if(ele=="L"):
                L+=1
            elif(ele=="R"):
                R+=1
            elif(ele=="U"):
                U+=1
            else:
                D+=1
           
        if(L==R and U==D):
            return True
        return False
                
        
        