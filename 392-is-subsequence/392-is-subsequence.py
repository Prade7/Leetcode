class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        length=len(s)
        i=0
        if(length==0):
            return True
        for ele in t:
            if(s[i]==ele):
                # count+=1
                i+=1
            
            if(i==length):
                return True
        return False