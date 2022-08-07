class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if(len(hand)%groupSize!=0):
            return False 
        count={}
        
        for ele in hand:
            if(ele not in count):
                count[ele]=1
            else:
                count[ele]+=1
        print(count)
        
        minH=list(count.keys())
        print(minH)
        # k=count.keys()
        heapq.heapify(minH)
        print(minH)
        while(minH):
            first=minH[0]
            for i in range(first,first+groupSize):
                if(i not in count):
                    return False
                count[i]-=1
                if(count[i]==0):
                    if(i!=minH[0]):
                        return False
                    heapq.heappop(minH)
                    
        return True