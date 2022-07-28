class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if(len(s)!=len(t)):
            return False
        s=list(s)
        t=list(t)
        s.sort()
        t.sort()
        if(s==t):
            return True
        
        
        