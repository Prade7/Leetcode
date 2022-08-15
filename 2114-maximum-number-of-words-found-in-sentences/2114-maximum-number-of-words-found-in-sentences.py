class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res=set()
        # sentences=sentences.split(",")
        # print(len(sentences[0]))
        for ele in sentences:
            res.add(len(ele.split()))
            
        return max(res)