class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=""
        c=0
        strs.sort(key=len)
        print(strs)
        r=strs[0]
        
        for ele in range(len(r)):
            c=0
            for i in range(len(strs)):
                if(r[ele]!=strs[i][ele]):
                    c=1
                    break
            if(c==0):
                result+=r[ele]
            if(c==1):
                break
        
        return (result)
                
                
        
        
        
            