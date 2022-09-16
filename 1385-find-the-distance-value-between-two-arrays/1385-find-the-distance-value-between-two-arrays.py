class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        c=0
        temp=0
        for i in arr1:
            for j in arr2:
                if(abs(i-j)<=d):
                    temp=1
            if(temp==1):
                temp=0
            else:
                c+=1
        return c