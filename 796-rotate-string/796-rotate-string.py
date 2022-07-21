class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if(len(s)<len(goal) or len(s)>len(goal)):
            return False
        a=s
        i=0
        for ele in range(len(s)):
        
            s=s[1::]+s[0]
            print(s)
            if(s==goal):
                return True
        return False
            # print(s)