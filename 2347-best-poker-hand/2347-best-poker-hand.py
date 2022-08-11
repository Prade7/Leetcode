class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        # print(set(suits))
        if(len(set(suits))==1):
            return "Flush"
        hm={}
        for ele in ranks:
            if(ele not in hm):
                hm[ele]=1
            else:
                hm[ele]+=1
        list1=list(hm.values())
        print(list1)
        for ele in list1:
            if(ele>=3):
                return "Three of a Kind"
        for ele in list1:
            if(ele>=2):
                return "Pair"
        return "High Card"