class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
         
        a=s.split()
        a=" ".join(a[::-1])
        return a    
        
        