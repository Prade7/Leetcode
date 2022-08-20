class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        if(len(s)!=len(pattern)):
            return False
      
        # if(len(set(s))==1 and len(set(pattern))==1):
            # return True
       
        
        if(len(set(pattern))!=len(set(s))):
            return False
        hm={}
        for i in range(len(s)):
            if(pattern[i] not in hm):
                hm[pattern[i]]=s[i]
        print(hm)
        for i in range(len(pattern)):
            if(hm[pattern[i]]!=s[i]):
                print(hm[pattern[i]])
                return False
        
        return True
            
        
        
        
        