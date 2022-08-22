class Solution:
    def validPalindrome(self, s: str) -> bool:
        
#         if(s==s[::-1]):
#             return True
        
#         start=0
#         end=len(s)-1
        
#         while(start<end):
            
#             if(s[start]!=s[end]):
#                 left=s[:start]+s[start+1:]
#                 right=s[:end]+s[end+1:]
                
#                 if(left==left[::-1] or right[::]==right[::-1]):
#                     return True
#             start+=1
#             end-=1
            
#         return False
    
     # def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                leftstring = s[:left]+s[left+1:]
                rightstring = s[:right]+s[right+1:]
                return leftstring == leftstring[::-1] or rightstring == rightstring[::-1]
            left += 1
            right -= 1
        return True