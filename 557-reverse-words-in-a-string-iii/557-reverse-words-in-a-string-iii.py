class Solution:
    def reverseWords(self, s: str) -> str:
        
        s=s.split()
        result=""
        
        for ele in s:
            result+=ele[::-1]+" "
        print(result)
        return result.strip()