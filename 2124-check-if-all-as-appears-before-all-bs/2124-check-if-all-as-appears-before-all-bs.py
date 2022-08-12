class Solution:
    def checkString(self, s: str) -> bool:
        r=False
      
        for ele in s:
            if(ele=="b"):
                r=True
                print(r)
            if(ele=="a" and r==True):
                return False
        
        return True