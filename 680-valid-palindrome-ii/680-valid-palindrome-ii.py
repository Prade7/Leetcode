class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        if(s==s[::-1]):
            return True
        
        start=0
        end=len(s)-1
        
        while(start<end):
            
            if(s[start]!=s[end]):
                left=s[:start]+s[start+1:]
                right=s[:end]+s[end+1:]
                
                return (left==left[::-1] or right[::]==right[::-1])
            start+=1
            end-=1
            
        return False