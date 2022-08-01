class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        d=[]
        for ele in s:
            if(ele not in d):
                d.append(ele)
            else:
                return ele