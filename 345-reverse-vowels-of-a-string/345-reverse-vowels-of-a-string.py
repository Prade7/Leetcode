class Solution:
    def reverseVowels(self, s: str) -> str:
#         vowels=["a","e","i","o","u","A","E","I","O","U"]
#         s=list(s)
#         start=0
#         end=len(s)-1
#         while(start<end):
#             if(s[start] in vowels) and (s[end] in vowels):
#                 s[start],s[end]=s[end],s[start]
#                 start+=1
#                 end-=1
#             elif(s[start] in vowels) and (s[end] not in vowels):
#                 end+=1
#             elif(s[end] in vowels) and (s[start] not in vowels):
#                 start-=1
#             # if(s[start] not in vowels) and (s[end] not in vowels):
#             else:
#                 start+=1
#                 end-=1

#         return "".join(s)
        
        
        
        d = ''
        start = 0
        end = len(s)-1
        s = list(s)
        l = ['a','e','i','o','u','A','E','I','O','U']
        while(start<end):
            if s[start] in l and s[end] in l:
                s[start],s[end] = s[end],s[start]  
                start += 1
                end -= 1
            elif s[start] in l and s[end] not in l:
                end -= 1
            elif s[start] not in l and s[end] in l:
                start += 1
            else:
                start += 1
                end -= 1
        s = ''.join(s)
        return s