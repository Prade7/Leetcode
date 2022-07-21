class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split(" ")
        print(s)
        # s=s.remove(' ')
        # print(s)
        p=[]
        for ele in s:
            if(ele.isalpha()):
                p.append(ele)
        d=p[-1]
        print(len(d))
        return len(d)