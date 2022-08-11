class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split()
        a=1
        result=[]
        while(a<len(s)+1):
            for ele in s:
                if(ele[-1]==str(a)):
                    result.append(ele[:-1])
                    a+=1
                    # print(result)
            # if(len(result)==len(s)):
            #     break
        print(result)
                    
        return " ".join(result)
        