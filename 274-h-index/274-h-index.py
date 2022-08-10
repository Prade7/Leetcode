class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i,ele in enumerate(citations):
            if(ele<i+1):
                return i
        return len(citations)