class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        up=[]
        low=[]
        
        for ele in s:
            if(ele.isupper()):
                up.append(ele)
            else:
                low.append(ele)
        up=set(up)
        up=list(up)
        low=set(low)
        low=list(low)
        up.sort(reverse=True)
        low.sort(reverse=True)
        lw=[]
        for ele in low:
            lw.append(ele.upper())
        print(lw)
        for ele in lw:
            if(ele in up):
                return ele
        return ""
            