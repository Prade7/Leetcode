class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res=[]
        for ele in sentences:
            res.append(len(ele.split()))
            
        return max(res)